# Plantilla para crear un nuevo modulo

Usa esta plantilla cuando quieras crear un curso para otro termino.

Reemplaza `<termino>` por un slug corto en minusculas, por ejemplo:

- `agents`
- `evals`
- `context-engineering`
- `memory`
- `workflows`

## Estructura

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

## README.md

```markdown
# <Nombre del termino>

Este modulo ensena a entender y aplicar `<termino>` en sistemas de IA generativa.

## Que vas a aprender

- ...
- ...
- ...

## Ejemplo del modulo

Construiremos ...

## Orden de lectura

1. `01-fundamentos.md`
2. `02-syllabus.md`
3. `03-lecciones.md`

## Que queda fuera

- ...
- ...
```

## 00-fuentes/01-fuente-principal.md

```markdown
# Analisis de fuente: <nombre>

## Tesis de la fuente

...

## Ideas utiles para el curso

- ...
- ...

## Riesgos o malentendidos

- ...
- ...

## Decisiones pedagogicas

- ...
- ...

## Donde se usa en el modulo

- `01-fundamentos.md`: ...
- `02-syllabus.md`: ...
- `03-lecciones.md`: ...
```

## 01-fundamentos.md

```markdown
# Fundamentos de <termino>

## Que es

...

## Donde vive en un sistema

...

## Elementos que lo componen

- ...
- ...

## Piezas obligatorias

- ...
- ...

## Piezas opcionales

- ...
- ...

## Errores frecuentes

- ...
- ...

## Vocabulario minimo

- ...
- ...
```

## 02-syllabus.md

```markdown
# Syllabus: <termino>

## Bloque 0. Fundamentos

Que estamos haciendo:

Por que importa:

Ejemplo:

Plantilla:

Entregable:

## Bloque 1. Problema y scope

Que estamos haciendo:

Por que importa:

Ejemplo:

Plantilla:

Entregable:
```

## 03-lecciones.md

```markdown
# Lecciones: construir <ejemplo>

## Leccion 1. Entender el problema

### Objetivo

...

### Por que importa

...

### Ejemplo trabajado

...

### Plantilla

...

### Resultado acumulado

...

### Criterio de calidad

...
```
