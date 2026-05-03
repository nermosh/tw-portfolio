---
title: White-label Content Strategy
engagement: intermedia-knowledge-manager-assistant
year: 2020–2024
role: Knowledge Manager and Technical Writer — primary reviewer and proofreader
  for brand correctness across all five publications.
goal: >-
  Keep one master content library that is published correctly to five
  white-label brands at the same time—each with its product set and release
  schedule—without content meant for one brand showing up on another.


  !!! note "What is a white-label arrangement?"
      Partner companies resell a product under their own brand name. Each partner brand had a different product catalog and sometimes a different release timeline for new features.
constraints: >-
  The KMS (Knowledge Management System — the platform used to write and publish
  articles) used **content variables** to customize what each brand's site
  showed. Variables are placeholder tokens — similar to a mail-merge field —
  that get replaced with brand-specific text when an article publishes. For
  example, `$fileSync` might show as one product name on one brand's site and a
  different name on another. Some variables hid entire content blocks from
  certain brands; others showed them only to specific brands. There were also
  variables for building links to external resources, and those cross-reference
  links had to be verified carefully too.


  If a variable token had a typo, the raw placeholder text would appear on the live site instead of the correct product name or feature description—with no warning, visible to real customers.
obstacles: The KMS preview mode couldn't render variables, because the
  substitution happened in a separate publishing pipeline after the draft left
  the system. This meant some errors only appeared after going live. The
  platform also didn't include **linting tools** (automated checkers that catch
  syntax errors before publishing)—it was built for part-time contributors on
  the support team, so professional-grade review tooling wasn't part of the
  setup.
lessons: Working with the Knowledge Base in this way taught me to visualize the
  content in my head, simulating the publishing pipeline so that I could see
  which parts of the text would be shown to which brands. With this skill, I was
  able to manage the variables and design the AI-assisted mass content update,
  which correctly rendered for each brand.
section: Knowledge Management
---
I built my product knowledge over years as a Support agent, which gave me a solid mental model of which features each brand had. Since the tooling didn't include a variable validation layer, manual review using checklists was the main safety check — shared across a team of four.

I caught most errors by carefully reading through the draft text in the **WYSIWYG editor** (a visual editor that shows you a formatted preview as you type). For anything that only showed up after publishing to production, I fixed it as quickly as possible.

Every other week the knowledge base got 2 to 5 new features to cover, resulting in 4–12 articles to publish across regional schedules. After every publish cycle I manually checked each article on every brand's site against a checklist—catching live errors immediately, before customers hit them. Live errors reaching customers were rare: the checklist kept the most critical variables under close review, and any recurring mistake patterns fed directly back into contributor onboarding and training.
