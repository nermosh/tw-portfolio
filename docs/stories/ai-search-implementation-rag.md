---
title: AI Search Implementation (RAG)
engagement: intermedia-knowledge-manager
year: "2024"
role: Content tester — I identified the root cause through testing and proposed
  an interface-level fix to the product team.
goal: Make sure the knowledge base content works well with the new RAG search
  and chatbot tool so users can obtain accurate, complete answers without having
  to contact Support.
constraints: >-
  When the company added an AI-powered search and chatbot tool to the knowledge
  base, we quickly discovered that making AI work well with existing content is
  a content strategy problem just as much as a technical one. 


  Testing revealed 3 content-level problems that the AI only discovered after it started working with the library. Each one required a different solution.


  1. **Product Disambiguation.** The RAG tool got confused when different products had features with the same name. It would sometimes provide instructions for the wrong product—mixing up two similar products in a single response. With 20 products in the catalog, naming overlap was common.

  2. **Incomplete Article Structure.** One large product's documentation had been migrated from the Confluence Knowledge Base (Atlassian's platform to publish the pages tied to the Support tickets within the system), where it was organized in a parent–child tree structure. Each child article assumed the reader had come from the parent and skipped the initial steps. A human browsing the knowledge base could navigate naturally through the tree. The RAG tool couldn't; it pulled individual articles in isolation and had no way to reconstruct the missing context, so it generated incomplete instructions. 

  3. **Screenshot Dependency.** Many articles used a screenshot of a UI element and expected the reader to figure out the step from the image alone, without a text description. A human reading the article could do that easily. The AI couldn't—it doesn't process images the same way, so those steps were invisible to it. This caused low-quality or incomplete AI-generated answers and showed up as a spike in negative feedback during beta testing.


  On top of that, during the RAG beta testing phase, an unexpected complication appeared with the **Knowledge Base Reporting**: beta testers' feedback was routed into the same channel as real customer responses. This caused a sharp spike in negative ratings that looked alarming until I understood where it was coming from. Without separating that data, the regular reports would have sent the team chasing a problem that wasn't there.
obstacles: ""
lessons: >-
  **Product Disambiguation.** AI confusion caused by naming overlap across 20
  products doesn't always require content rewrites. Tracing the problem to the
  query structure revealed a lower-effort fix: autocomplete prompting users to
  specify a product name before the AI processed the query.


  **Incomplete Article Structure.** Content written for tree navigation breaks when AI processes articles in isolation—it can't reconstruct missing context from a parent page. The fix (self-contained articles) also improved the human search experience, solving a pre-existing problem that had gone unaddressed. Documenting it as a style guide standard prevents recurrence.


  **Screenshot Dependency.**

  Steps embedded only in screenshots are invisible to AI. When the problem is widespread, a one-off fix isn't viable — it needs a structured initiative (in this case, an internship) and a scalable process. The discovery became the seed for a larger style guide and content rewrite project.


  **RAG Rollout Reporting.** New tech rollouts create data contamination risk in existing reports. Beta feedback spikes need to be isolated from regular customer satisfaction data, or leadership gets a distorted view of how the rollout is actually going. Report structure has to evolve alongside business priorities, not just metrics.
section: Knowledge Management
---
### Product Disambiguation

I identified the root cause through testing and proposed an interface-level fix to the product team.

I traced the problem back to the query structure: users were searching without specifying which product they meant, so the AI had to guess. I recommended adding auto-completion to the search input—prompting users to include the product name before the AI processed the query. This was a low-effort solution that didn't require changing any article content.

### Incomplete Article Structure

I fixed the structural issue in the affected articles and updated the style guide to prevent it recurring.

I added a section to the style guide on how to write **self-contained articles** — articles that make sense on their own, without requiring the reader to have navigated from a specific parent page. I rewrote the top-level articles for the affected product to include the missing initial steps directly, then worked with the Technical Writer who owned that product to link all child articles back to the right top-level article, giving the RAG tool the full context it needed.

!!! success "Highlight"
    This fix also improved the experience for human readers who landed on a child article directly from search—a problem that had existed before the RAG tool but had never been formally addressed.

### Screenshot Dependency

I identified the scope of the problem, determined it was too large for a one-off fix, and proposed a structured solution.

The screenshot-dependency issue affected a large portion of the librlibrary, and we couldn't address iticle by article manually. I identified it as a project suitable for a dedicated initiative and proposed it as an internship task.

!!! success "Highlight"
    This problem became the foundation for the full style guide project described in the next section—including the internship, the content analysis methodology, and the GPT-based rewriting workflow. The intern updated the top-50 most-visited articles as part of that project, directly addressing the screenshot-dependency issue at scale.

    The product team prioritized the autocomplete feature for implementation after the full RAG rollout. The broader content restructuring initiative targeted the most popular products first, with the top-50 articles completed during the internship.

### RAG Rollout Reporting

I identified the data contamination issue, updated the report structure to isolate it, and made sure leadership had a clear picture of what was actually happening.

I updated the Excel templates to track the metrics that mattered for the RAG rollout and restructured the reports to account for the beta feedback channel—so the testing spike was shown separately and didn't distort the regular customer satisfaction data.
