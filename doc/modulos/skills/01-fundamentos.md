# Fundamentos: que es una skill y como esta compuesta

## Proposito de este documento

Antes de disenar una skill conviene entender que pieza estamos construyendo. Aqui no vamos a empezar por el ejemplo ni por la plantilla pedagogica. Primero vamos a ver la anatomia completa: donde vive una skill, que archivos la componen, como se escribe `SKILL.md`, que campos existen en el YAML frontmatter, cuales son obligatorios, cuales son opcionales y para que sirven `scripts/`, `references/` y `assets/`.

La idea central del curso sigue siendo la misma:

Tools are great, systems are better.

Una herramienta da capacidad. Una skill pequena convierte esa capacidad en un sistema de trabajo: cuando activarse, que pasos seguir, que criterio aplicar, que formato producir y como validar el resultado.

---

## 1. Que es una skill

### Que estamos haciendo

Definimos una skill como una carpeta autocontenida que empaqueta instrucciones, criterio experto y recursos para que un agente trabaje mejor en una tarea recurrente.

Una skill puede ser muy pequena, pero no es solo un prompt. Es un pequeno sistema compuesto por:

- una carpeta con nombre propio
- un archivo obligatorio `SKILL.md`
- metadata en YAML
- instrucciones en Markdown
- recursos opcionales cuando hacen falta

### Por que importa

Si una skill se entiende como "un prompt guardado", se vuelve larga, generica y dificil de evaluar. Si se entiende como una pieza de sistema, se disena con limites claros:

- que tarea mejora
- cuando se activa
- que instrucciones carga
- que recursos consulta
- que salida produce
- como se valida

### Ejemplo

`decision-brief` no intenta gestionar reuniones completas. Solo ensena al agente a convertir notas desordenadas en un brief de decision.

```markdown
Tarea recurrente:
Convertir notas de reunion o conversacion en una decision clara.

Criterio experto:
Leer las notas con mentalidad decision-first, separar opciones de decision y no inventar responsables, fechas o riesgos.

Resultado:
Un brief breve con contexto, opciones, decision, riesgos y siguiente accion.
```

### Plantilla

```markdown
Nombre provisional de la skill:

Tarea recurrente que mejora:

Conocimiento o criterio que empaqueta:

Resultado observable:

Que NO intenta hacer:
```

### Entregable

Una definicion corta de la skill como unidad de trabajo, no como dominio entero.

---

## 2. Donde vive una skill

### Que estamos haciendo

Ubicamos la skill en el sistema. Una skill vive como una carpeta que el cliente o agente sabe descubrir. La ruta exacta depende de la herramienta que uses, pero el patron es estable: una carpeta por skill y dentro un archivo llamado exactamente `SKILL.md`.

### Por que importa

El agente no sabe que una skill existe por intuicion. El cliente la descubre escaneando rutas conocidas, lee su metadata y la ofrece al modelo como una capacidad disponible. Si la carpeta esta mal ubicada, si el archivo no se llama `SKILL.md` o si el frontmatter es invalido, la skill puede no cargarse.

### Ejemplo

Rutas habituales, segun cliente y configuracion:

```text
project/.agents/skills/decision-brief/SKILL.md
project/.client-name/skills/decision-brief/SKILL.md
user-home/.agents/skills/decision-brief/SKILL.md
user-home/.client-name/skills/decision-brief/SKILL.md
```

El estandar define que hay dentro de la carpeta. La ubicacion concreta depende del cliente: Codex, Claude Code, VS Code, Cursor u otro agente compatible pueden buscar en rutas distintas.

Estructura basica:

```text
decision-brief/
+-- SKILL.md
```

Estructura mas completa:

```text
decision-brief/
+-- SKILL.md
+-- scripts/
|   +-- check-brief-structure.py
+-- references/
|   +-- decision-quality.md
+-- assets/
|   +-- brief-template.md
+-- agents/
    +-- openai.yaml
```

`agents/openai.yaml` no pertenece al nucleo universal de una skill. Puede aparecer como metadata de interfaz en algunos entornos, por ejemplo para mostrar nombre, descripcion corta o prompt inicial en una UI. Para aprender el formato base, lo importante es `SKILL.md` y los recursos opcionales.

### Plantilla

