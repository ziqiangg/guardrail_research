import re
B="https://github.com/meta-llama/PurpleLlama/blob/172c1074069eb88ec834124272c1b1c4f8893445/"
SHA="172c1074069eb88ec834124272c1b1c4f8893445"
rep={"@@L@@":"**[Documented: repo meta-llama/PurpleLlama@172c1074]**","@@H86@@":"**[Documented: repo meta-llama/Llama-Prompt-Guard-2-86M@a8ded8e6]**","@@H22@@":"**[Documented: repo meta-llama/Llama-Prompt-Guard-2-22M@11614a15]**","@@D@@":"**[Documented]**","@@I@@":"**[Inferred]**","@@N@@":"**[Not disclosed]**","@@T@@":"**[To be verified]**","@@B@@":B,"@@SHA@@":SHA}
CLASSES=["ScanResult","CodeShieldScanResult","PromptGuardScanner","CodeShieldScanner","ScannerType","ScanDecision","UserMessage","SystemMessage","AssistantMessage","ToolMessage","MemoryMessage","AutoTokenizer","AutoModelForSequenceClassification"]
SINGLE=["ALLOW","BLOCK","WARN","IGNORE","USER","TOOL","ASSISTANT","MEMORY","SYSTEM"]
def tick(line):
    prot=[]
    def keep(m):
        prot.append(m.group(0)); return "\x00%d\x00"%(len(prot)-1)
    line=re.sub(r"\*\*\[[^\]]*\]\*\*","\x01",line) if False else line
    # protect labels, file names, urls, quoted-free tokens
    line=re.sub(r"\*\*\[[^\]]*\]\*\*",keep,line)
    line=re.sub(r"https?://\S+",keep,line)
    line=re.sub(r"[\w/.\-]+\.(?:py|md|yaml|toml|ipynb|json)(?:@172c1074(?::[\d,\-]+)?)?",keep,line)
    line=re.sub(r"@172c1074(?::[\d,\-]+)?",keep,line)
    line=re.sub(r"\b(?:%s)\b"%"|".join(CLASSES),lambda m:"`%s`"%m.group(0),line)
    line=re.sub(r"\b[A-Z]{2,}(?:_[A-Z0-9]+)+\b",lambda m:"`%s`"%m.group(0),line)
    line=re.sub(r"\b(?:%s)\b"%"|".join(SINGLE),lambda m:"`%s`"%m.group(0),line)
    line=re.sub(r"\b[a-z][a-z0-9]*(?:_[a-z0-9]+)+(?:\(\))?",lambda m:"`%s`"%m.group(0),line)
    line=re.sub(r"\x00(\d+)\x00",lambda m:prot[int(m.group(1))],line)
    return line
out=[]
for n in ["part1_pl1","part2_pl2","part4_pl6","part3_pl4"]:
    s=open(n+".tpl",encoding="utf-8").read()
    for k,v in rep.items(): s=s.replace(k,v)
    assert "@@" not in s,n
    lines=[]
    for l in s.rstrip("\n").split("\n"):
        if (l.startswith("• ") and not l.startswith("• http")) or l.startswith("  – "):
            if "https://github.com/" not in l: l=tick(l)
        lines.append(l)
    out.append("\n".join(lines)+"\n")
notes=open("notes.tpl",encoding="utf-8").read()
out.append(notes.rstrip("\n")+"\n")
open("../../../drafts/purplellama_cols_a.md","w",encoding="utf-8",newline="\n").write("".join(out))
