# Analisis de la guia de Anthropic sobre skills

Este documento sintetiza la guia local de Anthropic sobre construccion de skills, con foco en los principios de diseno que conviene trasladar a nuestro curso. No es un temario ni una reescritura de la guia: es una lectura tecnica orientada a decidir como ensenar a disenar, escribir, probar y mantener skills utiles.

## Idea central

Un skill es una carpeta que ensena a un agente a ejecutar una tarea o flujo de trabajo de forma consistente. Su valor no esta en "anadir informacion" sin mas, sino en convertir conocimiento repetible en instrucciones activables: criterios, pasos, validaciones, recursos, scripts y ejemplos que el agente pueda usar cuando el usuario pida un resultado concreto.

La guia insiste en una distincion importante:

- Las herramientas, MCPs o capacidades del entorno definen que puede hacer el agente.
- El skill define como debe hacerlo en un contexto determinado.

Esto cambia la forma de disenar. Un buen skill no deberia empezar por "que archivos meto", sino por "que resultado repetible quiero que el agente produzca mejor que con prompting ad hoc".

## Principios de diseno de skills

### 1. Empezar por casos de uso concretos

Anthropic recomienda identificar 2 o 3 casos de uso antes de escribir codigo o instrucciones. Esto evita skills genericos, dificiles de activar y de evaluar.

Un caso de uso bien definido deberia incluir:

- Que quiere conseguir el usuario.
- Que frases o situaciones deberian activar el skill.
- Que pasos requiere el flujo.
- Que herramientas, APIs, MCPs o capacidades locales intervienen.
- Que conocimiento experto debe quedar embebido.
- Cual es el resultado observable al final.

La consecuencia practica es clara: si no se puede describir el flujo en terminos de entrada, proceso y resultado, todavia no hay suficiente diseno para escribir el skill.

### 2. Disenar para activacion, no para documentacion

El frontmatter YAML no es metadata decorativa. Es el primer filtro de activacion. Claude lo usa para decidir si debe cargar el skill sin leer todavia el cuerpo completo.

Por eso la descripcion debe contener dos cosas:

- Que hace el skill.
- Cuando debe usarse, con disparadores concretos.

Una descripcion como "ayuda con proyectos" fracasa porque no delimita ni tarea ni contexto. Una descripcion efectiva menciona acciones, frases de usuario, tipos de archivo, servicios o dominios relevantes.

### 3. Progressive disclosure como arquitectura

La guia presenta los skills como un sistema de tres niveles:

1. Frontmatter YAML: siempre disponible para decidir si el skill aplica.
2. Cuerpo de `SKILL.md`: instrucciones principales, cargadas solo cuando el skill es relevante.
3. Archivos enlazados: referencias, scripts, plantillas o assets que se consultan solo si hacen falta.

Este modelo es clave porque protege el contexto. Un skill que mete todo en `SKILL.md` puede funcionar en ejemplos pequenos, pero escala mal: consume tokens, degrada respuestas y hace que las instrucciones importantes queden enterradas.

La regla practica seria:

- `SKILL.md` contiene el procedimiento esencial.
- `references/` contiene documentacion extensa, tablas, APIs, criterios detallados o ejemplos largos.
- `scripts/` contiene operaciones deterministas o validaciones que no conviene dejar al lenguaje natural.
- `assets/` contiene materiales reutilizables para generar salidas consistentes.

### 4. Composabilidad

Claude puede cargar varios skills a la vez. Por tanto, un skill no debe asumir que es el centro del sistema ni duplicar responsabilidades de otros skills.

Esto obliga a delimitar:

- Que problemas cubre.
- Que problemas no cubre.
- Cuando debe deferir a otro skill o herramienta.
- Que dependencias tiene.

Las descripciones demasiado amplias provocan sobre-activacion. Las instrucciones demasiado totalizantes dificultan que el agente combine capacidades.

### 5. Portabilidad con realismo

La guia plantea que los skills deben funcionar de forma portable entre Claude.ai, Claude Code y API, siempre que el entorno soporte las dependencias necesarias. Esto no significa evitar dependencias, sino declararlas y aislarlas.

Buenas implicaciones:

- Usar nombres y estructura estandar.
- Evitar supuestos invisibles sobre rutas, credenciales o entorno.
- Documentar requisitos en `compatibility` o en las instrucciones.
- Mantener scripts y referencias dentro de la carpeta del skill cuando sea posible.

## Anatomia de un `SKILL.md`

La estructura minima es:

```yaml
---
name: nombre-del-skill
description: Que hace y cuando usarlo, con disparadores concretos.
---
```

Despues del frontmatter, el cuerpo debe contener las instrucciones operativas.

Una estructura razonable incluye:

- Titulo del skill.
- Instrucciones principales.
- Pasos del flujo.
- Ejemplos de uso.
- Criterios de calidad.
- Manejo de errores.
- Enlaces a referencias internas.

