# Framework para crear un modulo didactico

Este framework sirve para repetir el metodo con mas terminos sin convertir `doc/` en un cajon de documentos.

Un modulo didactico no empieza escribiendo lecciones. Empieza definiendo que tiene que entender una persona para usar bien el termino.

## Principio

> Primero se entiende el concepto. Despues se decide el scope. Despues se construye algo pequeno. Finalmente se evalua.

Este orden evita cursos que parecen completos pero no ensenan a pensar.

## Estructura obligatoria de cada modulo

```text
doc/modulos/<termino>/
+-- README.md
+-- 00-fuentes/
|   +-- 01-fuente-principal.md
|   +-- 02-fuente-secundaria.md
|   +-- 03-fuente-practica.md
+-- 01-fundamentos.md
+-- 02-syllabus.md
+-- 03-lecciones.md
```

Puede haber mas archivos, pero estos son el minimo estable.

## Contrato de cada archivo

### `README.md`

Sirve como puerta de entrada del modulo.

Debe incluir:

- Que aprende la persona.
- Que ejemplo se construye.
- En que orden leer los documentos.
- Que queda fuera del modulo.

### `00-fuentes/`

Contiene el analisis de fuentes. No es un volcado de informacion.

Cada analisis debe incluir:

- Tesis de la fuente.
- Ideas utiles para el curso.
- Riesgos o malentendidos.
- Decisiones pedagogicas que se extraen.
- Que parte del modulo justifica esa fuente.

### `01-fundamentos.md`

Explica el concepto antes de construir nada.

Debe responder:

- Que es.
- Donde vive en un sistema real.
- De que elementos se compone.
- Que campos o piezas son obligatorias.
- Que piezas son opcionales.
- Que errores conceptuales son frecuentes.
- Que vocabulario minimo necesita el alumno.

### `02-syllabus.md`

Organiza el aprendizaje por bloques.

Cada bloque debe responder:

- Que estamos haciendo.
- Por que importa.
- Ejemplo.
- Plantilla.
- Entregable que queda.

### `03-lecciones.md`

Es el documento principal del curso.

Cada leccion debe producir algo concreto. No debe limitarse a explicar teoria.

Cada leccion debe incluir:

- Objetivo de la leccion.
- Por que importa.
- Ejemplo trabajado.
- Plantilla reutilizable.
- Resultado acumulado.
- Criterio de calidad.

## Secuencia pedagogica recomendada

1. Definir el problema que el termino ayuda a resolver.
2. Explicar la anatomia del termino.
3. Elegir un scope pequeno.
4. Definir casos de uso y no uso.
5. Escribir la primera version.
6. Separar conocimiento, recursos o automatizaciones si aplica.
7. Evaluar activacion, calidad y limites.
8. Podar o dividir si el modulo empieza a crecer demasiado.

## Checklist de calidad del modulo

- [ ] El modulo tiene una pregunta central clara.
- [ ] El ejemplo no intenta resolver un proceso enorme de principio a fin.
- [ ] Las fuentes estan analizadas, no resumidas sin criterio.
- [ ] El syllabus muestra una progresion real.
- [ ] Las lecciones producen entregables acumulativos.
- [ ] Las plantillas aparecen dentro del aprendizaje, no como anexos sueltos.
- [ ] Hay evals minimos.
- [ ] Hay una seccion de errores frecuentes.
- [ ] El modulo explica que queda fuera.
- [ ] El modulo puede copiarse como patron para otro termino.

## Senal de que el modulo esta mal planteado

Un modulo esta creciendo mal si:

- Tiene muchas definiciones pero ningun ejemplo construido.
- Tiene plantillas sin explicar cuando usarlas.
- Mezcla varios terminos que merecen modulos propios.
- Promete automatizar un proceso completo cuando solo deberia ensenar una fase.
- No tiene evals.
- No distingue entre fuente, interpretacion pedagogica y entregable.
