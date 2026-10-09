"""Builds benchtest/diagrams/presidio-explained.html (P10). Facts: presidio_two_level.md and presidio_inventory_final.md only."""
import io, os, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
SENT = os.path.join(ROOT, "benchtest", "diagrams", "sentinel-explained.html")
OUT = os.path.join(ROOT, "benchtest", "diagrams", "presidio-explained.html")

with io.open(SENT, encoding="utf-8", newline="") as f:
    sent = f.read().split("\n")
base_css = "\n".join(sent[5:109])  # lines 6-109, byte for byte
assert base_css.startswith(":root {") and base_css.endswith("ul.limits b { color: var(--ink); }")

line5 = "/* Layout: one reading column; overview map, parts and positioning, how it works, then checkpoints (input, output, reversible masking, images, your own patterns, retrieval, execution), a scorecard and limits */"
additions = """/* Additions for this page: tick marks on the score scale; let grid children shrink so only figures and tables scroll sideways on phones */
.tick { stroke: var(--ink); stroke-width: 1.5; }
.wrap > *, .stage > *, .grid2 > * { min-width: 0; }"""

# ---------- SVG helpers ----------
def marker(i, cls):
    return ('<marker id="%s" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
            '<path d="M0,0 L10,5 L0,10 z" class="%s"/></marker>' % (i, cls))

OFFS = {60: (27, [46]), 70: (30, [50, 68]), 80: (32, [52, 70]), 90: (33, [53, 70]), 100: (37, [57, 75])}

def box(cls, x, y, w, h, title, subs=(), ind="        "):
    tb, ts = OFFS[h]
    cx = x + w // 2
    out = [f'{ind}<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="8"/>',
           f'{ind}<text class="tb" x="{cx}" y="{y+tb}" text-anchor="middle">{title}</text>']
    for k, s in enumerate(subs):
        out.append(f'{ind}<text class="ts" x="{cx}" y="{y+ts[k]}" text-anchor="middle">{s}</text>')
    return "\n".join(out)

def svg(viewbox, aria, body, markers=()):
    defs = ""
    if markers:
        defs = "          <defs>\n" + "\n".join("            " + marker(i, c) for i, c in markers) + "\n          </defs>\n"
    return (f'        <svg viewBox="{viewbox}" role="img" aria-label="{aria}">\n{defs}{body}\n        </svg>')

IND = "          "

def fork(n, inp, gate, gate_cls, branch_ok, branch2, label_ok, label2, aria):
    """Fork geometry copied from the README. branch2 = (cls, title, subs). label2 is a .ts label."""
    b = []
    b.append(box("box", 10, 90, 160, 70, inp[0], inp[1:], IND))
    b.append(f'{IND}<line class="ln" x1="170" y1="125" x2="226" y2="125" marker-end="url(#a{n})"/>')
    b.append(box(gate_cls, 230, 75, 200, 100, gate[0], gate[1:], IND))
    b.append(f'{IND}<path class="lok" d="M430,105 C470,105 470,55 506,55" marker-end="url(#a{n}o)"/>')
    b.append(f'{IND}<path class="ln" d="M430,145 C470,145 470,195 506,195" marker-end="url(#a{n})"/>')
    b.append(f'{IND}<text class="tok" x="455" y="72" text-anchor="middle">{label_ok}</text>')
    b.append(f'{IND}<text class="ts" x="460" y="185" text-anchor="end">{label2}</text>')
    b.append(box("ok", 510, 25, 240, 60, branch_ok[0], branch_ok[1:], IND))
    b.append(box(branch2[0], 510, 165, 240, 60, branch2[1], [branch2[2]], IND))
    return svg("0 0 760 250", aria, "\n".join(b), [(f"a{n}", "ah"), (f"a{n}o", "ahok")])

def linear_edit(n, inp, gate, gate_cls, out, label, aria):
    b = []
    b.append(box("box", 10, 65, 160, 70, inp[0], inp[1:], IND))
    b.append(f'{IND}<line class="ln" x1="170" y1="100" x2="226" y2="100" marker-end="url(#a{n})"/>')
    b.append(box(gate_cls, 230, 50, 200, 100, gate[0], gate[1:], IND))
    b.append(f'{IND}<line class="led" x1="430" y1="100" x2="506" y2="100" marker-end="url(#a{n}e)"/>')
    b.append(f'{IND}<text class="ted" x="468" y="90" text-anchor="middle">{label}</text>')
    b.append(box("ed", 510, 65, 240, 70, out[0], out[1:], IND))
    return svg("0 0 760 200", aria, "\n".join(b), [(f"a{n}", "ah"), (f"a{n}e", "ahed")])

