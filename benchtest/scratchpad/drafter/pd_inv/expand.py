s=open('template.md',encoding='utf-8').read()
s=s.replace("(Python versions differ, see block (a))","(Python versions differ, see block (d))")
m={
"{R}":"[Documented: repo data-privacy-stack/presidio@2.2.364]",
"{P}":"[Documented: repo data-privacy-stack/presidio-research@0cb36502]",
"{PB}":"https://github.com/data-privacy-stack/presidio-research/blob/0cb365021884d849c5bc21957de67c91943c1662",
"{B}":"https://github.com/data-privacy-stack/presidio/blob/2.2.364",
"{S}":"https://presidio.dataprivacystack.org",
"{PD1}":"Presidio: PII detection in text (Analyzer)",
"{PD2}":"Presidio: PII anonymisation and masking in text (Anonymizer)",
"{PD3}":"Presidio: Reversible anonymisation and deanonymisation (encrypt and decrypt)",
"{PD4}":"Presidio: PII detection and redaction in images (Image Redactor)",
"{PD5}":"Presidio: PII detection and anonymisation in structured data (tables and JSON)",
"{PD6}":"Presidio: Custom-recognizer detection (regex patterns, deny lists, ad-hoc recognizers)",
}
for k,v in m.items(): s=s.replace(k,v)
open('/home/user/guardrail_research/benchtest/drafts/presidio_inventory.md','w',encoding='utf-8').write(s)
