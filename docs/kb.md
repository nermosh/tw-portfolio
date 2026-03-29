---
icon: lucide/book-user
---
# Knowledge Base Management

I spent ten years in the Technical Support department at Intermedia Communications — a US-based cloud communications company with customers across North America, Europe, and Asia-Pacific. Over that time, I grew from writing help articles into managing [the full knowledge base](https://support.intermedia.com/app/main): I started as a contributor, then supported the Knowledge Manager, and eventually took over that role fully.

At its largest, the knowledge base held over 1,300 articles covering 20 products, published across five white-label brands and up to four geographic regions — maintained by a team of four writers.

The work on this page covers content strategy, localization, platform migration, and AI tool adoption. These areas draw on editing, research, project coordination, and cross-cultural communication just as much as on technical writing — so if you come from one of those fields, you probably already have a stronger starting point here than you think.

## :lucide-layers: White-label Content Strategy

At its peak, the knowledge base covered about 20 products and over 1,300 articles. Part of that growth came from company acquisitions, which meant some articles had been written in different styles and formats before joining our library.

:lucide-target: **Goal:** Keep one master content library that published correctly to five white-label brands at the same time — each with its own product set and release schedule — without content meant for one brand showing up on another.

!!! note "What is a white-label arrangement?"
    Partner companies resell a product under their own brand name. Each partner brand had a different product catalog and sometimes a different release timeline for new features.

### :lucide-code: Variable Management

:lucide-triangle-alert: **Constraints:** The KMS (Knowledge Management System — the platform used to write and publish articles) used **content variables** to customize what each brand's site showed. Variables are placeholder tokens — similar to a mail-merge field — that get replaced with brand-specific text when an article publishes. For example, `$fileSync` might show as one product name on one brand's site and a different name on another. Some variables hid entire content blocks from certain brands; others showed them only to specific brands. There were also variables for building links to external resources, and those cross-reference links had to be verified carefully too.

If a variable token had a typo, the raw placeholder text would appear on the live site instead of the correct product name or feature description — with no warning, visible to real customers.

The KMS preview mode couldn't render variables, because the substitution happened in a separate publishing pipeline after the draft left the system. This meant some errors only appeared after going live. The platform also didn't include **linting tools** (automated checkers that catch syntax errors before publishing) — it was built for part-time contributors on the support team, so professional-grade review tooling wasn't part of the setup.

:lucide-user-check: **My role:** Knowledge Manager and Technical Writer — primary reviewer for brand correctness across all five publications.

I built my product knowledge over years as a Support agent, which gave me a solid mental model of which features each brand had. Since the tooling didn't include a variable validation layer, manual review using checklists was the main safety check — shared across a team of four.

I caught most errors by carefully reading through the draft text in the **WYSIWYG editor** (a visual editor that shows you a formatted preview as you type). For anything that only showed up after publishing to production, I fixed it as quickly as possible.

!!! success "Highlight"
    Every other week the knowledge base got 2 to 5 new features to cover, resulting in 4–12 articles to publish across regional schedules. After every publish cycle I manually checked each article on every brand's site against a checklist — catching live errors immediately, before customers hit them. Live errors reaching customers were rare: the checklist kept the most critical variables under close review, and any recurring mistake patterns fed directly back into contributor onboarding and training.

### :lucide-calendar-clock: Regional Release Scheduling

:lucide-triangle-alert: **Constraints:** Features didn't roll out to all regions at the same time. A typical release went to the US first, then Australia, then Europe — with Japan sometimes getting the same feature months later, occasionally with a different scope. The knowledge base needed region-specific article versions that went live on different dates, with content that could legitimately differ between regions for a while. Missing a regional publish date meant users in that country would see outdated or missing instructions right after a feature launched for them. The release dates could change often, so we were not able to use the scheduling feature of the KMS.

:lucide-user-check: **My role:** Knowledge Base Release coordinator — I tracked rollout schedules across all brands and regions and was responsible for making sure every regional article version went live on the correct date.

For feature releases, I matched each article update to the regional rollout schedule and published accordingly. For content updates that weren't tied to a release — just improvements to existing self-support content — I checked the weekly activity report to confirm that writers had updated all regional versions, not just the primary one. It's easy to miss the regional articles in those cases, and this check was the main safeguard against gaps reaching users in specific countries.

!!! success "Highlight"
    Managing five brands across four geographies with staggered release schedules — without a single automated scheduling or validation tool — required keeping a live mental model of the product matrix updated at all times. The absence of tooling made the process entirely dependent on process discipline and product knowledge built over years. Over three years in this role (two as contributor, one as Knowledge Manager), there were zero missed regional publish dates.

## :lucide-globe: Japan Partner Localization Workflow

The Japanese market was handled through a local partner brand. As part of their agreement, the partner was responsible for providing Japanese-language versions of all knowledge base content. This was a separate pipeline from how we handled other regions, where everything ran through the same KMS.

:lucide-target: **Goal:** Keep the Japanese-language knowledge base accurate and up to date, even though the two teams were working in completely separate systems with no automated connection between them.

:lucide-triangle-alert: **Constraints:** We used Oracle CX Knowledge for our KMS, while the Japanese partner worked in their own **TMS** (Translation Management System — software that manages the process of sending content for translation and receiving it back). The two systems had no **API integration** (an automated connection that lets software exchange data without anyone doing it manually), so every update had to be transferred by hand.

With a fully manual process, keeping the two versions in sync was an ongoing challenge. Content would sometimes **drift out of sync** — meaning the English source had been updated, but the Japanese version hadn't caught up yet. Coordinating on changes took real time from both teams.

There were also cross-cultural differences in how the two teams communicated — in pace, in how feedback was given, and in how decisions got made. These are normal things to navigate in international collaboration, but they did affect how long it took to agree on process changes.

:lucide-user-check: **My role:** Knowledge Manager and cross-team lead — I represented our content team in joint sessions with the Japanese partner and drove workflow improvements on both sides.

I ran regular meetings with the Japanese partner team to check on the current workflow, spot any content that had drifted out of sync, and suggest improvements.

Working across cultures meant adjusting how I communicated. I framed feedback as observations rather than corrections, gave the partner team time to review and reach their own consensus before expecting an answer, and wrote everything as precisely as possible to reduce translation ambiguity — because the written text is much easier to translate and process than live speech in a foreign language. These habits have stayed with me and shaped how I approach cross-team communication generally.

!!! success "Highlight"
    When I inherited the workflow, weekly sync meetings regularly ran over one hour — with long pauses while the partner team discussed internally and processed action items. By gradually moving parts of the discussion to async email exchange and making the agenda more structured, the meetings got shorter over time and eventually became unnecessary. Over approximately ten months, the workflow reached a point where it ran smoothly without regular check-ins.

## :lucide-arrow-right-left: Content Migration

A knowledge base that grows over many years naturally picks up content that becomes outdated, and formatting that shifts as platforms and standards evolve. When the company moved from a self-hosted open-source platform (with a Coveo search module) to Oracle CX Knowledge — an enterprise cloud solution — it was a good moment to also clean up the library.

:lucide-target: **Goal:** Move the full knowledge base to Oracle CX Knowledge, use the migration as a chance to improve content quality and remove outdated material, and make sure everything worked correctly on the new platform.

:lucide-triangle-alert: **Constraints:** A knowledge base of this size and age naturally has some drift — articles that were accurate when written but haven't been updated since, or content from acquired companies that was formatted differently. Articles that came in through acquisitions sometimes had HTML structure issues that caused display problems.

Given the volume of articles and the ongoing work on content from acquired companies, the migration moved forward with the full library — including some articles for deprecated features. After the migration, some articles that had displayed fine in the old system showed rendering issues in the new one — a normal part of any platform switch, but it required a dedicated clean-up pass.

:lucide-user-check: **My role:** Knowledge Manager's assistant — I handled the content review after migration, archived legacy articles, and fixed HTML formatting where needed. This migration happened while I was still in the assistant role, before I took on full Knowledge Manager responsibilities.

Before the migration, I went through the list of articles flagged automatically based on labels and update dates. I evaluated each one against a checklist: whether the feature was still supported and whether there were any duplicate or overlapping articles on the same topic.

After the migration, I reviewed the most popular articles for display issues and fixed them by editing the **HTML source code** (the markup language behind web pages) directly, to bring the formatting in line with Oracle CX standards.

!!! success "Highlight"
    Out of 130 articles flagged for review, I archived around 50 — cleaning up nearly 40% of the reviewed content before it could carry its issues into the new platform.

## :lucide-chart-bar: Analytics and Reporting

:lucide-target: **Goal:** Track how the support team's writing time was being used and figure out where content coverage was thin — meaning which products or features needed more articles, or other attention from the Support department, such as improved agent training or ticket templates.

### :lucide-search: Search Term Analysis

:lucide-triangle-alert: **Constraints:** Search term data was available, but it was hard to act on. Most customers searched with just 1–3 words, and since the product catalog had many products with similar-sounding features, the same search terms kept showing up across unrelated products. For example, `fax` relates to both the fax service in VoIP telephony and fax-to-email configuration in Exchange Mail Server. Even trickier: phone call features in the VoIP service and in the Call Center solution are nearly identical in description, but users need different settings, legal terms, and limits. There wasn't enough information in short queries to tell what a specific customer was actually looking for.

:lucide-user-check: **My role:** Analyst — I reviewed the search term reports, assessed their usefulness, and fed findings into content planning decisions.

Search term reports were part of the regular reporting cycle, but their value was limited by the query length and product overlap. I flagged this as a structural data problem and contributed to the internal discussion about adding auto-completion to the search input — a change that would help users form more specific queries and make the data more actionable. The feature was later prioritized as part of the RAG rollout planning.

### :lucide-file-chart-column: Regular Reporting

:lucide-triangle-alert: **Constraints:** The reporting process and Excel templates I inherited were built around a specific set of metrics that made sense at the time. As the team's priorities shifted — toward AI-assisted search and a more data-driven content strategy — the templates needed to evolve too. That meant learning the reporting layer in Oracle CX and reworking the calculation logic in the templates.

:lucide-user-check: **My role:** Reporting owner — I inherited the process from the previous KM, maintained it, and rebuilt parts of it as business needs changed.

I produced weekly and monthly reports for Support leadership using Oracle CX Knowledge data. Weekly reports tracked contributor productivity: authoring hours per person and the number of drafts and published articles, covering all contributors across the company — KB team members, product managers, technical writers, and other Client Success staff. Monthly reports tracked customer feedback volume by product category and by ticket status (backlog, in progress, canceled, done). I learned to build and customize reports directly in Oracle CX and set up auto-delivery of CSV exports so the process was less manual.

The trends identified in feedback analysis fed into a content improvement backlog, which experienced Support agents contributed to during their dedicated writing time.

!!! success "Highlight"
    When I left the company, I wrote step-by-step guides with screenshots and recorded a video walkthrough of the full reporting process — so the team could keep running and adapting the reports without losing the context that had built up over time.

### :lucide-flask-conical: RAG Rollout Reporting

:lucide-triangle-alert: **Constraints:** During the RAG beta testing phase, an unexpected complication appeared: beta testers' feedback was routed into the same channel as real customer responses. This caused a sharp spike in negative ratings that looked alarming until you understood where it was coming from. Without separating that data, the regular reports would have sent the team chasing a problem that wasn't there.

:lucide-user-check: **My role:** Reporting owner — I identified the data contamination issue, updated the report structure to isolate it, and made sure leadership had a clear picture of what was actually happening.

I updated the Excel templates to track the metrics that mattered for the RAG rollout, and restructured the reports to account for the beta feedback channel — so the testing spike was shown separately and didn't distort the regular customer satisfaction data.

## :lucide-bot: AI Search Implementation (RAG)

When the company added an AI-powered search and chatbot tool to the knowledge base, we quickly discovered that making AI work well with existing content is a content strategy problem just as much as a technical one.

!!! note "What is RAG?"
    Retrieval Augmented Generation is a method where an AI tool searches your document library before writing its answer, instead of relying only on what it was trained on. The better your content is structured, the better the AI's answers will be. This is increasingly a core part of what Technical Writers and Knowledge Managers do.

:lucide-target: **Goal:** Make sure the knowledge base content worked well with the new RAG search and chatbot tool, so users could get accurate, complete answers without having to contact Support.

Testing surfaced three content-level problems that weren't obvious until the AI started working with the library. Each one required a different fix.

### :lucide-split: Product Disambiguation

:lucide-triangle-alert: **Constraints:** The RAG tool got confused when different products had features with the same name. It would sometimes give instructions for the wrong product — mixing up two similar products in a single response. With 20 products in the catalog, naming overlap was common.

:lucide-user-check: **My role:** Content tester — I identified the root cause through testing and proposed an interface-level fix to the product team.

I traced the problem back to the query structure: users were searching without specifying which product they meant, so the AI had to guess. I recommended adding auto-completion to the search input — prompting users to include the product name before the AI processed the query. This was a low-effort fix that didn't require changing any article content.

### :lucide-git-branch: Incomplete Article Structure

:lucide-triangle-alert: **Constraints:** One large product's documentation had been migrated from Confluence Knowledge Base (Atlassian's platform to publish the pages tied to the Support tickets within the system), where it was organized in a parent–child tree structure. Each child article assumed the reader had come from the parent and skipped the initial steps. A human browsing the knowledge base could navigate naturally through the tree. The RAG tool couldn't — it pulled individual articles in isolation and had no way to reconstruct the missing context, so it generated incomplete instructions.

