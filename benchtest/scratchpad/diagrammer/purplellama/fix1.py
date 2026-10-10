import io
p = 'gen.py'
s = io.open(p, encoding='utf-8').read()


def rep(a, b):
    global s
    assert a in s, a[:80]
    s = s.replace(a, b, 1)


rep("<td>Two models, 86M and 22M (millions of internal settings), for prompt attacks</td>",
    "<td>Two models, 86M and 22M (named for their size), for prompt attacks</td>")
rep('''<figcaption>None of the three checkers acts on a result: Prompt Guard 2 gives a label, LlamaFirewall a decision and Code Shield advice, and your app (or a framework such as NeMo) does the refusing. LlamaFirewall is the closest to NeMo in shape, but Meta documents no topic rules or fixed replies in it. This page claims no link between NeMo and Purple Llama's tools. Llama Guard, which Meta keeps in the same project, is not repeated here.</figcaption>''',
    '''<figcaption>In the code Meta provides, none of the three checkers stops a chat by itself: Prompt Guard 2 gives a label, LlamaFirewall a decision and Code Shield advice, and your app (or a framework such as NeMo) does the refusing. LlamaFirewall is the one piece that works like a framework, but Meta documents no topic rules or fixed replies in it. This page claims no link between NeMo and Purple Llama's tools, and Llama Guard, which Meta keeps in the same project, is not repeated here.</figcaption>''')
rep("<td>No. Your app acts on the decision; the agent check never blocks, it asks for a person</td>",
    "<td>No. Your app acts on the decision (our reading of the code); the agent check never blocks, it asks for a person</td>")
rep('''<figcaption>Purple Llama has checks for what the user sends and for what the AI answers. Its checks on fetched text and on an agent's actions cover only part of the job, and the action check is experimental. It has no topic rules or fixed replies. At every point the tools only return a label or a decision; your app does the refusing. CyberSecEval is a measuring tool that tests AI models, outside the chat flow.</figcaption>''',
    '''<figcaption>Purple Llama has checks for what the user sends and for what the AI answers; its checks on fetched text and on an agent's actions cover only part of the job, and the action check is experimental. Meta documents no topic rules or fixed replies. At every point the tools only return a label or a decision and your app does the refusing, while CyberSecEval is a measuring tool that tests AI models outside the chat.</figcaption>''')
rep("<p>The pieces work the same way from the outside. Your app calls the tool from its own code and reads what comes back. Nothing here is a web service run by Meta.</p>",
    "<p>The pieces work the same way from the outside. Your app calls the tool from its own code and reads what comes back. Meta names no hosted service of its own for them.</p>")
rep("Purple Llama is Meta's umbrella project: it keeps Llama Guard and adds three checkers you run yourself (Prompt Guard 2, LlamaFirewall and Code Shield) and one test suite (CyberSecEval).",
    "Purple Llama is Meta's umbrella project: it holds Llama Guard alongside three checkers you run yourself (Prompt Guard 2, LlamaFirewall and Code Shield) and one test suite (CyberSecEval).")
rep("<td>Package version 1.0.3 on PyPI; two scanners are marked experimental</td>",
    "<td>Package version 1.0.3 on PyPI; AlignmentCheck and PIICheck are marked experimental</td>")
rep('''<figcaption>There is no "this is input" or "this is output" switch in Prompt Guard 2 or Code Shield: your app chooses what text to hand over. LlamaFirewall asks for a role with each message and picks its scanners from that. A score is the check's own estimate, and the pieces do not share one scale.</figcaption>''',
    '''<figcaption>There is no "this is input" or "this is output" switch in Prompt Guard 2 or Code Shield: your app chooses what text to hand over, and LlamaFirewall picks its scanners from the role you give each message. The Prompt Guard scanner reports a probability; every other scanner returns only 1.0 or 0.0.</figcaption>''')
