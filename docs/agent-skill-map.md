# Convene X agent team: skills, tools and org chart

Audit date: 9 November 2026. Live copies: Command Centre → Agents tab (org chart + skills per agent), and `00-overview/skill-map.md` in Doctor Doom. Sources: Doctor Doom vault in Google Drive
(`org-chart.md`, `team-roster.md`, `INDEX.md`, `tech-stack.md`, Agency Agents
Playbooks `README.md`, Convene X Agent Jobs sheet), the skills installed in
claude.ai, the plugins and connectors attached to this session, and this repo's
`.claude/skills/`.

Rule that applies to every agent: nothing sends, publishes, schedules, signs or
pays without the founder's explicit sign-off.

---

## 1. Org chart (22 agents + Jarvis)

```
Nathan (founder, signs off everything)
│
├── Jarvis ................. Orchestrator: routes every job, morning brief
│
├── Victor Drake ........... CRO Advisor, leads the revenue team    [manual only]
│   ├── Andrew Whitfield ... Head of Partnerships                     [manual only]
│   ├── Marcus Reid ........ Partnerships Architect                   [manual only]
│   ├── Morgan Ellis ....... Delegate & Guest Relations Lead          [manual only]
│   └── Jordan Pryce ....... Sales Ops, Intelligence & Quality Lead
├── Sienna Cole ............ Head of Event Operations & Delivery
├── Priya Anand ............ Head of Finance
├── Grace Bellamy .......... Operations & Admin Coordinator
├── Eleanor Voss ........... Legal & Compliance Lead                  [manual only]
│
└── Freya Lockhart ......... Head of Marketing & Content
    ├── Felix Grant ........ Brand & Quality Reviewer (gate before Freya signs off)
    ├── Iris Bennett ....... Senior Content Writer
    ├── Theo Marsh ......... Social Media & LinkedIn Strategist (owns Buffer posting)
    ├── Amara Osei ......... Email & Lifecycle Specialist
    ├── Leo Ferreira ....... Campaign Strategist
    ├── Callum Reyes ....... SEO & Technical Auditor
    ├── Dev Malhotra ....... Keyword & Search Insights Analyst
    ├── Nadia Kovač ........ Competitive Intelligence Analyst
    ├── Sana Iqbal ......... Performance & Analytics Lead
    ├── Kai Novak .......... Web & UX/UI Designer (owns convenexevents.com)
    ├── Zara Lindqvist ..... Motion & Microsite Specialist (one-off microsites only)
    └── Rhys Calder ........ Video Editor & Motion Film Producer (added 2026-11-06)
```

**Revenue team (agreed 9 Nov):** Andrew, Marcus, Morgan and Jordan report to Victor.
Every agent is a Claude Code agent `cx-<firstname>` in `.claude/agents/`, routed by `CLAUDE.md`.

---

## 2. Skills and tools by agent

Legend: **(repo)** = in this repo's `.claude/skills/`; **(vault)** = a file in
the Doctor Doom vault, not a callable skill; **NOT IN CLOUD** = named in the roster but
not installed where cloud sessions can see it (it may exist on your PC).

### Jarvis: Orchestrator
- Skills: `morning`, `productivity:start`, `productivity:update`, `productivity:task-management`, `productivity:memory-management`, `enterprise-search:search`, `enterprise-search:digest`, `enterprise-search:knowledge-synthesis`, `enterprise-search:search-strategy`, `enterprise-search:source-management`, `small-business:smb-router`, `small-business:smb-onboard`, `small-business:monday-brief`, `small-business:build-agent`, `small-business:build-connector`, `convenex-brain-builder`, `learn`, `import-memory`, `skill-creator`, `find-skills` (vault), `teach` / `grilling` / `grill-me` (vault)
- Tools: Google Drive, Docs, Sheets, Gmail (read), Google Calendar, Claude Docs, Make

### Victor Drake: CRO Advisor
- Skills: `sales:forecast`, `sales:pipeline-review`, `sales:team-pipeline`, `sales:deal-review`, `sales:deal-signals`, `sales:deal-slip-scenario`, `sales:deal-advance-gap`, `sales:win-loss-review`, `convenex-business-plan`, `small-business:business-pulse`, `small-business:growth-pulse`, `product-management:write-spec`, `product-management:roadmap-update`, `product-management:stakeholder-update`, `product-management:metrics-review`, `product-management:brainstorm`, `product-management:product-brainstorming`, `product-management:sprint-planning`
- Tools: CRM app, Finance Control (read), Convene X CRM sheet, HubSpot (read), Sheets
- Move out: `SKILL-design-teardown.md` and `ui-ux-skill-addition.md` sit in Victor's folder but are design skills. Move them to Kai.

