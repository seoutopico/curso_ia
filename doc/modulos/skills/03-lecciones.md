# Lecciones paso a paso: construir el skill `decision-brief`

## Punto de partida

Tools are great, systems are better.

Una herramienta le da al agente una capacidad: leer un archivo, llamar una API, buscar informacion, generar un documento o ejecutar un script. Pero una herramienta no decide por si sola que resultado importa, que pasos conviene seguir, que errores evitar ni cuando detenerse. Un sistema pequeno si puede hacerlo.

Una skill bien disenada es ese sistema pequeno: empaqueta criterio experto para una tarea recurrente. No pretende hacerlo todo. No sustituye al usuario. No convierte un proceso complejo en una caja negra gigante. Define cuando activarse, que hacer, que formato producir, que validar y que podar cuando deja de aportar.

En estas lecciones vamos a construir, paso a paso, un skill pequeno llamado `decision-brief`. Su trabajo sera convertir notas de reunion, conversacion o discusion tecnica en un breve documento de decision con:

- contexto
- opciones consideradas
- decision
- riesgos y dudas
- siguiente accion

La progresion importa. Primero entenderemos el problema. Despues acotaremos el scope. Luego definiremos casos de uso, description e instrucciones. A partir de ahi construiremos recursos reales como snippets didacticos: una reference, un asset y un script. Despues evaluaremos activacion, calidad, uso de recursos e iteracion. El resultado final sera un paquete de skill didactico incluido como snippets dentro de este documento. No crearemos una carpeta real de skill.

---

## Leccion 1. Entender el problema antes de escribir la skill

### Que estamos haciendo

Antes de escribir frontmatter, instrucciones o plantillas, observamos una tarea humana concreta: despues de una reunion o conversacion larga, alguien necesita saber que se decidio, por que, que alternativas se discutieron, que riesgos quedan y cual es el siguiente paso.

No estamos disenando "una skill para reuniones". Estamos buscando un fallo repetido en una tarea mas pequena: las notas suelen contener mucha informacion, pero la decision queda dispersa o implicita.

### Por que importa

Si empezamos escribiendo una skill sin entender el problema, acabaremos con documentacion generica: "resume bien", "se claro", "organiza la informacion". Eso puede sonar razonable, pero no cambia mucho el comportamiento del agente.

Una buena skill existe porque mejora algo observable. En este caso, mejora la conversion de material desordenado en un brief de decision. La diferencia entre herramienta y sistema aparece aqui: una herramienta puede resumir texto; el sistema fuerza una lectura orientada a decision.

### Ejemplo

Notas originales:

```markdown
Reunion producto/plataforma.
Ana quiere lanzar la beta el viernes, pero soporte dice que aun hay dudas con rollback.
Bruno propone esperar una semana para medir errores del nuevo flujo.
Carla dice que marketing ya aviso a clientes piloto y cambiar la fecha tiene coste.
Se acuerda lanzar solo para 20 clientes internos el viernes, no para todos los pilotos.
Pendiente: Diego confirma plan de rollback manana.
Riesgo: si el nuevo login falla, soporte no tiene todavia macro preparada.
```

Salida que buscamos:

```markdown
# Decision brief

## Contexto
El equipo discutio si lanzar la beta del nuevo flujo el viernes o retrasarla una semana por dudas de rollback y soporte.

## Opciones consideradas
- Lanzar la beta completa el viernes.
- Retrasar una semana para observar errores.
- Lanzar el viernes con alcance limitado.

## Decision
Lanzar el viernes solo para 20 clientes internos, no para todos los pilotos.

## Riesgos y dudas
- El plan de rollback aun no esta confirmado.
- Soporte no tiene preparada la macro para fallos del nuevo login.

## Siguiente accion
Diego confirma el plan de rollback manana.
```

La salida no intenta ser un acta completa. Tampoco inventa un plan de proyecto. Se concentra en aclarar una decision.

### Plantilla

Rellenamos la ficha inicial del problema:

```markdown
Problema recurrente:
Las reuniones y conversaciones terminan con decisiones dispersas entre contexto, opiniones y siguientes pasos.

Usuario tipico:
Product managers, tech leads, responsables de proyecto o cualquier persona que deba compartir una decision despues de una conversacion.

Entrada habitual:
Notas desordenadas, transcripciones parciales, hilos de chat, resumen informal de una discusion tecnica.

Salida deseada:
Un decision brief breve con contexto, opciones, decision, riesgos y siguiente accion.

Fallo frecuente sin skill:
El agente produce un resumen general, mezcla la decision con las opciones o inventa responsables y fechas.

Criterio experto que debe aplicar:
Leer el material con mentalidad decision-first: la decision es el centro, no la cronologia completa de la reunion.

Por que no basta con una herramienta general:
Porque resumir texto no garantiza distinguir decision, alternativas, incertidumbre y accion siguiente.
```

### Entregable

Al terminar esta leccion queda una ficha de problema. Todavia no tenemos una skill. Tenemos algo mas importante: una razon concreta para que la skill exista.

---

## Leccion 2. Acotar el scope: una skill pequena que compone bien

### Que estamos haciendo