:lucide-user-check: **My role:** Content architect and TW coach — I fixed the structural issue in the affected articles and updated the style guide to prevent it recurring.

I added a section to the style guide on how to write **self-contained articles** — articles that make sense on their own, without requiring the reader to have navigated from a specific parent page. I rewrote the top-level articles for the affected product to include the missing initial steps directly, then worked with the Technical Writer who owned that product to link all child articles back to the right top-level article, giving the RAG tool the full context it needed.

!!! success "Highlight"
    This fix also improved the experience for human readers who landed on a child article directly from search — a problem that had existed before the RAG tool but had never been formally addressed.

### :lucide-image-off: Screenshot Dependency

:lucide-triangle-alert: **Constraints:** Many articles used a screenshot of a UI element and expected the reader to figure out the step from the image alone, without a text description. A human reading the article could do that easily. The AI couldn't — it doesn't process images the same way, so those steps were invisible to it. This caused low-quality or incomplete AI-generated answers and showed up as a spike in negative feedback during beta testing.

:lucide-user-check: **My role:** Project initiator — I identified the scope of the problem, determined it was too large for a one-off fix, and proposed a structured solution.

The screenshot-dependency issue affected a large portion of the library and couldn't be addressed article by article manually. I identified it as a project suitable for a dedicated initiative and proposed it as an internship task.