La guia subraya que el `name` debe ser kebab-case, coincidir idealmente con la carpeta, no contener espacios ni mayusculas, y no usar nombres reservados relacionados con Claude o Anthropic.

La `description` debe ser breve, especifica y accionable. No deberia contener XML ni marcas que puedan interpretarse como inyeccion de instrucciones.

## Buenas practicas

### Instrucciones especificas y accionables

Una mala instruccion dice: "valida los datos antes de continuar".

Una buena instruccion dice que comando ejecutar, que archivo revisar, que condiciones validar y que hacer si falla. Cuanto mas critica sea una accion, menos deberia depender de una interpretacion vaga.

### Validaciones explicitas

Los flujos importantes deben incluir gates de validacion:

- Antes de llamar una API.
- Despues de generar una salida.
- Antes de finalizar un documento, codigo o cambio externo.
- Al detectar errores comunes.

Cuando una validacion sea mecanica, conviene convertirla en script. La guia lo formula de manera directa: el codigo es mas determinista que la interpretacion del lenguaje natural.

### Ejemplos representativos

Los ejemplos ayudan a fijar el comportamiento esperado. No deben ser decorativos, sino cubrir escenarios comunes, parametros esperados y resultado final.

Un buen ejemplo conecta:

- Frase del usuario.
- Acciones del agente.
- Herramientas o recursos usados.
- Resultado verificable.

### Troubleshooting integrado

El skill debe anticipar errores frecuentes: frontmatter invalido, problemas de conexion MCP, credenciales, permisos, nombres de herramientas, formatos de archivo o fallos de validacion.

Esto reduce la necesidad de que el usuario reprograme el flujo mediante prompts correctivos.

### Mantener `SKILL.md` enfocado

La guia recomienda mover detalle excesivo a `references/` y mantener el archivo principal por debajo de un tamano razonable. Un limite orientativo citado es menos de 5.000 palabras.

El objetivo no es brevedad por estetica, sino prioridad atencional: las instrucciones criticas deben aparecer pronto y ser faciles de seguir.

## Malas practicas

### Descripciones vagas

Problemas tipicos:

- "Ayuda con documentos".
- "Gestiona proyectos".
- "Automatiza procesos".

Estas descripciones no dan al modelo una condicion clara de activacion.

### Falta de disparadores

Un skill puede explicar bien lo que hace y aun asi no activarse si no incluye frases, situaciones o archivos que el usuario realmente mencionaria.

### Scope demasiado amplio

Un skill que pretende cubrir "analisis de datos", "documentacion", "gestion de proyectos" y "automatizacion" acabara compitiendo con otros skills y sera dificil de probar.

La guia recomienda aclarar tambien usos negativos cuando haya riesgo de sobre-activacion.

### Instrucciones enterradas

Si una validacion critica aparece al final de un documento largo, es probable que el agente la siga de forma inconsistente. Las reglas importantes deben ir arriba, con lenguaje directo.

### Demasiado contexto inline

Pegar manuales completos en `SKILL.md` rompe el principio de progressive disclosure. Las referencias largas deben vivir en archivos separados y ser consultadas bajo demanda.

### Confiar en el skill para arreglar un MCP roto

Si una llamada MCP falla porque el servidor no esta conectado, las credenciales expiraron o los nombres de herramientas son incorrectos, el problema no es del skill. La guia recomienda probar el MCP independientemente para aislar la causa.

## Como disenar un skill antes de escribirlo

Un proceso de diseno practico podria ser:

1. Elegir un resultado repetible.
2. Escribir 2 o 3 casos de uso concretos.
3. Definir disparadores de activacion y no activacion.
4. Mapear el flujo paso a paso.
5. Identificar herramientas, MCPs, scripts y recursos necesarios.
6. Definir criterios de exito.
7. Decidir que va en `SKILL.md`, `references/`, `scripts/` y `assets/`.
8. Probar primero una tarea dificil en conversacion normal.
9. Extraer la estrategia ganadora al skill.
10. Iterar con pruebas de activacion, funcionamiento y comparacion con baseline.

Este punto es especialmente importante para el curso: no deberiamos ensenar a escribir `SKILL.md` como primer paso. Antes hay que ensenar a descubrir el flujo.

## Limites de scope

La guia distingue entre enfoques problem-first y tool-first.

En un enfoque problem-first, el usuario expresa un resultado: "prepara el sprint", "crea el onboarding", "genera el informe". El skill decide que herramientas usar y en que orden.

En un enfoque tool-first, el usuario ya tiene una herramienta o MCP conectado y necesita buenas practicas: "usa Notion para estructurar este workspace", "usa Linear para convertir esto en tickets".

Ambos enfoques son validos, pero mezclarlos sin criterio ensancha demasiado el scope. Un skill deberia declarar implicitamente desde su descripcion si resuelve un problema completo o si ensena a usar mejor una herramienta concreta.

