import io
p = "benchtest/scratchpad/diagrammer/presidio/build.py"
s = io.open(p, encoding="utf-8").read()


def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:80])
    s = s.replace(a, b)


# R1
rep('<div class="eyebrow">Presidio and NeMo</div>', '<div class="eyebrow">Presidio, NeMo, Llama Guard and Sentinel</div>')
rep("<p>Presidio does not decide whether a message is safe. It finds personal data and, if asked, edits it. NeMo Guardrails calls Presidio for its personal-data checks, and Llama Guard and Sentinel have their own pages.</p>",
    "<p>The four tools sit at different levels. NeMo is a framework you run that decides where checks go. Llama Guard is one model you run that gives a verdict. Sentinel is a web service run by GovTech that gives a score for each check. Presidio is a toolkit you run that finds personal data and, if asked, edits it; it never decides whether a message is safe. NeMo Guardrails calls Presidio for its personal-data checks.</p>")
i = s.index('    <div class="tablewrap">\n      <table class="cats">\n        <thead><tr><th></th><th>Presidio</th></tr></thead>')
j = s.index('    </div>\n  </article>\n</section>\n\n<!-- HOW IT WORKS -->') + len('    </div>\n')
newt = '''    <div class="tablewrap">
      <table class="cats">
        <thead><tr><th></th><th>NeMo Guardrails</th><th>Llama Guard</th><th>GovTech Sentinel</th><th>Presidio</th></tr></thead>
        <tbody>
          <tr><td>What it is</td><td>A framework around your chatbot</td><td>One AI model</td><td>A web service with a menu of checks</td><td>An open-source toolkit of four parts that find and edit personal data</td></tr>
          <tr><td>Who runs it</td><td>You</td><td>You</td><td>GovTech (hosted); some models can be self-hosted</td><td>You. The FAQ says it "is not an official product of any company and comes with no warranty or SLA" (a promised service level).</td></tr>
          <tr><td>What it hands back</td><td>Allow or block</td><td>Safe or unsafe, plus a category</td><td>A score from 0 to 1 per check</td><td>Findings with scores, or edited text, images and tables. Never a pass or fail.</td></tr>
          <tr><td>Decides where checks run</td><td>Yes</td><td>No</td><td>No, your app chooses what text to send</td><td>No. Your app chooses which text, image or table to send.</td></tr>
          <tr><td>Your own rules and fixed replies</td><td>Yes</td><td>No</td><td>No</td><td>Your own patterns and word lists for what to find; no fixed replies</td></tr>
          <tr><td>Edits text</td><td>Masks personal data</td><td>No</td><td>Returns a masked copy (personal data, via AWS)</td><td>Yes, through the Anonymizer: swap, remove, mask, hash, encrypt and more</td></tr>
          <tr><td>Singapore languages</td><td>Depends on the model it calls</td><td>Listed languages do not include Chinese, Malay or Tamil</td><td>LionGuard: Singlish, Chinese, Malay, partial Tamil</td><td>English by default. Other languages need changes to the language-processing model and the detectors (called recognisers); no accuracy is published for any non-English one.</td></tr>
          <tr><td>Who can use it</td><td>Anyone (open source)</td><td>Anyone who accepts Meta's licence</td><td>Singapore Government public officers, closed beta</td><td>Anyone: open source under the MIT licence (a common open-source licence), which the project says will stay</td></tr>
        </tbody>
      </table>
    </div>
'''
s = s[:i] + newt + s[j:]
# R2, O8
rep('<dd>You can reach <mark>&lt;PERSON&gt;</mark> at <mark>&lt;EMAIL_ADDRESS&gt;</mark>.</dd>\n    </dl>\n    <p class="know"><b>Good to know:</b> no Presidio page shows the calls on an AI',
    '<dd>You can reach <mark>&lt;PERSON&gt;</mark> at <mark>&lt;EMAIL_ADDRESS&gt;</mark>. (illustrative)</dd>\n    </dl>\n    <p class="know"><b>Good to know:</b> no Presidio page shows the calls on an AI')
