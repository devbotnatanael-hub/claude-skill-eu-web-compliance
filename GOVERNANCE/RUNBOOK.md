---
project: EU_WEB_COMPLIANCE
doc_id: NTNL-EUWEB-RUN-001
title: NTNL adaptation and Nexe deployment
module: GOVERNANCE
status: review
version: 1.0.0
owner: Creator
reviewer: Skill Logic Auditor
executor: Nexe
created: 2026-10-13
updated: 2026-10-13
source_of_truth: git
git_path: GOVERNANCE/RUNBOOK.md
gdrive_status: toolbox_excel_summary
gdrive_path: null
supersedes: null
depends_on: [NTNL-EUWEB-SPAIN-001]
---

# Operation

NTNL_Protocol is the top-level framework; GitSidian governs textual artifacts. This is an Apache-2.0
fork of gricyk/claude-skill-eu-web-compliance at 5034795d5bcc68b63549e729fff1ad9567889bf1,
not an upstream 1.0.0 release. NTNL 1.0.0 is the first local adaptation identity.

Canonical source: https://github.com/devbotnatanael-hub/claude-skill-eu-web-compliance .
Nexe installation: `/home/codexntnl/.codex/skills/eu-web-compliance` points to a pinned deployment
under `/srv/codex-executor/skills/eu-web-compliance-1.0.0/`. Never edit runtime in place.
Linux/Nexe is the validated target; scanner uses POSIX O_NOFOLLOW. Other operating systems require
separate validation, not implied by the upstream portability claim.

Use when a legal review or scoped prepublication check is requested. No resident process, automatic
site audit, scheduler or law-update service. Reverify applicable official sources at usage. Catalog
monthly upstream monitoring does not authorize unattended installation or overwrite this fork.

# Validation and updates

Run `python3 -m unittest discover -s tests`, creator quick_validate and a fresh frozen Skill Logic
Auditor review before activating behavior changes. Review upstream differences and licence; merge
selectively on a codex/ branch, preserve NTNL controls, bump version, use independent review + PR.
The installer downloads the exact published commit using the governed installer with download method
(no ungoverned Git fallback). Check file hashes between canonical source and deployed skill; test the
scanner on bundled fixtures, not a real client website. Store receipt and review in GOVERNANCE.

Reversion: preserve any pre-existing runtime before changing it. First installation has absent
pre-state: unlink only the new named runtime symlink (after verifying its target), retain pinned
payload/evidence. Reinstall by relinking that same verified payload. On upgrades, atomically restore
the previous symlink/payload; do not delete old versions. Rehearse unlink/relink and byte parity.

# Decisions and limits

2026-10-13 Jordi authorized fork, reusable adaptation, independent review, installation, canonical
publication and existing toolbox Excel/Memo updates. This does not authorize a client website audit.
No client details enter the skill. Existing upstream references/examples are retained as third-party
material; national source links guide current verification rather than guarantee complete coverage.
Reports disclose omissions and uncertainty, not percentages or legal certification. Scanner defaults
are bounded heuristics on stable local trees, not protection against a concurrently hostile filesystem.
External `timeout 90s` is required for a hard scan wall-clock bound. Report timeout as incomplete.

Open: first real website review and behavior on non-Linux platforms are unverified. No host beyond
Nexe is accessed. Human-readable toolbox summary uses the already configured Excel mirror; no new
Drive destination or sharing is created.

# Change Log

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-10-13 | Nexe | Recorded authorized adaptation, validation, pinning/update and rollback contract. |
