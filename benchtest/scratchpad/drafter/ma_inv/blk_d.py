import json
from inv_common import *
HD=["Location","Description","Jurisdiction","Support level (full/limited)","Data residency at rest, in use, in transit","Supported filters with data residency enforced","Multi-language","CSAM","Image","Antivirus","Filter versions available","Source URL"]
HD[3]="Support level (full/limited)"
far=json.load(open('far.json')); dr=json.load(open('dr.json')); loc=json.load(open('loc.json')); fl=json.load(open('drfloor.json'))
ORDER=["asia-northeast1","asia-northeast3","asia-south1","asia-southeast1","australia-southeast2","northamerica-northeast2","us-central1","us-east1","us-east4","us-west1","us","europe-southwest1","europe-west1","europe-west2","europe-west3","europe-west4","europe-west9","eu"]
assert len(ORDER)==18 and set(ORDER)==set(loc)==set(dr)
V1="asia-northeast1 asia-northeast3 asia-south1 asia-southeast1 australia-southeast2 europe-southwest1 europe-west9 northamerica-northeast2 us us-central1 us-east4 us-west1".split()
V2="eu europe-west1 europe-west2 europe-west3 europe-west4 us-east1".split()
V3="asia-northeast1 asia-south1 asia-southeast1 australia-southeast2 eu europe-southwest1 europe-west1 europe-west2 europe-west3 europe-west4 europe-west9 northamerica-northeast2 us us-central1 us-east1 us-east4 us-west1".split()
V4="asia-northeast1 asia-south1 asia-southeast1 eu europe-southwest1 europe-west1 europe-west2 europe-west3 europe-west4 europe-west9 northamerica-northeast2 us us-central1 us-east1 us-east4 us-west1".split()
def fv(l):
    p=[]
    if l in V1:
        if l=="asia-northeast3": p.append("v1 Stable")
        elif l=="australia-southeast2": p.append("v1 (Legacy from 2026-09-25)")
        else: p.append("v1 Legacy")
    if l in V2: p.append("v2 Legacy")
    if l in V3:
        p.append("v3 (Stable from 2026-09-25)" if l=="australia-southeast2" else "v3 Stable")
    if l in V4: p.append("v4 Latest")
    return ", ".join(p)
R=[]
for l in ORDER:
    f=far[l]; d=dr[l]
    multi=l in ("eu","us")
    desc=loc[l]+(" (multi-region)" if multi else " (region)")
    support="Full" if d["support"].startswith("Full") else "Limited"
    resid=f"With templates and enforcement on: at rest {d['rest']}, in use {d['use']}, in transit {d['transit']} [Documented] (DR)"
    if l in fl:
        a=fl[l]
        resid+=f". With Agent Platform floor settings: at rest {a[1]}, in use {a[2]}, in transit {a[3]} [Documented] (DR)"
    else:
        resid+=". Agent Platform floor-settings table has no row for this multi-region [Not disclosed] (DR checked)"
    filt=", ".join(f["filters"])
    filt_cell=f"{filt} [Documented] (FAR)"
    if l=="asia-southeast1":
        filt_cell+=". Singapore is a limited-support region [Documented] (DR). With enforcement off in the template, cross-jurisdictional routing enables the other features, except image, which stays us and eu only [Documented] (FAR; TPL; RN 2026-08-27, 2026-06-22)"
    elif l=="asia-northeast3":
        filt_cell+=". Only Sensitive Data Protection is supported with enforcement on in Seoul [Documented] (FAR; RN 2026-09-04)"
    elif l=="australia-southeast2":
        filt_cell+=". Melbourne gained prompt injection and jailbreak and responsible AI on 2026-09-24 [Documented] (RN)"
    ml=f"{f['ml']} [Documented] (FAR)"
    if l in ("asia-south1","northamerica-northeast2"):
        ml+=". SAN says non-English content sent to prompt injection and jailbreak or responsible AI returns Skipped Detection here [Documented] (SAN)"
    cells=[f"{l} [Documented] (LOC)",f"{desc} [Documented] (LOC)",f"{d['jur']} [Documented] (DR)",f"{support} support [Documented] (DR; FAR)",resid,filt_cell,ml,f"{f['csam']} [Documented] (FAR)",f"{f['img']} [Documented] (FAR)",f"{f['av']} [Documented] (FAR)",f"{fv(l)} [Documented] (FV)"]
    R.append(row(cells))
BLOCK_D=table(HD,R)
if __name__=="__main__":
    print(len(R)); 
    for r in R[:3]: print(r[:700]); print()
