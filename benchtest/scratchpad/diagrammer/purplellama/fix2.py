import io
p = 'gen.py'
s = io.open(p, encoding='utf-8').read()
log = []


def rep(tag, a, b):
    global s
    assert a in s, (tag, a[:80])
    s = s.replace(a, b, 1)
    log.append(tag)


# ---- required
rep('RF1', "and Meta's test attaches the hidden-text scanner to tool output, and its docs give an example of hidden text in a PDF. No document-store integration",
    "and Meta's test attaches the hidden-text scanner to tool output. Meta's docs give an example of invisible text in a PDF, which they assign to the Prompt Guard and fixed-pattern scanners, not to the hidden-text scanner. No document-store integration")
rep('RF2a', "plus images and measuring, with an honest answer", "plus images and live monitoring, with an honest answer")
rep('RF2b', '''<tr><td>Measuring</td><td><span class="pill no">No</span></td><td><b>CyberSecEval</b> tests AI models before use and checks nothing in a live chat. It is not a barrier.</td></tr>''',
    '''<tr><td>Monitoring (live chats)</td><td><span class="pill no">No</span></td><td><b>CyberSecEval</b> tests AI models before use and checks nothing in a live chat; it is a measuring tool, not a barrier.</td></tr>''')
rep('RF3', "and AlignmentCheck has one benchmark.", "and AlignmentCheck has results only from Meta's own benchmark and one agent test (AgentDojo).")
rep('RF4a', "<td>Anyone: MIT-licensed; its Semgrep dependency has its own licence (an open question)</td>",
    "<td>Anyone: MIT-licensed; its Semgrep dependency has its own licence (LGPL 2.1), and what that means for a bench is an open question</td>")
rep('RF4b', "The Semgrep tool has its own licence terms, an open question.", "The Semgrep tool has its own licence (LGPL 2.1); whether it has consequences for a bench is an open question.")
rep('RF4c', "and the licence of the Semgrep tool is an open question.", "and whether the Semgrep tool's own licence (LGPL 2.1) has consequences for a bench is an open question.")
rep('RF5', "<td>Llama 3.1 or 3.2 text; Meta's pages differ</td>", "<td>Llama 3, 3.1 or 3.2 text; Meta's pages differ</td>")
rep('RF6', '''followed by <mark>the decoded hidden sentence</mark> (as in Meta's test)''',
    '''followed by <mark>the decoded hidden sentence</mark> (our reading of the code; Meta's test checks the block and the \\"Hidden ASCII\\" label)''')
rep('RF7', "LlamaFirewall's PyPI package (the public software index) and Code Shield's differ from that code in places, as the sections below say.",
    "Code Shield's PyPI package (the public software index) differs from that code in places, as its section below says; LlamaFirewall's PyPI package differs in three files, including how it fetches the Prompt Guard model.")
rep('RF8', "Llama Guard is one AI model that judges text and returns a verdict. It is a judge that reports; it never acts.",
    "Llama Guard is a single AI model from Meta that reads part of a chat and says whether it is harmful. It is a judge, not a security system: it gives a verdict, and your app decides what to do with it.")

# ---- optional accepted
rep('O1', "LlamaFirewall returns a result; it does not stop the chat itself.</figcaption>", "LlamaFirewall returns a result; it does not stop the chat itself (our reading of the code).</figcaption>")
rep('O2', "Purple Llama is Meta's open umbrella project", "Purple Llama is Meta's umbrella project")
rep('O3', "The period it keeps them is not stated, and its terms bar sending sensitive personal data.",
    "The period it keeps them is not stated. Its terms bar sending sensitive personal data and using the service for \"competitive analysis or benchmarking\".")
rep('O4', "<td>Anyone who accepts the Llama 4 licence and is approved; the terms leave a testing question open</td>",
    "<td>Anyone who accepts the Llama 4 licence and is approved, unless very large (over 700 million monthly users); the terms leave a testing question open</td>")
rep('O5', "every other scanner returns only 1.0 or 0.0", "every other built-in scanner returns only 1.0 or 0.0")
rep('O6', "LlamaFirewall 1.0.3 · scanners named as in Meta's code", "LlamaFirewall code at the commit read · short names for Meta's scanners")
rep('O7', 'A higher "fail" or "successful injection" percentage means more attacks got through the model.',
    'For the attack tests, a higher percentage of successful injections or of malicious or insecure replies means more attacks got through the model; for the over-refusal test, a higher refusal rate means more harmless requests were refused.')
rep('O8a', "Meta's paper reused the injection data once, to test the first Prompt Guard", "Meta's paper reused the injection data to test the first Prompt Guard")
rep('O8b', "Any use of its data for guardrail testing is a suggestion, not something Meta describes.",
    "Any use of its data for testing these guardrails is a suggestion; Meta describes it only for the first Prompt Guard.")
rep('O9', "<td>Not suited: they measure", "<td>Not likely to suit: they measure")
rep('O10a', "AlignmentCheck sends the whole trace and PIICheck sends the text to Together,", "AlignmentCheck sends the whole trace and the personal-data check sends the text to Together,")
rep('O10b', "<li><b>Failure behaviour varies.</b> PIICheck allows text when its call fails,", "<li><b>Failure behaviour varies.</b> The personal-data check allows text when its call fails,")
rep('O12', "human review required, the shape Meta's tutorial shows for a high-risk trace", "human review required, the shape Meta's tutorial shows for a high-risk trace (untested)")
rep('O13', "<td>No topic rules and no fixed replies. A custom scanner", "<td>Nothing official describes topic rules or fixed replies. A custom scanner")
rep('O14', "Meta Purple Llama · Prompt Guard 2, LlamaFirewall and Code Shield; CyberSecEval measures", "Meta Purple Llama · Prompt Guard 2, LlamaFirewall, Code Shield and CyberSecEval")

io.open(p, 'w', encoding='utf-8', newline='\n').write(s)
print(len(log), log)
