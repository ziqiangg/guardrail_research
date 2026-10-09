import json,collections,re
rows=json.load(open("cat.json"))
G=collections.OrderedDict()
def add(g,r): G.setdefault(g,[]).append(r)
persons={"PERSON_NAME","FIRST_NAME","LAST_NAME","MALE_NAME","FEMALE_NAME","EMAIL_ADDRESS","PHONE_NUMBER","USER_NAME","DATE_OF_BIRTH"}
places={"STREET_ADDRESS","LOCATION","LOCATION_COORDINATES","GEOGRAPHIC_DATA","ORGANIZATION_NAME"}
net={"IP_ADDRESS","MAC_ADDRESS","MAC_ADDRESS_UNIVERSAL","MAC_ADDRESS_LOCAL","IMEI_HARDWARE_ID","IMSI_ID","ICCID_NUMBER","TECHNICAL_ID","ADVERTISING_ID","URL","DOMAIN_NAME","HTTP_USER_AGENT"}
dates={"DATE","TIME"}
demo={"AGE","GENDER","MARITAL_STATUS","ETHNIC_GROUP","SEXUAL_ORIENTATION","RELIGIOUS_TERM","POLITICAL_TERM","TRADE_UNION","CRIME_STATUS","EMPLOYMENT_STATUS","IMMIGRATION_STATUS","COUNTRY_DEMOGRAPHIC","DEMOGRAPHIC_DATA"}
generic={"PASSPORT","GOVERNMENT_ID","GENERIC_ID","DRIVERS_LICENSE_NUMBER","VAT_NUMBER","VEHICLE_IDENTIFICATION_NUMBER"}
fin={"FINANCIAL_ID","FINANCIAL_ACCOUNT_NUMBER","IBAN_CODE","SWIFT_CODE","CREDIT_CARD_TRACK_NUMBER","CREDIT_CARD_EXPIRATION_DATE","CREDIT_CARD_DATA","CREDIT_CARD_NUMBER","CVV_NUMBER","AMERICAN_BANKERS_CUSIP_ID"}
health={"ICD9_CODE","ICD10_CODE","FDA_CODE","MEDICAL_DATA","MEDICAL_RECORD_NUMBER","MEDICAL_ID","MEDICAL_TERM","BLOOD_TYPE"}
cred={"STORAGE_SIGNED_POLICY_DOCUMENT","SSL_CERTIFICATE","AZURE_AUTH_TOKEN","GCP_CREDENTIALS","WEAK_PASSWORD_HASH","AUTH_TOKEN","AWS_CREDENTIALS","OAUTH_CLIENT_SECRET","HTTP_COOKIE","ENCRYPTION_KEY","TINK_KEYSET","SECURITY_DATA","JSON_WEB_TOKEN","STORAGE_SIGNED_URL","ANTHROPIC_API_KEY","GEMINI_API_KEY","XSRF_TOKEN","BASIC_AUTH_HEADER","PASSWORD","GCP_API_KEY","OPENAI_API_KEY"}
region={
 "United States":{"UNITED_STATES"},
 "Canada":{"CANADA"},
 "United Kingdom and Ireland":{"UNITED_KINGDOM","IRELAND"},
 "Western and Southern Europe":{"SPAIN","FRANCE","GERMANY","ITALY","PORTUGAL","AUSTRIA","BELGIUM","SWITZERLAND","THE_NETHERLANDS"},
 "Northern Europe":{"SWEDEN","FINLAND","NORWAY","DENMARK"},
 "Eastern Europe, Central Asia, Middle East and Africa":{"POLAND","CZECHIA","CROATIA","RUSSIA","UKRAINE","BELARUS","KAZAKHSTAN","ARMENIA","AZERBAIJAN","UZBEKISTAN","TURKEY","ISRAEL","SOUTH_AFRICA"},
 "East Asia":{"KOREA","JAPAN","CHINA","TAIWAN","HONG_KONG"},
 "South and Southeast Asia and Oceania (excluding Singapore)":{"INDIA","INDONESIA","THAILAND","AUSTRALIA","NEW_ZEALAND"},
 "Latin America":{"MEXICO","BRAZIL","ARGENTINA","CHILE","COLOMBIA","PARAGUAY","PERU","URUGUAY","VENEZUELA"},
 "Singapore":{"SINGAPORE"},
}
unk=[]
for r in rows:
    n=r['name'];loc=r['loc']
    if n.startswith("OBJECT_TYPE/"): add("image object",r)
    elif n.startswith("IMAGE_TYPE/"): add("image context",r)
    elif n.startswith("DOCUMENT_TYPE/CONTEXT/"): add("doc context",r)
    elif n.startswith("DOCUMENT_TYPE/R&D/SOURCE_CODE"): add("source code",r)
    elif n.startswith("DOCUMENT_TYPE/"): add("doc kinds",r)
    elif n in persons: add("persons",r)
    elif n in places: add("places",r)
    elif n in net: add("net",r)
    elif n in dates: add("dates",r)
    elif n in demo: add("demo",r)
    elif n in generic: add("generic",r)
    elif n in fin: add("fin",r)
    elif n in health: add("health",r)
    elif n in cred: add("cred",r)
    else:
        for g,s in region.items():
            if loc in s: add(g,r);break
        else: unk.append((n,loc))
print("UNK",unk)
tot=0
for g,v in G.items():
    av=collections.Counter("ANY" if x['av']=="ANY_LOCATION" else "REG" for x in v)
    tot+=len(v)
    print(g,len(v),dict(av))
print(tot,len(G))
json.dump({g:[x['name'] for x in v] for g,v in G.items()},open("groups.json","w"),indent=1)