!!! success "Highlight"
    This problem became the foundation for the full style guide project described in the next section — including the internship, the content analysis methodology, and the GPT-based rewriting workflow. The intern updated the top-50 most-visited articles as part of that project, directly addressing the screenshot-dependency issue at scale.

    The product team prioritized the autocomplete feature for implementation after the full RAG rollout. The broader content restructuring initiative targeted the most popular products first, with the top-50 articles completed during the internship.

## :lucide-book-open: Style Guide

As the knowledge base grew — through acquisitions, white-label expansion, and new AI tools — keeping content consistent became more than just an editorial preference. Inconsistency started causing real downstream problems, and the screenshot-dependency issue discovered during RAG testing made it clear that a formal style guide was overdue.

:lucide-target: **Goal:** Create a shared style guide for the knowledge base that would support consistent formatting, work well with machine translation, bring acquired-company content into alignment, and help the AI search tool work more reliably. The longer-term goal was to use the style guide as the foundation for a semi-automated article rewriting tool.

:lucide-triangle-alert: **Constraints:** A style guide existed, but it was scoped narrowly: AP Stylebook conventions for headings and punctuation, screenshot formatting rules, color usage, and variable syntax. It hadn't been updated to account for the machine translation pipeline, the RAG search implementation, or the full range of article types that had accumulated over the years.

