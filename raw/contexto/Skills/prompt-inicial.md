Actúa como experto en IA generativa y divulgador.

Quiero preparar un proyecto en git para enseñar a crear skills para agentes, basado en:

- agentskills.io Lee la web entera **muy importante**
- la guía de Anthropic sobre skills
- la transcripción adjunta sobre “How to write great skills”

Objetivo del proyecto:
Crear una carpeta `doc/` con documentación didáctica para aprender a diseñar skills pequeños, claros y útiles.

Enfoque:

- Defender la idea: “tools are great, systems are better”.
- Enseñar que un buen skill no debe intentar hacer un proceso enorme de principio a fin.
- Enseñar a dividir procesos grandes en skills pequeños o fases enfocadas.
- Usar un ejemplo didáctico no trivial, pero simple de seguir.
- El curso debe avanzar paso a paso: cada lección produce una parte concreta del skill.
- No quiero documentos inconexos ni plantillas sueltas sin explicar.
- Primero se entiende el problema; después se elige el scope; después se definen casos de uso; después se escribe la descripción; después las instrucciones; después se evalúa. A la gente le gustan les frameworks por lo tanto si crear un framework de como definicir un skill, es decir, antes de crear la skill pensar que se quiere hacer para poder crearla ¿Me explico?

Entregables:

1. Un analisis de cada fuentes de informacion, con un .md
2. Un syllabus en `doc/01-syllabus.md` organizado por bloques de aprendizaje.
3. Un documento principal de lecciones en `doc/02-lecciones.md` que guíe paso a paso la construcción de un skill pequeño.
4. Plantillas integradas dentro de las lecciones, con ejemplos rellenados.
5. Checklist de calidad.
6. Evals mínimos para saber si el skill funciona.

Restricciones:

- No usar MCP como tema central.
- No crear un ejemplo de skill que haga demasiadas cosas.
- No trabajar por capas sueltas; debe sentirse como un proceso humano de aprendizaje.
- Cada bloque debe responder: qué estamos haciendo, por qué importa, ejemplo, plantilla y qué entregable queda.

##Como
Lanza subagentes para el 1. Un analisis de cada fuentes de informacion, con un .md cada subagente crear su parte y un agente profesor divuslgador experto en ia generativa experto en skill revisara los 3 entregables de lso agente y creara el syllabus. Luego optroa agente lo redactara el curso y el de nuevo el agente profesor lo va a validad