```text
[skill-name]/
+-- SKILL.md                  requerido
+-- scripts/                  opcional
+-- references/               opcional
+-- assets/                   opcional
+-- agents/openai.yaml        opcional, segun cliente
```

### Entregable

Un mapa de carpeta que muestre donde vive la skill y que piezas incluye.

---

## 3. Anatomia completa de una skill

### Que estamos haciendo

Vemos todos los elementos que puede tener una skill. No todos son obligatorios, pero conviene conocerlos antes de decidir que incluir.

### Por que importa

Si solo hablamos de la unidad minima, parece que la skill se reduce a dos campos. No es asi. La unidad minima sirve para arrancar, pero el formato completo permite separar activacion, instrucciones, referencias, scripts y plantillas.

### Ejemplo

```text
skill-name/
+-- SKILL.md
|   +-- YAML frontmatter
|   |   +-- name: requerido
|   |   +-- description: requerido
|   |   +-- license: opcional
|   |   +-- compatibility: opcional
|   |   +-- metadata: opcional
|   |   +-- allowed-tools: opcional, experimental
|   +-- Markdown body
|       +-- workflow
|       +-- defaults
|       +-- gotchas
|       +-- output format
|       +-- validation
+-- scripts/
|   +-- codigo ejecutable opcional
+-- references/
|   +-- documentacion consultada bajo demanda
+-- assets/
|   +-- plantillas o recursos reutilizables
```

### Plantilla

```markdown
---
name: [skill-name]
description: [what it does and when to use it]
license: [optional]
compatibility: [optional]
metadata:
  [optional-key]: [optional-value]
allowed-tools: [optional, experimental]
---

# [Skill title]

[Markdown instructions]
```

### Entregable

Una vista completa de las piezas posibles antes de decidir cuales necesita la skill real.

---

## 4. `SKILL.md`: YAML frontmatter + Markdown

### Que estamos haciendo

Separamos las dos zonas de `SKILL.md`:

1. YAML frontmatter, entre delimitadores `---`.
2. Cuerpo Markdown, despues del segundo `---`.

### Por que importa

Cada zona tiene una responsabilidad distinta.

El YAML frontmatter responde: "que skill es esta y cuando deberia activarse?".

El Markdown responde: "una vez activada, como debe trabajar el agente?".

No conviene esconder el trigger en el cuerpo, porque el cuerpo normalmente se lee solo despues de que la skill se active.

### Ejemplo

```markdown
---
name: decision-brief
description: Use this skill when the user needs to turn meeting notes, conversation notes, chat threads, or rough discussion notes into a concise decision brief with context, options, decision, risks, and next action.
---

# Decision brief

Use this skill to turn rough discussion material into a brief decision document.

## Workflow

1. Identify whether the notes contain an explicit, implicit, or unsupported decision.
2. Extract only the context needed to understand the decision.
3. Separate options, decision, risks, and next action.
4. Validate that the brief does not invent facts.
```

### Plantilla

```markdown
---
[metadata YAML]
---

[Markdown instructions]
```

### Entregable

Un `SKILL.md` donde se ve claramente que parte es metadata y que parte es instruccion.

---

## 5. Campos del YAML frontmatter

### Que estamos haciendo

Exponemos todos los campos principales del frontmatter. Hay campos obligatorios y campos opcionales.

### Por que importa

Para crear una primera skill normalmente basta con `name` y `description`, pero el alumno debe saber que existen mas campos. Asi no confundimos "lo minimo para empezar" con "todo lo que permite el formato".

### Campos obligatorios

#### `name`

Identificador de la skill.

Reglas practicas:

- usar kebab-case
- solo minusculas, numeros y guiones
- no usar espacios
- no empezar ni terminar con guion
- evitar guiones dobles
- mantenerlo por debajo de 64 caracteres
- hacerlo coincidir con el nombre de la carpeta

Ejemplo correcto:

```yaml
name: decision-brief
```

Ejemplos incorrectos:

```yaml
name: Decision Brief
name: decision_brief
name: -decision-brief
name: decision--brief
```

#### `description`

Descripcion que ayuda al agente a decidir si debe activar la skill.

Debe incluir:

- que hace la skill
- cuando debe usarse
- entradas habituales
- frases o intenciones del usuario
- limites o casos cercanos donde no debe usarse, si hay riesgo de confusion

Reglas practicas:

