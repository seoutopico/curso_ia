---
name: term-course-builder
description: Create or extend modular teaching modules for generative AI terms using a repeatable editorial system with subagents when available. Use when the user asks to build a course/module for a concept such as skills, agents, evals, memory, context engineering, workflows, tools, RAG, prompts, or similar terms; when they ask to analyze sources and turn them into fundamentos, syllabus, lecciones, checklists, or evals; when they request subagents, delegated source analysis, an expert professor review, a course writer, or a professor validator; or when they want the same multi-agent research and lesson-writing process repeated for a new term.
---

# Term Course Builder

Use this skill to turn scattered sources into a coherent teaching module under `doc/modulos/<term>/`, using subagents for independent source analysis and validation when the user requests that workflow and subagent tools are available.

Core principle: do not create disconnected notes or loose templates. Build a human learning process: sources -> concept -> scope -> use cases -> worked example -> resources -> evals -> iteration.

## Workflow

1. Clarify the term, audience, output language, source set, and target repo structure. If the user already provided these, proceed.
2. Create or reuse `doc/modulos/<term>/` with this shape:

```text
doc/modulos/<term>/
+-- README.md
+-- 00-fuentes/
|   +-- 01-<source>.md
|   +-- 02-<source>.md
|   +-- 03-<source>.md
+-- 01-fundamentos.md
+-- 02-syllabus.md
+-- 03-lecciones.md
```

3. Analyze each source separately before synthesizing. Use `references/source-analysis-rubric.md`. Source analyses must read the source on its own terms and end with `## Implicaciones para nuestro curso`; do not map the source to module files during this phase.
4. Synthesize as a professor/editor after source analysis. Use `references/professor-review-rubric.md`.
5. Write `01-fundamentos.md` before syllabus or lessons. Explain what the term is, where it lives in a system, its components, required/optional parts, vocabulary, and common mistakes.
6. Write `02-syllabus.md` as learning blocks. Every block must answer: what we are doing, why it matters, example, template, and deliverable.
7. Write `03-lecciones.md` as the main course. Each lesson must produce a concrete part of the worked example and accumulate toward a final artifact.
8. Add checklists and minimum evals inside the module, not as unexplained standalone material.
9. Validate the module with `scripts/validate_module.py <module-dir>` after writing or reorganizing files.

## Role Pattern

If subagents or multi-agent tools are available, use them for separation of judgment:

- Source agents: one independent pass per major source. Ask for source analysis, not course writing and not file-by-file curriculum mapping.
- Professor agent: review source analyses and define the pedagogical thesis, module scope, and syllabus logic.
- Writer agent: draft lessons from the professor plan and source analyses.
- Professor validator: review the final module for coherence, missing theory, weak scope, loose templates, and eval gaps.

If subagents are not available, run the same phases sequentially and keep their outputs separated in the working notes.

Do not leak the desired final answer to validation agents. Pass raw artifacts and the task, not your diagnosis.

## Course Design Rules

- Start with the problem the term solves, not with definitions.
- Explain the anatomy of the term before asking the learner to build with it.
- Keep examples non-trivial but small enough to follow.
- Prefer one focused worked example over many shallow examples.
- Do not make a module that automates a whole business process end to end.
- Do not put templates in isolation; embed them in lessons with explanation and filled examples.
- Do not centralize unrelated topics in one module. Split into more modules when the concept changes.
- Treat source analysis, synthesis, syllabus, lessons, and validation as different phases.

## References

Read these only when needed:

- `references/module-framework.md`: use when creating a new module structure or deciding what each module file must contain.
- `references/source-analysis-rubric.md`: use before analyzing sources or delegating source analysis.
- `references/professor-review-rubric.md`: use before synthesis, syllabus review, or final validation.
- `references/lesson-design-rubric.md`: use when writing or reviewing `03-lecciones.md`.
- `references/subagent-workflow.md`: use when the user asks to launch subagents or repeat the multi-agent process.

## Assets

Use these as output templates when creating files:

- `assets/module-readme-template.md`
- `assets/source-analysis-template.md`
- `assets/fundamentals-template.md`
- `assets/syllabus-template.md`
- `assets/lessons-template.md`

## Scripts

Run:

```bash
python scripts/validate_module.py doc/modulos/<term>
```

Use it after creating or changing a module. If it reports missing files or weak required sections, fix the module and run it again.