Definimos que cubre `decision-brief` y que queda fuera. La skill debe ser suficientemente pequena para activarse con precision y suficientemente util para repetirse en muchos contextos.

La regla practica es esta: una skill buena vive entre un comando aislado y un proceso enorme. Si intenta cubrir todo el ciclo "grabar reunion, transcribir, extraer decisiones, crear tickets, actualizar roadmap y avisar al equipo", sera fragil. Ese flujo grande debe dividirse en fases o skills enfocadas.

### Por que importa

Cuando un skill intenta hacer un proceso enorme de principio a fin, el agente suele saltar demasiado rapido hacia la salida final. Hace menos trabajo en las fases que necesitan atencion: entender el problema, detectar incertidumbre, separar opciones o confirmar si realmente hubo decision.

Dividir no es burocracia. Es diseno de sistemas. Si una fase necesita trabajo propio, debe tener foco propio. `decision-brief` no gestiona proyectos; prepara un artefacto breve para confirmar o comunicar una decision.

### Ejemplo

Buen scope:

```markdown
Convertir notas de reunion, conversacion o discusion tecnica en un documento breve de decision.
```

Scope demasiado grande:

```markdown
Gestionar todo el seguimiento de decisiones de un equipo desde la reunion hasta la ejecucion.
```

Scope demasiado pequeno:

```markdown
Crear siempre el mismo bloque "Decision / Next step" para una unica reunion semanal.
```

El primero compone bien. Puede usarse antes de crear tickets, antes de mandar un correo o antes de actualizar un roadmap, pero no intenta hacer esas tareas.

### Plantilla

Rellenamos el mapa de scope:

```markdown
La skill sirve para:
Transformar notas o conversaciones en un brief de decision breve y verificable.

La skill no sirve para:
Actas completas, registros legales, project management completo, creacion detallada de tickets, decision making autonomo cuando no hay evidencia.

Entrada minima necesaria:
Notas, transcripcion parcial o resumen de una conversacion donde haya una decision explicita, implicita o una decision aun no cerrada.

Resultado final:
Un documento Markdown corto con contexto, opciones, decision, riesgos/dudas y siguiente accion.

Casos cercanos que no deben activarla:
"Hazme un acta completa", "convierte esto en tickets", "resume esta charla en tres ideas", "decide tu por nosotros".

Senal de que el scope es demasiado grande:
La skill empieza a incluir calendarios, asignacion de tareas, comunicacion a stakeholders y seguimiento de ejecucion.

Senal de que el scope es demasiado pequeno:
Solo funciona para una plantilla exacta de notas o para un equipo concreto sin aportar criterio reutilizable.
```

### Entregable

Queda un mapa de fronteras. Este mapa protege a la skill de crecer sin control y nos recuerda que los procesos grandes se resuelven mejor como sistemas de fases pequenas, no como una skill totalizante.

---

## Leccion 3. Definir casos de uso y criterios de exito

### Que estamos haciendo

Escribimos casos positivos y near-misses antes de redactar la `description`. Un caso positivo debe activar la skill. Un near-miss se parece, pero no deberia activarla.

### Por que importa

La activacion no se disena en abstracto. Se disena contra frases reales del usuario. Si no sabemos que prompts deben activar `decision-brief`, la description se volvera vaga. Y si no sabemos que prompts cercanos deben quedar fuera, la skill se usara para tareas equivocadas.

### Ejemplo

Caso positivo:

```markdown
Prompt del usuario:
"Te pego notas de una reunion. Sacame la decision, riesgos y siguiente paso."

Entrada:
Notas desordenadas con una decision explicita.

Pasos que debe seguir el agente:
1. Detectar la decision.
2. Separar contexto y opciones.
3. Identificar riesgos y dudas.
4. Redactar el brief.
5. Validar que no inventa duenos ni fechas.

Salida esperada:
Decision brief breve en Markdown.

Criterios de exito:
La decision queda separada del contexto y el siguiente paso es accionable.
```

Near-miss:

```markdown
Prompt del usuario:
"Hazme un acta completa de la reunion con todos los puntos tratados."

Por que no debe activar:
El usuario pide un registro amplio, no un brief de decision.
```

### Plantilla

Rellenamos una matriz minima:

```markdown
Caso 1:
Prompt: "Esta conversacion termino con una decision implicita. Ordenala para compartirla."
Debe activar: si
Criterio de exito: declara la decision inferida y separa la evidencia de la inferencia.

Caso 2:
Prompt: "Tenemos tres opciones discutidas; prepara un documento corto para confirmar la decision."
Debe activar: si
Criterio de exito: lista las opciones sin confundirlas con la decision final.

Caso 3:
Prompt: "Resume esto como decision, riesgos y siguiente accion."
Debe activar: si
Criterio de exito: evita un resumen generico y usa la estructura del brief.

Near-miss 1:
Prompt: "Convierte esto en tickets de Jira."
Debe activar: no
Motivo: el resultado principal son tickets, no un brief.

Near-miss 2:
Prompt: "Dame un resumen ejecutivo de esta charla."
Debe activar: no, salvo que pida decision explicita
Motivo: puede ser resumen general, no necesariamente decision brief.
```