### Andrew Whitfield: Head of Partnerships
- Skills: `convenex-offer-usp`, `sales:call-prep`, `sales:call-summary`, `sales:close-plan`, `sales:handle-objection`, `sales:account-research`, `sales:create-an-asset`, `small-business:proposal-builder`, `small-business:grant-rfp-writer` (sponsor RFPs), skill-sales / skill-negotiation / skill-commercial (vault)
- Tools: CRM app, quote calculator, Gmail (drafts only), Cal.com, Apollo, Jotform Sign, Google Docs

### Marcus Reid: Partnerships Architect
- Skills: `sales:account-plan`, `sales:account-tiering`, `sales:expansion-whitespace`, `sales:stakeholder-map`, `small-business:grow-pipeline`, `small-business:lead-finder`, `event-lead-magnet-builder`
- Tools: Prospecting Machine, CRM app, Apollo, Firecrawl people/company search, Apify

### Morgan Ellis: Delegate & Guest Relations Lead
- Skills: `convene-x-calcom:calcom-bookings`, `sales:draft-outreach`, `sales:inbox-sweep`, `sales:lead-triage`, `sales:route-lead`, `sales:schedule-meeting`, `small-business:speed-to-lead`, `small-business:outreach-composer`, `small-business:inbox-manager`, `customer-support:draft-response`, `customer-support:customer-research`, `customer-support:ticket-triage`, `customer-support:customer-escalation`, `customer-support:kb-article` (guest FAQs), `small-business:ticket-deflector`
- Tools: CRM app, Events Control (guest lists), Gmail (drafts only), Google Calendar, Cal.com, Jotform, Convene X CRM sheet

### Jordan Pryce: Sales Ops, Intelligence & Quality Lead
- Skills: `sales:crm-hygiene-check`, `sales:update-opportunity`, `sales:log-activity`, `sales:account-context`, `sales:rep-context`, `sales:daily-briefing`, `sales:end-of-day`, `sales:weekly-wrap`, `sales:renewal-radar`, `sales:customer-health`, `sales:customer-voice`, `sales:setup`, `small-business:crm-autopilot`, `small-business:call-list`, `small-business:reactivate`, `data:validate-data`, `data:explore-data`, `data:data-context-extractor`, `/cx-sales-research` (PC only)
- Tools: CRM app, Prospecting Machine, Convene X CRM sheet, HubSpot, Zoho CRM, Apollo, Apify, Supabase

### Sienna Cole: Head of Event Operations & Delivery
- Skills: `operations:runbook`, `operations:process-doc`, `operations:risk-assessment`, `operations:status-report`, `operations:change-request`, `operations:capacity-plan`, `operations:vendor-review` (venues, caterers)
- Tools: Events Control, Google Calendar, Docs, Sheets, WordPress (event pages, read)
- Vault: Guide 1 (Five-Step Framework), Guide 2 (45-Minute Conversation Arc), event-campaign-runbook

### Priya Anand: Head of Finance
- Skills: `finance:journal-entry`, `finance:journal-entry-prep`, `finance:reconciliation`, `finance:close-management`, `finance:financial-statements`, `finance:variance-analysis`, `finance:audit-support`, `finance:sox-testing` (not needed yet), `small-business:cash-flow-snapshot`, `small-business:close-month`, `small-business:month-end-prep`, `small-business:invoice-chase`, `small-business:ap-processor`, `small-business:pay-the-bills`, `small-business:report-pack`, `small-business:tax-prep`, `small-business:tax-season-organizer`, `xlsx`
- Tools: Finance Control and the quote calculator (our own claude.ai apps; we do not use Xero), Sheets.

### Grace Bellamy: Operations & Admin Coordinator
- Skills: `operations:process-optimization`, `docx`, `pdf`, `pptx`, `docs`, `google-workspace`, `pdf-viewer:open`, `pdf-viewer:fill-form`, `pdf-viewer:annotate`, `slack-by-salesforce:channel-digest`, `slack-by-salesforce:summarize-channel`, `slack-by-salesforce:standup`
- Tools: Convene X Standing (members), Events Control (dates), Drive, Docs, Sheets, Google Calendar, WordPress (BuddyPress members, read)

