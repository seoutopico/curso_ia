# Analisis de la transcripcion: How to write great skills

La charla propone una rubrica practica para distinguir skills utiles de skills que solo agregan ruido. El problema de fondo no es la falta de skills, sino la falta de criterios para evaluarlas, mantenerlas y convertir procedimientos humanos en instrucciones que un agente pueda ejecutar de forma consistente.

El framework que aparece en la transcripcion se organiza en cuatro decisiones: trigger, estructura, steering y pruning. No son fases decorativas; cada una controla un tipo distinto de coste. El trigger decide quien carga la skill y cuando. La estructura decide que entra en el `SKILL.md` principal y que queda como referencia externa. El steering decide como se empuja realmente la conducta del agente. El pruning elimina texto que no cambia comportamiento.

## 1. Trigger: model-invoked vs user-invoked

La primera decision de diseno es si la skill debe ser invocada por el modelo o por el usuario.

Una skill model-invoked expone su descripcion al contexto del agente. Esa descripcion funciona como un puntero: el modelo puede leerla, decidir que aplica y cargar el `SKILL.md`. Esto reduce la carga cognitiva del usuario, porque no necesita recordar manualmente que skill usar. El coste es doble: consume contexto en cada turno y aumenta la imprevisibilidad, porque el modelo puede no invocarla aunque sea relevante, o invocarla cuando no conviene.

Una skill user-invoked no se expone como candidato automatico. El usuario la llama explicitamente. Esto mantiene bajo el context load del agente y elimina una clase de fallos de routing automatico, pero transfiere trabajo al usuario: debe conocer el inventario de skills y saber cuando aplicar cada una.

La transcripcion no defiende una opcion universal. La decision depende del equilibrio entre dos cargas:

- Context load: tokens y atencion del agente consumidos por descripciones siempre presentes.
- Cognitive load: memoria y criterio que se exige al usuario para elegir la skill correcta.

Una organizacion que instale muchas skills model-invoked puede degradar la calidad global del agente aunque cada skill parezca buena por separado. Una coleccion puramente user-invoked puede ser potente para usuarios expertos, pero opaca para usuarios nuevos. El diseno del trigger debe tratarse como una decision de producto, no como una preferencia tecnica menor.

## 2. Estructura: steps y reference

La charla reduce la estructura interna de una skill a dos unidades principales:

- Steps: el procedimiento que el agente debe seguir.
- Reference: informacion de apoyo que ayuda a ejecutar esos pasos.

Esta distincion es importante porque evita que el `SKILL.md` se convierta en un documento mixto donde instrucciones, plantillas, definiciones y contexto de fondo compiten por la misma atencion.

Una skill puede ser casi todo procedimiento, como una lista corta de pasos. Tambien puede ser casi toda referencia, si su funcion principal es proporcionar conocimiento especializado. Pero cuando ambas cosas aparecen, conviene separarlas explicitamente: los pasos deben decir que hacer; la referencia debe aportar material cuando ese paso lo necesite.

El criterio clave es mantener el `SKILL.md` principal pequeno. No por estetica, sino porque todo lo que entra ahi se carga cuando la skill se invoca. Si una plantilla, definicion o guia solo se usa en una rama concreta, debe moverse a un archivo de referencia externo y dejar en el `SKILL.md` un puntero claro del tipo: "si necesitas actualizar X, lee Y".

Esto introduce una forma simple de analizar una skill:

1. Identificar sus ramas reales de uso.
2. Preguntar que referencia se necesita siempre.
3. Sacar fuera lo que solo se necesita en algunas ramas.
4. Dejar en el `SKILL.md` solo los pasos y referencias inevitables.

La consecuencia es que una skill no se estructura por "todo lo que sabemos sobre el tema", sino por flujo de ejecucion.

## 3. Steering: leading words y comportamiento observable

La parte mas importante de steering es el uso de leading words: terminos compactos que arrastran mucho significado operativo. El ejemplo central es "vertical slice". En vez de explicar largamente que el agente no debe construir capa por capa, se usa una expresion conocida que concentra una manera de trabajar: entregar una porcion funcional atravesando capas.

El valor de un leading word no esta en sonar bien, sino en modificar conducta. Una buena palabra guia cumple varias condiciones:

- Es breve.
- Activa conocimiento previo del modelo.
- Se puede repetir de forma consistente dentro de la skill.
- Aparece luego en el razonamiento, planes o salidas del agente.
- Cambia decisiones practicas, no solo el tono.

Esto convierte el steering en algo verificable. Si la skill usa "vertical slice" pero el agente sigue proponiendo implementar base de datos, API y frontend por separado, el leading word no esta funcionando o no esta suficientemente anclado. Si el agente empieza a repetirlo y sus planes cambian, la palabra esta haciendo trabajo real.

