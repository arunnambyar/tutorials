# AI Agent Instructions for Tutorials Repository

This repository is a **curated technical knowledge base** documenting core Computer Science concepts through structured tutorials. Agents should maintain clarity, pedagogical value, and consistency across documentation.

## Repository Structure

The repository organizes three primary tutorial domains:

- **`git/`** — Comprehensive Git version control systems documentation
  - `docs/` — Sequential deep-dive articles (001_what.md → 005_git_lifecycle.md)
  - `static/` — Visual diagrams and images supporting Git concepts
  
- **`design_patterns/`** — Design patterns education using vehicle analogies
  - `docs/index.md` — Three design pattern perspectives (Creational, Structural, Behavioral)
  - `static/images/` — Pattern illustrations and POV diagrams
  
- **`es/`** — Elasticsearch documentation
  - `query/` — Elasticsearch|SQL (ES|QL) query examples
  - Limited content currently; expansion area

## Key Editorial Patterns

### 1. Pedagogical Structure
- **Problem-first approach**: Documents articulate *why* concepts matter before explaining *what* they are
- **Concrete analogies**: Design patterns use vehicle comparisons consistently; Git uses collaborative team scenarios
- **Visual reinforcement**: Mermaid diagrams and images accompany complex concepts
- **Progressive disclosure**: Content builds from fundamentals (001_what) to advanced (lifecycle, commands)

### 2. Content Organization
- Use **emoji headers** (🔰, 📚, 🛠️, 🧪) for visual scanability
- Markdown headers should be **question-based or descriptive**, not just topic names
- Include **"Why is this required?"** sections before deep dives
- Provide **cross-references** between related documents using relative links `[Link](./docs/file.md)`

### 3. Diagram Standards
- **Mermaid flowcharts/graphs** for process flows (Git workflows, data flows)
- **Tables** for comparative content (design patterns by POV, command syntax)
- **Static PNG images** in `static/` folder for complex diagrams (vehicle analogies, architecture)
- Place images referenced as `![Alt](../static/folder/image.png)` with relative paths

## Writing Guidelines for This Repository

### Content Style
- **Tone**: Educational and clear, avoid jargon until defined
- **Examples**: Use consistent domain (Git uses collaborative teams; design patterns use vehicles)
- **Note blocks**: Use `> [!NOTE]` syntax for clarifications and corrections (see design_patterns/README.md)
- **Avoid generic advice**: Focus on specific, discoverable patterns in *this* codebase, not aspirational practices

### When Adding New Documentation
1. Place concept articles in `docs/` subdirectories with numbered prefixes if sequential (e.g., `006_advanced_topic.md`)
2. Add visual assets to `static/folder-name/` mirroring the category
3. Update parent README.md with new content links
4. Reference existing analogies and examples from related tutorials for consistency

### Git Documentation Specifics
- Current structure: **Basics** (001–004) → **Concepts** (005+) → **Commands** → **Advanced** → **Collaboration**
- Each section should introduce problem context before solutions
- Expected sections exist for Commands, Advanced, and Collaboration but are incomplete—extend or create stubs

## Common Tasks

### Adding a New Tutorial Section
1. Create folder under root: `new_topic/`
2. Create `new_topic/README.md` with folder index and cross-links to `docs/`
3. Add detailed documents to `new_topic/docs/` with sequential numbering
4. Place supporting images in `new_topic/static/`
5. Update root `README.md` with link to new section

### Updating Documentation
- Preserve existing numbered document order (don't renumber)
- Add new concepts with incremented numbering
- Keep analogies and examples consistent with repo's pedagogical approach
- Update README.md cross-references when modifying file names or paths

### Reviewing Content Quality
- Verify all relative links resolve (`../static/`, `./docs/`)
- Confirm Mermaid diagrams render correctly (use VS Code preview or GitHub rendering)
- Check emoji headers are consistent across similar section types
- Ensure "problem → solution" narrative flow in concept articles

## Critical Files to Reference

- `README.md` — Entry point and topic index; update when adding sections
- `design_patterns/README.md` — Exemplifies pedagogical problem-first structure and analogy use
- `git/docs/001_what.md` — Reference for Git documentation style, diagram placement, and progressive complexity
- `design_patterns/docs/index.md` — Reference for table-based pattern organization and POV perspective

## No Special Build/Deployment Steps

This is a **documentation-only repository** (no code compilation, testing, or CI/CD). Focus on content quality, link validity, and pedagogical clarity. All changes are markdown and asset edits.