The screenshot-dependency problem in particular was too widespread to fix manually one article at a time. It needed a documented standard and a scalable process to address it across the full library.

!!! note "If you've worked in editorial, journalism, or publishing"
    This challenge will feel familiar. Establishing a house style from scratch — especially one that needs to serve multiple audiences and tools at once — is the same discipline, applied to software and support content.

:lucide-user-check: **My role:** Lead author and owner of the style guide. I also scoped the project, recruited and onboarded an intern to support the research phase, and worked with the DEV team on the rewriting tool built around the guide.

### Building the style guide with an intern

I identified the screenshot-dependency project as a good fit for an internship and participated in hiring and onboarding the intern. I selected a representative sample of articles that covered the full range of content types in the library and assigned the intern to analyze them — identifying patterns that could affect AI accessibility and machine translation quality, and suggesting better phrasing templates and structural approaches for each pattern.

The intern's analysis gave us a solid evidence base. I led the main work of turning those findings into a coherent set of rules, working through each pattern with the intern and making the final calls on the recommended approach. I built the guide on three reference layers. The **Microsoft Writing Style Guide** was the primary standard — a natural fit given that Intermedia was a Platinum Microsoft partner, and the guide that most enterprise tech teams in the US treat as a baseline. The **AP Stylebook** had been the KB's historical reference, so I kept its conventions where they didn't conflict. Sections on international communication — how to write dates, times, and culturally neutral phrasing — drew on the **Google Developer Documentation Style Guide**, which handles these cases well. Translation guidance came directly from **Oracle** (our KMS vendor) and **Weglot** (our auto-translation vendor), covering what content structures and sentence patterns their tools handle most reliably. Once reviewed, I published the guide and became its ongoing owner, updating it as new content types came in.

### Testing with a custom GPT before the full tool was built

The DEV team was working on a more complete application — a tool where a KB contributor could select an article, get an AI-generated rewrite based on the style guide rules, review it for factual accuracy, and publish the corrected version. That tool took longer to build than expected.

While it was in development, I built a **custom shared GPT** (a reusable AI assistant configured with specific instructions) that simulated the same workflow. Testing revealed two gaps in the initial style guide rules: the GPT invented non-existent UI navigation paths when menu names weren't specified explicitly, which led us to add precise menu-naming requirements; and it applied the same rewriting approach regardless of article type or interface, so we added explicit rules distinguishing how-to articles from explanatory ones, and hardware interfaces from desktop and web UIs. This let the team start testing the process, catch edge cases, and refine the style guide rules iteratively — without waiting for the full tool. By the time the application was ready, the process was already well-tested.

!!! success "Highlight"
    When I left the company, the custom GPT was in regular use by the 4 Knowledge Base team members who had a GPT license — including the intern, who used it to update the top 50 articles during her internship. The full DEV-built rewriting tool was still in final stages and hadn't been rolled out yet.