### Entregable

Queda una matriz de activacion. La usaremos en la siguiente leccion para escribir la `description` como una decision de producto, no como una frase decorativa.

---

## Leccion 4. Escribir la `description`: el trigger como decision de producto

### Que estamos haciendo

Redactamos el frontmatter de la skill. En especial, la `description`. Esta descripcion es lo primero que vera el agente para decidir si debe cargar el `SKILL.md`.

### Por que importa

La `description` no es un resumen publicitario. Es el trigger. Si es demasiado amplia, la skill se activara para cualquier resumen de reunion. Si es demasiado estrecha, no se activara cuando el usuario hable de una decision implicita sin usar las palabras "decision brief".

Aqui aparece otra vez la tesis del curso: tools are great, systems are better. La herramienta puede escribir Markdown; el sistema decide cuando aplicar el procedimiento correcto.

### Ejemplo

Descripcion debil:

```yaml
description: Helps summarize meetings.
```

Problemas:

- "summarize" activa una tarea demasiado amplia.
- No menciona decisiones, opciones, riesgos ni siguiente accion.
- No marca fronteras con actas, tickets o resumen general.

Descripcion mejor:

```yaml
---
name: decision-brief
description: Use this skill when the user needs to turn meeting notes, conversation notes, chat threads, or rough technical discussion notes into a concise decision brief with context, options, decision, risks, and next action. Use it when the decision may be explicit, implicit, or not yet supported by enough evidence. Do not use it for full meeting minutes, legal records, project plans, ticket creation, or generic summarization.
---
```

Esta version dice cuando usarla, que entradas espera, que salida produce y que tareas cercanas quedan fuera.

### Plantilla

Usamos una plantilla de trigger:

```yaml
---
name: nombre-en-kebab-case
description: Use this skill when [usuario necesita resultado concreto] from [entradas habituales], including [casos implicitos o dificiles]. Do not use it for [near misses].
---
```

Rellenada para nuestro caso:

```yaml
---
name: decision-brief
description: Use this skill when the user needs to turn meeting notes, conversation notes, chat threads, or rough technical discussion notes into a concise decision brief with context, options, decision, risks, and next action. Use it when the decision may be explicit, implicit, or not yet supported by enough evidence. Do not use it for full meeting minutes, legal records, project plans, ticket creation, or generic summarization.
---
```

### Entregable

Queda una `description` candidata y una prueba rapida:

```markdown
Debe activar:
- "Sacame la decision y siguiente paso de estas notas."
- "Esta conversacion de Slack termino en algo implicito; conviertelo en brief."

No debe activar:
- "Haz un acta completa."
- "Crea tickets a partir de esta reunion."
- "Resume esta llamada en tres ideas."
```

---

## Leccion 5. Escribir instrucciones: workflow, steering y formato de salida

### Que estamos haciendo

Convertimos el criterio experto en instrucciones operativas. No buscamos una prosa bonita; buscamos pasos que cambien la conducta del agente.

Para `decision-brief`, usaremos tres palabras guia:

- `decision-first`: el brief existe para aclarar la decision, no para contar toda la reunion.
- `evidence-linked`: las decisiones, riesgos y acciones deben estar conectadas con la entrada.
- `actionable-next-step`: el cierre debe ser una accion concreta, con dueno y plazo solo si aparecen en las notas.

### Por que importa

El steering no se consigue con frases genericas como "se claro y util". Esas frases suelen ser no-ops: si las borramos, probablemente la salida seria parecida.

Una instruccion util cambia una decision practica. Por ejemplo: "Si no hay evidencia suficiente, escribe `Decision not yet supported by notes`" evita que el agente invente una decision. Eso si cambia comportamiento.

### Ejemplo

Entrada ambigua:

```markdown
Pedro cree que deberiamos migrar a Postgres.
Lucia dice que antes falta medir coste.
Marco propone seguir con MySQL hasta cerrar benchmark.
No hubo cierre claro. Quedaron en revisar datos el lunes.
```

Mala salida:

```markdown
Decision: Migrar a Postgres.
```

Buena salida:

```markdown
## Decision
Decision not yet supported by notes. La conversacion muestra preferencia por comparar alternativas, pero no una decision final de migracion.

## Siguiente accion
Revisar datos del benchmark el lunes.
```

### Plantilla

Primer borrador del cuerpo de instrucciones:

```markdown
## Workflow

1. Read the source material with a decision-first lens.
2. Classify the decision state: explicit, implicit, or not supported by notes.
3. Extract only the context needed to understand the decision.
4. List meaningful options considered, including the chosen option if clear.
5. Write the decision. If evidence is insufficient, say so directly.
6. Capture risks, open questions, and assumptions without inventing facts.
7. End with one actionable next step. Include owner and date only when present.
8. Run the validation checklist before finalizing.

## Output format

# Decision brief

## Context
[2-4 sentences maximum.]

## Options considered
- [Option]

## Decision
[Decision, implicit decision with caveat, or "Decision not yet supported by notes."]

## Risks and open questions
- [Risk or question]

## Next action
[Concrete action, owner/date if present, or "Next action not specified in notes."]
```