# ---------- Overview ----------
overview = f'''    <svg viewBox="0 0 900 400" role="img" aria-label="A user's message goes to Presidio's personal-data scan before it reaches the AI model. The AI model's draft answer goes through the same scan before the user sees it. In both places the scan only reports what it found and, if asked, returns a masked copy; your app decides what to do with the findings. Images, documents fetched for the AI model, and the text of tool calls can be scanned too, but only partly: images are in beta, and Presidio's own pages show no example for documents or tools. Presidio has no check for harmful content, prompt attacks or topics.">
      <defs>
        {marker("o-a", "ah")}
      </defs>
      <rect class="box" x="10" y="170" width="100" height="60" rx="8"/>
      <text class="tb" x="60" y="197" text-anchor="middle">User</text>
      <text class="ts" x="60" y="216" text-anchor="middle">asks a question</text>

      <rect class="gate" x="150" y="155" width="170" height="90" rx="8"/>
      <text class="tb" x="235" y="188" text-anchor="middle">Input scan</text>
      <text class="ts" x="235" y="208" text-anchor="middle">finds personal data</text>
      <text class="ts" x="235" y="225" text-anchor="middle">and can mask it</text>

      <rect class="box" x="370" y="160" width="130" height="80" rx="8"/>
      <text class="tb" x="435" y="192" text-anchor="middle">AI model</text>
      <text class="ts" x="435" y="212" text-anchor="middle">writes the answer</text>

      <rect class="gate" x="550" y="155" width="170" height="90" rx="8"/>
      <text class="tb" x="635" y="188" text-anchor="middle">Output scan</text>
      <text class="ts" x="635" y="208" text-anchor="middle">finds personal data</text>
      <text class="ts" x="635" y="225" text-anchor="middle">and can mask it</text>

      <rect class="box" x="770" y="170" width="100" height="60" rx="8"/>
      <text class="tb" x="820" y="205" text-anchor="middle">User</text>

      <line class="ln" x1="110" y1="200" x2="146" y2="200" marker-end="url(#o-a)"/>
      <line class="ln" x1="320" y1="200" x2="366" y2="200" marker-end="url(#o-a)"/>
      <line class="ln" x1="500" y1="200" x2="546" y2="200" marker-end="url(#o-a)"/>
      <line class="ln" x1="720" y1="200" x2="766" y2="200" marker-end="url(#o-a)"/>
      <text class="ts" x="343" y="147" text-anchor="middle">masked copy</text>
      <text class="ts" x="523" y="147" text-anchor="middle">draft</text>
      <text class="ts" x="743" y="147" text-anchor="middle">masked copy</text>

      <!-- images: beta -->
      <rect class="part" x="150" y="30" width="170" height="80" rx="8"/>
      <text class="tb" x="235" y="62" text-anchor="middle">Images</text>
      <text class="ts" x="235" y="82" text-anchor="middle">text in pictures only</text>
      <path class="ln" d="M235,110 V151" marker-end="url(#o-a)"/>

      <!-- documents: no Presidio example -->
      <rect class="part" x="350" y="30" width="170" height="80" rx="8"/>
      <text class="tb" x="435" y="62" text-anchor="middle">Your documents</text>
      <text class="ts" x="435" y="82" text-anchor="middle">no Presidio example</text>
      <path class="ln" d="M435,110 V156" marker-end="url(#o-a)"/>

      <!-- harm, attacks, topics: not supported -->
      <rect class="na" x="560" y="30" width="150" height="80" rx="8"/>
      <text class="tb" x="635" y="62" text-anchor="middle">Harm, attacks</text>
      <text class="ts" x="635" y="82" text-anchor="middle">no Presidio check</text>
      <path class="lna" d="M635,110 V151" marker-end="url(#o-a)"/>

      <!-- bottom row -->
      <path class="ln" d="M235,245 V306" marker-end="url(#o-a)"/>
      <text class="ts" x="245" y="280">findings</text>
      <rect class="gate dev" x="150" y="310" width="170" height="70" rx="8"/>
      <text class="tb" x="235" y="340" text-anchor="middle">Your app</text>
      <text class="ts" x="235" y="360" text-anchor="middle">decides what to do</text>

      <path class="ln" d="M435,240 V306" marker-end="url(#o-a)"/>
      <text class="ts" x="445" y="280">tool calls</text>
      <rect class="part" x="360" y="310" width="150" height="70" rx="8"/>
      <text class="tb" x="435" y="340" text-anchor="middle">Actions, tools</text>
      <text class="ts" x="435" y="360" text-anchor="middle">scans their data only</text>

      <path class="ln" d="M635,245 V306" marker-end="url(#o-a)"/>
      <text class="ts" x="645" y="280">findings</text>
      <rect class="gate dev" x="550" y="310" width="170" height="70" rx="8"/>
      <text class="tb" x="635" y="340" text-anchor="middle">Your app</text>
      <text class="ts" x="635" y="360" text-anchor="middle">keeps the key, if any</text>
    </svg>'''

# ---------- Diagram 1: positioning zones ----------
d1 = '''        <svg viewBox="0 0 760 300" role="img" aria-label="Two groups. Presidio is a toolkit of four separate parts that you call from your own code: the Analyzer finds personal data in text, the Anonymizer edits the text, the Image Redactor paints over personal data in pictures, and presidio-structured masks values in tables and JSON. It hands back findings or edited data, never a verdict. NeMo Guardrails is a framework that runs Presidio for its personal-data checks on the user's message, the AI's answer and passages from documents.">
          <rect class="zone" x="10" y="20" width="490" height="260" rx="10"/>
          <text class="zl" x="26" y="44">Presidio</text>
          <text class="ts" x="26" y="64">a toolkit of parts you call</text>
          <rect class="gate" x="26" y="80" width="225" height="70" rx="8"/>
          <text class="tb" x="138" y="108" text-anchor="middle">Analyzer</text>
          <text class="ts" x="138" y="128" text-anchor="middle">finds personal data in text</text>
          <rect class="gate" x="259" y="80" width="225" height="70" rx="8"/>
          <text class="tb" x="371" y="108" text-anchor="middle">Anonymizer</text>
          <text class="ts" x="371" y="128" text-anchor="middle">edits the text it is given</text>
          <rect class="gate" x="26" y="160" width="225" height="70" rx="8"/>
          <text class="tb" x="138" y="188" text-anchor="middle">Image Redactor (beta)</text>
          <text class="ts" x="138" y="208" text-anchor="middle">paints over text in pictures</text>
          <rect class="gate" x="259" y="160" width="225" height="70" rx="8"/>
          <text class="tb" x="371" y="188" text-anchor="middle">presidio-structured (alpha)</text>
          <text class="ts" x="371" y="208" text-anchor="middle">masks tables and JSON</text>
          <text class="ts" x="255" y="262" text-anchor="middle">gives: findings or edited data, no verdict</text>

          <rect class="zone" x="520" y="20" width="230" height="260" rx="10"/>
          <text class="zl" x="536" y="44">NeMo Guardrails</text>
          <text class="ts" x="536" y="64">a framework you run</text>
          <rect class="box" x="536" y="80" width="198" height="44" rx="8"/>
          <text class="t" x="635" y="107" text-anchor="middle">Calls Presidio on input</text>
          <rect class="box" x="536" y="134" width="198" height="44" rx="8"/>
          <text class="t" x="635" y="161" text-anchor="middle">Calls Presidio on output</text>
          <rect class="box" x="536" y="188" width="198" height="44" rx="8"/>
          <text class="t" x="635" y="215" text-anchor="middle">Calls it on retrieved text</text>
          <text class="ts" x="635" y="262" text-anchor="middle">see the NeMo page</text>
        </svg>'''

