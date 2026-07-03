# Sistema de cursos por terminos

Este repositorio no esta organizado como una carpeta plana de documentos. Esta pensado como un sistema escalable para crear cursos didacticos sobre terminos de IA generativa.

La regla principal es:

> `doc/` contiene el sistema comun. Cada termino vive en su propio modulo.

## Estructura

```text
doc/
+-- README.md
+-- 00-sistema/
|   +-- 01-framework-modulo.md
|   +-- 02-plantilla-nuevo-termino.md
+-- modulos/
    +-- skills/
        +-- README.md
        +-- 00-fuentes/
        |   +-- 01-agentskills.md
        |   +-- 02-guia-anthropic.md
        |   +-- 03-transcripcion-how-to-write-great-skills.md
        +-- 01-fundamentos.md
        +-- 02-syllabus.md
        +-- 03-lecciones.md
```

## Como se usa

Para leer el curso de skills:

1. Empieza por `modulos/skills/README.md`.
2. Lee `01-fundamentos.md` para entender el concepto.
3. Sigue `02-syllabus.md` para ver el mapa del curso.
4. Trabaja `03-lecciones.md` como documento principal.

Para crear un nuevo termino:

1. Lee `00-sistema/01-framework-modulo.md`.
2. Copia la estructura propuesta en `00-sistema/02-plantilla-nuevo-termino.md`.
3. Crea un nuevo directorio en `doc/modulos/<termino>/`.
4. Mantiene las fuentes, fundamentos, syllabus y lecciones dentro de ese modulo.

## Convencion de modulos

Cada modulo debe responder a cuatro capas:

- Fuentes: de donde sale el criterio.
- Fundamentos: que es el termino, donde vive, de que se compone y que errores conceptuales evita.
- Syllabus: como se aprende en bloques.
- Lecciones: como se construye paso a paso un ejemplo pequeno, claro y evaluable.

El modulo no debe ser una coleccion de plantillas. Debe sentirse como un proceso humano de aprendizaje: problema, scope, casos de uso, diseno, instrucciones, recursos, evaluacion e iteracion.
