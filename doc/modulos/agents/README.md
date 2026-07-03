# Agentes

Este modulo ensena a entender, disenar y evaluar agentes en sistemas de IA generativa.

La idea central es:

> No todo sistema con herramientas es un agente. Un agente aparece cuando el modelo puede decidir pasos, usar herramientas, observar resultados y continuar hasta cumplir un objetivo bajo limites claros.

## Que vas a aprender

- Que es un agente y como se diferencia de un workflow.
- Donde vive un agente dentro de un sistema real.
- Que piezas lo componen: modelo, instrucciones, herramientas, estado, memoria, entorno, permisos, evaluacion y supervision.
- Cuando no conviene construir un agente.
- Como dividir un problema grande en un agente pequeno y evaluable.
- Como disenar guardrails, puntos de control y evals minimos.

## Ejemplo trabajado

Construiremos el diseno de un agente pequeno llamado `issue-triage-agent`.

Su objetivo no es resolver incidencias de principio a fin. Su objetivo es leer una incidencia, clasificarla, pedir la informacion que falta y proponer el siguiente paso verificable.

## Orden de lectura

1. `00-fuentes/`: analisis de fuentes.
2. `01-fundamentos.md`: teoria y anatomia de un agente.
3. `02-syllabus.md`: mapa del curso por bloques.
4. `03-lecciones.md`: curso paso a paso.

## Que queda fuera

- Agentes completamente autonomos sin supervision.
- Arquitecturas multiagente enormes.
- MCP como tema central.
- Demos que solo encadenan prompts sin explicar decisiones de sistema.