# ---------- Diagram 2: find, then edit (two rows) ----------
d2 = f'''        <svg viewBox="0 0 760 270" role="img" aria-label="Step one: your app sends text and a language code to the Analyzer, which returns a list of findings, each with a data type, a start and end position and a score from 0 to 1. Step two: your app passes the text, the findings and an edit for each data type to the Anonymizer, which returns the edited text and a list of the changes. Presidio keeps nothing between the two calls, so your app carries the findings across.">
          <defs>
            {marker("a2", "ah")}
          </defs>
          <rect class="box" x="10" y="25" width="210" height="80" rx="8"/>
          <text class="tb" x="115" y="57" text-anchor="middle">Your app sends</text>
          <text class="ts" x="115" y="77" text-anchor="middle">text + a language code</text>
          <text class="ts" x="115" y="95" text-anchor="middle">options are extra</text>
          <line class="ln" x1="220" y1="65" x2="276" y2="65" marker-end="url(#a2)"/>
          <rect class="gate" x="280" y="25" width="160" height="80" rx="8"/>
          <text class="tb" x="360" y="57" text-anchor="middle">Analyzer</text>
          <text class="ts" x="360" y="77" text-anchor="middle">finds personal data</text>
          <line class="ln" x1="440" y1="65" x2="486" y2="65" marker-end="url(#a2)"/>
          <rect class="box" x="490" y="25" width="260" height="80" rx="8"/>
          <text class="tb" x="620" y="57" text-anchor="middle">A list of findings</text>
          <text class="ts" x="620" y="77" text-anchor="middle">type · start · end</text>
          <text class="ts" x="620" y="95" text-anchor="middle">score from 0 to 1</text>

          <path class="ln" d="M620,105 V135 H115 V161" marker-end="url(#a2)"/>
          <text class="ts" x="372" y="128" text-anchor="middle">your app carries the findings across</text>

          <rect class="box" x="10" y="165" width="210" height="80" rx="8"/>
          <text class="tb" x="115" y="197" text-anchor="middle">Your app sends</text>
          <text class="ts" x="115" y="217" text-anchor="middle">text + findings</text>
          <text class="ts" x="115" y="235" text-anchor="middle">+ one edit per type</text>
          <line class="ln" x1="220" y1="205" x2="276" y2="205" marker-end="url(#a2)"/>
          <rect class="gate" x="280" y="165" width="160" height="80" rx="8"/>
          <text class="tb" x="360" y="197" text-anchor="middle">Anonymizer</text>
          <text class="ts" x="360" y="217" text-anchor="middle">applies the edits</text>
          <line class="ln" x1="440" y1="205" x2="486" y2="205" marker-end="url(#a2)"/>
          <rect class="box" x="490" y="165" width="260" height="80" rx="8"/>
          <text class="tb" x="620" y="197" text-anchor="middle">Edited text</text>
          <text class="ts" x="620" y="217" text-anchor="middle">+ a list of the changes</text>
          <text class="ts" x="620" y="235" text-anchor="middle">no score, no verdict</text>
        </svg>'''

# ---------- Score scale ----------
dscale = '''        <svg viewBox="0 0 760 110" role="img" aria-label="A score scale from 0 to 1. Presidio's default cut-off is 0, so every finding is returned. Presidio's docs use 0.4 and 0.7 as example cut-offs and recommend none; your app chooses its own.">
          <rect class="box" x="40" y="30" width="680" height="26" rx="4"/>
          <line class="tick" x1="40" y1="24" x2="40" y2="62"/>
          <line class="tick" x1="312" y1="24" x2="312" y2="62"/>
          <line class="tick" x1="516" y1="24" x2="516" y2="62"/>
          <line class="tick" x1="720" y1="24" x2="720" y2="62"/>
          <text class="ts" x="40" y="18" text-anchor="middle">0</text>
          <text class="ts" x="312" y="18" text-anchor="middle">0.4</text>
          <text class="ts" x="516" y="18" text-anchor="middle">0.7</text>
          <text class="ts" x="720" y="18" text-anchor="middle">1</text>
          <text class="ts" x="40" y="84" text-anchor="start">default: everything is returned</text>
          <text class="ts" x="312" y="84" text-anchor="middle">docs example</text>
          <text class="ts" x="516" y="84" text-anchor="middle">another docs example</text>
        </svg>'''

# ---------- Stage diagrams ----------
d3 = fork(3, ("User's message", "any text, one language"),
          ("Analyzer", "rules + a name model", "type, position, score"), "gate",
          ("Continues to the AI model", "nothing changed"),
          ("gate dev", "Your app decides", "mask, refuse or log"),
          "none", "found",
          "The user's message is sent to the Analyzer with a language code. The Analyzer returns a list of findings, each with a data type, a position and a score from 0 to 1. If it finds nothing, the message continues to the AI model unchanged. If it finds something, your app decides what to do: mask it, refuse the message or log it.")

d4 = linear_edit(4, ("Message + findings", "text and its findings"),
                 ("Anonymizer", "one edit per data type", "default: swap for a label"), "gate",
                 ("Masked message", "goes on to the AI model"), "edits",
                 "The user's message and the Analyzer's findings are sent to the Anonymizer. For each finding it applies the edit chosen for that data type, by default swapping the value for a label naming its type. The masked message continues to the AI model. Nothing is blocked, and anything the Analyzer missed stays in the text.")

d5 = linear_edit(5, ("AI's draft answer", "may contain names, emails"),
                 ("Find, then mask", "Analyzer, then Anonymizer", "same two steps as diagram 4"), "gate",
                 ("Edited answer shown", "personal data swapped for labels"), "edits",
                 "The AI model's draft answer is scanned by the Analyzer, and the Anonymizer swaps each finding for a label. The edited answer is shown to the user. Nothing is blocked, and anything the Analyzer misses is shown as written.")

d6 = f'''        <svg viewBox="0 0 760 270" role="img" aria-label="The user's message contains a name. The Anonymizer encrypts the name into a coded token, using a key that your app holds, and the AI model sees only the token. The AI model's answer comes back with the token in it. The decrypt step uses the same key to put the real name back, and the user sees the answer with the real name.">
          <defs>
            {marker("a6", "ah")}
            {marker("a6e", "ahed")}
          </defs>
{box("box", 10, 20, 190, 70, "User's message", ["contains a real name"], IND)}
          <line class="led" x1="200" y1="55" x2="276" y2="55" marker-end="url(#a6)"/>
{box("ed", 280, 20, 200, 70, "Encrypt", ["name becomes a token"], IND)}
          <line class="led" x1="480" y1="55" x2="556" y2="55" marker-end="url(#a6e)"/>
          <text class="ted" x="518" y="45" text-anchor="middle">token</text>
{box("box", 560, 20, 190, 70, "AI model", ["sees only the token"], IND)}
          <line class="ln" x1="655" y1="90" x2="655" y2="176" marker-end="url(#a6)"/>
          <text class="ts" x="645" y="138" text-anchor="end">answer with token</text>
{box("box", 560, 180, 190, 70, "AI's draft answer", ["still carries the token"], IND)}
          <line class="ln" x1="560" y1="215" x2="484" y2="215" marker-end="url(#a6)"/>
{box("ed", 280, 180, 200, 70, "Decrypt", ["token becomes the name"], IND)}
          <line class="led" x1="280" y1="215" x2="204" y2="215" marker-end="url(#a6e)"/>
{box("ed", 10, 180, 190, 70, "Shown to the user", ["real name restored"], IND)}
          <rect class="gate dev" x="290" y="104" width="180" height="62" rx="8"/>
          <text class="tb" x="380" y="130" text-anchor="middle">Your app</text>
          <text class="ts" x="380" y="150" text-anchor="middle">holds the key</text>
          <line class="ln" x1="380" y1="90" x2="380" y2="104"/>
          <line class="ln" x1="380" y1="166" x2="380" y2="180"/>
        </svg>'''
