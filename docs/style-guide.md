---
icon: lucide/book-open-check
---
# Style Guide

Style guide work is not a one-time writing project. It is an ongoing process of auditing what exists, defining what should be true, testing rules against real content, and making sure the standard actually gets used. The sections below show how I approach each of those stages.

## :lucide-search: Audit and Research

A style guide that isn't grounded in the actual content it will govern tends to produce rules that look good on paper but don't hold up in practice. Before writing any new rule, I start with the content itself.

### Knowledge base, 20 products, 1,300+ articles

The existing guide covered AP Stylebook conventions, screenshot formatting, color standards, and variable syntax. To find what it was missing, I selected a representative sample of articles across all content types and assigned an intern to analyze them — documenting patterns that caused problems for machine translation and AI search, with real examples and suggested alternatives. The analysis produced a prioritized list of content problems across the library, which became the evidence base for every new rule added.

<!-- NEXT PROJECT EXAMPLE -->

### B2B sportsbook platform — documentation from scratch

Starting point: under 100 articles total, most of them internal policies. About 25 product articles were publicly available; another 15 existed only in Russian as legacy content. There was a glossary with no clear owner and no agreed English variant — contributors had been mixing British and US English throughout.

The audit covered existing content, product UI, and internal communication channels to establish which English variant the product itself used. Structured interviews with managers across each department mapped the audiences, their priorities, and what they valued most in documentation. The glossary was the first formal output: groomed, expanded, and published in Confluence, which enabled Rovo AI to automatically recognize and surface term definitions across Confluence and Jira.

!!! success "What this produces"
    An evidence base, not a preference list. Every rule traces back to a documented pattern from real content — which also makes it easier to explain to contributors why the rule exists.

## :lucide-pen-tool: Defining the Standard

Defining rules means making judgment calls: what level of prescription is useful without being constraining, which edge cases to address explicitly, and which reference standards to defer to. It also means knowing when an existing convention is worth keeping and when it needs to change.

### Knowledge base, 20 products, 1,300+ articles

The project extended the existing AP-based guide in four areas:

- **Screenshot rules**: Changed from formatting-only guidance to functional rules. Images must visually guide navigation without requiring the reader to read menu names. No text labels on top of images. Every image-dependent step must be completable from the text alone.
- **Article type patterns**: Introduced specific structures for hardware quick start guides, mobile app overviews, and mobile app how-to articles — defining required sections, order, and phrasing conventions for each type.
- **Phrasing for accessibility and translation**: Added rules for sentence length and structure, terminology consistency, pronoun avoidance in procedural steps, and punctuation conventions optimized for machine translation — drawing on direct input from Oracle (KMS vendor) and Weglot (translation vendor).
- **Inline icons and icon library**: Introduced the use of product UI icons directly in article text, alongside the label, so users can match what they read to what they see on screen. Built an internal library cataloguing icons across all 20 product interfaces.

The guide was built on three reference layers: **Microsoft Writing Style Guide** as the primary standard (aligned with the company's Platinum Microsoft partner status), **Google Developer Documentation Style Guide** for international communication conventions, and **AP Stylebook** for the existing conventions already in use.

<!-- NEXT PROJECT EXAMPLE -->

### B2B sportsbook platform — two guides, two audiences

The client-facing Documentation Portal got a formal style guide built from scratch: US English (matching the product UI and codebase wording), **Google Developer Documentation Style Guide** as the primary reference for structure and international conventions, and a clear editorial stance on the open decisions — Oxford comma enforced by spellchecker, title case for headings to match the existing product UI. The Client Success team reviewed and approved it, then contributed examples from their actual and planned content — making it an illustrated reference rather than an abstract rules document.

The internal wiki standard started differently: no rules first, structure first. Before formalizing anything, I wrote articles reactively while the product context was still being built — experimenting with formats to find what actually worked. Once patterns emerged, I introduced the **Diataxis framework** as the organizing principle, then built on it: Backoffice reports follow a consistent Filter → Table article structure; shared UI components (filters, validation rules) are described once in a dedicated reference article and transcluded into every page that needs them, so updates propagate automatically.

!!! note "For writers coming from national or regional documentation standards"
    The Microsoft and Google guides represent the international baseline expected in global English-language TW roles. Familiarity with at least one signals that a writer can work in US-based or globally distributed teams without needing alignment coaching on the fundamentals.

## :lucide-flask-conical: Testing and Validation

Rules that haven't been tested against real content have unknown failure modes. Testing surfaces gaps before they reach contributors — and before the gap is a contributor's mistake rather than a rule that wasn't specific enough.

### Knowledge base, 20 products, 1,300+ articles

Before the full DEV-built rewriting tool was ready, I built a custom shared GPT configured with the style guide rules to simulate the workflow. Team members submitted article drafts; the GPT returned rewrites. Testing revealed two rule gaps:

- **Menu-naming ambiguity**: The GPT invented plausible but incorrect navigation paths when menu labels weren't specified explicitly enough. Fixed by requiring exact UI labels with no paraphrasing.
- **Article type and interface blindness**: The GPT applied uniform rewriting regardless of article type or interface (hardware vs. desktop vs. web). Fixed by adding explicit structure rules per type — which also tightened the article type patterns added in the previous phase.

<!-- NEXT PROJECT EXAMPLE -->

### B2B sportsbook platform — Rovo agent and iterative authoring

The reactive writing phase served as distributed testing: writing articles while the product context was still incomplete forced every structural decision to hold up under real conditions, not just in theory. Patterns that didn't survive contact with actual content were revised before being formalized.

The dedicated validation tool is a Rovo AI agent that reviews a Confluence article against its Diataxis document type — identifying sections that belong in a different genre and either flagging them or drafting the split into a new page. Auto-creation works but has an intermittent permissions issue that limits reliability. A migration to Claude Code-based automation is planned, including using it to analyze the full set of existing articles and generate a draft of the internal style guide with examples drawn directly from what has already been written.

!!! success "What this produces"
    Rules that have been stress-tested before rollout — and a team that has already practiced the workflow by the time the tooling is ready.

## :lucide-users: Adoption and Handoff

A style guide that contributors don't use is decoration. Getting a guide adopted means making it accessible at the right moment, connecting it to the tools people are already using, and ensuring it can be maintained after the original author moves on.

### Knowledge base, 20 products, 1,300+ articles

The guide was published in the team's shared knowledge base and linked directly from contributor onboarding documentation — so new writers encountered it in their first week. The custom GPT put the rules into a tool contributors could use immediately, without having to read the guide in full first. All four team members with a GPT license adopted it; the intern used it to update the top-50 most-visited articles during her 1.5-month internship.

At handoff, I produced step-by-step documentation and a video walkthrough of the full GPT-based workflow, including instructions for updating the GPT prompt when rules change. The guide itself included a version control section: who owns updates, what triggers a review, and how to handle conflicting input from new tools or vendors.

<!-- NEXT PROJECT EXAMPLE -->

### B2B sportsbook platform — handoff by enabling, not by instructing

The client-facing style guide was handed to the Client Success team after their review and approval. Because they had contributed the illustrative examples themselves, the guide already reflected their content — which reduced the gap between "rules document" and "thing we actually use."

The AI drafting workflow couldn't be shared directly (Gemini doesn't support shared Gems the way custom GPTs do), so instead of handing off the tool, I wrote a step-by-step instruction for the team to rebuild the same Gem with the same prompt. The team now produces content to the portal independently. No ongoing involvement required.

!!! success "What this produces"
    A guide that outlives the person who wrote it — because the process for maintaining it is as documented as the rules themselves.