Un buen limite de scope permite responder:

- Que activa el skill.
- Que no deberia activarlo.
- Que parte del flujo queda fuera.
- Que dependencias externas son necesarias.
- Que errores puede manejar y cuales debe reportar.

## Recursos, scripts y assets

### `references/`

Debe usarse para conocimiento extenso o consultable:

- Guias de API.
- Patrones de consulta.
- Matrices de decision.
- Reglas de negocio.
- Ejemplos largos.
- Criterios editoriales o de calidad.

El `SKILL.md` debe enlazar estas referencias con instrucciones claras sobre cuando leerlas.

### `scripts/`

Debe usarse cuando una operacion sea mejor expresada como codigo:

- Validar formatos.
- Transformar datos.
- Generar archivos.
- Comprobar consistencia.
- Ejecutar checks repetibles.

Los scripts aumentan fiabilidad si tienen entradas y salidas claras. Tambien reducen ambiguedad en tareas donde el lenguaje natural tiende a producir variaciones.

### `assets/`

Debe usarse para materiales reutilizables:

- Plantillas.
- Fuentes.
- Iconos.
- Ejemplos base.
- Archivos de configuracion.

Los assets son utiles cuando el skill produce salidas que deben mantener identidad visual, estructura o formato.

## Evaluacion e iteracion

La guia propone tres tipos de prueba.

### 1. Pruebas de activacion

Comprueban si el skill se carga cuando debe y no se carga cuando no debe.

Debe probarse con:

- Peticiones obvias.
- Parafrasis.
- Casos limite.
- Peticiones no relacionadas.

La descripcion se ajusta segun senales de undertriggering o overtriggering.

### 2. Pruebas funcionales

Comprueban si el skill ejecuta correctamente el flujo:

- Salidas validas.
- Llamadas API correctas.
- Manejo de errores.
- Edge cases.
- Consistencia entre ejecuciones.

Estas pruebas deben estar ligadas a los casos de uso iniciales. Si no se puede probar, probablemente el caso de uso esta mal definido.

### 3. Comparacion con baseline

La pregunta no es solo "funciona", sino "mejora el resultado frente a no tener skill".

Metricas sugeridas:

- Menos mensajes de ida y vuelta.
- Menos llamadas fallidas.
- Menos tokens.
- Menos correcciones del usuario.
- Mayor consistencia estructural.
- Primera ejecucion exitosa para usuarios nuevos.

La guia reconoce que parte de la evaluacion sera cualitativa, pero aun asi pide criterios observables.

## Patrones utiles

### Orquestacion secuencial

Adecuada cuando el orden importa: crear entidad, validar, usar ID resultante, ejecutar siguiente paso, confirmar. Requiere dependencias claras y manejo de rollback o fallo.

### Coordinacion multi-MCP

Adecuada cuando un flujo cruza servicios: diseno, almacenamiento, tickets, notificaciones. Requiere fases separadas y paso explicito de datos entre herramientas.

### Refinamiento iterativo

Adecuada para outputs de calidad: informes, documentos, interfaces, analisis. Requiere criterios de calidad, loops de revision y una condicion de parada.

### Seleccion contextual de herramientas

Adecuada cuando hay varias formas de conseguir el mismo resultado. El skill debe incluir reglas de decision y explicar brevemente por que elige una ruta.

### Inteligencia de dominio

Adecuada cuando el valor esta en reglas especializadas: compliance, metodologia interna, estilo editorial, arquitectura, investigacion. Aqui el skill no solo automatiza; aplica juicio estructurado.

## Implicaciones para nuestro curso

El curso deberia ensenar skills como diseno de sistemas de trabajo para agentes, no como una plantilla Markdown.

Puntos que conviene incorporar:

- Empezar cada skill desde casos de uso y criterios de exito.
- Separar activacion, instrucciones y recursos usando progressive disclosure.
- Tratar la descripcion YAML como una pieza critica de diseno.
- Ensenar explicitamente undertriggering y overtriggering.
- Practicar delimitacion de scope antes de escribir.
- Incluir patrones de arquitectura de skill: secuencial, multi-herramienta, iterativo, decision tree y dominio experto.
- Usar scripts cuando la validacion o transformacion de datos deba ser determinista.
- Usar `references/` para documentacion pesada y evitar `SKILL.md` enciclopedicos.
- Evaluar skills comparandolos con un baseline sin skill.
- Iterar a partir de fallos reales, no solo de checklist estatica.

Una buena progresion didactica seria que el estudiante primero haga funcionar manualmente un flujo dificil, luego extraiga el patron, despues lo convierta en skill y finalmente lo pruebe contra disparadores, casos funcionales y baseline.

La idea mas importante para transmitir: un skill efectivo no es "mas contexto"; es contexto organizado para activarse en el momento correcto, guiar un flujo concreto y producir resultados verificables con menos intervencion del usuario.