# fix: first arrow in d6 should be grey (message is unchanged), use marker a6 with .ln
d6 = d6.replace('<line class="led" x1="200" y1="55" x2="276" y2="55" marker-end="url(#a6)"/>',
                '<line class="ln" x1="200" y1="55" x2="276" y2="55" marker-end="url(#a6)"/>')
d6 = d6.replace('<line class="ln" x1="560" y1="215" x2="484" y2="215" marker-end="url(#a6)"/>',
                '<line class="ln" x1="560" y1="215" x2="484" y2="215" marker-end="url(#a6)"/>')

d7 = svg("0 0 760 200",
         "A picture, either sent by the user or returned in an answer, goes to the Image Redactor. It reads the words in the picture with OCR, which is software that reads text from images, runs the Analyzer on those words, and paints a solid box over each word that matches. The user or the AI model receives the picture with the boxes. Text that OCR cannot read is not found, and faces and signatures are not stated to be covered.",
         "\n".join([
             box("box", 10, 65, 160, 70, "Image", ["sent or returned"], IND),
             f'{IND}<line class="ln" x1="170" y1="100" x2="226" y2="100" marker-end="url(#a7)"/>',
             box("part", 230, 50, 200, 100, "OCR, then Analyzer", ["reads the words in it", "English by default"], IND),
             f'{IND}<line class="led" x1="430" y1="100" x2="506" y2="100" marker-end="url(#a7e)"/>',
             f'{IND}<text class="ted" x="468" y="90" text-anchor="middle">paints over</text>',
             box("ed", 510, 65, 240, 70, "Picture with solid boxes", ["over the matching words"], IND)]),
         [("a7", "ah"), ("a7e", "ahed")])

d8 = f'''        <svg viewBox="0 0 760 270" role="img" aria-label="Your app sends the text to scan, and your own pattern: a regular expression, which is a text-matching rule, or a list of words. Both go to the Analyzer, which runs your pattern alongside its built-in checks. It returns findings in the usual form, with the data type you named, the position and a score you set.">
          <defs>
            {marker("a8", "ah")}
          </defs>
{box("box", 10, 30, 190, 70, "Text to scan", ["prompt, answer or passage"], IND)}
{box("gate dev", 10, 170, 190, 70, "Your pattern", ["a rule or a word list"], IND)}
          <path class="ln" d="M200,65 C230,65 230,115 256,115" marker-end="url(#a8)"/>
          <path class="ln" d="M200,205 C230,205 230,155 256,155" marker-end="url(#a8)"/>
{box("gate", 260, 85, 200, 100, "Analyzer", ["built-in checks plus", "your pattern"], IND)}
          <line class="ln" x1="460" y1="135" x2="526" y2="135" marker-end="url(#a8)"/>
{box("box", 530, 100, 220, 70, "Findings, as usual", ["your type name, a score you set"], IND)}
        </svg>'''

d9 = linear_edit(9, ("Passages", "fetched for the AI model"),
                 ("Personal-data scan", "same Analyzer and", "Anonymizer as diagram 4"), "part",
                 ("Passages with labels", "masked copies go to the AI"), "edits",
                 "Passages fetched from your documents are scanned with the same Analyzer and Anonymizer. Each finding is swapped for a label before the passages are handed to the AI model. Presidio's own pages show no example of this; it is the same call on a different piece of text.")

d10 = linear_edit(10, ("Tool result", "a table or a JSON object"),
                  ("presidio-structured", "maps columns to data types", "then masks every value"), "part",
                  ("Same table or object", "values masked in place"), "masks",
                  "A tool's result, held as a table or a JSON object, is passed to presidio-structured. It analyses the values to decide which columns or keys hold personal data, then applies an edit to every value in them. The same table or object comes back with those values masked. Whether the tool call itself is allowed is not checked.")

# ---------- Body ----------
def pill(k, t):
    return f'<span class="pill {k}">{t}</span>'

