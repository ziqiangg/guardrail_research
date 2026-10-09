import re,glob
base='benchtest/scratchpad/drafter/ma_b/'
def rd(f): return open(base+f,encoding='utf-8',errors='replace').read()
def norm(t):
    t=t.replace('“','"').replace('”','"').replace('’',"'")
    return re.sub(r'\s+',' ',t)
pages={
 'overview':['overview.txt'],'sanitize page':['sanitize-prompts-responses.txt'],'templates page':['manage-templates.txt'],
 'templates reference':['reference_rest_v1_projects.locations.templates.txt'],'REST reference':['reference_rest_v1_projects.locations.templates.txt'],
 'quotas':['quotas.txt'],'integrations page':['integrations.txt'],'SanitizationResult':['reference_rest_v1_SanitizationResult.txt'],
 'DataItem':['dataitem.txt'],'sanitizeModelResponse':['smr.txt'],'Gemini Enterprise':['model-armor-gemini-enterprise-integration.txt'],
 'Agent Platform':['model-armor-vertex-integration.txt'],'Agent Gateway':['model-armor-agent-gateway-integration.txt'],
 'Apigee integration':['model-armor-apigee-integration.txt'],'Apigee policy':['apigee_sanitize-llm-response-policy.txt','apigee_sanitize-user-prompt-policy.txt'],
 'networking':['model-armor-networking-integration.txt'],'MCP':['model-armor-mcp-google-cloud-integration.txt'],'LangChain':['model-armor-langchain-integration.txt'],
 'release note':['release-notes.txt'],'release notes':['release-notes.txt'],'floor settings':['configure-floor-settings.txt'],'set-filter-version':['sfv.txt'],
 'logging':['configure-logging.txt'],'pricing':['sccp.txt'],'product page':['prod.txt'],'blog':['blog.txt'],'data residency':['data-residency.txt'],
 'feature availability':['feature-availability-by-region.txt'],'service.pb.go':['gcgo/modelarmor/apiv1/modelarmorpb/service.pb.go'],
}
txt=open('benchtest/drafts/modelarmor_cols_b.md',encoding='utf-8').read()
bad=0;tot=0
for i,l in enumerate(txt.split('\n'),1):
    if not l.startswith(('•','  –')): continue
    m=re.search(r'\(([^()]*(?:\([^()]*\)[^()]*)*)\)\s*\*\*\[',l)
    hint=m.group(1) if m else ''
    files=set()
    for k,v in pages.items():
        if k.lower() in hint.lower(): files.update(v)
    l2=re.sub(r'`[^`]*`','',l)
    for q in re.finditer(r'"([^"]{8,})"',l2):
        qq=norm(q.group(1)).strip().rstrip('.,;')
        tot+=1
        if not files:
            print('NOHINT L%d: %s | hint=%s'%(i,qq[:50],hint[:50])); bad+=1; continue
        R=norm(' '.join(rd(f) for f in files)); R2=R.replace(' | ',' ')
        parts=re.split(r'…|\.\.\.',qq)
        if not all(p.strip() in R or p.strip() in R2 for p in parts):
            bad+=1; print('NOT-IN-CITED L%d: %s | hint=%s'%(i,qq[:70],hint[:70]))
print('quotes',tot,'bad',bad)
