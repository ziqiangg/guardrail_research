# -*- coding: utf-8 -*-
# Generates parts (a) and (b) of cloak_inventory.md ; URL keys resolved by U()
G = "https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/"
P = "https://www.developer.tech.gov.sg/products/categories/data-and-apis/cloak/"
URLS = {
 "HOME": G+"home.md", "FAQ": G+"faqs.md", "FTAI": G+"fta/intro-to-fta.md", "USE": G+"fta/usage-guide.md",
 "ENTI": G+"fta/entity-types/intro.md", "NAME": G+"fta/entity-types/personal/name.md", "NRIC": G+"fta/entity-types/personal/nric.md",
 "EMAIL": G+"fta/entity-types/personal/email-address.md", "PHONE": G+"fta/entity-types/personal/phone-number.md",
 "NRPG": G+"fta/entity-types/personal/nrp.md", "ADDR": G+"fta/entity-types/personal/full-address.md",
 "LOCN": G+"fta/entity-types/personal/country.md", "PASS": G+"fta/entity-types/personal/passport.md",
 "CURR": G+"fta/entity-types/financial/currency.md", "CARD": G+"fta/entity-types/financial/credit-card.md",
 "SGBK": G+"fta/entity-types/financial/sg-bank-account.md", "IBAN": G+"fta/entity-types/financial/intl-bank-account.md",
 "IPAD": G+"fta/entity-types/technical-security/ip-address.md", "URLE": G+"fta/entity-types/technical-security/url.md",
 "DATE": G+"fta/entity-types/others/datetime.md", "UENP": G+"fta/entity-types/others/uen.md",
 "ORGN": G+"fta/entity-types/others/organization.md", "EXCP": G+"fta/entity-types/others/exceptions.md",
 "CUST": G+"fta/entity-types/others/custom.md", "FIXD": G+"fta/custom-entities/custom-entities-fixed-list.md",
 "STRC": G+"fta/custom-entities/custom-entities-structured.md", "LLMI": G+"fta/custom-entities/custom-entities-unstructured/intro.md",
 "ADDE": G+"fta/custom-entities/custom-entities-unstructured/add-entities.md", "PRMP": G+"fta/custom-entities/custom-entities-unstructured/write-prompts.md",
 "SAMPD": G+"fta/custom-entities/custom-entities-unstructured/samples/datetime-specific.md",
 "CONF": G+"fta/advanced-features/confidence-level.md", "INCL": G+"fta/advanced-features/inclusion-feature.md",
 "ALIAS": G+"fta/anonymisation-techniques/alias.md", "ENCR": G+"fta/anonymisation-techniques/encrypt.md",
 "PSEU": G+"fta/anonymisation-techniques/pseudonymisation.md", "REDA": G+"fta/anonymisation-techniques/redact.md",
 "REPL": G+"fta/anonymisation-techniques/replace.md", "RUNQ": G+"fta/anonymisation-techniques/replace-unique.md",
 "MASK": G+"fta/anonymisation-techniques/masking/intro.md", "NRMK": G+"fta/anonymisation-techniques/masking/nric-masking.md",
 "TECHI": G+"fta/anonymisation-techniques/intro.md",
 "SECR": G+"decryption/secrets-manager.md", "FTDC": G+"decryption/free-text-decryption.md", "TABD": G+"decryption/tabular-decryption.md",
 "DECI": G+"decryption/intro-to-decryption.md", "TPL": G+"templates/templates.md", "APIG": G+"developer-api-guide.md",
 "PKG": G+"packages-anonymiser.md", "REGG": G+"registration-guide.md", "REL": G+"release-notes.md", "CRED": G+"credits.md",
 "VIDG": G+"video-guides.md", "TABI": G+"tabular/intro-to-tabular.md", "TABU": G+"tabular/usage-guide.md", "SIDE": "https://docs.developer.tech.gov.sg/docs/cloak-guide/_sidebar.md",
 "PO": P+"overview", "PF": P+"features-roadmap", "PFAQ": P+"faqs", "PUC": P+"use-cases", "PGS": P+"getting-started",
 "SITE": "https://www.cloak.gov.sg", "REGP": "https://www.cloak.gov.sg/register", "PKGP": "https://www.cloak.gov.sg/packages",
 "TERMS": "https://go.gov.sg/cloak-terms", "TERMSPDF": "https://file.go.gov.sg/cloak-terms.pdf", "PRIV": "https://go.gov.sg/cloak-privacy",
 "PRIVPDF": "https://file.go.gov.sg/cloak-privacy.pdf", "MIR": "https://mirage.gov.sg",
 "APIGUIDE": "https://docs.developer.tech.gov.sg/docs/cloak-api-guide/", "APISPEC": "https://docs.developer.tech.gov.sg/docs/cloak-api-specifications-openapi/",
 "PKGGUIDE": "https://docs.developer.tech.gov.sg/docs/cloak-anonymiser-package-guide/?product=Cloak",
 "SPYLIC": "https://github.com/explosion/spaCy/blob/release-v3.8.16/LICENSE",
 "SPYMODEL": "https://github.com/explosion/spacy-models/blob/ca6f473afda3c4943d3919d3e39406c1b3f48b85/meta/en_core_web_sm-3.8.0.json",
 "PRESLIC": "https://github.com/data-privacy-stack/presidio/blob/2.2.364/LICENSE",
 "PRESTR": "https://presidio.dataprivacystack.org/project_transition/",
 "PRESENT": "https://microsoft.github.io/presidio/supported_entities/",
 "PRESENC": "https://microsoft.github.io/presidio/tutorial/12_encryption/",
 "PCDLIC": "https://github.com/Legrandin/pycryptodome/blob/v3.24.0/LICENSE.rst",
 "PCRYPTO": "https://pypi.org/project/pycrypto/",
}
CK1 = "Cloak: Free-text PII detection and anonymisation"
CK2 = "Cloak: Custom entity detection in free text (lists, regex and LLM)"
CK3 = "Cloak: Reversible anonymisation and decryption (encrypt and restore)"
INV = "— (inventory only, not in Table 3)"
LEG = "— (legacy, not in Table 3)"
ALL3 = "; ".join([CK1, CK2, CK3])
def U(keys):
    return " ; ".join(URLS[k] for k in keys.split())
def row(cells, urlkeys):
    cells = list(cells) + [U(urlkeys)]
    for c in cells:
        assert "|" not in c and "**" not in c and "`" not in c, c
    return "| " + " | ".join(cells) + " |"
