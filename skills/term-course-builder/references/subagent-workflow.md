# Subagent Workflow

Use subagents when the work benefits from independent passes.

Keep the phases separate. Source analysts analyze sources. The professor turns analyses into course structure. The writer writes the module. The validator reviews the module.

## Recommended roles

### Source analyst

Prompt shape:

"Analyze this source as a source for a teaching module about <term>. Do not write the course. Do not map it to `01-fundamentos.md`, `02-syllabus.md`, or `03-lecciones.md`. First explain the source on its own terms: lectura central, thesis, important concepts and distinctions, design principles, risks, misunderstandings, and limits. Only at the end include `## Implicaciones para nuestro curso`, explaining what idea force, early concepts, later concepts, exclusions, worked example, and evals this source suggests. The output should feel like editorial source analysis, not a curriculum matrix."

Source analysts must not produce sections named:

- "Where it maps"
- "Donde se usa"
- "Use in `01-fundamentos.md`"
- "Use in `02-syllabus.md`"
- "Use in `03-lecciones.md`"

Those decisions belong to the professor synthesizer.

### Professor synthesizer

Prompt shape:

"Review these source analyses. Do not summarize them mechanically. Extract the pedagogical thesis, scope, worked example, course sequence, missing theory, exclusions, and evaluation needs for a module about <term>. Compare sources, resolve tensions, and decide what the module should defend."

The professor may map ideas to module files because synthesis happens after source analysis.

### Course writer

Prompt shape:

"Using the source analyses and professor synthesis, draft the module files. Preserve the required structure and make lessons cumulative. Keep templates inside the learning process, with filled examples."

### Professor validator

Prompt shape:

"Validate this module as a course. Find gaps in theory, scope, progression, templates, examples, source fidelity, and evals. Return concrete fixes. Check whether the module preserves the source thesis or flattened it into a catalog."

## Validation integrity

- Pass raw source analysis and module files, not your expected answer.
- Keep roles separated.
- Do not ask validation agents to confirm your conclusion.
- Treat disagreement as signal.
- If a source analysis looks like a file mapping or a product-feature catalog, reject it and rerun that source with the source analyst prompt.