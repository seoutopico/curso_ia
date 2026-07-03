# Source Analysis Rubric

Use one pass per source. Do not merge sources during analysis.

The goal is not to fill a curriculum matrix. The goal is to understand the source on its own terms, extract its useful judgment, and only then explain what it implies for the course.

## Required shape

### Lectura central

Explain the core reading of the source in plain language.

Answer:

- What is this source really about?
- What problem is it trying to solve?
- What idea would be lost if the course ignored this source?

This section should feel like editorial analysis, not a neutral abstract.

### Tesis de la fuente

State the source's main claim in 2-5 paragraphs.

Do not start with how the source maps to module files. First explain what the source argues, assumes, warns about, or makes visible.

### Conceptos y distinciones importantes

Extract the concepts that matter inside the source.

Prefer:

- Definitions.
- Distinctions.
- Design principles.
- Mental models.
- Patterns.
- Failure modes.
- Evaluation criteria.

Avoid turning this into a long catalog of product features, URLs, or headings.

### Principios de diseno

Explain what design principles follow from the source.

A principle is not a fact. It should guide decisions.

Examples:

- "Keep the core instruction small because context is scarce."
- "Use workflows when the path is known and agents when the path must be decided at runtime."
- "Treat observability as part of the design, not a later debugging feature."

### Riesgos y malentendidos

Identify what readers could misunderstand if this source were taught badly.

Good risks are conceptual, not just operational:

- Confusing a protocol with a system.
- Treating a tool as a strategy.
- Adding autonomy before control.
- Turning a focused pattern into a giant process.

### Limites de la fuente

Explain what the source does not prove, does not cover, or should not be overinterpreted to mean.

This prevents the course from turning one source into doctrine.

### Implicaciones para nuestro curso

Only now translate the source into course design.

Do not create a file-by-file mapping here. Do not write "this goes in 01-fundamentos, this goes in 02-syllabus".

Instead answer:

- What idea force should this source contribute to the module?
- What should learners understand before building anything?
- What should appear early?
- What should appear later?
- What should be excluded or delayed?
- What kind of worked example would fit this source?
- What minimum evals or checks does this source suggest?

## Quality bar

A good source analysis:

- Reads the source before designing the course.
- Has a clear thesis.
- Explains concepts in relation to the source, not as scattered notes.
- Separates source analysis from course implications.
- Ends with `## Implicaciones para nuestro curso`.
- Does not include a section called "Where it maps", "Donde se usa", or a file-by-file module mapping.

A bad source analysis:

- Starts by listing where content goes in `01-fundamentos.md`, `02-syllabus.md`, or `03-lecciones.md`.
- Looks like a checklist filled mechanically.
- Mixes many sources without a reading of each one.
- Produces a catalog of URLs, standards, tools, or product features.
- Says how to teach before explaining what the source actually says.