body = f'''
<div class="wrap">

<header>
  <div class="eyebrow">Data Privacy Stack Presidio · release 2.2.364, created at Microsoft</div>
  <h1>How Presidio masks a conversation</h1>
  <p class="lede">Presidio is an open-source toolkit for finding and hiding personal data in text, images and tables. It was created at Microsoft and is moving to a community-run group, Data Privacy Stack; you run it yourself. Your app gives it a piece of text; it hands back where personal data sits (names, emails, ID numbers) with a score from 0 to 1 for each, and, as a separate step, an edited copy with that data masked. It never blocks anything. This page shows what it finds, where it fits in a chat, and what it leaves to your app.</p>
  <div class="legend" aria-label="Colour key">
    <span><i class="sw gate"></i>Check done by Presidio</span>
    <span><i class="sw dev"></i>Your app's job (not Presidio)</span>
    <span><i class="sw pass"></i>Allowed through</span>
    <span><i class="sw edit"></i>Changed, then allowed</span>
    <span><i class="sw part"></i>Partly supported</span>
    <span><i class="sw na"></i>Not supported</span>
  </div>
</header>

<!-- OVERVIEW -->
<section class="overview">
  <figure>
{overview}
    <figcaption>Presidio scans for personal data in what the user sends and in what the AI answers, and can hand back a masked copy. Pictures, documents and the data tools send and return are covered only in part. It has no check for harmful content, prompt attacks or topics. At every point your app decides what to do with the findings, and if it uses reversible masking, your app holds the key.</figcaption>
  </figure>
</section>

<!-- POSITIONING -->
<section class="stage">
  <div class="stage-head">
    <div class="eyebrow">Presidio and NeMo</div>
    <h2>A toolkit of parts, not a judge</h2>
    <p>Presidio does not decide whether a message is safe. It finds personal data and, if asked, edits it. NeMo Guardrails calls Presidio for its personal-data checks, and Llama Guard and Sentinel have their own pages.</p>
  </div>

  <article class="rail">
    <div class="rail-head">
      <h3>1. Four parts you call from your own code</h3>
      <span class="tag">What Presidio is, and how it relates to NeMo Guardrails</span>
    </div>
    <figure>
{d1}
      <figcaption>The Presidio docs call it "a library or SDK rather than a service": you add the parts to your own software or run them as services of your own. NeMo's personal-data masking on output and on retrieved passages (diagrams 4 and 5 on the NeMo page) runs Presidio.</figcaption>
    </figure>
    <div class="tablewrap">
      <table class="cats">
        <thead><tr><th>Part</th><th>Takes in</th><th>Hands back</th><th>How you run it</th><th>Maturity</th></tr></thead>
        <tbody>
          <tr><td>Analyzer</td><td>One piece of text and a language code</td><td>A list of findings: type, start, end, score from 0 to 1</td><td>Python package (a code library), or a Docker image (a ready-to-run bundle) with a web service</td><td>No pre-release warning found</td></tr>
          <tr><td>Anonymizer</td><td>The text, the Analyzer's findings and an edit for each type</td><td>The edited text and a list of the changes</td><td>Python package, or a Docker image</td><td>No pre-release warning found</td></tr>
          <tr><td>Image Redactor</td><td>A picture, or a medical (DICOM) image file</td><td>The picture with solid boxes over matching text</td><td>Python package (the text-reading software, OCR, is installed separately), or a Docker image</td><td>Beta: "not production ready"</td></tr>
          <tr><td>presidio-structured</td><td>A table or a JSON object (a standard format for structured data)</td><td>The same table or object with the values in personal-data columns or keys masked</td><td>Python package only; no web service or Docker image found</td><td>Alpha</td></tr>
        </tbody>
      </table>
    </div>
    <div class="tablewrap">
      <table class="cats">
        <thead><tr><th></th><th>Presidio</th></tr></thead>
        <tbody>
          <tr><td>Who made it</td><td>Created at Microsoft. The project is "in the process of transitioning" to an independent, community-governed organisation, Data Privacy Stack, and Microsoft supports the move.</td></tr>
          <tr><td>Who runs it</td><td>You. The FAQ says it "is not an official product of any company and comes with no warranty or SLA" (a promised service level).</td></tr>
          <tr><td>Who can use it</td><td>Anyone: it is open source under the MIT licence (a common open-source licence), which the project says will stay.</td></tr>
          <tr><td>What it hands back</td><td>Findings with scores, or edited text, images and tables. Never a pass or fail.</td></tr>
          <tr><td>Decides where checks run</td><td>No. Your app chooses which text, image or table to send. There is no setting for input versus output.</td></tr>
          <tr><td>Edits text</td><td>Yes, through the Anonymizer: swap, remove, mask, hash, encrypt and more.</td></tr>
          <tr><td>Languages</td><td>English by default. Other languages need changes to both the name model and the detectors (called recognisers); no accuracy is published for any non-English one.</td></tr>
        </tbody>
      </table>
    </div>
  </article>
</section>

<!-- HOW IT WORKS -->
<section class="stage">
  <div class="stage-head">
    <div class="eyebrow">How it works</div>
    <h2>Find the personal data first, then edit it</h2>
    <p>Finding and editing are two separate calls. The Analyzer says where personal data is; the Anonymizer changes the text where your app tells it to.</p>
  </div>

  <article class="rail">
    <div class="rail-head">
      <h3>2. Two calls: find, then edit</h3>
      <span class="tag">Analyzer and Anonymizer, as Python code or as web requests</span>
    </div>
    <figure>
{d2}
      <figcaption>The Analyzer runs a set of recognisers, small detectors that each look for one or more data types. Presidio keeps no memory between calls, so your app carries the findings from the first call to the second. The Anonymizer finds nothing itself: personal data the Analyzer misses stays in the text. The same calls work on a prompt, an answer or any other text.</figcaption>
    </figure>
    <figure>
{dscale}
      <figcaption>A score is the Analyzer's confidence from 0 to 1. The default cut-off is 0, so every finding comes back and your app can raise it. The docs recommend no cut-off for the default setup: 0.4 and 0.7 appear only as examples, and Presidio's own demo notebook used 0.4.</figcaption>
    </figure>
  </article>

  <article class="rail">
    <div class="rail-head">
      <h3>What Presidio can find</h3>
      <span class="tag">Grouped from the supported-entities page and the default recogniser file</span>
    </div>
    <div class="tablewrap">
      <table class="cats">
        <thead><tr><th>Group</th><th>Example types</th><th>In a default English setup</th></tr></thead>
        <tbody>
          <tr><td>Contact and money</td><td class="code">EMAIL_ADDRESS<br>PHONE_NUMBER<br>CREDIT_CARD<br>IBAN_CODE</td><td>On, together with IP addresses, web addresses, dates and times, and Bitcoin addresses. The phone check tests numbers against eight regions (US, GB, DE, FR, IL, IN, CA, BR); Singapore is not one of them.</td></tr>
          <tr><td>Names and places</td><td class="code">PERSON<br>LOCATION</td><td>On, found by a name model from the spaCy language toolkit. Every hit starts with the same fixed score, 0.85.</td></tr>
          <tr><td>United States IDs</td><td class="code">US_SSN<br>US_PASSPORT<br>US_DRIVER_LICENSE</td><td>On for five of seven types (SSN is the US social security number). The other two are off.</td></tr>
          <tr><td>United Kingdom IDs</td><td class="code">UK_NHS</td><td>Only the NHS number is on. Driving licence, national insurance number, passport, postcode and vehicle registration are off.</td></tr>
          <tr><td>Singapore</td><td class="code">SG_NRIC_FIN<br>SG_UEN</td><td>The NRIC and FIN pattern (Singapore's national ID numbers) is switched off in the default file. The UEN type (a business registration number) is on the entity page but has no entry in the default file, so whether it runs is open.</td></tr>
          <tr><td>Other countries</td><td class="code">AU_TFN<br>IN_AADHAAR<br>DE_TAX_ID<br>KR_RRN</td><td>Off. The file holds types for Australia, India, Korea, Germany, Sweden, Turkey, Thailand, South Africa, Nigeria, the Philippines and Canada. Finland has no entry in it.</td></tr>
          <tr><td>Spain, Italy, Poland</td><td class="code">ES_NIF<br>IT_FISCAL_CODE<br>PL_PESEL</td><td>Marked on in the file, but the default setup loads English only, so they do not run. That is our reading of the code; it matches the type list in the vendor's notebook.</td></tr>
          <tr><td>Medical terms</td><td class="code">MEDICAL_MEDICATION<br>MEDICAL_HISTORY</td><td>Off. They need an extra install and a third-party model, so they are not part of a default setup.</td></tr>
          <tr><td>Secrets</td><td class="code">none</td><td>No type exists for API keys, passwords or other secrets. The pages and the default file were checked; nothing is disclosed.</td></tr>
        </tbody>
      </table>
    </div>
    <p class="know"><b>Good to know:</b> the entity page lists 80 distinct types (our count). In the default file, 24 of 74 recogniser entries are switched on. The docs say "there is no guarantee that Presidio will find all sensitive information".</p>
  </article>

  <article class="rail">
    <div class="rail-head">
      <h3>What the Anonymizer can do to a finding</h3>
      <span class="tag">Eight edits; "replace" is the default</span>
    </div>
    <div class="tablewrap">
      <table class="cats">
        <thead><tr><th>Edit</th><th>What it does</th><th>Can Presidio undo it?</th></tr></thead>
        <tbody>
          <tr><td class="code">replace</td><td>Swaps the value for a label such as &lt;PHONE_NUMBER&gt; (the default), or for text you choose.</td><td>No</td></tr>
          <tr><td class="code">redact</td><td>Removes the value completely.</td><td>No</td></tr>
          <tr><td class="code">mask</td><td>Overwrites characters with one you pick. You say how many, and from which end.</td><td>No</td></tr>
          <tr><td class="code">hash</td><td>Swaps the value for a one-way scrambled code (a salted hash). The same value gives the same code only if you supply the same salt, the extra input that makes it unique.</td><td>No</td></tr>
          <tr><td class="code">custom</td><td>Swaps the value for the result of your own function. Python only; the web service refuses it.</td><td>Depends on your function</td></tr>
          <tr><td class="code">keep</td><td>Leaves the value in the text but still lists it in the changes.</td><td>Nothing changed</td></tr>
          <tr><td class="code">surrogate_ahds</td><td>Writes realistic stand-in values using Azure Health Data Services. Needs an Azure account.</td><td>No</td></tr>
          <tr><td class="code">encrypt</td><td>Encrypts the value (with AES, a standard encryption method) into a coded token.</td><td>Yes, with the decrypt step and the same key</td></tr>
        </tbody>
      </table>
    </div>
    <p class="know"><b>Good to know:</b> a hash gets a random salt unless you give one, so the same name hashes differently each time by default. Presidio keeps no session, so your app must keep any salt or key itself.</p>
  </article>
</section>

<!-- INPUT -->
<section class="stage">
  <div class="stage-head">
    <div class="eyebrow">Stage 1 · Input</div>
    <h2>Finding and masking what the user typed</h2>
    <p>These two steps look at the user's message before the AI model sees it. Presidio does the finding and the masking; your app decides what to do with the findings.</p>
  </div>

  <div class="grid2">
    <article class="rail">
      <div class="rail-head">
        <h3>3. Finding personal data in a message</h3>
        <span class="tag">Analyzer · input and output · {pill("yes", "Yes")}</span>
      </div>
      <figure>
{d3}
        <figcaption>Presidio returns where the data is, never whether the message may go on. With the default setting every finding comes back, and your app can raise the cut-off. You can ask for only some types.</figcaption>
      </figure>
      <dl class="example">
        <dt>In</dt><dd>You can reach Jane Tan at jane.tan@example.com.</dd>
        <dt>Result</dt><dd>PERSON and EMAIL_ADDRESS, each with start, end and a score from 0 to 1 (illustrative)</dd>
      </dl>
      <p class="know"><b>Good to know:</b> in Presidio's own demo notebook (1,500 made-up text samples, default detectors, cut-off 0.4), about 7 in 10 of the things it flagged were real and it found about 6 in 10 of the personal data present. The notebook calls default settings "not recommended for production". These are Presidio's numbers on synthetic data; ours may differ.</p>
    </article>

    <article class="rail">
      <div class="rail-head">
        <h3>4. Masking it before the AI sees it</h3>
        <span class="tag">Anonymizer · input · {pill("yes", "Yes")}</span>
      </div>
      <figure>
{d4}
        <figcaption>Nothing is blocked. The message still goes on, with each finding swapped for a label naming its type. The masked text is the Anonymizer's output; your app has to pass that copy on to the AI model.</figcaption>
      </figure>
      <dl class="example">
        <dt>In</dt><dd>My NRIC is S1234567D, email tan@example.com. (illustrative)</dd>
        <dt>Masked</dt><dd>My NRIC is S1234567D, email <mark>&lt;EMAIL_ADDRESS&gt;</mark>. (expected in a default setup; not tested)</dd>
      </dl>
      <p class="know"><b>Good to know:</b> the example shows why the default setup matters: the Singapore NRIC pattern is switched off in the default file, so it is not expected to be masked until you turn it on. The Anonymizer only edits what the Analyzer found.</p>
    </article>
  </div>
</section>

<!-- OUTPUT -->
<section class="stage">
  <div class="stage-head">
    <div class="eyebrow">Stage 2 · Output</div>
    <h2>Masking personal data in the AI's answer</h2>
    <p>The same two steps can run on the AI's draft answer before the user sees it. Presidio has no input or output setting; your app chooses which text to send.</p>
  </div>

  <article class="rail">
    <div class="rail-head">
      <h3>5. Masking personal data in an answer</h3>
      <span class="tag">Analyzer and Anonymizer · output · {pill("yes", "Yes")}</span>
    </div>
    <figure>
{d5}
      <figcaption>Nothing is blocked here either. The answer still goes out, with each finding swapped for a label. You choose which edit to use for each type of data.</figcaption>
    </figure>
    <dl class="example">
      <dt>Draft</dt><dd>You can reach Jane Tan at jane.tan@example.com.</dd>
      <dt>Shown</dt><dd>You can reach <mark>&lt;PERSON&gt;</mark> at <mark>&lt;EMAIL_ADDRESS&gt;</mark>.</dd>
    </dl>
    <p class="know"><b>Good to know:</b> no Presidio page shows the calls on an AI's answer; they are the same calls on a different piece of text. That is our reading of the code; we have not tested it yet. The vendor's LiteLLM page covers masking on the way in, using LiteLLM, a separate product that sits between your app and the AI model.</p>
  </article>
</section>

<!-- REVERSIBLE -->
<section class="stage">
  <div class="stage-head">
    <div class="eyebrow">Input and output · Reversible masking</div>
    <h2>Hiding a name from the AI model, then putting it back</h2>
    <p>Most masking cannot be undone. Presidio's encrypt edit can, because your app keeps the key. It is the only edit with a built-in way back.</p>
  </div>

  <article class="rail">
    <div class="rail-head">
      <h3>6. Encrypt before the AI, decrypt after</h3>
      <span class="tag">Anonymizer encrypt and decrypt · input and output · {pill("yes", "Yes")}</span>
    </div>
    <figure>
{d6}
      <figcaption>The AI model never sees the real name, yet the user does. Presidio's docs show three routes: encryption (shown here), a mapping your app keeps (a sample), and LiteLLM restoring masked labels in the answer. A sample from the vendor describes the same idea for chats with an OpenAI model.</figcaption>
    </figure>
    <dl class="example">
      <dt>To AI</dt><dd>Write a polite reply to <mark>[a 44-character coded token]</mark>. (illustrative)</dd>
      <dt>Draft</dt><dd>Dear <mark>[the same token]</mark>, thank you for your message. (illustrative)</dd>
      <dt>Shown</dt><dd>Dear <mark>Jane Tan</mark>, thank you for your message. (illustrative)</dd>
    </dl>
    <p class="know"><b>Good to know:</b> Presidio keeps no memory between calls, so your app must hold the key and find the token again if the AI model moves or edits it. The docs give no guidance on where to store keys, and their web example puts the key in the request body of a service with no built-in login.</p>
  </article>
</section>

<!-- IMAGES -->
<section class="stage">
  <div class="stage-head">
    <div class="eyebrow">Stage 2b · Images</div>
    <h2>Painting over personal data in pictures</h2>
    <p>The Image Redactor reads the words in a picture, looks for personal data in them, and paints over each match. The package is marked beta.</p>
  </div>

  <article class="rail">
    <div class="rail-head">
      <h3>7. Text inside an image</h3>
      <span class="tag">Image Redactor (beta), with OCR · input and output · {pill("partly", "Partly")}</span>
    </div>
    <figure>
{d7}
      <figcaption>OCR (optical character recognition) is software that reads text from a picture; the default one, Tesseract, is installed separately. The box is a solid fill, black by default. A second engine handles medical DICOM scans, but it only paints over text in the pixels, not in the file's metadata.</figcaption>
    </figure>
    <dl class="example">
      <dt>In</dt><dd>a screenshot showing "Jane Tan, jane.tan@example.com" (illustrative)</dd>
      <dt>Result</dt><dd>the same picture with solid boxes over the name and the email (illustrative)</dd>
    </dl>
    <p class="know"><b>Good to know:</b> the docs say the package is "still in beta and not production ready". Whether faces, signatures, handwriting or QR codes are covered is not stated. The only figures are from a demo on four medical sample files, which is a demonstration, not a benchmark; no accuracy is published for ordinary images.</p>
  </article>
</section>

<!-- CUSTOM PATTERNS -->
<section class="stage">
  <div class="stage-head">
    <div class="eyebrow">Input and output · Your own patterns</div>
    <h2>Adding detectors for your own data</h2>
    <p>You can teach the Analyzer new kinds of data, such as an internal staff ID or a list of titles. This is the closest Presidio comes to a forbidden-word list, but it reports matches; it does not block.</p>
  </div>

  <article class="rail">
    <div class="rail-head">
      <h3>8. A pattern or word list of your own</h3>
      <span class="tag">Custom patterns and word lists · input and output · {pill("yes", "Yes")}</span>
    </div>
    <figure>
{d8}
      <figcaption>A regular expression is a text-matching rule, such as "five digits in a row". You give each pattern a score; a word list scores 1.0 unless you say otherwise. Context words near a match can raise its score. An allow list does the opposite: it stops chosen values being reported.</figcaption>
    </figure>
    <dl class="example">
      <dt>Rule</dt><dd>Word list TITLE: Mr., Mrs., Miss (Presidio's docs)</dd>
      <dt>In</dt><dd>Mr. Schmidt</dd>
      <dt>Result</dt><dd>TITLE found at "Mr.", score 1.0 (the word-list default)</dd>
    </dl>
    <p class="know"><b>Good to know:</b> patterns match letters, not meaning, so a reworded or disguised value is missed. A pattern you send to the web service runs on the server, with a 60-second timeout by default, and the docs say that service has no built-in login. NeMo's regex blocklist blocks a message; a Presidio pattern leaves that decision to your app.</p>
  </article>
</section>

<!-- RETRIEVAL -->
<section class="stage">
  <div class="stage-head">
    <div class="eyebrow">Stage 3 · Retrieval, partly</div>
    <h2>Scanning passages from your documents</h2>
    <p>Presidio has no document-specific check. Its text steps work on any text, so passages fetched for the AI model can be scanned before the model reads them.</p>
  </div>

  <article class="rail">
    <div class="rail-head">
      <h3>9. Passages before the AI reads them</h3>
      <span class="tag">Analyzer and Anonymizer on retrieved text · {pill("partly", "Partly")}</span>
    </div>
    <figure>
{d9}
      <figcaption>The AI model cannot repeat personal data it was never shown. Same steps as diagram 4, but run earlier, on your documents.</figcaption>
    </figure>
    <p class="know"><b>Good to know:</b> Presidio's own pages never show it on retrieved passages; NVIDIA's NeMo docs do run Presidio on retrieved chunks. That is our reading of the code for Presidio itself; we have not tested it yet.</p>
  </article>
</section>

<!-- EXECUTION -->
<section class="stage">
  <div class="stage-head">
    <div class="eyebrow">Stage 5 · Execution, partly</div>
    <h2>Masking tables and JSON, such as tool results</h2>
    <p>Presidio does not check whether an action should run. It can mask the data a tool sends or returns, if that data is a table or a JSON object.</p>
  </div>

  <article class="rail">
    <div class="rail-head">
      <h3>10. Personal data in a tool's data</h3>
      <span class="tag">presidio-structured (alpha) · {pill("partly", "Partly")}</span>
    </div>
    <figure>
{d10}
      <figcaption>It works out which columns or keys hold which type of personal data, then edits every value in them. The edit is applied to the whole cell, not just the matching part, and the same table or object comes back.</figcaption>
    </figure>
    <p class="know"><b>Good to know:</b> the package is marked alpha, and Presidio's docs describe it for protecting data sets; they do not tie it to AI tool results, so that fit is our reading. Python only, with no web service. Objects nested in lists need a hand-written map, a free-text cell is replaced as a whole, and tables that mix free text with structure are listed as future work.</p>
  </article>
</section>

<!-- SCORECARD -->
<section class="stage">
  <div class="stage-head">
    <div class="eyebrow">At a glance</div>
    <h2>Presidio at NeMo's five checkpoints</h2>
    <p>The same five places NeMo can check, plus images, reversible masking and your own patterns, with an honest answer for each.</p>
  </div>
  <div class="tablewrap">
    <table class="cats">
      <thead><tr><th>Checkpoint</th><th>Presidio?</th><th>Why</th></tr></thead>
      <tbody>
        <tr><td>Input</td><td>{pill("yes", "Yes")}</td><td>Finds and masks personal data in the user's message (diagrams 3 and 4). Only for the types switched on; harmful content, prompt attacks and topics are outside what Presidio does.</td></tr>
        <tr><td>Output</td><td>{pill("yes", "Yes")}</td><td>The same two steps on the AI's draft answer (diagram 5). No Presidio page shows it, so that is our reading.</td></tr>
        <tr><td>Retrieval (your documents)</td><td>{pill("partly", "Partly")}</td><td>The text steps work on any passage, but Presidio's pages show no example. NVIDIA's NeMo docs run Presidio on retrieved chunks.</td></tr>
        <tr><td>Dialog (topics, fixed replies)</td><td>{pill("no", "No")}</td><td>No conversation rules, topic checks or fixed replies. Nothing official describes any.</td></tr>
        <tr><td>Execution (actions, tools)</td><td>{pill("partly", "Partly")}</td><td>Can mask the tables and JSON a tool sends or returns (alpha). It does not judge whether an action should run.</td></tr>
        <tr><td>Images</td><td>{pill("partly", "Partly")}</td><td>Finds text in a picture with OCR and paints over it (beta). Faces and signatures are not stated to be covered.</td></tr>
        <tr><td>Reversible masking</td><td>{pill("yes", "Yes")}</td><td>Encrypt and decrypt are built in. Keeping the key, and finding the token again in the AI's answer, are your app's job.</td></tr>
        <tr><td>Your own patterns</td><td>{pill("yes", "Yes")}</td><td>Regex, word lists and allow lists. It reports matches and never blocks.</td></tr>
      </tbody>
    </table>
  </div>
</section>

<!-- LIMITATIONS -->
<section class="stage">
  <div class="stage-head">
    <div class="eyebrow">Limitations</div>
    <h2>What Presidio does not do, or does not tell us</h2>
  </div>
  <article class="rail">
    <ul class="limits">
      <li><b>It finds and edits; it never decides.</b> You get findings or edited text, with no pass, fail or block. Your app refuses, logs, chooses the cut-off and passes the masked copy on.</li>
      <li><b>It only covers personal data.</b> It has no check for prompt attacks, harmful content or topics. No type exists for API keys, passwords or other secrets.</li>
      <li><b>The default setup is narrow.</b> It is English only, and 24 of the 74 recogniser entries are switched on. The Singapore NRIC pattern is off, whether the UEN type runs is open, and Singapore phone numbers are not in the phone check's regions.</li>
      <li><b>Published accuracy is thin.</b> The only figures are the vendor's demo notebooks on made-up data, and the second one changed several things at once. No per-type accuracy, no non-English accuracy, no recommended cut-off and no speed figures are published.</li>
      <li><b>The web services have no built-in security.</b> The FAQ says the endpoints have no authentication by design. Encrypted connections (TLS), rate limits and request size are not stated, and keys travel in the request in the docs' example.</li>
      <li><b>Some parts are pre-release or samples.</b> The Image Redactor is beta, presidio-structured is alpha, the language-model recogniser is marked experimental, and the deployment pages are samples. The FAQ says there is "no warranty or SLA" (no promised service level).</li>
      <li><b>The project is mid-move, and its docs disagree.</b> It is moving from Microsoft to Data Privacy Stack. The live docs were last published on 2026-07-04, before release 2.2.364, so the docs and the code differ in places (for example, the web API file omits options the code accepts), and the older Microsoft container images are no longer updated.</li>
      <li><b>Some options send text elsewhere.</b> The Azure AI Language, Azure Health Data Services, Azure OpenAI and Azure Document Intelligence options send text or images to Azure (our reading of the code), and how long the health service keeps text is not stated. The default setup needs no account and no key.</li>
    </ul>
  </article>
</section>

<footer>
  <p>Sources: the Presidio documentation (presidio.dataprivacystack.org, the Data Privacy Stack host), its project transition page, the Presidio source code at release 2.2.364 and the presidio-research evaluation repository at 0.3.2, and NVIDIA's NeMo Guardrails page on Presidio (for the NeMo link only). Accuracy figures are Presidio's own demo results in presidio-research. Example messages are illustrative unless marked as quoted from Presidio's docs.</p>
  <p><a href="https://presidio.dataprivacystack.org/">Presidio home</a> · <a href="https://presidio.dataprivacystack.org/analyzer/">Analyzer</a> · <a href="https://presidio.dataprivacystack.org/supported_entities/">Supported entities</a> · <a href="https://presidio.dataprivacystack.org/anonymizer/">Anonymizer</a> · <a href="https://presidio.dataprivacystack.org/image-redactor/">Image Redactor</a> · <a href="https://presidio.dataprivacystack.org/structured/">presidio-structured</a> · <a href="https://presidio.dataprivacystack.org/analyzer/adding_recognizers/">Adding recognisers</a> · <a href="https://presidio.dataprivacystack.org/samples/python/encrypt_decrypt/">Encrypt and decrypt sample</a> · <a href="https://presidio.dataprivacystack.org/samples/docker/litellm/">LiteLLM sample</a> · <a href="https://presidio.dataprivacystack.org/installation/">Installation</a> · <a href="https://presidio.dataprivacystack.org/faq/">FAQ</a> · <a href="https://presidio.dataprivacystack.org/project_transition/">Project transition</a> · <a href="https://presidio.dataprivacystack.org/evaluation/">Evaluation</a> · <a href="https://github.com/data-privacy-stack/presidio-research/blob/0.3.2/notebooks/4_Evaluate_Presidio_Analyzer.ipynb">Evaluation notebook 4</a> · <a href="https://github.com/data-privacy-stack/presidio-research/blob/0.3.2/notebooks/5_Evaluate_Custom_Presidio_Analyzer.ipynb">Evaluation notebook 5</a> · <a href="https://github.com/data-privacy-stack/presidio/blob/2.2.364/presidio-analyzer/presidio_analyzer/conf/default_recognizers.yaml">Default recogniser file</a> · <a href="https://docs.nvidia.com/nemo/guardrails/configure-guardrails/guardrail-catalog/third-party/presidio">NeMo: Presidio</a></p>
</footer>

</div>
'''

head = f'''<title>How Presidio Masks a Conversation</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&family=Source+Sans+3:wght@400;600&family=JetBrains+Mono:wght@400&display=swap">
<style>
{line5}
{base_css}
{additions}
</style>
'''

with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write(head + body)
print("wrote", OUT)