- ser concreta
- mencionar el resultado observable
- hablar desde la intencion del usuario
- incluir triggers reales
- no pasar de 1024 caracteres

Ejemplo:

```yaml
description: Use this skill when the user needs to turn meeting notes, conversation notes, chat threads, or rough discussion notes into a concise decision brief with context, options, decision, risks, and next action. Do not use it for full meeting minutes, project plans, ticket creation, or generic summarization.
```

### Campos opcionales

#### `license`

Indica la licencia de la skill si se distribuye o comparte.

```yaml
license: MIT
```

Tambien puede apuntar a un archivo de licencia incluido en la carpeta:

```yaml
license: See LICENSE.txt
```

#### `compatibility`

Describe requisitos de entorno o compatibilidad.

Usalo solo cuando haga falta: cliente esperado, paquetes del sistema, version de Python, necesidad de red, herramientas externas, etc.

```yaml
compatibility: Requires Python 3.11+ and access to the project repository.
```

#### `metadata`

Mapa libre de claves y valores. Sirve para informacion adicional que algunos clientes o equipos pueden usar.

```yaml
metadata:
  author: curso-skills
  version: "1.0.0"
  category: writing
```

No debe convertirse en un cajon de sastre. Si una informacion no ayuda a descubrir, mantener o ejecutar la skill, probablemente sobra.

#### `allowed-tools`

Campo opcional y experimental para declarar herramientas permitidas o esperadas. El soporte depende del cliente.

```yaml
allowed-tools: Bash(python:*) Read Write
```

No lo uses como tema central del curso. Conviene mencionarlo para completar la anatomia, pero no depender de el en ejercicios iniciales.

### Ejemplo completo de frontmatter

```yaml
---
name: decision-brief
description: Use this skill when the user needs to turn meeting notes, conversation notes, chat threads, or rough discussion notes into a concise decision brief with context, options, decision, risks, and next action. Do not use it for full meeting minutes, project plans, ticket creation, or generic summarization.
license: MIT
compatibility: Works in any agent client that supports Agent Skills and Markdown output.
metadata:
  author: curso-skills
  version: "0.1.0"
  category: writing
---
```

Para el curso, la version inicial recomendada sigue siendo mas simple:

```yaml
---
name: decision-brief
description: Use this skill when the user needs to turn meeting notes, conversation notes, chat threads, or rough discussion notes into a concise decision brief with context, options, decision, risks, and next action. Do not use it for full meeting minutes, project plans, ticket creation, or generic summarization.
---
```

### Plantilla

```yaml
---
name: [nombre-corto-en-kebab-case]
description: Use this skill when [resultado concreto] from [entradas habituales]. Use it when [casos dificiles o implicitos]. Do not use it for [casos cercanos fuera de scope].
license: [opcional]
compatibility: [opcional]
metadata:
  [clave-opcional]: [valor-opcional]
allowed-tools: [opcional, experimental]
---
```

### Entregable

Una tabla de campos del frontmatter donde el alumno marque:

```markdown
| Campo | Obligatorio | Lo usaremos? | Por que |
|---|---:|---:|---|
| name | si | si | Identifica la skill |
| description | si | si | Activa la skill |
| license | no | no | No se distribuye aun |
| compatibility | no | no | No hay requisitos especiales |
| metadata | no | no | No aporta en la primera version |
| allowed-tools | no | no | Experimental y no necesario |
```

---

## 6. El cuerpo Markdown: instrucciones operativas

### Que estamos haciendo

Escribimos la parte Markdown de `SKILL.md`. Aqui viven las instrucciones que el agente seguira cuando la skill ya este activada.

### Por que importa

El cuerpo no debe repetir teoria general. Debe contener instrucciones que cambian comportamiento.

Buenas secciones para una skill pequena:

- `Workflow`: pasos del procedimiento
- `Defaults`: decisiones por defecto
- `Gotchas`: errores probables que debe evitar
- `Output format`: estructura de salida
- `Validation`: comprobaciones antes de terminar

### Ejemplo