rep("in Meta's own private English test, the 86M model caught about 98 in 100 attacks while wrongly flagging 1 in 100 harmless prompts. The 22M model caught about 89 in 100 at the same false-alarm rate. These are Meta's numbers on Meta's data; ours may differ. Meta recommends no cut-off score, and how well it works on fetched text or tool output is not evaluated separately.",
    "in Meta's own private English test, the 86M model caught about 98 in 100 attacks while wrongly flagging 1 in 100 harmless prompts, and the 22M model about 89 in 100. These are Meta's numbers on Meta's data; ours may differ. Meta recommends no cut-off, and fetched text and tool output are not evaluated separately.")
rep('''<figcaption>This is the setup you get with no configuration. You can attach any scanner to any role, and the same scanner can look at a user message, a tool result or an answer. Meta's agent test (AgentDojo) scanned only user and tool messages with Prompt Guard. LlamaFirewall returns a result; it does not stop the chat itself.</figcaption>''',
    '''<figcaption>This is the setup with no configuration; you can attach any scanner to any role. Meta's agent test (AgentDojo) scanned only user and tool messages with Prompt Guard. LlamaFirewall returns a result; it does not stop the chat itself.</figcaption>''')
rep('''a message can carry a structured request for an action (a tool call), but no scanner reads it. A harmful argument is seen only if the same text also appears in the message content. That is our reading of the code, and Meta's pages do not say. LlamaFirewall also overwrites each scanner's status with "success" in the result it returns, so a scanner's error status never reaches your app.''',
    '''a message can carry a structured request for an action (a tool call), but no scanner reads it, so a harmful argument is seen only if the same text is also in the message content (our reading of the code; Meta's pages do not say). LlamaFirewall also overwrites each scanner's status with "success" in the result it returns, so a scanner's error status never reaches your app.''')
rep("the scanner cuts text at 512 tokens and does not split it, so anything after that is not scored. It may also reload the model on every scan, which is not stated. A blocked result repeats the whole text in its reason.",
    "the scanner cuts text at 512 tokens and does not split it, so anything after that is not scored, and it may reload the model on every scan (not stated). A blocked result repeats the whole text in its reason.")
rep("<td>So after a normal install the PyPI code runs (our reading of the code). Any issue, even low severity, blocks</td>",
    "<td>So after a normal install the PyPI code runs, and any issue blocks, even a low-severity one (our reading of the code)</td>")
rep('''whether these differences change results needs testing. On its own, Code Shield recommends block only when an issue has error severity, and a Semgrep finding may never reach that (our reading of the code; untested). If Code Shield itself fails, it quietly reports "not insecure". The Semgrep tool has its own licence terms, and whether they matter here is an open question.''',
    '''whether these differences change results needs testing. On its own, Code Shield recommends block only for an error-severity issue, and a Semgrep finding may never reach that; if Code Shield itself fails, it quietly reports "not insecure" (our reading of the code; untested). The Semgrep tool has its own licence terms, an open question.''')
rep("a good score does not make an app safe, and a bad one does not make a guardrail weak. Meta's paper reused the injection data once to test the first Prompt Guard (71 in 100 caught at 1 false alarm in 100). The runner has no guardrail mode, its guardrail flag does nothing in the code read, and no CyberSecEval results were found for Prompt Guard 2 or the LlamaFirewall scanners. Any use of its data for guardrail testing is a suggestion, not something Meta describes.",
    "a good score does not make an app safe, and a bad one does not make a guardrail weak. Meta's paper reused the injection data once, to test the first Prompt Guard (71 in 100 caught at 1 false alarm in 100); the runner has no guardrail mode (its LlamaFirewall flag does nothing in the code read), and no results were found for Prompt Guard 2 or the LlamaFirewall scanners. Any use of its data for guardrail testing is a suggestion, not something Meta describes.")
rep("<li><b>None of the checkers acts.</b> You get a label, a decision or advice, and your app does the refusing.",
    "<li><b>None of the checkers stops a chat by itself.</b> You get a label, a decision or advice, and your app does the refusing (our reading of the code).")
io.open(p, 'w', encoding='utf-8', newline='\n').write(s)
print('ok')
