# Subagent Workflow

Use subagents when the work benefits from independent passes.

## Recommended roles

### Source analyst

Prompt shape:

"Analyze this source for a teaching module about <term>. Focus on thesis, useful ideas, risks, pedagogical decisions, and where it maps in the module. Do not write the course."

### Professor synthesizer

Prompt shape:

"Review these source analyses and propose the pedagogical thesis, scope, syllabus logic, missing theory, and evaluation needs for a module about <term>."

### Course writer

Prompt shape:

"Using the source analyses and professor plan, draft the module files. Preserve the required structure and make lessons cumulative."

### Professor validator

Prompt shape:

"Validate this module as a course. Find gaps in theory, scope, progression, templates, examples, and evals. Return concrete fixes."

## Validation integrity

- Pass raw source analysis and module files, not your expected answer.
- Keep roles separated.
- Do not ask validation agents to confirm your conclusion.
- Treat disagreement as signal.