```markdown
# Decision brief

Use this skill to turn rough discussion material into a brief decision document.

## Workflow

1. Read the notes with a decision-first lens.
2. Classify the decision as explicit, implicit, or not supported.
3. Keep only context needed to understand the decision.
4. Separate options, decision, risks, and next action.
5. Validate that every claim is supported by the notes.

## Defaults

- Keep the brief short.
- Preserve uncertainty.
- Do not invent owners or dates.

## Output format

# Decision brief

## Context
[Only the context needed.]

## Options considered
- [Option]

## Decision
[Decision or "Decision not yet supported by notes."]

## Risks and open questions
- [Risk or missing information]

## Next action
[Concrete action or "Next action not specified in notes."]

## Validation

- The output is not a generic summary.
- The decision is separated from context and options.
- Risks and next actions are supported by the notes.
```

### Plantilla

```markdown
# [Skill title]

Use this skill to [observable result].

## Workflow

1. [Paso obligatorio]
2. [Paso obligatorio]
3. [Paso obligatorio]

## Defaults

- [Decision por defecto]

## Gotchas

- [Error probable que debe evitar]

## Output format

[Plantilla de salida]

## Validation

- [Check verificable]
```

### Entregable

Un cuerpo Markdown corto, accionable y verificable.

---

## 7. Recursos opcionales: `scripts/`, `references/` y `assets/`

### Que estamos haciendo

Distinguimos las carpetas opcionales. No son obligatorias, pero son importantes cuando la skill necesita mas que instrucciones.

### Por que importa

La skill no debe meterlo todo en `SKILL.md`. Si una informacion se usa solo a veces, si una validacion es mecanica o si una plantilla es larga, conviene separarla.

### `scripts/`

Usa `scripts/` para codigo ejecutable: validaciones, transformaciones, generacion de archivos o pasos repetibles.

Buen uso:

```text
scripts/check-brief-structure.py
```

Cuando usarlo:

- el agente reescribe el mismo codigo una y otra vez
- la validacion debe ser determinista
- hay que procesar datos o archivos de forma repetible
- conviene tener `--help`, errores claros y salida estructurada

### `references/`

Usa `references/` para documentacion que el agente debe leer bajo demanda.

Buen uso:

```text
references/decision-quality-rubric.md
```

Cuando usarlo:

- hay una guia larga
- hay reglas internas
- hay ejemplos extensos
- no se necesita en todas las ejecuciones

El `SKILL.md` debe decir cuando leer la referencia:

```markdown
Read `references/decision-quality-rubric.md` only when the user asks to apply the internal decision quality rubric.
```

### `assets/`

Usa `assets/` para plantillas, recursos estaticos, archivos base, imagenes, fuentes o ejemplos que se usaran como material de salida.

Buen uso:

```text
assets/brief-template.md
```

Cuando usarlo:

- hay una plantilla corporativa exacta
- hay recursos que no hace falta leer como instrucciones
- el agente debe copiar o adaptar un archivo base

### Otros archivos

Evita meter documentacion auxiliar dentro de la carpeta de la skill si no la necesita el agente para ejecutar la tarea. En especial, no uses un `README.md` dentro de la skill como sustituto de `SKILL.md`. Si el repo necesita un README para humanos, que viva fuera de la carpeta de la skill.

### Plantilla

```markdown
Debe estar en SKILL.md porque se usa siempre:

Debe ir a references/ porque solo se consulta bajo condicion:

Debe ir a scripts/ porque es mecanico o repetible:

Debe ir a assets/ porque es una plantilla o recurso reusable:

Debe eliminarse porque no cambia comportamiento:
```

### Entregable

Una decision explicita sobre recursos: incluirlos, posponerlos o descartarlos.

---

## 8. Progressive disclosure: como se carga una skill

### Que estamos haciendo

Entendemos la carga progresiva.

Una skill no deberia cargar todo desde el principio. El patron habitual tiene tres niveles:

1. Catalogo: `name` y `description`.
2. Instrucciones: cuerpo completo de `SKILL.md`.
3. Recursos: archivos de `scripts/`, `references/` o `assets/` cuando hacen falta.

### Por que importa

Cada token compite por atencion. Si el agente carga demasiada informacion, puede seguir peor las instrucciones importantes.

Progressive disclosure no es solo una optimizacion tecnica. Es una regla de diseno: cada pieza debe vivir donde aporta mas y molesta menos.

### Ejemplo

Para `decision-brief`:

```markdown
Nivel 1 - Catalogo:
name + description

Nivel 2 - Instrucciones:
workflow decision-first, output format, defaults y validation

Nivel 3 - Recursos:
ninguno en la version inicial
```