### Eleanor Voss: Legal & Compliance Lead
- Skills: `legal:review-contract`, `legal:triage-nda`, `legal:compliance-check`, `legal:legal-risk-assessment`, `legal:legal-response`, `legal:brief`, `legal:meeting-briefing`, `legal:vendor-check`, `legal:signature-request` (prepare only), `operations:compliance-tracking`, `small-business:contract-review`, `pdf-viewer:sign` (prepare only), skill-compliance-os (vault)
- Tools: Drive, Docs, Jotform Sign (prepare only)

### Freya Lockhart: Head of Marketing & Content
- Skills: `content-coach` (repo), `brand-brief` (repo), `small-business:content-strategy`, `small-business:marketing-monday`, `marketing:draft-content`
- Tools: everything her team uses (read); final sign-off before anything goes to you

### Felix Grant: Brand & Quality Reviewer
- Skills: `convenex-brand-direction`, `marketing:brand-review`, `small-business:brand-style`, `canva:brand-check`, `canva:get-design-feedback`, `design:design-critique`, `design:ux-copy`, `post-grader` (repo, final gate)
- Tools: Canva (read), WordPress (read)

### Iris Bennett: Senior Content Writer
- Skills: `content-writer`, `marketing:content-creation`, `convenex-content-multiplier`, `repurpose` (repo), `convenex-newsletter-writer`
- Tools: WordPress (drafts only), Claude Docs, Google Docs

### Theo Marsh: Social Media & LinkedIn Strategist
- Skills: `social-media-expert`, `post-writer` (repo), `viral-hooks` (repo), `post-scheduler` (repo, Buffer), `convenex-carousel-writer`, `small-business:social-content-engine`, `canva:resize-for-social-media`, linkedin-hook-writer (vault)
- Tools: Social Media Machine, Buffer, Canva, HubSpot social (read)

### Amara Osei: Email & Lifecycle Specialist
- Skills: `marketing:email-sequence`
- Tools: Gmail (drafts only), HubSpot marketing email (drafts). **No bulk email platform yet** (Brevo planned).

### Leo Ferreira: Campaign Strategist
- Skills: `marketing:campaign-plan`, `small-business:ad-manager` (dormant until ad budget)
- Tools: HubSpot campaigns, Google Calendar
- Vault: event-campaign-runbook, landing-page-sprint

### Callum Reyes: SEO & Technical Auditor
- Skills: `seo-auditor`, `marketing:seo-audit`, `small-business:seo-ai-visibility`, fixing-metadata (vault), skill-aeo (vault)
- Tools: DataForSEO, Rank Math via WordPress, Firecrawl. SEO_Data connector **needs sign-in**.

### Dev Malhotra: Keyword & Search Insights Analyst
- Skills: `keyword-researcher`, ai-citation-copy (vault), skill-aeo (vault)
- Tools: DataForSEO (keywords, AI mentions)

### Nadia Kovač: Competitive Intelligence Analyst
- Skills: `competitor-analyst`, `marketing:competitive-brief`, `product-management:competitive-brief`, `sales:competitive-intelligence`, `last30days`, `small-business:review-reputation`, `product-management:synthesize-research`, `design:research-synthesis`
- Tools: Firecrawl, Apify, DataForSEO backlinks

### Sana Iqbal: Performance & Analytics Lead
- Skills: `marketing:performance-report`, `small-business:report-builder`, `data:analyze`, `data:build-dashboard`, `data:create-viz`, `data:data-visualization`, `data:statistical-analysis`, `data:sql-queries`, `data:write-query`, `dataviz`
- Tools: CRM app, Finance Control, Social Media Machine, Buffer metrics, HubSpot analytics, Sheets, Supabase

### Kai Novak: Web & UX/UI Designer
- Skills: `web-artifacts-builder`, `theme-factory`, `design:design-system`, `design:design-handoff`, `design:accessibility-review`, `design:user-research`, all `engineering:*` (10), `code-review`, `simplify`, `security-review`. Vault: Elementor skills (lmoncany ×2, jezweb, proofpilot), baseline-ui, improve-ui, ui-skills-root, create-design-md, design-loop, design-teardown, fixing-accessibility, fixing-motion-performance, vercel-react-best-practices, agent-browser
- Tools: WordPress, Figma
- `web-designer` (repo, rebuilt from the vault), plus `jezweb-wordpress-elementor`, `lmoncany-elementor-wordpress`, `proofpilot-elementor-calibration`, `design-loop`, `design-teardown` (repo)

### Zara Lindqvist: Motion & Microsite Specialist
- Skills: `canvas-design`, `small-business:canva-creator`, `canva:edit-design`, `canva:implement-feedback`, `canva:bulk-create`, scroll-film-studio (vault), skill-graphic-designer (vault)
- Tools: Canva, Higgsfield, Figma
- `motion-microsite` and `scroll-film-studio` (repo, rebuilt from the vault)

