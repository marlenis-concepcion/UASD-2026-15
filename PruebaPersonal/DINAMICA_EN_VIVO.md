# Dinámica en vivo: transformar un programa con agentes docentes

## Propósito

Demostrar que un docente puede entregar el programa real de una asignatura y utilizar agentes de IA para diagnosticarlo, investigarlo, actualizarlo, diseñar una unidad, crear evaluaciones y preparar retroalimentación, manteniendo al docente **human in the loop**.

## Invitación al grupo

> ¿Quién desea levantar la mano y compartir en el grupo el programa de una asignatura que imparte? Trabajaremos con ese documento para mostrar cómo la IA puede simplificar tareas reales del día a día docente. No buscamos que la IA decida por usted: los agentes prepararán propuestas y usted validará cada paso.

## Requisitos del documento

- Programa o syllabus en PDF, DOCX o texto legible.
- Sin nombres, matrículas, calificaciones ni datos personales de estudiantes.
- Preferiblemente una asignatura que el docente conozca bien.
- Debe contener, si están disponibles: competencias, objetivos, contenidos, metodología, evaluación, créditos y bibliografía.

## Selección del caso

Elegir un programa que:

1. Sea comprensible para un grupo multidisciplinario.
2. Tenga al menos una unidad que pueda trabajarse durante la demostración.
3. Presente una necesidad concreta: contenido desactualizado, evaluación débil, actividades poco auténticas o carga excesiva de corrección.
4. Permita que el docente propietario valide inmediatamente las propuestas.

Si nadie comparte un documento o surge un problema técnico, utilizar uno de los programas de programación guardados en `fwdprogramasasignaturasdeinformatica/`.

Antes de comenzar, crear un caso independiente en `../TrabajoDocentes/AAAA-MM-DD_asignatura_docente/`. Copiar allí la fuente y guardar todos los resultados en sus subcarpetas. No modificar `agentes/` durante la demostración.

## Preguntas iniciales al docente voluntario

1. ¿Qué asignatura y carrera es?
2. ¿A qué nivel y cantidad aproximada de estudiantes se dirige?
3. ¿La docencia es presencial, virtual o híbrida?
4. ¿Qué parte del programa desea mejorar?
5. ¿Cuál tarea le consume más tiempo actualmente?
6. ¿La asignatura es teórica, teórico-práctica o exclusivamente práctica?
7. ¿Qué debe ser capaz de hacer el estudiante al terminar la unidad?

## Recorrido de agentes para la demostración

No es necesario ejecutar los 17 agentes. Se mostrará una cadena corta y comprensible:

### 1. Coordinador y analista

- Identifican Escuela, Cátedra, créditos, modalidad y tipo de asignatura.
- Extraen competencias, contenidos, evaluación y vacíos.
- Separan hechos del programa, datos faltantes y propuestas.

**Validación:** preguntar al docente si el análisis representa correctamente su asignatura.

### 2. Agente de diagnóstico

- Crea entre 5 y 8 preguntas diagnósticas.
- Distribuye preguntas en varios niveles de Bloom.
- Indica cómo los resultados modificarían el primer ciclo de enseñanza.

**Validación:** el docente elimina, corrige o aprueba las preguntas.

### 3. Investigador y actualizador curricular

- Identifican un contenido que requiera actualización.
- Proponen qué mantener, modificar, incorporar o eliminar.
- Presentan fuente, vigencia y justificación.

**Validación:** aclarar que una propuesta no modifica el programa oficial; debe seguir el proceso de Cátedra y Escuela.

### 4. Agente de resultados y actividades

- Formula uno o dos resultados observables con Taxonomía de Bloom.
- Crea una actividad de aula invertida: antes, durante y después.
- Define evidencia, duración, recursos y uso permitido de IA.

**Validación:** el docente comprueba viabilidad y pertinencia disciplinar.

### 5. Agente de evaluación

- Clasifica la asignatura según el esquema UASD aplicable.
- Diseña un instrumento breve y una rúbrica.
- Comprueba alineación con el resultado y la actividad.

**Validación:** el docente aprueba los criterios y ponderaciones antes de usarlos.

### 6. Agentes de calificación y retroalimentación

- Utilizan una entrega ficticia o anonimizada.
- Identifican evidencia por criterio y proponen una valoración.
- Preparan fortalezas, mejora prioritaria y próximo paso.

**Validación:** el docente confirma la calificación; el agente no modifica registros oficiales.

## Prompt de apertura

```text
Actúa como agente coordinador docente de la UASD. Analiza el programa adjunto
sin modificarlo. Identifica Facultad o área, Escuela o unidad académica,
asignatura, créditos, modalidad, tipo de asignatura, competencias, resultados,
contenidos, metodología y sistema de evaluación.

Separa la respuesta en:
1. Información explícita del documento.
2. Información faltante que debe responder el docente.
3. Posibles oportunidades de mejora, marcadas únicamente como propuestas.
4. Reglas UASD que deben verificarse antes de continuar.

No inventes datos. Cita la página o sección del programa que sustenta cada
hallazgo y detente para solicitar validación docente.
```

## Cierre con el grupo

Preguntar:

> Después de observar el proceso, ¿qué tarea de su trabajo cotidiano delegaría primero a un agente: investigar, actualizar contenidos, crear actividades, diseñar evaluaciones, revisar rúbricas o preparar retroalimentación?

La conclusión debe ser:

> La IA hace el trabajo operativo y repetitivo; el docente aporta contexto, criterio y decisión. Eso es human in the loop.
