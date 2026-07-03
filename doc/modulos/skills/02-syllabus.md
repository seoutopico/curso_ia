# Syllabus: diseno de skills pequenos, claros y utiles

## Tesis del curso

Tools are great, systems are better.

Una herramienta amplia permite hacer muchas cosas, pero no decide por si sola como trabajar bien. Una skill pequena convierte criterio experto en un sistema operativo minimo: cuando activarse, que pasos seguir, que formato producir, que recursos consultar, que validar y que podar cuando deja de aportar.

Este curso ensena a disenar skills como unidades de trabajo reutilizables, activables y verificables. No buscamos crear muchas skills ni cubrir dominios enteros. Buscamos aprender a encapsular una tarea recurrente para que un agente la haga mejor, con menos ambiguedad y menos correcciones del usuario.

El ejemplo continuo sera un skill llamado `decision-brief`: convierte notas de reunion, conversacion o intercambio asincrono en un breve documento de decision con contexto, opciones, decision, riesgos y siguiente accion.

---

## Bloque 0. Fundamentos: anatomia de una skill

**Que estamos haciendo**

Entendemos que es una skill antes de disenarla: donde vive, que contiene, como se estructura `SKILL.md`, que es YAML frontmatter, que campos son obligatorios y que recursos opcionales puede incluir.

**Por que importa**

Sin esta base, el alumno confunde una skill con un prompt largo. Una skill es una carpeta autocontenida con metadata, instrucciones y recursos que el agente carga progresivamente.

**Ejemplo**

```text
decision-brief/
+-- SKILL.md
+-- references/
+-- assets/
+-- scripts/
```

**Plantilla**

```markdown
Skill:
Ubicacion:
Campo name:
Campo description:
Cuerpo Markdown:
Recursos opcionales:
```

**Entregable**

Un mapa de anatomia de la skill: carpeta, `SKILL.md`, YAML, Markdown, `references/`, `assets/` y `scripts/`.

---

## Bloque 1. Entender el problema antes de escribir la skill

**Que estamos haciendo**

Identificamos una tarea recurrente que merece convertirse en skill. Antes de escribir frontmatter, instrucciones o recursos, observamos que resultado se repite, donde falla el agente sin ayuda y que criterio humano queremos empaquetar.

**Por que importa**

Una skill no es "mas contexto". Es contexto organizado para mejorar una familia concreta de tareas. Si el problema no esta claro, la skill tiende a crecer como documentacion generica: se activa mal, consume contexto y no cambia el comportamiento.

**Ejemplo**

Problema observable: despues de reuniones o conversaciones largas, el agente suele resumir mucho, pero no deja clara la decision. Mezcla contexto, opiniones, opciones descartadas y siguientes pasos.

Skill candidata: `decision-brief`.

**Plantilla**

```markdown
Problema recurrente:
Usuario tipico:
Entrada habitual:
Salida deseada:
Fallo frecuente sin skill:
Criterio experto que debe aplicar:
Por que no basta con una herramienta general:
```

**Entregable**

Una ficha de problema de una pagina que justifica por que la skill deberia existir.

---

## Bloque 2. Elegir scope: una unidad de trabajo que componga bien

**Que estamos haciendo**

Delimitamos que cubre la skill y que queda fuera. Buscamos una escala intermedia: mas grande que un comando aislado, mas pequena que un dominio entero.

**Por que importa**

El scope gobierna la activacion, la estructura, los recursos y la evaluacion. Una skill demasiado amplia se convierte en "ayuda con reuniones". Una demasiado estrecha solo sirve para un caso irrepetible.

**Ejemplo**

Buen scope: producir un brief de decision a partir de notas, transcripciones parciales o conversaciones.

Fuera de scope: grabar la reunion, transcribir, crear tickets, actualizar roadmap, redactar actas legales o decidir por el equipo.

**Plantilla**

```markdown
La skill sirve para:
La skill no sirve para:
Entrada minima necesaria:
Resultado final:
Casos cercanos que no deben activarla:
Senal de que el scope es demasiado grande:
Senal de que el scope es demasiado pequeno:
```

**Entregable**

Un mapa de scope con fronteras positivas y negativas.

---

## Bloque 3. Definir casos de uso y criterios de exito

**Que estamos haciendo**

Escribimos 2 o 3 casos de uso concretos antes de redactar la skill. Cada caso conecta una peticion realista del usuario, una entrada, un flujo y una salida observable.

**Por que importa**

Los casos de uso evitan disenar desde abstracciones. Tambien dan la base para evaluar activacion, calidad y recursos.

**Ejemplo**

- "Te pego notas de una reunion. Sacame la decision y el siguiente paso."
- "Esta conversacion de Slack termino en una decision implicita. Conviertela en brief para compartir."
- "Tenemos tres opciones discutidas; prepara un documento corto para confirmar la decision con el equipo."