Si el equipo anade una guia larga de calidad:

```markdown
Read `references/decision-quality.md` only when the user asks to apply the internal decision quality rubric.
```

### Plantilla

```markdown
Nivel 1: que debe aparecer en name/description:

Nivel 2: que debe estar siempre en SKILL.md:

Nivel 3: que solo debe cargarse bajo condicion:

Que deberia eliminarse:
```

### Entregable

Un mapa de carga progresiva que justifica donde vive cada pieza de informacion.

---

## 9. Que no es una skill

### Que estamos haciendo

Delimitamos falsos amigos: cosas que parecen skills pero no funcionan como skills buenas.

### Por que importa

Muchos malos disenos nacen de confundir una skill con otro artefacto.

### Ejemplo

Una skill no es:

- un prompt largo pegado en un archivo
- una wiki completa del equipo
- un manual generico sobre un dominio
- un asistente universal para una categoria enorme
- una lista de deseos sin validacion
- una forma de esconder procesos fragiles sin evaluarlos

`decision-brief` seria mala si intentara:

```markdown
Grabar reuniones, transcribir, resumir, decidir, crear tickets, actualizar roadmap, mandar correos y hacer seguimiento semanal.
```

Ese flujo deberia dividirse en fases:

```markdown
1. Extraer decision.
2. Confirmar decision.
3. Convertir decision validada en tareas.
4. Comunicar decision.
```

`decision-brief` solo cubre la primera fase.

### Plantilla

```markdown
Esta skill NO es:

Proceso grande que no debe intentar cubrir:

Fases separables:

Fase que esta skill si cubre:
```

### Entregable

Una frontera conceptual clara: la skill es pequena a proposito.

---

## 10. Mini skill completa para leer antes de construir

### Que estamos haciendo

Leemos una version pequena pero completa de `decision-brief`. Incluye carpeta, YAML, Markdown, campos obligatorios, workflow y validacion.

### Por que importa

Antes de aprender a disenar paso a paso, conviene ver el objeto entero. Asi las lecciones posteriores no parecen abstractas.

### Ejemplo

```text
decision-brief/
+-- SKILL.md
```

```markdown
---
name: decision-brief
description: Use this skill when the user needs to turn meeting notes, conversation notes, chat threads, or rough discussion notes into a concise decision brief with context, options, decision, risks, and next action. Do not use it for full meeting minutes, project plans, ticket creation, or generic summarization.
---

# Decision brief

Use this skill to turn rough discussion material into a brief decision document.

## Workflow

1. Read the source material with a decision-first lens.
2. Classify the decision as explicit, implicit, or not supported by notes.
3. Extract only the context needed to understand the decision.
4. Separate options considered, decision, risks, and next action.
5. Preserve uncertainty instead of inventing facts.

## Output format

# Decision brief

## Context
[Only the context needed to understand the decision.]

## Options considered
- [Option]

## Decision
[Decision, inferred decision with caveat, or "Decision not yet supported by notes."]

## Risks and open questions
- [Risk or missing information]

## Next action
[Concrete action with owner/date if present, or "Next action not specified in notes."]

## Validation

- The output is not a generic summary.
- The decision is separated from context and options.
- Risks and next actions are supported by the notes.
- Owners, dates, and commitments are not invented.
```

### Plantilla

```markdown
---
name: [skill-name]
description: Use this skill when [trigger]. Do not use it for [near misses].
license: [optional]
compatibility: [optional]
metadata:
  [optional-key]: [optional-value]
allowed-tools: [optional, experimental]
---

# [Skill title]

Use this skill to [observable result].

## Workflow

1. [Step]
2. [Step]
3. [Step]

## Output format

[Expected structure]

## Validation

- [Check]
```

### Entregable

Un mapa mental completo de la anatomia de una skill antes de empezar el proceso de diseno del syllabus y las lecciones.

---

## Cierre

Una skill vive como una carpeta pequena. Su pieza obligatoria es `SKILL.md`. `SKILL.md` combina YAML frontmatter y Markdown:

- YAML decide como se descubre y cuando se activa.
- Markdown guia que hacer cuando ya se activo.
- `scripts/`, `references/` y `assets/` solo aparecen cuando justifican su coste.

La unidad minima sirve para empezar. La anatomia completa sirve para disenar con criterio.

