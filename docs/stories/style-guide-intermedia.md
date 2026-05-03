---
title: Style Guide for AI Tools Adoption
engagement: intermedia-knowledge-manager
year: "2024"
role: Knowledge manager — I scoped the project, recruited and onboarded an
  intern to support the research phase, and worked with the DEV team on the
  automated rewriting tool built around the guide.
goal: Create a shared style guide that would support consistent formatting, work
  well with machine translation and AI search, and bring acquired-company
  content into alignment. The longer-term goal was to use the guide as the
  foundation for a semi-automated article rewriting tool.
constraints: An AP Stylebook-based guide existed but covered only formatting
  conventions—screenshot rules, color standards, and variable syntax. It hadn't
  been updated for the machine translation pipeline, the RAG search
  implementation, or the full range of article types that had accumulated over
  years of growth and acquisitions. The screenshot-dependency problem was too
  widespread to fix article by article—it needed a documented standard and a
  scalable process. The DEV-built rewriting tool also took longer to build than
  expected, requiring a workaround before the full system was ready.
obstacles: ""
lessons: >-
  Testing rules via a shared GPT before the full tool was ready revealed two
  gaps: the GPT invented navigation paths when menu labels weren't specified
  exactly, and applied uniform rewriting regardless of article type or
  interface. Finding these before contributors encountered them meant the rules
  were tighter from day one.

  Handoff documentation — step-by-step guides and a video walkthrough — meant the guide and the GPT-based workflow could be maintained after I left without losing the context built up over the project.
section: Style Guide
---
### Audit and Research

The existing guide covered AP Stylebook conventions, screenshot formatting, color standards, and variable syntax. To find what it was missing, I selected a representative sample of articles across all content types and assigned an intern to analyze them — documenting patterns that caused problems for machine translation and AI search, with real examples and suggested alternatives.

I identified the screenshot-dependency project as a good fit for an internship and participated in hiring and onboarding the intern. I led the main work of turning the intern's findings into a coherent set of rules, working through each pattern with the intern and making the final calls on the recommended approach. The analysis produced a prioritized list of content problems across the library, which became the evidence base for every new rule added.

### Defining the Standard

The project extended the existing guide in four areas:

- **Screenshot rules**: Changed from formatting-only guidance to functional rules. Images must visually guide navigation without requiring the reader to read menu names. No text labels on top of images. Every image-dependent step must be completable from the text alone.
- **Article type patterns**: Introduced specific structures for hardware quick start guides, mobile app overviews, and mobile app how-to articles — defining required sections, order, and phrasing conventions for each type.
- **Phrasing for accessibility and translation**: Added rules for sentence length and structure, terminology consistency, pronoun avoidance in procedural steps, and punctuation conventions optimized for machine translation — drawing on direct input from Oracle (KMS vendor) and Weglot (translation vendor).
- **Inline icons and icon library**: Introduced the use of product UI icons directly in article text, alongside the label, so users can match what they read to what they see on screen. Built an internal library cataloguing icons across all 20 product interfaces.

The guide was built on three reference layers: **Microsoft Writing Style Guide** as the primary standard (aligned with the company's Platinum Microsoft partner status), **Google Developer Documentation Style Guide** for international communication conventions, and **AP Stylebook** for the existing conventions already in use.

### Testing and Validation

The DEV team was working on a rewriting tool where a contributor could select an article, get an AI-generated rewrite based on the style guide rules, review it for factual accuracy, and publish the corrected version. While that tool was in development, I built a **custom shared GPT** configured with the style guide rules to simulate the same workflow. Team members submitted article drafts; the GPT returned rewrites.

Testing revealed two rule gaps:

- **Menu-naming ambiguity**: The GPT invented plausible but incorrect navigation paths when menu labels weren't specified explicitly enough. Fixed by requiring exact UI labels with no paraphrasing.
- **Article type and interface blindness**: The GPT applied uniform rewriting regardless of article type or interface (hardware vs. desktop vs. web). Fixed by adding explicit structure rules per type — which also tightened the article type patterns added in the previous phase.

This let the team start testing the process, catch edge cases, and refine the style guide rules iteratively — without waiting for the full tool. By the time the application was ready, the process was already well-tested.

### Adoption and Handoff

The guide was published in the team's shared knowledge base and linked directly from contributor onboarding documentation — so new writers encountered it in their first week. The custom GPT put the rules into a tool contributors could use immediately, without having to read the guide in full first. All four team members with a GPT license adopted it; the intern used it to update the top-50 most-visited articles during her 1.5-month internship.

At handoff, I produced step-by-step documentation and a video walkthrough of the full GPT-based workflow, including instructions for updating the GPT prompt when rules change. The guide itself included a version control section: who owns updates, what triggers a review, and how to handle conflicting input from new tools or vendors.

!!! success "Highlight"
    When I left the company, the custom GPT was in regular use by all 4 Knowledge Base team members who had a GPT license — including the intern, who used it to update the top 50 articles during her internship. The full DEV-built rewriting tool was still in final stages and hadn't been rolled out yet.
