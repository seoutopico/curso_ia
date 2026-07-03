# Module Framework

Use this framework to create repeatable teaching modules under `doc/modulos/<term>/`.

## Minimum structure

```text
doc/modulos/<term>/
+-- README.md
+-- 00-fuentes/
|   +-- 01-source.md
|   +-- 02-source.md
|   +-- 03-source.md
+-- 01-fundamentos.md
+-- 02-syllabus.md
+-- 03-lecciones.md
```

## File contracts

### README.md

Include:

- What the learner will learn.
- The worked example.
- Reading order.
- What is out of scope.

### 00-fuentes/

Each source analysis must include:

- Thesis of the source.
- Useful ideas for the course.
- Risks or misunderstandings.
- Pedagogical decisions extracted from the source.
- Where the source informs the module.

### 01-fundamentos.md

Explain before building:

- What the term is.
- Where it lives in a real system.
- What elements compose it.
- Required pieces.
- Optional pieces.
- Common mistakes.
- Minimum vocabulary.

### 02-syllabus.md

Each block must answer:

- What we are doing.
- Why it matters.
- Example.
- Template.
- Deliverable.

### 03-lecciones.md

Each lesson must include:

- Objective.
- Why it matters.
- Worked example.
- Template.
- Accumulated result.
- Quality criterion.

## Pedagogical sequence

1. Define the problem the term solves.
2. Explain the anatomy of the term.
3. Choose a small scope.
4. Define use and non-use cases.
5. Build the first version.
6. Add resources, automation, or references only when useful.
7. Evaluate activation, quality, and limits.
8. Prune or split if the module grows too broad.