Rellenado con el ejemplo de beta:

```markdown
# Decision brief

## Context
The team discussed whether to launch the beta on Friday or delay it because rollback and support readiness were still uncertain.

## Options considered
- Launch the full beta on Friday.
- Delay one week to observe errors.
- Launch Friday with limited scope.

## Decision
Launch Friday only for 20 internal customers, not for all pilot customers.

## Risks and open questions
- Rollback plan still needs confirmation.
- Support does not yet have a macro for new-login failures.

## Next action
Diego confirms the rollback plan tomorrow.
```

### Entregable

Queda el nucleo del `SKILL.md`: workflow, steering y formato de salida. Todavia falta decidir que recursos, scripts o assets merecen existir.

---

## Leccion 6. Decidir recursos, scripts y assets

### Que estamos haciendo

Decidimos que debe vivir en `SKILL.md` y que debe moverse a archivos de apoyo. Esta vez no nos quedamos en decir "no hacen falta recursos". Vamos a construir una version extendida de `decision-brief` para aprender como se disenan `references/`, `assets/` y `scripts/`.

Tendremos dos versiones:

- Version minima: solo `SKILL.md`.
- Version extendida didactica: `SKILL.md` + reference + asset + script.

### Por que importa

Progressive disclosure es economia de atencion. Todo lo que metemos en `SKILL.md` se carga cada vez que la skill se activa. Pero si nunca practicamos recursos externos, el curso queda incompleto: no aprendemos a decidir cuando una guia, una plantilla o una validacion deben salir del archivo principal.

La pregunta correcta no es "puedo anadir un recurso?". La pregunta correcta es: "esta pieza debe estar siempre en contexto, debe cargarse bajo condicion, debe ser una plantilla o debe ejecutarse como codigo?".

### Ejemplo

Para `decision-brief`, esta es la decision de arquitectura:

```text
decision-brief/
+-- SKILL.md
+-- references/
|   +-- decision-quality-rubric.md
+-- assets/
|   +-- brief-template.md
+-- scripts/
    +-- check-brief-structure.py
```

Por que existe cada pieza:

```markdown
SKILL.md
Contiene lo que el agente necesita siempre: trigger, workflow, steering, defaults, formato basico y validacion.

references/decision-quality-rubric.md
Contiene criterios mas detallados para evaluar la calidad de una decision. Solo se lee cuando el usuario pide evaluar calidad, aplicar una rubrica o revisar si una decision esta bien formulada.

assets/brief-template.md
Contiene una plantilla exacta de salida. Se usa cuando el usuario pide el formato completo o cuando la organizacion exige una estructura estable.

scripts/check-brief-structure.py
Valida mecanicamente que el brief generado contiene las secciones obligatorias. Se usa antes de finalizar cuando se produce un archivo o cuando hay ejecucion por lotes.
```

### Plantilla

```markdown
Recurso:

Tipo:
- SKILL.md
- reference
- asset
- script

Por que existe:

Cuando se carga o usa:

Que error evita:

Que pasaria si lo dejamos inline en SKILL.md:

Que pasaria si lo eliminamos:
```

Rellenada para nuestro caso:

```markdown
Recurso: references/decision-quality-rubric.md
Tipo: reference
Por que existe: contiene criterios extendidos que no hacen falta en cada ejecucion.
Cuando se carga o usa: solo si el usuario pide evaluar calidad de decision o aplicar rubrica.
Que error evita: inflar SKILL.md con teoria y criterios largos.
Que pasaria si lo dejamos inline en SKILL.md: cada uso de la skill cargaria contexto innecesario.
Que pasaria si lo eliminamos: el agente podria producir briefs, pero tendria menos criterio para revision avanzada.
```

### Entregable

Queda un mapa de recursos. A partir de aqui vamos a construir cada pieza.

---

## Leccion 7. Construir una `reference`: conocimiento bajo demanda

### Que estamos haciendo

Creamos una referencia para informacion que ayuda en algunos casos, pero no debe estar siempre en `SKILL.md`.

Una reference no es un cajon de notas. Debe tener una condicion clara de lectura.

### Por que importa

Si metemos criterios largos dentro de `SKILL.md`, el agente los carga incluso cuando solo necesita producir un brief simple. Si los movemos a `references/`, el agente puede leerlos solo cuando el usuario pide revision, calidad, auditoria o una rubrica mas exigente.

### Ejemplo

Archivo didactico:

```text
references/decision-quality-rubric.md
```

Contenido:

```markdown
# Decision quality rubric

## Cuando leer esta referencia

Lee esta referencia solo cuando el usuario pida evaluar la calidad de una decision, aplicar una rubrica, revisar si el brief esta listo para compartir, o comparar varias decisiones.

## Criterios de calidad

Una decision buena debe cumplir:

- Decision clara: el lector entiende que opcion se eligio.
- Evidencia visible: la decision se puede conectar con notas o argumentos.
- Opciones separadas: las alternativas no se mezclan con la decision final.
- Riesgos explicitos: los riesgos relevantes aparecen sin exagerar.
- Incertidumbre preservada: si falta informacion, se marca.
- Siguiente accion concreta: hay una accion, responsable o condicion cuando existe en las notas.

## Fallos frecuentes

- Convertir una conversacion sin cierre en una decision falsa.
- Confundir la opcion preferida por una persona con decision del grupo.
- Inventar fechas o responsables.
- Escribir un resumen largo en vez de un brief accionable.
- Ocultar condiciones importantes como "si legal aprueba" o "si soporte confirma".
```