rep('(expected in a default setup; not tested)', '(illustrative: what we expect from a default setup; not tested)')
# R3
rep('<dd>TITLE found at "Mr.", score 1.0 (the word-list default)</dd>', '<dd>TITLE found at "Mr.", score 1.0, the word-list default (illustrative: the docs show the call, not its output)</dd>')
# R4, O7
rep("The NRIC and FIN pattern (Singapore's national ID numbers) is switched off in the default file. The UEN type (a business registration number)",
    "The NRIC and FIN pattern (Singapore's identity card numbers and foreign identification numbers) is switched off in the default file. The UEN type (a registration number for Singapore businesses and other organisations)")
# R5, O2
rep("The only figures are the vendor's demo notebooks on made-up data, and the second one changed several things at once. No per-type accuracy, no non-English accuracy, no recommended cut-off and no speed figures are published.",
    "The only text-detection figures are the vendor's demo notebooks on made-up data, and the second one changed several things at once. No per-type accuracy, no non-English accuracy and no recommended cut-off for the default setup are published, and the only speed figure is one notebook timing with the hardware not stated.")
# R6
rep('<b>The web services have no built-in security.</b>', '<b>The web services have no built-in login.</b>')
# R7
rep("before release 2.2.364, so the docs and the code differ in places (for example, the web API file omits options the code accepts), and the older Microsoft container images are no longer updated.",
    "before release 2.2.364, and the docs and the code differ in places (for example, the web API description omits options the code accepts, and one docs example names an edit differently from the code). The older Microsoft container images are no longer updated.")
# R8
rep("(for the NeMo link only)", "(for how NeMo uses Presidio)")
# O9
rep("Writes realistic stand-in values using Azure Health Data Services. Needs an Azure account.", "Writes realistic stand-in values using Azure Health Data Services (a Microsoft cloud service). Needs an Azure account.")
# O5
rep("The docs give no guidance on where to store keys,", "The same name encrypts to a different token each time, so the AI model cannot tell that two tokens are the same person. The docs give no guidance on where to store keys,")
# O1 / R026: retrieval
rep("<p>Presidio has no document-specific check. Its text steps work on any text, so passages fetched for the AI model can be scanned before the model reads them.</p>",
    "<p>Presidio has no retrieval-specific check. It does document some file inputs that fetched material could arrive in: CSV and JSON files, pictures and medical image files, and a PDF sample. Passages in those forms can be scanned before the AI model reads them.</p>")
rep("The AI model cannot repeat personal data it was never shown. Same steps as diagram 4, but run earlier, on your documents.",
    "The AI model cannot repeat personal data it was never shown, but anything the Analyzer misses still reaches it. Same steps as diagram 4, but run earlier, on your documents.")
rep("Presidio's own pages never show it on retrieved passages; NVIDIA's NeMo docs do run Presidio on retrieved chunks. That is our reading of the code for Presidio itself; we have not tested it yet.",
    "Presidio's own pages do not describe retrieval: its documented inputs are CSV and JSON files, images, and a PDF sample that marks personal data in the PDF's text layer. NVIDIA's NeMo docs run Presidio on retrieved chunks. That Presidio's own steps work on a plain passage is our reading of the code; we have not tested it yet.")
# scorecard O1
rep("The same two steps on the AI's draft answer (diagram 5). No Presidio page shows it, so that is our reading.",
    "Nothing in Presidio's calls separates input from output, so the same two steps run on the AI's draft answer (diagram 5). No Presidio page shows an example, so that is our reading.")
rep("The text steps work on any passage, but Presidio's pages show no example. NVIDIA's NeMo docs run Presidio on retrieved chunks.",
    "Partly because Presidio documents file inputs a passage could arrive in: CSV and JSON files, images, and a PDF sample (diagram 9). It does not describe retrieval itself; NVIDIA's NeMo docs run Presidio on retrieved chunks.")
io.open(p, "w", encoding="utf-8").write(s)
print("ok")
