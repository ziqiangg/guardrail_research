# -*- coding: utf-8 -*-
"""Page parts for lionguard-explained.html (scratch, not committed)."""


def marker(mid, cls):
    return ('<marker id="%s" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            'orient="auto"><path d="M0,0 L10,5 L0,10 z" class="%s"/></marker>' % (mid, cls))


def defs(n, kinds, pad=10):
    m = {"": ("a%d" % n, "ah"), "o": ("a%do" % n, "ahok"), "n": ("a%dn" % n, "ahno")}
    p = " " * pad
    out = [p + "<defs>"]
    for k in kinds:
        out.append(p + "  " + marker(*m[k]))
    out.append(p + "</defs>")
    return "\n".join(out)


def fork(n, aria, in_t, in_s, g_t, g_s, lab_ok, lab_no, ok_t, ok_s, no_t, no_s, gcls="gate", pad=8):
    p = " " * pad
    L = []
    L.append(p + '<svg viewBox="0 0 760 250" role="img" aria-label="%s">' % aria)
    L.append(defs(n, ["", "o", "n"], pad + 2))
    L.append(p + '  <rect class="box" x="10" y="90" width="160" height="70" rx="8"/>')
    L.append(p + '  <text class="tb" x="90" y="120" text-anchor="middle">%s</text>' % in_t)
    L.append(p + '  <text class="ts" x="90" y="140" text-anchor="middle">%s</text>' % in_s)
    L.append(p + '  <line class="ln" x1="170" y1="125" x2="226" y2="125" marker-end="url(#a%d)"/>' % n)
    L.append(p + '  <rect class="%s" x="230" y="75" width="200" height="100" rx="8"/>' % gcls)
    L.append(p + '  <text class="tb" x="330" y="112" text-anchor="middle">%s</text>' % g_t)
    L.append(p + '  <text class="ts" x="330" y="132" text-anchor="middle">%s</text>' % g_s[0])
    L.append(p + '  <text class="ts" x="330" y="150" text-anchor="middle">%s</text>' % g_s[1])
    L.append(p + '  <path class="lok" d="M430,105 C470,105 470,55 506,55" marker-end="url(#a%do)"/>' % n)
    L.append(p + '  <path class="lno" d="M430,145 C470,145 470,195 506,195" marker-end="url(#a%dn)"/>' % n)
    L.append(p + '  <text class="tok" x="455" y="72" text-anchor="middle">%s</text>' % lab_ok)
    L.append(p + '  <text class="tno" x="460" y="185" text-anchor="end">%s</text>' % lab_no)
    L.append(p + '  <rect class="ok" x="510" y="25" width="240" height="60" rx="8"/>')
    L.append(p + '  <text class="tb" x="630" y="52" text-anchor="middle">%s</text>' % ok_t)
    L.append(p + '  <text class="ts" x="630" y="71" text-anchor="middle">%s</text>' % ok_s)
    L.append(p + '  <rect class="no dev" x="510" y="165" width="240" height="60" rx="8"/>')
    L.append(p + '  <text class="tb" x="630" y="192" text-anchor="middle">%s</text>' % no_t)
    L.append(p + '  <text class="ts" x="630" y="211" text-anchor="middle">%s</text>' % no_s)
    L.append(p + '</svg>')
    return "\n".join(L)


HEAD = '''<title>How GovTech LionGuard Scores a Conversation</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&family=Source+Sans+3:wght@400;600&family=JetBrains+Mono:wght@400&display=swap">
<style>
/* Layout: one reading column; overview map, four-way comparison, how it works, who supplies which part, then checkpoints (input, output), languages and accuracy, a scorecard and limits */
'''

ADDITIONS = '''
/* Additions for this page: links to sibling pages inside body text; maker tints for the "who supplies which part" map; score-scale bars */
.stage-head a, .know a { color: var(--accent); }
.mk-gov { fill: var(--gate-soft); stroke: var(--accent); stroke-width: 2; }
.mk-emb { fill: var(--surface); stroke: var(--accent); stroke-width: 1.5; stroke-dasharray: 3 3; }
.mk-nd { fill: var(--bg); stroke: var(--muted); stroke-width: 1.5; stroke-dasharray: 7 5; }
.mk-plan { fill: var(--bg); stroke: var(--line); stroke-width: 1.5; stroke-dasharray: 4 4; }
.bar-ok { fill: var(--pass-soft); stroke: var(--pass); stroke-width: 1.5; }
.bar-ed { fill: var(--edit-soft); stroke: var(--edit); stroke-width: 1.5; }
.bar-no { fill: var(--stop-soft); stroke: var(--stop); stroke-width: 1.5; }
.tick { stroke: var(--ink); stroke-width: 1.5; }
</style>
'''

HEADER = '''
<div class="wrap">

<header>
  <div class="eyebrow">GovTech LionGuard · open models: LionGuard 2, 2.1 and 2 Lite</div>
  <h1>How GovTech LionGuard scores a conversation</h1>
  <p class="lede">LionGuard is a small scoring model from Singapore's GovTech that looks for harmful content in English, Singlish, Chinese, Malay and Tamil. GovTech publishes it on Hugging Face, a public site for sharing AI models, and you run it yourself. Only the small classifier is GovTech's: LionGuard 2 and 2.1 send each text to OpenAI or Google Gemini to be turned into numbers first, and only Lite does that step on your own machine. For each text your app gets back a probability from 0 to 1 for every harm category, with no verdict and no cut-off supplied. This page shows how that works, where it fits in a chat, and what it leaves to your app.</p>
  <div class="legend" aria-label="Colour key">
    <span><i class="sw gate"></i>Check done by LionGuard</span>
    <span><i class="sw dev"></i>Your app's job (not LionGuard)</span>
    <span><i class="sw pass"></i>Allowed through</span>
    <span><i class="sw stop"></i>Stopped</span>
    <span><i class="sw na"></i>Not supported</span>
  </div>
</header>
'''

OVERVIEW = '''
<!-- OVERVIEW -->
<section class="overview">
  <figure>
    <svg viewBox="0 0 900 400" role="img" aria-label="A user's message is turned into numbers by an embedding step that another company runs, then scored by LionGuard's input check before it reaches the AI model. The AI model's answer goes through the same two steps before the user sees it. In both cases your app compares the scores with its own cut-off and refuses or discards. Documents fetched for the AI model have no dedicated LionGuard check, and actions the AI model takes have no LionGuard check.">
      <defs>
        <marker id="o-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" class="ah"/></marker>
      </defs>
      <rect class="box" x="10" y="170" width="100" height="60" rx="8"/>
      <text class="tb" x="60" y="197" text-anchor="middle">User</text>
      <text class="ts" x="60" y="216" text-anchor="middle">asks a question</text>

      <rect class="gate" x="150" y="155" width="170" height="90" rx="8"/>
      <text class="tb" x="235" y="188" text-anchor="middle">Input check</text>
      <text class="ts" x="235" y="208" text-anchor="middle">harmful content</text>
      <text class="ts" x="235" y="225" text-anchor="middle">· 11 probabilities</text>

      <rect class="box" x="370" y="160" width="130" height="80" rx="8"/>
      <text class="tb" x="435" y="192" text-anchor="middle">AI model</text>
      <text class="ts" x="435" y="212" text-anchor="middle">writes the answer</text>

      <rect class="gate" x="550" y="155" width="170" height="90" rx="8"/>
      <text class="tb" x="635" y="188" text-anchor="middle">Output check</text>
      <text class="ts" x="635" y="208" text-anchor="middle">harmful content</text>
      <text class="ts" x="635" y="225" text-anchor="middle">· 11 probabilities</text>

      <rect class="box" x="770" y="170" width="100" height="60" rx="8"/>
      <text class="tb" x="820" y="205" text-anchor="middle">User</text>

      <line class="ln" x1="110" y1="200" x2="146" y2="200" marker-end="url(#o-a)"/>
      <line class="ln" x1="320" y1="200" x2="366" y2="200" marker-end="url(#o-a)"/>
      <line class="ln" x1="500" y1="200" x2="546" y2="200" marker-end="url(#o-a)"/>
      <line class="ln" x1="720" y1="200" x2="766" y2="200" marker-end="url(#o-a)"/>
      <text class="ts" x="343" y="147" text-anchor="middle">if allowed</text>
      <text class="ts" x="523" y="147" text-anchor="middle">draft</text>
      <text class="ts" x="743" y="147" text-anchor="middle">if allowed</text>

      <!-- embedding steps: another company's (or local for Lite) -->
      <rect class="mk-emb" x="150" y="30" width="170" height="80" rx="8"/>
      <text class="tb" x="235" y="62" text-anchor="middle">Embedding step</text>
      <text class="ts" x="235" y="82" text-anchor="middle">OpenAI, Google or local</text>
      <path class="ln" d="M235,110 V151" marker-end="url(#o-a)"/>
      <text class="ts" x="245" y="136">numbers</text>

      <rect class="mk-emb" x="550" y="30" width="170" height="80" rx="8"/>
      <text class="tb" x="635" y="62" text-anchor="middle">Embedding step</text>
      <text class="ts" x="635" y="82" text-anchor="middle">OpenAI, Google or local</text>
      <path class="ln" d="M635,110 V151" marker-end="url(#o-a)"/>
      <text class="ts" x="645" y="136">numbers</text>

      <!-- documents: no dedicated check -->
      <rect class="na" x="350" y="30" width="170" height="80" rx="8"/>
      <text class="tb" x="435" y="62" text-anchor="middle">Your documents</text>
      <text class="ts" x="435" y="82" text-anchor="middle">no dedicated check</text>
      <path class="lna" d="M435,110 V156" marker-end="url(#o-a)"/>

      <!-- bottom row -->
      <path class="ln" d="M235,245 V306" marker-end="url(#o-a)"/>
      <text class="ts" x="245" y="280">probabilities</text>
      <rect class="gate dev" x="150" y="310" width="170" height="70" rx="8"/>
      <text class="tb" x="235" y="340" text-anchor="middle">Your app</text>
      <text class="ts" x="235" y="360" text-anchor="middle">applies its cut-off</text>

      <path class="lna" d="M435,240 V306" marker-end="url(#o-a)"/>
      <text class="ts" x="445" y="280">wants to act</text>
      <rect class="na" x="360" y="310" width="150" height="70" rx="8"/>
      <text class="tb" x="435" y="340" text-anchor="middle">Actions, tools</text>
      <text class="ts" x="435" y="360" text-anchor="middle">no LionGuard check</text>

      <path class="ln" d="M635,245 V306" marker-end="url(#o-a)"/>
      <text class="ts" x="645" y="280">probabilities</text>
      <rect class="gate dev" x="550" y="310" width="170" height="70" rx="8"/>
      <text class="tb" x="635" y="340" text-anchor="middle">Your app</text>
      <text class="ts" x="635" y="360" text-anchor="middle">discards the draft</text>
    </svg>
    <figcaption>LionGuard can score what the user sends and what the AI answers, one text at a time, after an embedding step that another company runs (OpenAI or Google) or, for Lite, that runs on your own machine. It has no dedicated check for documents fetched for the AI, and none for actions the AI takes. At every point it returns probabilities only; your app decides the cut-off and what happens next.</figcaption>
  </figure>
</section>
'''

POSITION = '''
<!-- FOUR-WAY -->
<section class="stage">
  <div class="stage-head">
    <div class="eyebrow">LionGuard, NeMo, Llama Guard and Sentinel</div>
    <h2>A small scorer you run, not a service or a framework</h2>
    <p>The four tools sit at different levels. <a href="nemo-rails-explained.html">NeMo</a> is a framework you run that decides where checks go. <a href="llama-guard-explained.html">Llama Guard</a> is one model you run that gives a verdict. <a href="sentinel-explained.html">Sentinel</a> is a web service run by GovTech that gives a score for each check. LionGuard is a small model that GovTech publishes and you run, which gives a probability for each harm category and needs another company's embedding model in front of it.</p>
  </div>

  <article class="rail">
    <div class="rail-head">
      <h3>1. Four different kinds of tool</h3>
      <span class="tag">What each one is, and what it hands back to your app</span>
    </div>
    <figure>
      <svg viewBox="0 0 760 300" role="img" aria-label="Four columns. NeMo Guardrails is a framework you run: it places the checks, runs your rules and calls safety models, and it gives allow or block. Llama Guard is one model you run, and it gives a safe or unsafe verdict. GovTech Sentinel is a hosted menu of checks that gives a score from 0 to 1 for each check. GovTech LionGuard is a small classifier you run, with another company's embedding model in front of it, and it gives 11 probabilities from 0 to 1 and no verdict.">
        <rect class="zone" x="10" y="20" width="170" height="260" rx="10"/>
        <text class="zl" x="26" y="44">NeMo Guardrails</text>
        <text class="ts" x="26" y="64">a framework you run</text>
        <rect class="box" x="22" y="80" width="146" height="44" rx="8"/>
        <text class="ts" x="95" y="107" text-anchor="middle">Places the checks</text>
        <rect class="box" x="22" y="134" width="146" height="44" rx="8"/>
        <text class="ts" x="95" y="161" text-anchor="middle">Runs your rules</text>
        <rect class="box" x="22" y="188" width="146" height="44" rx="8"/>
        <text class="ts" x="95" y="215" text-anchor="middle">Calls safety models</text>
        <text class="ts" x="95" y="262" text-anchor="middle">gives: allow or block</text>

        <rect class="gate" x="200" y="95" width="170" height="110" rx="8"/>
        <text class="tb" x="285" y="135" text-anchor="middle">Llama Guard</text>
        <text class="ts" x="285" y="157" text-anchor="middle">one model you run</text>
        <text class="ts" x="285" y="177" text-anchor="middle">reads text, judges it</text>
        <text class="ts" x="285" y="262" text-anchor="middle">gives: safe or unsafe</text>

        <rect class="zone" x="390" y="20" width="170" height="260" rx="10"/>
        <text class="zl" x="406" y="44">GovTech Sentinel</text>
        <text class="ts" x="406" y="64">a hosted menu of checks</text>
        <rect class="gate" x="402" y="80" width="146" height="44" rx="8"/>
        <text class="ts" x="475" y="107" text-anchor="middle">Harm and attack</text>
        <rect class="gate" x="402" y="134" width="146" height="44" rx="8"/>
        <text class="ts" x="475" y="161" text-anchor="middle">Off-topic, leakage</text>
        <rect class="gate" x="402" y="188" width="146" height="44" rx="8"/>
        <text class="ts" x="475" y="215" text-anchor="middle">Refusal, AWS checks</text>
        <text class="ts" x="475" y="262" text-anchor="middle">gives: a 0 to 1 score</text>

        <rect class="zone" x="580" y="20" width="170" height="260" rx="10"/>
        <text class="zl" x="596" y="44">GovTech LionGuard</text>
        <text class="ts" x="596" y="64">a small scorer you run</text>
        <rect class="mk-emb" x="592" y="80" width="146" height="44" rx="8"/>
        <text class="ts" x="665" y="107" text-anchor="middle">Other firm's embedder</text>
        <rect class="gate" x="592" y="134" width="146" height="44" rx="8"/>
        <text class="ts" x="665" y="161" text-anchor="middle">GovTech classifier</text>
        <rect class="gate" x="592" y="188" width="146" height="44" rx="8"/>
        <text class="ts" x="665" y="215" text-anchor="middle">2, 2.1 and 2 Lite</text>
        <text class="ts" x="665" y="254" text-anchor="middle">gives: 11 probabilities,</text>
        <text class="ts" x="665" y="270" text-anchor="middle">no verdict</text>
      </svg>
      <figcaption>Only NeMo acts on a result. Llama Guard, Sentinel and LionGuard all report, and your app (or a framework such as NeMo) does the refusing. LionGuard is also one of Sentinel's checks; that hosted service has its own page. This page claims no link between LionGuard and NeMo or Llama Guard.</figcaption>
    </figure>
    <div class="tablewrap">
      <table class="cats">
        <thead><tr><th></th><th>NeMo Guardrails</th><th>Llama Guard</th><th>GovTech Sentinel</th><th>GovTech LionGuard</th></tr></thead>
        <tbody>
          <tr><td>What it is</td><td>A framework around your chatbot</td><td>One AI model</td><td>A web service with a menu of checks</td><td>A small AI model that scores harmful content, in three versions</td></tr>
          <tr><td>Who runs it</td><td>You</td><td>You</td><td>GovTech (hosted); some models can be self-hosted</td><td>You run the classifier, which GovTech publishes; OpenAI or Google run the embedding step for versions 2 and 2.1</td></tr>
          <tr><td>What it hands back</td><td>Allow or block</td><td>Safe or unsafe, plus a category</td><td>A score from 0 to 1 per check</td><td>A probability from 0 to 1 for each of 11 outputs; no verdict</td></tr>
          <tr><td>Decides where checks run</td><td>Yes</td><td>No</td><td>No, your app chooses what text to send</td><td>No, your app chooses what text to score</td></tr>
          <tr><td>Your own rules and fixed replies</td><td>Yes</td><td>No</td><td>No</td><td>No</td></tr>
          <tr><td>Edits text</td><td>Masks personal data</td><td>No</td><td>Returns a masked copy (personal data, via AWS)</td><td>No, it returns probabilities only</td></tr>
          <tr><td>Singapore languages</td><td>Depends on the model it calls</td><td>Listed languages do not include Chinese, Malay or Tamil</td><td>LionGuard: Singlish, Chinese, Malay, partial Tamil</td><td>English, Singlish, Chinese, Malay and Tamil; the paper calls Tamil performance moderate</td></tr>
          <tr><td>Who can use it</td><td>Anyone (open source)</td><td>Anyone who accepts Meta's licence</td><td>Singapore Government public officers, closed beta</td><td>Model files are public on Hugging Face under a GovTech licence text; Lite also needs a Hugging Face login and acceptance of Google's Gemma terms</td></tr>
        </tbody>
      </table>
    </div>
    <p class="know"><b>Good to know:</b> the hosted <a href="sentinel-explained.html">Sentinel</a> service lists the same three LionGuard versions as one of its checks; how it serves them is covered on its own page, and this page is about running the models yourself.</p>
  </article>
</section>
'''

HOW = '''
<!-- HOW IT WORKS -->
<section class="stage">
  <div class="stage-head">
    <div class="eyebrow">How it works</div>
    <h2>Turn the text into numbers, then score each kind of harm</h2>
    <p>LionGuard works in two steps. First, an embedding model turns the text into a list of numbers, a kind of fingerprint of its meaning. Then GovTech's small classifier reads those numbers and gives a probability for each harm output. LionGuard 2, 2.1 and Lite differ only in which embedding model does the first step.</p>
  </div>

  <article class="rail">
    <div class="rail-head">
      <h3>2. One text in, eleven probabilities out</h3>
      <span class="tag">GovTech's models on Hugging Face, loaded and run by your own code</span>
    </div>
    <figure>
      <svg viewBox="0 0 760 270" role="img" aria-label="Your app sends one text to check, or a list of texts, with no system prompt or other chat context. The text first goes to an embedding step run by another company: OpenAI for LionGuard 2, Google Gemini for 2.1, or Google's EmbeddingGemma on your own machine for Lite. The resulting numbers go to GovTech's small classifier, which returns a probability from 0 to 1 for each of 11 outputs: an overall flag and six harm categories, four of them with two levels. It returns no verdict.">
        <defs>
          <marker id="a2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" class="ah"/></marker>
        </defs>
        <rect class="box" x="10" y="20" width="170" height="230" rx="8"/>
        <text class="tb" x="26" y="48">Your app sends</text>
        <text class="t" x="26" y="80">A text to check</text>
        <text class="ts" x="26" y="99">message or AI answer</text>
        <text class="t" x="26" y="130">Or a list of texts</text>
        <text class="ts" x="26" y="149">each scored on its own</text>
        <text class="t" x="26" y="180">No chat context</text>
        <text class="ts" x="26" y="199">no system prompt sent</text>

        <line class="ln" x1="180" y1="125" x2="204" y2="125" marker-end="url(#a2)"/>
        <rect class="mk-emb" x="208" y="70" width="150" height="110" rx="8"/>
        <text class="tb" x="283" y="102" text-anchor="middle">Embedding step</text>
        <text class="ts" x="283" y="122" text-anchor="middle">another company's</text>
        <text class="ts" x="283" y="140" text-anchor="middle">OpenAI or Google,</text>
        <text class="ts" x="283" y="158" text-anchor="middle">or local (Lite)</text>

        <line class="ln" x1="358" y1="125" x2="382" y2="125" marker-end="url(#a2)"/>
        <rect class="gate" x="386" y="70" width="140" height="110" rx="8"/>
        <text class="tb" x="456" y="102" text-anchor="middle">LionGuard</text>
        <text class="ts" x="456" y="122" text-anchor="middle">GovTech's classifier</text>
        <text class="ts" x="456" y="140" text-anchor="middle">a file of about 3 MB</text>
        <text class="ts" x="456" y="158" text-anchor="middle">no cut-off built in</text>
        <line class="ln" x1="526" y1="125" x2="550" y2="125" marker-end="url(#a2)"/>

        <rect class="box" x="554" y="20" width="196" height="230" rx="8"/>
        <text class="tb" x="570" y="48">LionGuard returns</text>
        <text class="t" x="570" y="80">11 probabilities</text>
        <text class="ts" x="570" y="99">0 to 1 each, no verdict</text>
        <text class="t" x="570" y="130">An overall flag</text>
        <text class="ts" x="570" y="149">is the text unsafe at all?</text>
        <text class="t" x="570" y="180">Six harm categories</text>
        <text class="ts" x="570" y="199">four with Level 1 and 2</text>
      </svg>
      <figcaption>The first step is the only part that differs between versions, and it is not GovTech's work (diagram 3). Your app can take the overall flag as its verdict, or the highest of the category probabilities. The paper keeps the overall flag because it boosts accuracy, and reports that about 4 in 100 examples show the flag and the categories disagreeing.</figcaption>
    </figure>
    <figure>
      <svg viewBox="0 0 760 110" role="img" aria-label="A score scale from 0 to 1 showing the bands on GovTech's public demo page. Below 0.40 passes, from 0.40 to below 0.70 warns, and 0.70 or above fails. The paper reports accuracy at a 0.5 point. GovTech ships no cut-off with the models.">
        <rect class="bar-ok" x="40" y="30" width="272" height="26" rx="4"/>
        <rect class="bar-ed" x="312" y="30" width="204" height="26"/>
        <rect class="bar-no" x="516" y="30" width="204" height="26" rx="4"/>
        <line class="tick" x1="40" y1="24" x2="40" y2="62"/>
        <line class="tick" x1="312" y1="24" x2="312" y2="62"/>
        <line class="tick" x1="380" y1="24" x2="380" y2="62"/>
        <line class="tick" x1="516" y1="24" x2="516" y2="62"/>
        <line class="tick" x1="720" y1="24" x2="720" y2="62"/>
        <text class="ts" x="40" y="18" text-anchor="middle">0</text>
        <text class="ts" x="312" y="18" text-anchor="middle">0.40</text>
        <text class="ts" x="380" y="18" text-anchor="middle">0.50</text>
        <text class="ts" x="516" y="18" text-anchor="middle">0.70</text>
        <text class="ts" x="720" y="18" text-anchor="start" dx="6">1</text>
        <text class="tok" x="176" y="84" text-anchor="middle">pass</text>
        <text class="ted" x="414" y="84" text-anchor="middle">warn</text>
        <text class="tno" x="618" y="84" text-anchor="middle">fail</text>
      </svg>
      <figcaption>LionGuard ships no cut-off. These bands come from GovTech's public demo page and are demo behaviour, not a recommendation; the paper reports its accuracy at 0.5. Your app chooses and tests its own cut-off, and could set one for each category.</figcaption>
    </figure>
    <p class="know"><b>Good to know:</b> GovTech states no maximum text length, so any limit comes from the embedding model: its owners list 8,192 tokens (short pieces of words) for OpenAI's and 2,048 for each of Google's two. What happens on longer text is not stated. For LionGuard 2 the paper reports about 300 tokens a second on one CPU, without saying whether that includes the call to OpenAI.</p>
  </article>

  <article class="rail">
    <div class="rail-head">
      <h3>The six harm categories and the overall flag</h3>
      <span class="tag">GovTech's model cards; 11 outputs in all</span>
    </div>
    <div class="tablewrap">
      <table class="cats">
        <thead><tr><th>Category</th><th>Level 1</th><th>Level 2 (more serious)</th></tr></thead>
        <tbody>
          <tr><td>Overall flag</td><td colspan="2">One flag for "unsafe in general", separate from the six categories</td></tr>
          <tr><td>Hateful</td><td>Discriminatory: derogatory or generalised negative statements about a protected group</td><td>Hate speech: explicit calls for harm or violence against a protected group</td></tr>
          <tr><td>Insults</td><td colspan="2">No levels: demeans, humiliates or mocks without referring to a protected trait</td></tr>
          <tr><td>Sexual</td><td>Not appropriate for minors: mild-to-moderate sexual content</td><td>Not appropriate for all ages: explicit or graphic sexual content</td></tr>
          <tr><td>Physical violence</td><td colspan="2">No levels: glorification of violence or threats of physical harm</td></tr>
          <tr><td>Self-harm</td><td>Ideation: expressions of suicidal thoughts or encouragement of self-harm</td><td>Action or suicide: descriptions of ongoing or imminent self-harm</td></tr>
          <tr><td>All other misconduct</td><td>Generally not socially accepted: unethical or immoral behaviour that is not necessarily illegal</td><td>Illegal activities: instructions or credible threats of serious harm; helping with crimes</td></tr>
        </tbody>
      </table>
    </div>
    <p class="know"><b>Good to know:</b> GovTech's playbook says that when a Level 2 instance is detected, Level 1 is also flagged by design. Every output belongs to harmful content or to the overall flag; none is a jailbreak or prompt-injection category.</p>
  </article>

  <article class="rail">
    <div class="rail-head">
      <h3>Which LionGuard</h3>
      <span class="tag">Three versions that share a method and differ only in the embedding model</span>
    </div>
    <div class="tablewrap">
      <table class="cats">
        <thead><tr><th>Version</th><th>Embedding step</th><th>Where your text goes</th><th>What you need</th><th>Published accuracy</th></tr></thead>
        <tbody>
          <tr><td>LionGuard 2</td><td>OpenAI's text-embedding-3-large</td><td>To OpenAI, to be embedded (our reading of the code)</td><td>Your own OpenAI key</td><td>Paper: F1 of 77 on GovTech's own test set</td></tr>
          <tr><td>LionGuard 2.1</td><td>Google's gemini-embedding-001</td><td>To Google, to be embedded (our reading of the code)</td><td>Your own Gemini key</td><td>Blog: F1 of 73 on a private GovTech test split</td></tr>
          <tr><td>LionGuard 2 Lite</td><td>Google's embeddinggemma-300m, run locally</td><td>Stays on your machine; the card says it "runs fully locally, with no external API calls"</td><td>A Hugging Face login and acceptance of Google's Gemma terms; no API key</td><td>None published</td></tr>
        </tbody>
      </table>
    </div>
    <p class="know"><b>Good to know:</b> GovTech's playbook recommends 2.1 "for best performance" and Lite "for local deployment". The classifier file is about 3 MB for 2 and 2.1 and about 1 MB for Lite. An older LionGuard 1 is also on Hugging Face; the LionGuard 2 paper says LionGuard 2 replaces it, and it is left out of this page.</p>
  </article>
</section>
'''

MAKERS = '''
<!-- WHO SUPPLIES WHAT -->
<section class="stage">
  <div class="stage-head">
    <div class="eyebrow">Behind the model</div>
    <h2>Who supplies which part</h2>
    <p>Only the small classifier is GovTech's. The embedding step in front of it comes from another company, or from Google's model running on your own machine, and some things GovTech does not say.</p>
  </div>

  <article class="rail">
    <div class="rail-head">
      <h3>3. Parts and who makes them</h3>
      <span class="tag">Grouped by who supplies the part; dashed boxes mean not disclosed or not yet available</span>
    </div>
    <figure>
      <svg viewBox="0 0 760 370" role="img" aria-label="Five rows. GovTech, published: the small classifier in three versions, with weights and code on Hugging Face, and open data, meaning a training-data subset and a public test set. Another company, hosted embedding step: OpenAI for LionGuard 2 and Google Gemini for 2.1, each needing your own key. Google, local embedding step: EmbeddingGemma for Lite, a gated download that needs a Hugging Face login and acceptance of Google's terms. Not disclosed or not published: training code, any accuracy for Lite, and an operating cut-off. Planned: a retrained LionGuard 2 for Sentinel users first, with no statement on whether it will be published on Hugging Face.">
        <text class="tb" x="10" y="44">GovTech</text>
        <text class="ts" x="10" y="62">published</text>
        <rect class="mk-gov" x="190" y="20" width="275" height="56" rx="8"/>
        <text class="tb" x="327" y="44" text-anchor="middle">Small classifier, 3 versions</text>
        <text class="ts" x="327" y="63" text-anchor="middle">weights and code on Hugging Face</text>
        <rect class="mk-gov" x="475" y="20" width="275" height="56" rx="8"/>
        <text class="tb" x="612" y="44" text-anchor="middle">Open data</text>
        <text class="ts" x="612" y="63" text-anchor="middle">training subset, public test set</text>

        <text class="tb" x="10" y="114">Another company</text>
        <text class="ts" x="10" y="132">embedding step, hosted</text>
        <rect class="mk-emb" x="190" y="90" width="275" height="56" rx="8"/>
        <text class="tb" x="327" y="114" text-anchor="middle">OpenAI</text>
        <text class="ts" x="327" y="133" text-anchor="middle">LionGuard 2 · your own key</text>
        <rect class="mk-emb" x="475" y="90" width="275" height="56" rx="8"/>
        <text class="tb" x="612" y="114" text-anchor="middle">Google Gemini</text>
        <text class="ts" x="612" y="133" text-anchor="middle">LionGuard 2.1 · your own key</text>

        <text class="tb" x="10" y="184">Google</text>
        <text class="ts" x="10" y="202">embedding step, local</text>
        <rect class="mk-emb" x="190" y="160" width="275" height="56" rx="8"/>
        <text class="tb" x="327" y="184" text-anchor="middle">EmbeddingGemma</text>
        <text class="ts" x="327" y="203" text-anchor="middle">Lite · runs on your machine</text>
        <rect class="mk-emb" x="475" y="160" width="275" height="56" rx="8"/>
        <text class="tb" x="612" y="184" text-anchor="middle">Gated download</text>
        <text class="ts" x="612" y="203" text-anchor="middle">login and accept Google's terms</text>

        <text class="tb" x="10" y="254">Not disclosed</text>
        <text class="ts" x="10" y="272">or not published</text>
        <rect class="mk-nd" x="190" y="230" width="180" height="56" rx="8"/>
        <text class="tb" x="280" y="254" text-anchor="middle">Training code</text>
        <text class="ts" x="280" y="273" text-anchor="middle">none found on GitHub</text>
        <rect class="mk-nd" x="380" y="230" width="180" height="56" rx="8"/>
        <text class="tb" x="470" y="254" text-anchor="middle">Lite accuracy</text>
        <text class="ts" x="470" y="273" text-anchor="middle">no figure published</text>
        <rect class="mk-nd" x="570" y="230" width="180" height="56" rx="8"/>
        <text class="tb" x="660" y="254" text-anchor="middle">Cut-off</text>
        <text class="ts" x="660" y="273" text-anchor="middle">none ships with it</text>

        <text class="tb" x="10" y="324">Planned</text>
        <text class="ts" x="10" y="342">not yet available</text>
        <rect class="mk-plan" x="190" y="300" width="275" height="56" rx="8"/>
        <text class="tb" x="327" y="324" text-anchor="middle">Retrained LionGuard 2</text>
        <text class="ts" x="327" y="343" text-anchor="middle">first for Sentinel users</text>
        <rect class="mk-nd" x="475" y="300" width="275" height="56" rx="8"/>
        <text class="tb" x="612" y="324" text-anchor="middle">Public release of it</text>
        <text class="ts" x="612" y="343" text-anchor="middle">not stated</text>
      </svg>
      <figcaption>The classifier is trained on top of a frozen embedding model, so LionGuard gets its view of the text from that model. The paper warns that an update to OpenAI's embedding model may need retraining. All three versions run GovTech's own code from the Hugging Face repository when loaded.</figcaption>
    </figure>
    <p class="know"><b>Good to know:</b> LionGuard 2 and 2.1 send each text to OpenAI or Google to be embedded, and Lite embeds on your own machine. That is our reading of GovTech's code; we have not tested it yet. Whether OpenAI's and Google's terms allow sending harmful or explicit test text is still to be verified.</p>
  </article>
</section>
'''

INPUT = '''
<!-- INPUT -->
<section class="stage">
  <div class="stage-head">
    <div class="eyebrow">Stage 1 · Input</div>
    <h2>Scoring what the user typed</h2>
    <p>This check scores the user's message before the AI model sees it. Your app compares each probability with its cut-off and decides whether to continue.</p>
  </div>

  <article class="rail">
    <div class="rail-head">
      <h3>4. Harmful content, Singapore-tuned</h3>
      <span class="tag">LionGuard 2, 2.1 or 2 Lite (GovTech) · input and output · <span class="pill yes">Yes</span></span>
    </div>
    <figure>
''' + fork(4,
           "The user's message is turned into numbers by the embedding step and scored by LionGuard, which gives a probability for each of 11 harm outputs. If every probability is below the app's cut-off, the message continues to the AI model. If one is above it, the app sends a refusal.",
           "User's message", "text, then numbers",
           "LionGuard", ["after the embedding step", "11 probabilities"],
           "all low", "a score high",
           "Continues to the AI model", "nothing changed",
           "Your app sends a refusal", "category tells you why", pad=6) + '''
      <figcaption>The scoring is the same for every language it covers: English, Singlish, Chinese, Malay and Tamil. Your app picks the cut-off and writes the refusal; LionGuard never blocks anything. The same model can score the AI's answer (diagram 5).</figcaption>
    </figure>
    <dl class="example">
      <dt>In</dt><dd>Give me step-by-step instructions to hurt my neighbour. (illustrative)</dd>
      <dt>Scores</dt><dd>overall flag high · physical violence high · the other outputs low (illustrative; no real values shown)</dd>
      <dt>Result</dt><dd>your app's cut-off decides; LionGuard does not refuse</dd>
    </dl>
    <p class="know"><b>Good to know:</b> on GovTech's own test set, LionGuard 2 scored 77 (F1, a 0 to 100 accuracy measure) against 55 for OpenAI's moderation tool and 27 for Llama Guard 4. That is GovTech's data, built around Singapore. GovTech reports no result for jailbreaks or prompt injection.</p>
  </article>
</section>
'''

OUTPUT = '''
<!-- OUTPUT -->
<section class="stage">
  <div class="stage-head">
    <div class="eyebrow">Stage 2 · Output</div>
    <h2>Scoring the AI's answer</h2>
    <p>The same model can read the AI's draft answer before the user sees it. There is no separate output version: you choose which text to send.</p>
  </div>

  <article class="rail">
    <div class="rail-head">
      <h3>5. Harmful content in the answer</h3>
      <span class="tag">LionGuard 2, 2.1 or 2 Lite (GovTech) · input and output · <span class="pill yes">Yes</span></span>
    </div>
    <figure>
''' + fork(5,
           "The AI model's draft answer is turned into numbers by the embedding step and scored by LionGuard, which gives a probability for each of 11 harm outputs. If every probability is below the app's cut-off, the answer is shown to the user. If one is above it, the app discards the draft and replies another way.",
           "AI's draft answer", "same two steps",
           "LionGuard", ["after the embedding step", "11 probabilities"],
           "all low", "a score high",
           "Answer shown to the user", "unchanged",
           "Your app discards the draft", "and replies another way", pad=6) + '''
      <figcaption>The paper describes LionGuard 2 as a "bidirectional filter" around a chatbot, screening user prompts and verifying model responses, and says it can also be used in testing an app's responses for unsafe content. Discarding and replying are your app's job.</figcaption>
    </figure>
    <dl class="example">
      <dt>Draft</dt><dd>Here are step-by-step instructions to hurt your neighbour. (illustrative)</dd>
      <dt>Scores</dt><dd>overall flag high · physical violence high (illustrative; no real values shown)</dd>
      <dt>Result</dt><dd>above your cut-off, so your app discards the draft</dd>
    </dl>
    <p class="know"><b>Good to know:</b> the model sees one text with no role and no chat history, so direction is only your choice of what to embed (our reading of the code; we have not tested it yet). Its training texts were mostly online comments (20,333 of 26,207), plus 2,098 synthetic rewrites in a chatbot style.</p>
  </article>
</section>
'''

LANG = '''
<!-- LANGUAGES -->
<section class="stage">
  <div class="stage-head">
    <div class="eyebrow">Input and output · Languages and accuracy</div>
    <h2>Five languages, with Tamil the weakest</h2>
    <p>LionGuard is tuned for English, Singlish, Chinese, Malay and Tamil. The published scores below are GovTech's own, on its own test data.</p>
  </div>

  <article class="rail">
    <div class="rail-head">
      <h3>What GovTech reports</h3>
      <span class="tag">F1, a 0 to 100 accuracy measure, at a 0.5 cut-off, rounded; GovTech's own results, not ours</span>
    </div>
    <div class="tablewrap">
      <table class="cats">
        <thead><tr><th>Test</th><th>LionGuard 2 (paper)</th><th>LionGuard 2.1 (blog)</th></tr></thead>
        <tbody>
          <tr><td>GovTech's own test set</td><td>77</td><td>73 (a private split, so not directly comparable with 77)</td></tr>
          <tr><td>Singlish (RabakBench)</td><td>88</td><td>86</td></tr>
          <tr><td>Chinese (RabakBench)</td><td>88</td><td>87</td></tr>
          <tr><td>Malay (RabakBench)</td><td>78</td><td>84</td></tr>
          <tr><td>Tamil (RabakBench)</td><td>67</td><td>73</td></tr>
        </tbody>
      </table>
    </div>
    <p class="know"><b>Good to know:</b> RabakBench is GovTech's own multilingual test set. The paper prints Chinese and Malay in a different order in two tables; this page follows the order that matches GovTech's blog. No figure is published for LionGuard 2 Lite. The paper says its training data had little to no Chinese, Malay or Tamil-only examples, so those languages rely on the embedding model carrying meaning across languages, and all the embedding models it tested did worse on Tamil.</p>
  </article>
</section>
'''

SCORE = '''
<!-- SCORECARD -->
<section class="stage">
  <div class="stage-head">
    <div class="eyebrow">At a glance</div>
    <h2>LionGuard at NeMo's five checkpoints</h2>
    <p>The same five places NeMo can check, with an honest answer for each.</p>
  </div>
  <div class="tablewrap">
    <table class="cats">
      <thead><tr><th>Checkpoint</th><th>LionGuard?</th><th>Why</th></tr></thead>
      <tbody>
        <tr><td>Input</td><td><span class="pill yes">Yes</span></td><td>Harmful content in the user's message, in five languages. There is no prompt-attack, off-topic or personal-data check.</td></tr>
        <tr><td>Output</td><td><span class="pill yes">Yes</span></td><td>The same scoring on the AI's draft answer. You choose which text to send.</td></tr>
        <tr><td>Retrieval (your documents)</td><td><span class="pill no">No</span></td><td>No dedicated check. The model scores one text with no role, so a passage could be sent to it, but nothing official describes this.</td></tr>
        <tr><td>Dialog (topics, fixed replies)</td><td><span class="pill no">No</span></td><td>No topic rules, no off-topic check and no replies. It scores harm categories only.</td></tr>
        <tr><td>Execution (actions, tools)</td><td><span class="pill no">No</span></td><td>No check for tool requests or actions. Nothing official describes scoring tool inputs or outputs.</td></tr>
      </tbody>
    </table>
  </div>
</section>
'''

LIMITS = '''
<!-- LIMITATIONS -->
<section class="stage">
  <div class="stage-head">
    <div class="eyebrow">Limitations</div>
    <h2>What LionGuard does not do, or does not tell us</h2>
  </div>
  <article class="rail">
    <ul class="limits">
      <li><b>It never acts.</b> You get probabilities, not decisions, and there is no official cut-off. Your app refuses, discards and replies.</li>
      <li><b>Only the small classifier is GovTech's.</b> LionGuard 2 and 2.1 depend on OpenAI's and Google's embedding services and your own key for each; Lite runs locally but needs a Hugging Face login and acceptance of Google's Gemma terms. Whether those companies' terms allow harmful test text is still to be verified.</li>
      <li><b>The licence texts are recorded, but how they relate is not stated.</b> The repository file says MIT licence subject to further conditions (Singapore law, arbitration, GovTech marks excluded); the paper says weights are published "exclusively for research and public interest purposes only".</li>
      <li><b>Little published accuracy.</b> LionGuard 2 has a paper; 2.1 has one blog table on a private test split; Lite has no figure. No operating threshold, maximum text length or Lite speed is stated.</li>
      <li><b>It scores harmful content only.</b> No result or claim is reported for jailbreaks or prompt injection, and there is no topic, document or tool check.</li>
      <li><b>Language limits.</b> Tamil is the weakest language, and the paper recommends human oversight in high-stakes settings.</li>
      <li><b>Its own sources disagree in places.</b> One code comment names a different OpenAI model than the card, the paper's two tables order Chinese and Malay differently, and the Sentinel docs spell the OpenAI model differently from the card.</li>
      <li><b>Updates and code are not fully open.</b> No training code was found on GitHub, and a retrained LionGuard 2 is announced for Sentinel users with no word on a public release. Each model runs GovTech's Python from its repository when loaded, so a bench could pin a revision. GovTech's hosted demo page may log submitted text to a Google Sheet and sends chat messages to OpenAI.</li>
    </ul>
  </article>
</section>
'''

FOOTER = '''
<footer>
  <p>Sources: GovTech's LionGuard model cards and code on Hugging Face (LionGuard 2, 2.1 and 2 Lite, each read at a fixed revision), its datasets and demo page, the GovTech Responsible AI playbook, GovTech's blog posts of 29 July 2025, 21 August 2026 and 28 September 2026, the LionGuard 2 paper (arXiv 2507.15339) and the RabakBench paper (arXiv 2507.05980), the Sentinel guardrails documentation (for the cross-reference only), and the embedding model owners' own pages from OpenAI and Google (for model identity, limits, access and terms only). Accuracy figures are GovTech's own reported results. Example messages in the stage sections are illustrative.</p>
  <p><a href="https://govtech-responsibleai.github.io/playbook/tools/lionguard/">Playbook: LionGuard</a> · <a href="https://huggingface.co/govtech/lionguard-2/tree/be4e38c988d3d5ec72a32a4bc84e8a6d5b76b591">LionGuard 2 model</a> · <a href="https://huggingface.co/govtech/lionguard-2.1/tree/1c3a9ea7718f81ea32e6688c0ff18ac8866525e8">LionGuard 2.1 model</a> · <a href="https://huggingface.co/govtech/lionguard-2-lite/tree/d56c17a08a937f2591a906fb5c8ec699a844c422">LionGuard 2 Lite model</a> · <a href="https://huggingface.co/govtech/lionguard-2/blob/be4e38c988d3d5ec72a32a4bc84e8a6d5b76b591/LICENSE">Repository licence</a> · <a href="https://huggingface.co/spaces/govtech/lionguard-demo/tree/4ade46d19acee9c9088c711533a7c47fe24a8e3b">Demo page</a> · <a href="https://huggingface.co/datasets/govtech/lionguard-2-synthetic-instruct/tree/8aa43f6172eb7eb158fd433fe3cf627c9a30db26">Training-data subset</a> · <a href="https://huggingface.co/datasets/govtech/RabakBench/tree/3c02a5b8574b0d0374d532704be6971e67532e22">RabakBench data</a> · <a href="https://arxiv.org/html/2507.15339">LionGuard 2 paper</a> · <a href="https://arxiv.org/html/2507.05980">RabakBench paper</a> · <a href="https://blog.ai.gov.sg/introducing-lionguard-2-multilingual-llm-guardrail-for-singapore/">Blog: LionGuard 2</a> · <a href="https://blog.ai.gov.sg/guardrails-in-the-wild-closing-the-retraining-loop-for-lionguard-2/">Blog: retraining loop</a> · <a href="https://blog.ai.gov.sg/decision-models-for-guardrails-exploring-jev-and-kev-for-moderation/">Blog: decision models</a> · <a href="https://www.aiguardian.gov.sg/docs/wiki/Sentinel-Guardrails">Sentinel guardrails</a> · <a href="https://developers.openai.com/api/docs/guides/embeddings">OpenAI embeddings</a> · <a href="https://ai.google.dev/gemini-api/docs/embeddings">Gemini embeddings</a> · <a href="https://huggingface.co/google/embeddinggemma-300m">EmbeddingGemma</a> · <a href="https://ai.google.dev/gemma/terms">Gemma terms</a></p>
</footer>

</div>
'''
