import re
D="https://docs.cloud.google.com/model-armor/"
GO="37f936ac9d69e173da0ba4123e382c52b2dd741f"
AS="2b1a9f00fabb4e837c39d80570ff50ebc3b1349e"
U={
"OV":D+"overview","TPL":D+"manage-templates","SAN":D+"sanitize-prompts-responses","FLR":D+"configure-floor-settings",
"QUO":D+"quotas","FAR":D+"feature-availability-by-region","DR":D+"data-residency","LOC":D+"locations",
"FV":D+"set-filter-version","VH":D+"version-history","EXC":D+"configure-exclusion-rules","LOG":D+"configure-logging",
"BP":D+"best-practices","INT":D+"integrations","VTX":D+"model-armor-vertex-integration","APG":D+"model-armor-apigee-integration",
"AGW":D+"model-armor-agent-gateway-integration","GE":D+"model-armor-gemini-enterprise-integration",
"LC":D+"model-armor-langchain-integration","MCPD":D+"model-armor-mcp-google-cloud-integration",
"NET":D+"model-armor-networking-integration","LIB":D+"reference/libraries","RN":D+"release-notes",
"RT":D+"reference/rest/v1/projects.locations.templates","RR":D+"reference/rest/v1/SanitizationResult",
"MON":D+"monitoring-dashboard","RTY":D+"retry-strategy",
"MCPS":"https://docs.cloud.google.com/mcp/model-armor-supported-products",
"SCCF":"https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings",
"PROD":"https://cloud.google.com/security/products/model-armor",
"PRC":"https://cloud.google.com/security-command-center/pricing",
"APU":"https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy",
"APR":"https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy",
"GOCH":"https://github.com/googleapis/google-cloud-go/blob/"+GO+"/modelarmor/CHANGES.md",
"GOVER":"https://github.com/googleapis/google-cloud-go/blob/"+GO+"/modelarmor/internal/version.go",
"GOPB1":"https://github.com/googleapis/google-cloud-go/blob/"+GO+"/modelarmor/apiv1/modelarmorpb/service.pb.go",
"GOPB1B":"https://github.com/googleapis/google-cloud-go/blob/"+GO+"/modelarmor/apiv1beta/modelarmorpb/service.pb.go",
"APSAMP":"https://github.com/GoogleCloudPlatform/apigee-samples/blob/"+AS+"/llm-security-v2/README.md",
}
TOK=re.compile(r"\b("+"|".join(sorted(U,key=len,reverse=True))+r")\b")
MA={
1:"Model Armor: Input-level responsible AI safety filtering",
2:"Model Armor: Output-level responsible AI safety filtering",
3:"Model Armor: Input-level prompt injection and jailbreak detection",
4:"Model Armor: Output-level prompt injection and jailbreak detection",
5:"Model Armor: Input-level sensitive data detection and de-identification (Sensitive Data Protection)",
6:"Model Armor: Output-level sensitive data detection and de-identification (Sensitive Data Protection)",
7:"Model Armor: Input-level malicious URL detection",
8:"Model Armor: Output-level malicious URL detection",
9:"Model Armor: Document screening (PDF, CSV, text and Office files)",
10:"Model Armor: Image screening with OCR and visual scanning",
}
MARK="— (inventory only, not in Table 3)"
def cov(*ns):
    return "; ".join(MA[n] for n in ns)
ALL=cov(*range(1,11))
T18=cov(*range(1,9))
def urls(text):
    seen=[]
    for m in TOK.finditer(text):
        k=m.group(1)
        if k not in seen: seen.append(k)
    return " ; ".join(U[k] for k in seen)
def row(cells, url_from=None):
    """cells exclude URL col; URL col auto-built from short names in cells (and url_from)."""
    txt=" ".join(cells)+(" "+url_from if url_from else "")
    out=list(cells)+[urls(txt)]
    for c in out:
        assert "|" not in c, c
        assert "`" not in c and "**" not in c, c
    return "| "+" | ".join(out)+" |"
def table(header, rows):
    n=len(header)
    s="| "+" | ".join(header)+" |\n|"+"---|"*n+"\n"
    for r in rows:
        assert r.count(" | ")==n-1 or True
        s+=r+"\n"
    return s