**Plantilla**

```markdown
Caso de uso:
Prompt del usuario:
Entrada:
Pasos que debe seguir el agente:
Salida esperada:
Criterios de exito:
Riesgos o edge cases:
```

**Entregable**

Una matriz con casos positivos y near-misses que no deberian activar la skill.

---

## Bloque 4. Escribir la description: el trigger como decision de producto

**Que estamos haciendo**

Redactamos la `description` del frontmatter como condicion de activacion. No describe la skill de forma ornamental: le dice al agente cuando debe cargarla.

**Por que importa**

La descripcion es el punto de mayor apalancamiento. Si es vaga, la skill no se usa. Si es demasiado amplia, se usa cuando no toca.

**Ejemplo**

```yaml
---
name: decision-brief
description: Use this skill when the user needs to turn meeting notes, conversation notes, chat threads, or rough discussion notes into a concise decision brief with context, options, decision, risks, and next action. Use it when the decision may be explicit or implicit. Do not use it for full meeting minutes, legal records, project plans, ticket creation, or generic summarization.
---
```

**Plantilla**

```yaml
---
name: nombre-en-kebab-case
description: Use this skill when [resultado concreto] from [entradas habituales], including [casos implicitos]. Do not use it for [near misses].
---
```

**Entregable**

Una descripcion candidata y una mini prueba de activacion con prompts positivos y negativos.

---

## Bloque 5. Escribir instrucciones: pasos, steering y formato de salida

**Que estamos haciendo**

Convertimos el criterio experto en instrucciones operativas. Separamos pasos, reglas de decision, formato de salida y validacion minima. Usamos palabras guia que cambien conducta.

**Por que importa**

Una skill buena no documenta todo lo que sabemos; guia el comportamiento del agente bajo presion. Las instrucciones deben ayudarle a hacer el trabajo correcto, no solo sonar razonables.

**Ejemplo**

Leading words para `decision-brief`:

- `decision-first`: el brief existe para aclarar la decision.
- `evidence-linked`: cada decision o riesgo debe conectarse con la entrada.
- `actionable-next-step`: el brief termina con una accion concreta.

**Plantilla**

```markdown
## Workflow
1. [Paso]
2. [Paso]
3. [Paso]

## Defaults
- [Default]

## Output format
[Plantilla]

## Validation
- [Check]
```

**Entregable**

Un primer borrador del cuerpo de `SKILL.md`.

---

## Bloque 6. Mapear progressive disclosure: que va en cada nivel

**Que estamos haciendo**

Decidimos que vive en `description`, que vive en `SKILL.md` y que se mueve a recursos externos.

**Por que importa**

Progressive disclosure protege la atencion del agente. No todo lo util debe cargarse siempre.

**Ejemplo**

- `description`: cuando usar `decision-brief`.
- `SKILL.md`: workflow, formato, defaults y validacion basica.
- `references/`: rubrica extensa de calidad de decisiones.
- `assets/`: plantilla corporativa exacta.
- `scripts/`: validador mecanico de estructura.

**Plantilla**

```markdown
Nivel 1 - Catalogo:
Nivel 2 - SKILL.md:
Nivel 3 - references/:
Nivel 3 - assets/:
Nivel 3 - scripts/:
Contenido a eliminar:
```

**Entregable**

Un mapa de carga progresiva para la skill.

---

## Bloque 7. Disenar una reference: conocimiento bajo demanda

**Que estamos haciendo**

Creamos una referencia corta para informacion que ayuda en algunos casos, pero no debe cargar siempre.

**Por que importa**

`references/` evita inflar `SKILL.md` con guias largas, ejemplos extensos o criterios que solo aplican bajo condicion.

**Ejemplo**

`references/decision-quality-rubric.md` solo se lee cuando el usuario pide evaluar la calidad de una decision o aplicar una rubrica interna.

**Plantilla**

```markdown
# [Reference name]

## Cuando leer esta referencia
[Condicion clara]

## Criterios
- [Criterio]

## Errores frecuentes
- [Error]
```

**Entregable**

Una referencia breve y una linea en `SKILL.md` que diga exactamente cuando leerla.

---

## Bloque 8. Disenar un asset: plantilla reutilizable

**Que estamos haciendo**

Creamos un asset cuando el resultado necesita una estructura exacta que conviene reutilizar.

**Por que importa**

`assets/` separa materiales de salida de las instrucciones. Una plantilla larga no siempre debe vivir en `SKILL.md`.

**Ejemplo**

`assets/brief-template.md` contiene la plantilla oficial del decision brief.

**Plantilla**

```markdown
# [Template title]

## [Section]
[Placeholder]
```

**Entregable**

Un asset de plantilla y una instruccion en `SKILL.md` sobre cuando usarlo.

---

## Bloque 9. Disenar un script: validacion determinista

**Que estamos haciendo**