Ahora `SKILL.md` debe apuntar a la reference con una condicion concreta:

```markdown
## References

- Read `references/decision-quality-rubric.md` only when the user asks to evaluate decision quality, apply a rubric, compare decision options, or review whether the brief is ready to share.
```

### Plantilla

```markdown
# [Reference title]

## Cuando leer esta referencia

[Condicion concreta. Evita "leer si hace falta".]

## Criterios

- [Criterio]

## Fallos frecuentes

- [Fallo]

## Como usar esta referencia

[Instruccion breve para aplicar el contenido.]
```

### Entregable

Queda una reference pequena y una linea en `SKILL.md` que explica cuando leerla.

---

## Leccion 8. Construir un `asset`: plantilla reutilizable

### Que estamos haciendo

Creamos un asset cuando el resultado necesita una plantilla estable. A diferencia de una reference, el asset no explica criterio: se usa como material de salida.

### Por que importa

Una plantilla larga dentro de `SKILL.md` puede ocupar demasiado. Si la plantilla es oficial, repetible o cambia independientemente de las instrucciones, conviene moverla a `assets/`.

### Ejemplo

Archivo didactico:

```text
assets/brief-template.md
```

Contenido:

```markdown
# Decision brief

## Context
[Two to four sentences. Include only the context needed to understand the decision.]

## Options considered
- [Option 1]
- [Option 2]
- [Option 3 if relevant]

## Decision
[State the decision. If inferred, label it as inferred. If unsupported, write: "Decision not yet supported by notes."]

## Evidence
- [Note, quote, or paraphrased evidence supporting the decision]

## Risks and open questions
- [Risk, dependency, missing information, or open question]

## Next action
[Concrete action. Include owner and date only if present in the notes.]
```

`SKILL.md` debe indicar cuando usar el asset:

```markdown
## Assets

- Use `assets/brief-template.md` when the user asks for the standard decision brief format, when producing a file, or when consistency matters more than brevity.
```

### Plantilla

```markdown
# [Template name]

## [Section]
[Placeholder with precise instruction]

## [Section]
[Placeholder with precise instruction]
```

Decision importante:

```markdown
Si la plantilla es corta y se usa siempre, puede vivir en SKILL.md.
Si la plantilla es larga, oficial o solo se usa en algunos casos, debe vivir en assets/.
```

### Entregable

Queda un asset de plantilla y una instruccion en `SKILL.md` sobre cuando usarlo.

---

## Leccion 9. Construir un `script`: validacion determinista

### Que estamos haciendo

Creamos un script minimo para validar una parte mecanica del resultado. No usamos scripts para sustituir el juicio del agente, sino para comprobar cosas objetivas.

### Por que importa

El lenguaje natural es flexible. Eso es bueno para redactar, pero malo para validaciones mecanicas. Si necesitamos comprobar que existen secciones obligatorias, que un JSON es valido o que una tabla tiene columnas concretas, un script reduce errores.

### Ejemplo

Archivo didactico:

```text
scripts/check-brief-structure.py
```

Script:

```python
#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

REQUIRED = [
    "# Decision brief",
    "## Context",
    "## Options considered",
    "## Decision",
    "## Risks and open questions",
    "## Next action",
]


def main():
    parser = argparse.ArgumentParser(description="Validate decision brief structure.")
    parser.add_argument("file", help="Markdown file to validate")
    args = parser.parse_args()

    text = Path(args.file).read_text(encoding="utf-8")
    missing = [section for section in REQUIRED if section not in text]

    result = {
        "valid": not missing,
        "missing_sections": missing,
    }
    print(json.dumps(result, indent=2))
    return 0 if not missing else 1


if __name__ == "__main__":
    raise SystemExit(main())
```

`SKILL.md` debe explicar cuando ejecutarlo:

```markdown
## Scripts

- Run `python scripts/check-brief-structure.py <output.md>` when writing the brief to a file, when generating multiple briefs, or when the user asks for validation. If the script reports missing sections, fix the brief and run it again.
```

### Plantilla

```markdown
Script:
Entrada:
Salida:
Errores que detecta:
Como se invoca:
Cuando debe ejecutarse:
Cuando NO debe ejecutarse:
```

Rellenada:

```markdown
Script: scripts/check-brief-structure.py
Entrada: archivo Markdown con el brief.
Salida: JSON con valid true/false y missing_sections.
Errores que detecta: secciones obligatorias ausentes.
Como se invoca: python scripts/check-brief-structure.py output.md
Cuando debe ejecutarse: outputs a archivo, lotes, validacion solicitada.
Cuando NO debe ejecutarse: respuestas breves en chat donde no se crea archivo.
```

### Entregable

Queda un script con contrato de entrada/salida y una instruccion de uso dentro de `SKILL.md`.

---

