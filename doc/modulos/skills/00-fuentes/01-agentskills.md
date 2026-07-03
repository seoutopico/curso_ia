# Analisis de agentskills.io para crear skills pequenos y utiles

## Lectura central

La web de Agent Skills presenta las skills como un formato ligero para empaquetar conocimiento operativo que un agente no deberia tener que redescubrir en cada tarea. La unidad minima es deliberadamente pequena: una carpeta con un `SKILL.md`, frontmatter YAML y unas instrucciones en Markdown. Todo lo demas (`scripts/`, `references/`, `assets/`) es opcional y solo tiene sentido cuando reduce ambiguedad, repeticion o coste de contexto.

La idea mas importante para ensenar no es "crear capacidades grandes", sino convertir experiencia practica en una pieza reusable, activable y verificable. Una buena skill no sustituye al agente ni le da una enciclopedia: le da criterio situado, pasos no obvios, defaults, restricciones y artefactos concretos para una clase de tareas.

## Progressive disclosure como principio de diseno

Agent Skills se apoya en una carga progresiva de tres niveles:

1. Catalogo: al inicio solo se cargan `name` y `description`.
2. Instrucciones: el `SKILL.md` completo se carga cuando la tarea encaja con la descripcion.
3. Recursos: scripts, referencias y assets se cargan solo cuando hacen falta.

Esto cambia como se escribe una skill. La descripcion no es un resumen decorativo: es el mecanismo de activacion. El cuerpo del `SKILL.md` no es documentacion general: es lo que el agente debe tener en contexto cada vez que usa la skill. Los ficheros de apoyo no son anexos para leer "por si acaso": deben estar referenciados con condiciones claras de uso.

Para un curso, progressive disclosure debe explicarse como economia de atencion. Cada token que entra en una skill compite con la conversacion, el codigo, las herramientas y otras skills. Por eso conviene ensenar a separar:

- Lo que el agente necesita saber siempre que la skill se active.
- Lo que solo necesita en ciertos casos.
- Lo que puede ejecutar mejor como script que razonar desde cero.
- Lo que el agente ya sabe y no hace falta repetir.

Una regla practica: si una instruccion no evita un error probable, no fija una convencion local, no desbloquea un procedimiento fragil y no mejora el resultado observable, probablemente sobra.

## Scope: la skill como unidad coherente

La web insiste en que el scope se parece al diseno de una funcion: debe encapsular una unidad de trabajo que componga bien con otras. Si es demasiado estrecha, obliga a activar varias skills para una sola tarea y puede crear conflictos. Si es demasiado amplia, se activa mal y mete instrucciones irrelevantes en contexto.

La escala adecuada suele estar entre "un comando" y "un dominio entero". Ejemplos de buen scope:

- "Procesar formularios PDF con los scripts internos del equipo".
- "Revisar endpoints de esta API siguiendo nuestras reglas de auth, errores y logging".
- "Crear informes mensuales con la estructura y graficos esperados por el area financiera".

Ejemplos de scope problematico:

- "Ayudar con PDFs" porque no delimita tareas ni decisiones.
- "Todo lo relacionado con data engineering" porque mezcla demasiados procedimientos.
- "Ejecutar exactamente esta consulta para este caso unico" porque no generaliza.

El curso deberia entrenar a detectar el patron reusable detras de una tarea real. Una skill nace mejor despues de resolver una tarea concreta con el agente, observar donde fallo, que correcciones hubo y que pasos se repiten.

## La descripcion como trigger

El `description` es el punto de mayor apalancamiento. Los clientes cargan esa descripcion en el catalogo inicial y el modelo la usa para decidir si debe activar la skill. Si es vaga, la skill no se usa. Si es demasiado amplia, se usa cuando no toca.

Buenas descripciones:

- Dicen cuando usar la skill, no solo que contiene.
- Se formulan como instruccion: "Use this skill when...".
- Describen la intencion del usuario, no la implementacion interna.
- Incluyen casos implicitos, donde el usuario no nombra exactamente el dominio.
- Marcan frontera con tareas cercanas que no deben activarla.
- Son concisas y caben de sobra en el limite de 1024 caracteres.

Ejemplo pobre:

```yaml
description: Ayuda con CSV.
```

Ejemplo mas util:

```yaml
description: >
  Use this skill when the user needs to analyze, clean, transform, summarize,
  or visualize tabular data from CSV, TSV, or Excel files, including cases
  where they ask for charts, derived columns, data quality checks, or a
  short analytical report. Do not use it for database ETL or spreadsheet UI
  formatting tasks.
```