Creamos un script minimo cuando una comprobacion es mecanica, repetitiva o demasiado fragil para dejarla solo en lenguaje natural.

**Por que importa**

Los scripts convierten parte del sistema en ejecucion verificable. No sustituyen al criterio del agente; reducen errores mecanicos.

**Ejemplo**

`scripts/check-brief-structure.py` valida que el output tenga secciones obligatorias: Context, Options considered, Decision, Risks and open questions, Next action.

**Plantilla**

```markdown
Script:
Entrada:
Salida:
Errores que detecta:
Como se invoca desde SKILL.md:
Cuando NO hace falta:
```

**Entregable**

Un script didactico o pseudocodigo ejecutable, con contrato de entrada/salida y uso documentado.

---

## Bloque 10. Integrar el paquete de skill completo

**Que estamos haciendo**

Unimos `SKILL.md`, `references/`, `assets/` y `scripts/` en una version extendida de `decision-brief`.

**Por que importa**

El curso debe mostrar dos niveles: version minima y version con recursos. Asi el alumno entiende que no se crean carpetas por inercia, pero tambien aprende a usarlas.

**Ejemplo**

```text
decision-brief/
+-- SKILL.md
+-- references/decision-quality-rubric.md
+-- assets/brief-template.md
+-- scripts/check-brief-structure.py
```

**Plantilla**

```markdown
Recurso:
Por que existe:
Cuando se carga:
Como se referencia desde SKILL.md:
Como se valida:
```

**Entregable**

Un paquete didactico completo de skill, aunque se presente como snippets dentro de la documentacion.

---

## Bloque 11. Evaluar activacion, calidad y recursos

**Que estamos haciendo**

Probamos si la skill se activa cuando debe, no se activa cuando no debe, mejora el resultado frente a no usarla y usa recursos solo cuando corresponde.

**Por que importa**

Crear una skill no demuestra que aporte valor. Crear recursos tampoco. Hay que observar si reducen errores sin inflar contexto innecesariamente.

**Ejemplo**

- Prompt normal: no deberia leer la rubrica extensa.
- Prompt con rubrica: deberia leer `references/decision-quality-rubric.md`.
- Output final: puede validarse con `scripts/check-brief-structure.py`.

**Plantilla**

```markdown
Prueba:
Prompt:
Debe activar skill: si/no
Debe leer reference: si/no
Debe usar asset: si/no
Debe ejecutar script: si/no
Mejora observable:
Fallo detectado:
Cambio propuesto:
```

**Entregable**

Una tabla de evaluacion que cubra trigger, calidad y uso de recursos.

---

## Bloque 12. Podar, dividir e iterar

**Que estamos haciendo**

Revisamos la skill para eliminar no-ops, sediment, duplicacion y recursos injustificados. Ajustamos scope, descripcion, instrucciones y recursos a partir de fallos reales.

**Por que importa**

Las skills se degradan cuando acumulan texto historico y archivos que nadie usa. Podar tambien aplica a `references/`, `assets/` y `scripts/`.

**Ejemplo**

- Si la reference repite el workflow, se recorta.
- Si el asset es identico al output format, se elimina o se deja solo uno.
- Si el script valida algo trivial que el agente nunca falla, se elimina.
- Si la skill crece hacia tickets y roadmap, se divide en otra skill.

**Plantilla**

```markdown
Elemento:
Que decision cambia:
Que error evita:
Se usa siempre o bajo condicion:
Accion: mantener / mover / convertir en script / eliminar / dividir
```

**Entregable**

Una version podada de la skill y un changelog breve.

---

## Framework de diseno antes de crear una skill

Antes de abrir un editor, responde estas preguntas en orden:

1. Que tarea recurrente queremos mejorar?
2. Que resultado observable debe producir el agente?
3. Que falla hoy cuando el agente lo intenta sin skill?
4. Que criterio experto debe quedar empaquetado?
5. Que 2 o 3 casos de uso concretos justifican la skill?
6. Que prompts deberian activarla?
7. Que prompts cercanos no deberian activarla?
8. Cual es el scope minimo que sigue siendo util?
9. Que queda claramente fuera?
10. Que pasos necesita ver el agente siempre?
11. Que informacion solo debe cargarse bajo condicion?
12. Que plantilla deberia ser asset?
13. Que logica deberia ser script?
14. Que referencia deberia vivir fuera de `SKILL.md`?
15. Que palabra guia puede cambiar la conducta del agente?
16. Que validacion demuestra que la salida sirve?
17. Contra que baseline vamos a comparar?
18. Que texto o archivo no cambia comportamiento y puede eliminarse?
19. Como sabremos que la skill merece seguir existiendo?

La respuesta deseada no es "tenemos una skill". La respuesta deseada es: tenemos un sistema pequeno que hace que el agente trabaje mejor en una tarea concreta.