## Leccion 10. Integrar recursos en `SKILL.md`

### Que estamos haciendo

Actualizamos el `SKILL.md` para que el agente sepa que recursos existen y cuando usarlos. El punto clave es no decir "mira la carpeta references". Hay que indicar condiciones de carga.

### Por que importa

Un recurso no sirve si el agente no sabe cuando leerlo. Y un recurso puede hacer dano si se lee siempre sin necesidad. La integracion es parte del diseno.

### Ejemplo

Seccion nueva para `SKILL.md`:

```markdown
## References

- Read `references/decision-quality-rubric.md` only when the user asks to evaluate decision quality, apply a rubric, compare decision options, or review whether the brief is ready to share.

## Assets

- Use `assets/brief-template.md` when the user asks for the standard decision brief format, when producing a file, or when consistency matters more than brevity.

## Scripts

- Run `python scripts/check-brief-structure.py <output.md>` when writing the brief to a file, when generating multiple briefs, or when the user asks for validation. If the script reports missing sections, fix the brief and run it again.
```

Mapa final de carga:

```markdown
Siempre en SKILL.md:
- description
- workflow
- leading words
- defaults basicos
- validation minima

Bajo condicion en references/:
- decision-quality-rubric.md

Como material de salida en assets/:
- brief-template.md

Como validacion mecanica en scripts/:
- check-brief-structure.py
```

### Plantilla

```markdown
## References

- Read `[path]` only when [condicion concreta].

## Assets

- Use `[path]` when [condicion concreta].

## Scripts

- Run `[command]` when [condicion concreta]. If it fails, [accion de recuperacion].
```

### Entregable

Queda una version extendida de la skill que demuestra progressive disclosure con recursos reales.

---

## Leccion 11. Evaluar activacion, calidad y recursos

### Que estamos haciendo

Probamos si la skill se activa cuando debe, no se activa cuando no debe, mejora la salida frente a un resumen generico y usa `references/`, `assets/` y `scripts/` solo cuando corresponde.

La evaluacion minima no tiene que ser una suite enorme. Para empezar, bastan pocos casos bien elegidos: positivos, near-misses y un caso ambiguo.

### Por que importa

Crear una skill no demuestra que aporte valor. Crear recursos tampoco. El valor aparece cuando reducen errores recurrentes sin inflar el contexto ni complicar el flujo: decisiones inventadas, contexto excesivo, opciones mezcladas con la decision, siguientes pasos vagos o salidas con estructura rota.

Tambien evaluamos la `description`. Si dispara ante "acta completa", esta demasiado amplia. Si no dispara ante "decision implicita", esta demasiado estrecha.

### Ejemplo

Eval funcional minima:

```markdown
Prompt:
"Esta conversacion termino con una decision implicita. Ordenala como decision, riesgos y siguiente accion."

Entrada:
"No votamos formalmente, pero despues de revisar costes nadie defendio seguir con proveedor A. Marta pidio avanzar con proveedor B si legal confirma el DPA. Riesgo: migracion antes de agosto."

Debe activar:
Si.

Salida esperada:
- Contexto breve sobre comparacion de proveedores.
- Opciones A y B.
- Decision implicita: avanzar con proveedor B sujeto a confirmacion legal del DPA.
- Riesgo de migracion antes de agosto.
- Siguiente accion: legal confirma DPA.

Assertions:
- No dice que la decision sea incondicional.
- No inventa fecha exacta.
- Incluye la condicion legal.
```

Near-miss:

```markdown
Prompt:
"Hazme un acta completa con asistentes, agenda y todos los acuerdos."

Debe activar:
No.

Motivo:
El usuario pide un acta completa, no un decision brief.
```

### Plantilla

Usamos esta tabla de evaluacion:

```markdown
| Prueba | Prompt | Debe activar | Mejora observable | Fallo detectado | Cambio propuesto |
|---|---|---:|---|---|---|
| Positiva explicita | "Sacame la decision de estas notas" | Si | Decision separada del contexto | Ninguno | Mantener |
| Positiva implicita | "Ordena esta conversacion; la decision quedo implicita" | Si | Declara condicion e incertidumbre | Puede sonar demasiado segura | Reforzar evidencia |
| Ambigua | "No hubo cierre; prepara estado de decision" | Si | Declara decision no soportada | Ninguno | Mantener |
| Near-miss acta | "Haz un acta completa" | No | Evita formato equivocado | Si activa, description amplia | Anadir exclusion |
| Near-miss tickets | "Convierte esto en tickets" | No | Evita invadir project management | Si activa, scope amplio | Anadir exclusion |
```

### Checklist de calidad

Antes de considerar buena la salida, revisamos:

```markdown
- [ ] La salida no es un resumen general.
- [ ] La decision aparece en una seccion propia.
- [ ] Si la decision es implicita, se marca como inferencia.
- [ ] Si no hay evidencia suficiente, se dice explicitamente.
- [ ] Las opciones consideradas no se confunden con la decision.
- [ ] Los riesgos y dudas proceden de las notas.
- [ ] No se inventan duenos, fechas, metricas ni compromisos.
- [ ] El siguiente paso es concreto o queda marcado como no especificado.
- [ ] El brief es breve: no intenta ser acta, PRD ni plan de proyecto.
```

