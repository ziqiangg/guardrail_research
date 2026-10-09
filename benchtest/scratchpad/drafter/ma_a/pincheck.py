import re
txt=open("/home/user/guardrail_research/benchtest/drafts/modelarmor_cols_a.md",encoding="utf-8").read().split("## Reviewer notes")[0]
cols=re.split(r"(?m)^## Column ",txt)[1:]
MAP=[
(r"\boverview\b(?! page, 2026)", "model-armor/overview"),
(r"templates page","manage-templates"),
(r"sanitize page","sanitize-prompts-responses"),
(r"REST templates ref","reference/rest/v1/projects.locations.templates"),
(r"REST result ref","reference/rest/v1/SanitizationResult"),
(r"quotas page","model-armor/quotas"),
(r"filter version page","set-filter-version"),
(r"version history","model-armor/version-history"),
(r"release note","model-armor/release-notes"),
(r"feature availability page","feature-availability-by-region"),
(r"data residency page","model-armor/data-residency"),
(r"exclusion rules page","configure-exclusion-rules"),
(r"logging page","configure-logging"),
(r"floor settings page","configure-floor-settings"),
(r"integrations page","model-armor/integrations"),
(r"Agent Platform page","model-armor-vertex-integration"),
(r"Agent Gateway page","agent-gateway-integration"),
(r"Gemini Enterprise page","gemini-enterprise-integration"),
(r"MCP page","mcp-google-cloud-integration"),
(r"networking page","networking-integration"),
(r"LangChain page","langchain-integration"),
(r"Apigee page","apigee-integration"),
(r"Apigee policy ref","apigee/docs/api-platform"),
(r"product page","security/products/model-armor"),
(r"pricing page","security-command-center/pricing"),
(r"Google Cloud blog","blog/products"),
(r"client libraries page","reference/libraries"),
(r"locations page","model-armor/locations"),
(r"best practices page","best-practices"),
(r"service\.pb\.go","service.pb.go"),
]
bad=0
for c in cols:
    cid=c.split(":")[0]
    r9=c.split("### R9")[1]
    body=c.split("### R9")[0]
    urls=re.findall(r"https?://\S+",r9)
    for pat,frag in MAP:
        if re.search(pat,body) and not any(frag in u for u in urls):
            print(cid,"hint",pat,"-> missing R9 url fragment",frag); bad+=1
    # repo label check
    if "[Documented: repo googleapis/google-cloud-go@37f936ac]" in body and not any("37f936ac9d69" in u for u in urls):
        print(cid,"repo url missing"); bad+=1
    for u in urls:
        if u not in [x for x in urls if urls.count(x)==1]: print(cid,"dup url",u)
print("pin problems",bad)