### Rhys Calder: Video Editor & Motion Film Producer
- Skills: `video-production` (repo, ffmpeg playbook), `blotato-video` (repo, kie.ai video; renamed from `generate`)
- Tools: Higgsfield, Canva video
- **PC ONLY:** video-director, huashu-motion, take-one, explainroo, argo-guide, rossark-motion-skill, reanimate, earshot, real-sound (need local installs in `C:\Users\User\video-tools`)

### Not assigned (no current need)
- `human-resources:*` (9 skills), `small-business:hiring-screener`, `small-business:job-post-builder`, `small-business:payroll-prep`, `small-business:plan-payroll`: no staff yet
- `small-business:inventory-planner`, `small-business:restock`: no stock
- lark-doc (vault): Lark isn't used
- Claude Code system skills (`init`, `run`, `loop`, `update-config`, `claude-api`, `workflow-authoring`, `plugin-authoring`, `keybindings-help`, `fewer-permission-prompts`, `session-start-hook`): tooling, not agent work
- chisle, chisle-audit, chisle-review, chisle-help (vault): purpose unclear. Tell me what they're for and I'll place them.

---

## 3. Problems found

1. ~~The org chart is out of date.~~ **Fixed 9 Nov:** `org-chart.md` in Drive is rewritten with all 22 agents + Jarvis. The Command Centre Agents tab now includes Rhys, shows the org chart, and lists each agent's skills.
2. **No agent runs on a schedule.** The Agent Jobs sheet shows all 8 scheduled jobs and 6 starter jobs were cancelled on 6 Nov to replan. `team-roster.md` now says so (fixed 9 Nov); `INDEX.md` still has the old wording.
3. ~~Empty files in the Drive root.~~ **Fixed 9 Nov:** 15 empty files and 2 identical skill-graphic-designer copies moved to the Drive bin.
4. ~~Roster skill names don't match what's installed.~~ **Fixed 9 Nov:** `team-roster.md` now uses the installed names (`marketing:campaign-plan`, `email-sequence`, `brand-review`, `performance-report`).
5. ~~`generate` name clash.~~ **Fixed 9 Nov:** the repo skill is now `blotato-video`.
6. ~~`cx-` agents PC only.~~ **Fixed 9 Nov:** all 22 rebuilt from the vault into `.claude/agents/`; `CLAUDE.md` routes "get Amara to…".
7. **Connectors failing in cloud sessions:** Slack, Notion, Asana, Ahrefs, Klaviyo, Similarweb, Calendly, Clay and others (proxy refused), plus n8n. SEO_Data, BigQuery and Datadog need sign-in.

---

## 4. Missing skills (ranked)

| # | Missing | For | Why it matters |
|---|---|---|---|
| 1 | ~~`web-designer`~~ | Kai | Done 9 Nov |
| 2 | ~~`motion-microsite`~~ | Zara | Done 9 Nov |
| 3 | Rhys's 9 video tools | Rhys | PC only (local installs); cloud uses `video-production` + `blotato-video` |
| 4 | Delegate fit scorer / guest-list builder | Morgan | Scores sign-ups against the Director+ ICP and five sectors, and builds the host sign-off list. That's the core of the business, and no skill does it. |
| 5 | Event run-sheet & seating plan | Sienna | Day-of timings, table plan, host briefing pack. `operations:runbook` is generic. |
| 6 | Venue shortlist & booking brief | Sienna | Pulls from the 10+ London venue pages on the site and compares options |
| 7 | Sponsor proposal & Deal Form generator | Andrew | Fills the order form and T&C from a template; `proposal-builder` is generic |
| 8 | Post-event debrief & testimonial request | Sienna, Amara | Closes the loop after each event (tech-stack gap #8) |
| 9 | Event P&L / per-event budget | Priya | Cost per seat, sponsor margin. The finance skills are month-end, not per-event. |
| 10 | Speaker & table-host recruiter | Sienna | Sienna owns this, but has no skill for it |
| 11 | Do-not-contact list manager | Jordan | Was a starter job; needs a repeatable skill |
| 12 | Membership admin (BuddyPress / cx-standing) | Grace | Onboarding SOP exists, but no skill |

Tool gaps (from `tech-stack.md`, still open): Brevo (bulk email, SMS, WhatsApp),
Make scenarios wired to the CRM, Stripe payment links, and UTM source tracking.
Accounting runs in our own Finance Control app, not Xero.