### Evals minimos

Para una primera version, exigimos al menos:

```markdown
1. Decision explicita:
   Debe extraer decision, opciones, riesgos y siguiente accion sin anadir informacion.

2. Decision implicita:
   Debe formular la decision como inferencia y conservar condiciones.

3. Decision ausente:
   Debe escribir "Decision not yet supported by notes" y listar que falta.

4. Near-miss de acta:
   No deberia activar la skill.

5. Near-miss de tickets:
   No deberia activar la skill.

6. Uso de reference:
   Prompt: "Evalua si esta decision esta lista para compartir usando una rubrica."
   Debe leer `references/decision-quality-rubric.md`.

7. Uso de asset:
   Prompt: "Genera el brief con la plantilla estandar."
   Debe usar `assets/brief-template.md`.

8. Uso de script:
   Prompt: "Guarda el brief en un archivo y valida la estructura."
   Debe ejecutar `python scripts/check-brief-structure.py <output.md>`.
```

### Entregable

Queda una tabla de evals y una checklist. La skill ya no es solo un archivo: tiene una manera minima de demostrar que funciona.

---

## Leccion 12. Podar, dividir e iterar

### Que estamos haciendo

Revisamos la skill para eliminar no-ops, sediment y duplicacion. Tambien decidimos si alguna parte deberia separarse en otra skill.

### Por que importa

Las skills se degradan cuando acumulan texto historico. Cada frase debe hacer al menos una de estas cosas:

- activar una decision
- imponer una secuencia
- cambiar el formato de salida
- evitar un error probable
- indicar cuando consultar un recurso
- validar el resultado

Si no hace nada de eso, consume contexto.

### Ejemplo

Texto candidato a eliminar:

```markdown
Be professional, concise, and helpful.
```

Por que se elimina:

```markdown
No cambia una decision concreta. El agente ya intenta ser util y profesional.
```

Texto que se mantiene:

```markdown
If the notes do not support a decision, write "Decision not yet supported by notes" instead of choosing an option.
```

Por que se mantiene:

```markdown
Evita una alucinacion probable y fija una salida verificable.
```

Caso donde dividiria la skill:

```markdown
Nuevo requisito:
"Ademas del decision brief, crea tickets, actualiza roadmap, redacta email a stakeholders y programa seguimiento."

Decision:
No ampliar `decision-brief` hasta cubrir todo. Dividir el proceso:
- `decision-brief`: aclarar la decision.
- otra skill o fase: convertir decision validada en tickets.
- otra skill o fase: preparar comunicacion a stakeholders.
```

El principio es simple: cuando una fase necesita trabajo propio, no debe quedar enterrada dentro de una skill gigante.

### Plantilla

Usamos una plantilla de poda:

```markdown
Frase o seccion:
"Include a beautiful and polished document."

Que decision cambia:
Ninguna.

Que error evita:
Ninguno especifico.

Se usa siempre o solo en una rama:
No queda claro.

Accion:
Eliminar.
```

Y otra para una frase que si se mantiene:

```markdown
Frase o seccion:
"Include owner and date only when present in the notes."

Que decision cambia:
Evita completar responsables o fechas por inferencia.

Que error evita:
Invencion de compromisos.

Se usa siempre o solo en una rama:
Siempre, al escribir Next action.

Accion:
Mantener.
```

### Entregable

Queda una version podada y un criterio de mantenimiento: si el skill crece para cubrir fases posteriores, se divide. No estamos creando un asistente universal de reuniones; estamos creando una unidad pequena que compone bien.

---

## Leccion 13. Resultado acumulado: `SKILL.md` final del ejemplo

### Que estamos haciendo

Integramos lo aprendido en un paquete final didactico. Este bloque muestra el `SKILL.md` y las referencias a los recursos externos. No crea una carpeta real en el repositorio; presenta los archivos como snippets de curso.

### Por que importa

El objetivo no es tener Markdown bonito. El objetivo es tener un sistema pequeno:

- se activa en el momento correcto
- guia un flujo concreto
- mantiene el scope
- evita invenciones
- produce una salida verificable
- se puede evaluar y podar

### Ejemplo

Snippet final:

```markdown
---
name: decision-brief
description: Use this skill when the user needs to turn meeting notes, conversation notes, chat threads, or rough technical discussion notes into a concise decision brief with context, options, decision, risks, and next action. Use it when the decision may be explicit, implicit, or not yet supported by enough evidence. Do not use it for full meeting minutes, legal records, project plans, ticket creation, or generic summarization.
---

# Decision brief

Use this skill to turn rough discussion material into a brief decision document.

Core steering:

- decision-first: the brief exists to clarify the decision, not to summarize the whole conversation.
- evidence-linked: decisions, risks, and next actions must be supported by the source notes.
- actionable-next-step: the brief must end with a concrete next action, or state that none is specified.

## Workflow

1. Read the source material with a decision-first lens.
2. Classify the decision state:
   - explicit: the notes clearly state the decision.
   - implicit: the notes strongly imply a decision but do not state it formally.
   - not supported: the notes do not contain enough evidence for a decision.
3. Extract only the context needed to understand the decision.
4. List meaningful options considered. Do not list every comment as an option.
5. Write the decision:
   - For explicit decisions, state the decision directly.
   - For implicit decisions, label it as an inferred decision and include the condition or evidence.
   - If unsupported, write: "Decision not yet supported by notes."
6. Capture risks, open questions, and assumptions without inventing facts.
7. Write one next action. Include owner and date only when present in the notes.
8. Validate the brief before finalizing.

## Output format

# Decision brief

## Context
[2-4 sentences with only the context needed to understand the decision.]

## Options considered
- [Option discussed]
- [Option discussed]

## Decision
[Decision, inferred decision with caveat, or "Decision not yet supported by notes."]

## Risks and open questions
- [Risk, doubt, dependency, or missing information]

## Next action
[Concrete action with owner/date if present, or "Next action not specified in notes."]

## Defaults

- Keep the brief short.
- Prefer bullets for options, risks, and questions.
- Preserve uncertainty instead of smoothing it away.
- Do not create owners, dates, priorities, metrics, or commitments that are not in the notes.
- Do not turn the brief into meeting minutes, a project plan, or tickets.

## References

- Read `references/decision-quality-rubric.md` only when the user asks to evaluate decision quality, apply a rubric, compare decision options, or review whether the brief is ready to share.

## Assets

- Use `assets/brief-template.md` when the user asks for the standard decision brief format, when producing a file, or when consistency matters more than brevity.

## Scripts

- Run `python scripts/check-brief-structure.py <output.md>` when writing the brief to a file, when generating multiple briefs, or when the user asks for validation. If the script reports missing sections, fix the brief and run it again.

## Validation

Before finalizing, check:

- The output is a decision brief, not a general summary.
- The decision is separated from context and options.
- Implicit decisions are clearly labeled as inferred.
- Missing decisions are marked as unsupported by notes.
- Risks and next actions are evidence-linked.
- The next action is concrete, or explicitly marked as not specified.
```

### Plantilla

Cuando disenes una skill pequena similar, usa esta estructura base:

```markdown
---
name: [kebab-case-name]
description: Use this skill when [resultado concreto] from [entradas habituales]. Use it when [casos dificiles]. Do not use it for [near misses].
---

# [Skill title]

Use this skill to [resultado observable].

Core steering:
- [leading word]: [decision practica que cambia].

## Workflow
1. [Paso obligatorio]
2. [Paso obligatorio]
3. [Paso obligatorio]

## Output format
[Plantilla de salida]

## Defaults
- [Default que evita ambiguedad]

## Validation
- [Check verificable]
```

Rellenada en una linea para nuestro caso:

```markdown
Skill pequena: `decision-brief`
Resultado: convertir notas desordenadas en un brief de decision.
Frontera: no actas, no tickets, no project management completo.
Steering: decision-first, evidence-linked, actionable-next-step.
Validacion: decision clara o ausencia declarada, riesgos sin inventar, siguiente accion concreta.
```

### Entregable

Queda el paquete final como artefacto didactico: `SKILL.md`, una reference, un asset y un script. Tambien queda una forma de pensar: no escribimos una skill para cubrir todo un dominio, sino para encapsular una tarea recurrente con activacion, scope, pasos, salida, recursos y evaluacion.

---

## Checklist final de calidad

Antes de dar por buena una skill pequena, revisa:

```markdown
- [ ] Resuelve una tarea recurrente, no un dominio entero.
- [ ] Tiene un resultado observable.
- [ ] La description dice cuando usarla y cuando no usarla.
- [ ] Hay 2 o 3 casos positivos escritos antes de cerrar la skill.
- [ ] Hay near-misses para evitar sobre-activacion.
- [ ] El workflow cabe en pocos pasos claros.
- [ ] Las palabras guia cambian comportamiento real.
- [ ] El formato de salida esta definido si el formato importa.
- [ ] La skill no intenta hacer un proceso enorme de principio a fin.
- [ ] Las fases grandes se dividen en skills o pasos enfocados.
- [ ] El `SKILL.md` contiene solo lo que se usa siempre.
- [ ] Los recursos externos se justifican por uso condicional.
- [ ] Cada reference tiene una condicion clara de lectura.
- [ ] Cada asset representa una plantilla o recurso de salida, no instrucciones duplicadas.
- [ ] Cada script tiene contrato de entrada/salida y un momento claro de ejecucion.
- [ ] Los scripts solo aparecen cuando hay validacion o transformacion mecanica.
- [ ] Hay evals minimos de activacion y calidad.
- [ ] La salida mejora frente a un resumen generico.
- [ ] Se eliminaron no-ops, sediment y duplicaciones.
```

## Cierre

`decision-brief` es pequeno a proposito. Esa es la leccion principal.

Una skill no gana valor por abarcar mas. Gana valor cuando el agente trabaja mejor en una tarea concreta: se activa con precision, sigue un flujo simple, usa criterio experto, evita errores previsibles y entrega algo que podemos revisar.

Las herramientas amplian lo que el agente puede hacer. Los sistemas pequenos mejoran como lo hace.


