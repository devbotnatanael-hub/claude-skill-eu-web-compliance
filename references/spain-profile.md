---
project: EU_WEB_COMPLIANCE
doc_id: NTNL-EUWEB-SPAIN-001
title: Spain and EU applicability profile
module: REFERENCES
status: review
version: 1.0.0
owner: Creator
reviewer: Skill Logic Auditor
executor: Nexe
created: 2026-10-13
updated: 2026-10-13
source_of_truth: git
git_path: references/spain-profile.md
gdrive_status: toolbox_excel_summary
gdrive_path: null
supersedes: null
depends_on: []
---

# Spain + EU review profile

Use across websites, without client facts. This is an issue-selection guide, not legal advice or a
complete inventory of every sector law. Verify current official texts during each review and record
source/check date. Facts unavailable from a site (contracts, retention practice, operator details,
turnover, employee count) remain pending, never invented. Resolve high-impact ambiguity with counsel.

## Select applicable rules

- Establish operator and establishment, intended markets, personal data/recipients, users including
  children, commercial purpose, public-sector role, online contracts, user content and AI features.
  Mere worldwide accessibility does not automatically apply every country's laws. GDPR territorial
  scope is Article 3 (establishment, offering goods/services to people in the Union, or monitoring
  their behaviour there). Add non-EU jurisdictions only where actual triggers justify it; identify
  local official sources and remaining uncertainty rather than promising worldwide compliance.
- Corporate/contact site: assess GDPR/LOPDGDD when personal data is processed; LSSI obligations
  according to service/operator scope. Do not automatically demand ecommerce checkout, DPO or a
  DPIA. Assess those against actual statutory triggers.
- Ecommerce: assess consumer information, price/terms/order process, withdrawal and exceptions,
  electronic contracting and accessibility scope. Distinguish B2B from consumer transactions.
- Platforms/hosting: assess DSA service classification, role and applicable exemptions rather than
  inferring all platform duties from a comment box. AI: classify actual provider/deployer/use and
  verify current AI Act applicable dates, not headline claims or proposals.

## Spain checks and official starting points

| Topic | Practical decision and primary source |
|---|---|
| Privacy | GDPR Articles 5,6,12–14,28,32 and transfer rules as applicable; LOPDGDD. Information about processing is not automatically a consent requirement. A contact form may have an appropriate non-consent basis; explain the actual basis. [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj), [LOPDGDD](https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673). |
| Children | GDPR Article 8 applies to consent-based processing for information-society services offered directly to a child; Spain LOPDGDD Article 7 generally sets 14 for a minor's own data-processing consent, subject to acts requiring parental assistance. Do not infer parental consent is mandatory for all processing involving minors. Verify exact context. |
| Legal notice | LSSI Article 10 identification/contact and applicable registry/professional/tax/price information; obtain actual operator facts, do not invent a corporate template. [LSSI](https://www.boe.es/buscar/act.php?id=BOE-A-2002-13758). |
| Cookies/storage | LSSI Article 22.2 and current AEPD guidance. Examine actual purpose and exemptions, not cookie names alone. Test fresh sessions before choice, after rejection, after acceptance and withdrawal. In the AEPD approach accepting and rejecting should be presented with equal prominence; distinguish strictly necessary storage. Do not declare every third-party request an unlawful cookie or every cookie wall categorically prohibited. [AEPD guide](https://www.aepd.es/guias/guia-cookies.pdf). |
| Marketing | LSSI Article 21: prior request/express authorization and the limited prior-customer exception for similar own products/services, with the required easy/free objection mechanism. Do not say consent is always the only route. |
| Consumer sales | Assess precontractual information, total pricing, order/payment obligations, withdrawal periods/exceptions and digital-content conditions according to activity. [TRLGDCU](https://www.boe.es/buscar/act.php?id=BOE-A-2007-20555), LSSI Articles 27–28. |
| Accessibility | Assess Ley11/2023 relevant products/services including ecommerce, exemptions and transitions; the microenterprise service exemption is not a blanket exemption from all accessibility duties. Also consider RD193/2023 for public-facing goods/services and RD1112/2018 for public-sector sites where applicable. Separate legal scope from beneficial WCAG technical practice. [Ley11/2023](https://www.boe.es/buscar/act.php?id=BOE-A-2023-11022), [RD193/2023](https://www.boe.es/buscar/act.php?id=BOE-A-2023-7417), [RD1112/2018](https://www.boe.es/buscar/act.php?id=BOE-A-2018-12699). |

AEPD guidance helps interpretation; distinguish it from statutory wording. State the legal basis for
material findings and label unresolved applicability VERIFY. Evidence examples: network capture,
observed banner behaviour, exact code location or document passage. Do not publish raw personal data,
credentials, internal reports or placeholder legal documents.

## Proportional outcome

Report material applicable problems, recommended corrections, unresolved internal facts, and limits of
coverage. No percentage, certification or claim that passing the scanner proves legal compliance.
A narrow review can finish with explicitly unexamined areas; it does not require auditing every byte.

## Change Log

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-10-13 | Nexe | Added reusable official-source applicability profile for Spain/EU and other-market extension. |