La pagina sobre optimizacion de descripciones propone evaluarlas con prompts positivos y negativos. Esto es muy pedagogico: no basta con escribir una descripcion que "suena bien"; hay que comprobar si dispara en los casos adecuados. Los negativos mas utiles son near-misses: prompts que comparten palabras clave pero piden otra cosa.

## Estructura del `SKILL.md`

El formato minimo exige `name` y `description`; el cuerpo puede tener cualquier Markdown. Para ensenar skills pequenas, conviene partir de una estructura simple:

```markdown
---
name: nombre-corto
description: Use this skill when...
---

## Workflow

1. ...
2. ...
3. ...

## Defaults

- ...

## Gotchas

- ...

## Validation

- ...
```

No todas las skills necesitan todas las secciones. El punto no es imponer una plantilla rigida, sino dar al agente instrucciones escaneables. Las secciones con mas valor suelen ser:

- `Workflow`: pasos principales, especialmente si hay dependencias.
- `Defaults`: herramienta, libreria o criterio recomendado cuando hay varias opciones.
- `Gotchas`: errores concretos que el agente cometeria por una suposicion razonable.
- `Validation`: como comprobar que el resultado sirve.
- `Output format`: plantilla exacta cuando el formato importa.

La web recomienda mantener el `SKILL.md` por debajo de 500 lineas y alrededor de 5000 tokens. Para un curso, seria mejor ser aun mas exigentes al principio: skills de 20-80 lineas, una sola responsabilidad, un ejemplo y una validacion clara.

## Scripts, references y assets

Los directorios opcionales no son adorno. Cada uno cumple una funcion distinta:

- `scripts/`: codigo ejecutable para pasos repetibles, fragiles o faciles de validar mecanicamente.
- `references/`: documentacion que el agente solo debe leer bajo ciertas condiciones.
- `assets/`: plantillas, imagenes, esquemas, datos de ejemplo o recursos estaticos.

La recomendacion importante es no cargar recursos de apoyo de forma ansiosa. El `SKILL.md` debe decir cuando leerlos:

```markdown
Read `references/api-errors.md` only if the API returns a non-2xx response.
Use `assets/report-template.md` when the user asks for a client-facing report.
Run `scripts/validate-output.py` before finalizing generated JSON.
```

Los scripts merecen una leccion especifica porque convierten conocimiento en ejecucion verificable. La web aconseja:

- Versionar comandos de terceros (`npx eslint@9`, `uvx ruff@0.8.0`) para reproducibilidad.
- Declarar requisitos en `compatibility` si dependen de runtime, red o paquetes.
- Evitar prompts interactivos.
- Implementar `--help`.
- Dar errores accionables.
- Usar stdout para datos estructurados y stderr para diagnosticos.
- Preferir JSON, CSV o TSV a texto libre cuando otro paso vaya a consumir la salida.
- Hacer scripts idempotentes o incluir `--dry-run` en operaciones con riesgo.
- Controlar el tamano de salida para no saturar el contexto.

La idea docente: cuando el agente reinventa la misma logica en varias ejecuciones, probablemente esa logica debe moverse a `scripts/`.

## Evaluacion: que la skill aporte valor medible

La web separa dos tipos de evaluacion:

- Activacion: si la descripcion dispara cuando debe y no dispara cuando no debe.
- Calidad de salida: si usar la skill mejora el resultado frente a no usarla o frente a la version anterior.

Para activacion, propone crear unas 20 queries realistas, con positivos y negativos, y ejecutarlas varias veces para medir tasa de trigger. La leccion clave es que la descripcion tambien se testea. Ademas, conviene separar train y validation para no sobreajustar la descripcion a ejemplos concretos.

Para calidad, propone evals con:

- Prompt realista.
- Output esperado.
- Ficheros de entrada opcionales.
- Assertions verificables.
- Comparacion con baseline sin skill o con version anterior.
- Revision humana de los outputs.
- Lectura de trazas de ejecucion para entender fallos.

Esto encaja bien con una practica de curso: empezar con 2-3 evals, no con una suite enorme. Primero se observa que falla; luego se escriben assertions mas precisas. Una skill deberia demostrar al menos una de estas mejoras:

- Reduce errores recurrentes.
- Produce un formato mas consistente.
- Ahorra pasos al agente.
- Usa mejor herramientas especificas.
- Maneja casos limite que el agente omitia.
- Mejora calidad sin inflar demasiado tokens o tiempo.

