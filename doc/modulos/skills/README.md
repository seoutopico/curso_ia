# Skills para agentes

Este modulo ensena a disenar skills pequenos, claros y utiles para agentes.

La idea central es:

> Tools are great, systems are better.

Una skill no debe intentar hacer un proceso enorme de principio a fin. Debe encapsular una capacidad enfocada: una forma de pensar, decidir, escribir, validar o transformar algo dentro de un sistema mas amplio.

## Que vas a aprender

- Que es una skill y donde vive dentro de un sistema.
- Como se compone una skill: carpeta, `SKILL.md`, YAML, Markdown, recursos y scripts.
- Como elegir un scope pequeno.
- Como escribir una `description` que active la skill en el momento correcto.
- Como convertir instrucciones vagas en un procedimiento util.
- Como usar `references/`, `assets/` y `scripts/` sin inflar el `SKILL.md`.
- Como evaluar si la skill funciona.

## Ejemplo del modulo

Construiremos una skill pequena llamada `decision-brief`.

Su objetivo no es gestionar decisiones de principio a fin. Su objetivo es convertir una decision confusa en un brief claro con contexto, opciones, decision, riesgos y siguiente paso.

## Orden de lectura

1. `00-fuentes/`: analisis de las fuentes usadas.
2. `01-fundamentos.md`: teoria y anatomia de una skill.
3. `02-syllabus.md`: mapa del curso por bloques.
4. `03-lecciones.md`: curso paso a paso.

## Fuentes analizadas

- `00-fuentes/01-agentskills.md`
- `00-fuentes/02-guia-anthropic.md`
- `00-fuentes/03-transcripcion-how-to-write-great-skills.md`

## Que queda fuera

- MCP como tema central.
- Skills que intentan automatizar procesos empresariales completos.
- Plantillas sueltas sin explicar.
- Un curso general de agentes.
