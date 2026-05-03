---
title: Style Guides for a Platform Launching from Scratch
engagement: betby-technical-writer
year: "2025"
role: Lead author for both the client-facing Documentation Portal style guide and
  the internal Confluence wiki standard.
goal: >-
  Establish documentation standards for two distinct audiences from scratch — a
  client-facing Documentation Portal and an internal Confluence wiki — starting
  with under 100 articles and no agreed English variant or active style standard.
constraints: >-
  Almost no existing content to build on: under 100 articles total, mostly
  internal policies. About 25 product articles were publicly available; another
  15 existed only in Russian as legacy content. The glossary had no clear owner
  and no agreed English variant — contributors had been mixing British and US
  English throughout. The dedicated Rovo AI validation agent has an intermittent
  permissions issue that limits its reliability for automated article creation.
lessons: >-
  Starting with reactive authoring rather than formalizing rules upfront meant
  every structural decision survived contact with real content before being
  codified. The client-facing guide was more readily adopted because the Support team contributed examples from their own content — making it reflect
  what they actually wrote, not an abstract ideal. When tooling can't be shared
  directly (Gemini Gems don't support sharing the way custom GPTs do),
  documenting how to rebuild it is the next best handoff.
section: Style Guide
---
### Audit and Research

The audit covered existing content, product UI, and internal communication channels to establish which English variant the product itself used. Structured interviews with managers across each department mapped the audiences, their priorities, and what they valued most in documentation. The glossary was the first formal output: groomed, expanded, and published in Confluence, which enabled Rovo AI to automatically recognize and surface term definitions across Confluence and Jira.

### Defining the Standard

The client-facing Documentation Portal got a formal style guide built from scratch: US English (matching the product UI and codebase wording), **Google Developer Documentation Style Guide** as the primary reference for structure and international conventions, and a clear editorial stance on the open decisions — Oxford comma enforced by spellchecker, title case for headings to match the existing product UI. The Client Success team reviewed and approved it, then contributed examples from their actual and planned content — making it an illustrated reference rather than an abstract rules document.

The internal wiki standard started differently: no rules first, structure first. Before formalizing anything, I wrote articles reactively while the product context was still being built — experimenting with formats to find what actually worked. Once patterns emerged, I introduced the **Diataxis framework** as the organizing principle, then built on it: Backoffice reports follow a consistent Filter → Table article structure; shared UI components (filters, validation rules) are described once in a dedicated reference article and transcluded into every page that needs them, so updates propagate automatically.

### Testing and Validation

The reactive writing phase served as distributed testing: writing articles while the product context was still incomplete forced every structural decision to hold up under real conditions, not just in theory. Patterns that didn't survive contact with actual content were revised before being formalized.

The dedicated validation tool is a Rovo AI agent that reviews a Confluence article against its Diataxis document type — identifying sections that belong in a different genre and either flagging them or drafting the split into a new page. Auto-creation works but has an intermittent permissions issue that limits reliability. A migration to Claude Code-based automation is planned, including using it to analyze the full set of existing articles and generate a draft of the internal style guide with examples drawn directly from what has already been written.

### Adoption and Handoff

The client-facing style guide was handed to the Client Success team after their review and approval. Because they had contributed the illustrative examples themselves, the guide already reflected their content — which reduced the gap between "rules document" and "thing we actually use."

The AI drafting workflow couldn't be shared directly (Gemini doesn't support shared Gems the way custom GPTs do), so instead of handing off the tool, I wrote a step-by-step instruction for the team to rebuild the same Gem with the same prompt. The team now produces content to the portal independently. No ongoing involvement required.