Tambien hay una advertencia importante: una skill que el agente ya resuelve bien sin ayuda no esta aportando suficiente valor. En ese caso, tal vez no hace falta crearla.

## Riesgos y limites

El formato es simple, pero no elimina riesgos.

El primer riesgo es la activacion incorrecta. Una descripcion demasiado generica mete instrucciones irrelevantes en tareas donde no corresponden. Una descripcion demasiado estrecha deja la skill sin usar. Esto se corrige con evals de trigger y near-misses.

El segundo riesgo es el exceso de contexto. Una skill larga, exhaustiva o llena de opciones compite con el resto de la tarea y puede empeorar el rendimiento. La web recomienda defaults claros, detalle moderado y referencias bajo demanda.

El tercer riesgo es la falsa autoridad. Si una skill se genera desde conocimiento generico, puede sonar razonable pero no capturar las convenciones reales del proyecto. Las mejores skills se extraen de tareas reales, runbooks, issues, code reviews, incidentes y artefactos existentes.

El cuarto riesgo es la fragilidad operativa. Scripts sin `--help`, comandos no versionados, dependencias no documentadas, prompts interactivos o salidas gigantes hacen que el agente pierda tiempo o se bloquee.

El quinto riesgo es la seguridad. Las skills de proyecto pueden venir de repositorios no confiables y contienen instrucciones que el agente podria obedecer. La guia de implementacion recomienda controles de confianza para cargar skills de proyecto, allowlists cuidadosas para recursos y diagnosticos visibles cuando algo no valida.

El sexto riesgo es la portabilidad aparente. El formato es abierto y muchos clientes lo soportan, pero cada cliente puede diferir en rutas de descubrimiento, activacion, observabilidad, permisos, carga de recursos y manejo de contexto. Para ensenar bien, hay que distinguir entre lo que pertenece al estandar (`SKILL.md`, frontmatter, estructura) y lo que depende del cliente.

## Ideas utiles para ensenar creacion de skills

Una skill pequena y buena suele responder a estas preguntas:

- Que tarea recurrente mejora?
- Que sabria una persona experta que el agente no sabe?
- Cuando debe activarse?
- Cuando no debe activarse?
- Que pasos son obligatorios?
- Que defaults debe elegir?
- Que errores concretos debe evitar?
- Que recurso externo debe cargar solo bajo condicion?
- Que puede validar antes de terminar?
- Como sabemos que funciona mejor que no tener skill?

Tambien conviene ensenar el ciclo de vida:

1. Resolver una tarea real con el agente.
2. Extraer el patron reusable.
3. Escribir una primera skill pequena.
4. Probar activacion con prompts positivos y near-misses.
5. Probar calidad contra baseline.
6. Leer trazas, no solo outputs.
7. Recortar, aclarar o mover contenido a scripts/references/assets.
8. Repetir hasta que el delta sea claro.

La version inicial no debe aspirar a cubrirlo todo. Debe capturar el 20% de conocimiento que evita el 80% de errores recurrentes.

## Implicaciones para nuestro curso

El curso deberia presentar las skills como una tecnica de empaquetado de criterio, no como otra forma de prompt largo. El mensaje principal: una skill sirve cuando hace que el agente actue mejor en una familia concreta de tareas gracias a conocimiento que no estaba en el modelo o no estaba disponible en contexto.

Deberiamos usar ejemplos pequenos desde el principio. El quickstart de dados es bueno para explicar mecanica, pero los ejercicios del curso deberian pasar pronto a casos con expertise real: convenciones de un repo, formato de entregable, validacion de datos, uso de una API interna o un flujo repetitivo de revision.

La descripcion debe tener un papel central. En el curso, cada skill deberia evaluarse con prompts que deben activarla y prompts cercanos que no deben hacerlo. Esto ensena que escribir una skill incluye disenar su frontera.

Progressive disclosure deberia ser una restriccion practica en todos los ejercicios. El alumnado deberia justificar que queda en `SKILL.md`, que se mueve a `references/`, que se convierte en `scripts/` y que se elimina por ser conocimiento generico.

La evaluacion debe aparecer temprano, aunque sea minima. Dos o tres casos con baseline bastan para cambiar la mentalidad: no se trata de que la skill exista, sino de que mejore algo observable. Las assertions simples, la revision humana y la lectura de trazas son suficientes para empezar.

Finalmente, conviene insistir en los limites: no toda tarea merece una skill, no toda instruccion mejora al agente y no todo contenido debe entrar en contexto. La habilidad clave que el curso deberia desarrollar es criterio de seleccion: crear skills pequenas, claras, activables, testeables y mantenibles.