La leccion mas amplia es que muchas instrucciones largas pueden reemplazarse por vocabulario preciso. El ingles, como dice la charla, funciona como una API amplia: escoger bien una expresion puede ser mas eficaz que anadir parrafos de prohibiciones.

## 4. Leg work: cuando dividir skills grandes

Otro problema de steering aparece cuando el agente hace poco trabajo en una fase porque ya ve el objetivo final. El ejemplo de la transcripcion es el plan mode: si el flujo completo dice "pregunta aclaraciones y luego crea un plan", el agente tiende a hacer pocas preguntas y saltar rapido al plan, porque interpreta que el plan es la meta principal.

La solucion propuesta es ocultar el futuro cuando una fase necesita mas esfuerzo propio. En vez de una skill grande con todos los pasos, se divide el proceso en skills separadas: por ejemplo, una skill dedicada a interrogar el problema y otra posterior para redactar el PRD. Asi el agente solo ve la fase actual y no optimiza prematuramente hacia la salida final.

Este criterio es mas importante que una regla general de "skills pequenas siempre". Hay que dividir cuando una fase necesita leg work adicional: exploracion del codigo, preguntas, investigacion, comparacion de alternativas, lectura de documentos o validacion con el usuario. Si el agente salta demasiado rapido, probablemente ve demasiada meta futura.

## 5. Pruning: no-ops, sediment y DRY

La poda no es una fase cosmetica. Es el mecanismo que evita que las skills se conviertan en documentacion acumulativa sin fuerza operativa.

La charla identifica tres fallos recurrentes:

- DRY roto: la misma definicion, plantilla o criterio aparece en varios lugares. Esto aumenta mantenimiento y crea contradicciones. Cada pieza debe tener una sola fuente de verdad.
- Sediment: acumulacion de material historico, aportes de varias personas, notas obsoletas o secciones que nadie se atreve a borrar. El resultado es un `SKILL.md` largo, con material no ramificado ni jerarquizado.
- No-ops: texto que parece instruccion, pero no cambia el comportamiento del agente. Si al borrar un parrafo la salida seria igual, ese parrafo probablemente no pertenece a la skill.

El test de eliminacion es central: preguntarse que pasaria si una frase, parrafo o seccion desapareciera. Si el agente seguiria actuando igual, ese texto consume contexto sin aportar control. En una buena skill, cada parte debe orientar una decision, activar una referencia, imponer una secuencia o modificar el estandar de salida.

Pruning tambien implica detectar material que no pertenece al `SKILL.md` principal aunque sea valioso. Algo puede no ser basura y aun asi estar en el lugar equivocado. Si solo aplica a una rama, debe vivir como referencia externa.

## 6. Lectura critica del framework

El framework es util porque no evalua una skill por su completitud documental, sino por su comportamiento bajo carga. Una skill buena no es la que explica mas, sino la que ayuda al agente a actuar mejor con menos contexto.

Tambien desplaza el foco desde "prompt engineering" hacia "sistema operativo de trabajo". Las skills son procedimientos empaquetados: tienen routing, memoria externa, instrucciones de ejecucion, referencias y criterios de mantenimiento. Por eso los problemas se parecen mas a arquitectura de informacion que a redaccion aislada de prompts.

La tension mas importante es esta: cargar mas contexto puede hacer que una skill parezca mas completa, pero tambien puede empeorar el rendimiento del agente. La skill excelente no maximiza informacion; maximiza informacion relevante en el momento adecuado.

## Implicaciones para nuestro curso

El curso deberia ensenar a evaluar y disenar skills con una rubrica pequena y repetible, no como una coleccion de trucos. El nucleo deberia ser: decidir el trigger, separar steps/reference, usar leading words, exigir leg work cuando haga falta y podar agresivamente.

Para los ejercicios, conviene trabajar sobre skills existentes y pedir a los alumnos que hagan diagnostico:

- Que parte aumenta context load sin aportar comportamiento.
- Que parte aumenta cognitive load del usuario.
- Que referencias deberian salir del `SKILL.md`.
- Que leading words gobiernan la conducta.
- Que pasos necesitan mas leg work.
- Que secciones son no-ops o sediment.

Tambien conviene evitar que el curso derive hacia un catalogo de skills. El objetivo no es "tener muchas skills", sino saber cuando una skill merece existir, cuando debe dividirse, cuando debe ser user-invoked, cuando debe ser model-invoked y cuando debe borrarse.

Una buena practica para el curso seria introducir una plantilla minima de revision:

1. Trigger: quien debe invocarla y que carga impone.
2. Structure: que pasos hay y que referencias se cargan siempre.
3. Steering: que leading words cambian conducta.
4. Leg work: que fases requieren foco aislado.
5. Pruning: que texto se puede eliminar, mover o deduplicar.

Con esa plantilla, el curso puede mantenerse practico y diferenciarse de un syllabus general sobre agentes. La promesa no seria "aprende a escribir skills", sino "aprende a reducir skills hasta que cada palabra haga trabajo".
