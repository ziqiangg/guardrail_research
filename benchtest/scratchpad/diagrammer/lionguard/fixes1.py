import io
fn='benchtest/scratchpad/diagrammer/lionguard/parts.py'
p=io.open(fn,encoding='utf-8').read()
R=[
# RF1
("GovTech LionGuard · open models: LionGuard 2, 2.1 and 2 Lite","GovTech LionGuard · LionGuard 2, 2.1 and 2 Lite on Hugging Face"),
('<text class="tb" x="612" y="44" text-anchor="middle">Open data</text>','<text class="tb" x="612" y="44" text-anchor="middle">Public data</text>'),
("and open data, meaning a training-data subset","and public data, meaning a training-data subset"),
# RF2
("GovTech publishes it on Hugging Face, a public site for sharing AI models, and you run it yourself. Only the small classifier is GovTech's: LionGuard 2 and 2.1 send each text","GovTech publishes it on Hugging Face, a public site for sharing AI models, for you to run, but only the small classifier is GovTech's: by our reading of GovTech's code, LionGuard 2 and 2.1 send each text"),
# RF3
("<td>Paper: F1 of 77 on GovTech's own test set</td>","<td>Paper: F1 (a 0 to 100 accuracy measure) of 77 on GovTech's own test set</td>"),
# RF4
("LionGuard 2 has a paper; 2.1 has one blog table on a private test split; Lite has no figure. No operating threshold, maximum text length or Lite speed is stated.","LionGuard 2 has a paper; 2.1 has one blog table, on a private test split and RabakBench; Lite has no figure. No operating threshold, maximum text length, or speed for 2.1 or Lite is stated."),
# RF5
("<td>73 (a private split, so not directly comparable with 77)</td>","<td>73 (on what the blog calls a held-out private test split)</td>"),
# RF6
('first for Sentinel users</text>','for Sentinel users only</text>'),
("a retrained LionGuard 2 for Sentinel users first, with no statement","a retrained LionGuard 2 for Sentinel users only, with no statement"),
# O1
("a file of about 3 MB</text>","a file of 1 to 3 MB</text>"),
# O2
("The scoring is the same for every language it covers: English, Singlish, Chinese, Malay and Tamil.","One model scores every language it covers: English, Singlish, Chinese, Malay and Tamil, though less well in Tamil."),
# O3
("after an embedding step that another company runs (OpenAI or Google)","after an embedding step (turning the text into numbers) that another company runs (OpenAI or Google)"),
# O4
("Lite also needs a Hugging Face login and acceptance of Google's Gemma terms</td></tr>\n        </tbody>\n      </table>\n    </div>\n    <p class=\"know\"><b>Good to know:</b> the hosted","Lite also needs a Hugging Face login and acceptance of Google's Gemma terms; the paper says the weights are for research and public interest purposes only</td></tr>\n        </tbody>\n      </table>\n    </div>\n    <p class=\"know\"><b>Good to know:</b> the hosted"),
# O5
("Gemma terms; no API key</td>","Gemma terms; no key needed</td>"),
# O6
("A score scale from 0 to 1 showing the bands on GovTech's public demo page.","A score scale from 0 to 1 showing the bands that GovTech's public demo page applies to the overall flag."),
("These bands come from GovTech's public demo page and are demo behaviour","These bands, applied to the overall flag, come from GovTech's public demo page and are demo behaviour"),
# O7
("<p>LionGuard is tuned for English, Singlish, Chinese, Malay and Tamil. The published scores below are GovTech's own, on its own test data.</p>","<p>LionGuard is tuned for English, Singlish, Chinese, Malay and Tamil. The published scores below are GovTech's own, on its own test data; RabakBench is GovTech's own multilingual test set.</p>"),
("<b>Good to know:</b> RabakBench is GovTech's own multilingual test set. The paper prints","<b>Good to know:</b> the paper prints"),
# O8
("<td>Singlish (RabakBench)</td>","<td>Singlish (RabakBench; the blog says English/Singlish)</td>"),
# O9
("its owners list 8,192 tokens (short pieces of words) for OpenAI's and 2,048 for each of Google's two.","its owners list 8,192 for OpenAI's and 2,048 tokens (short pieces of words) for each of Google's two."),
# O10
("The first step is the only part that differs between versions, and it is not GovTech's work (diagram 3).","GovTech says the versions differ only in the first step, which is not GovTech's work (diagram 3)."),
]
for a,b in R:
    assert p.count(a)==1,(p.count(a),a[:60])
    p=p.replace(a,b)
io.open(fn,'w',encoding='utf-8',newline='\n').write(p)
print('ok',len(R))
