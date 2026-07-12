# Sistema de agentes docentes

Este directorio organiza las tareas docentes como agentes especializados. Cada agente recibe entradas verificables, ejecuta una función delimitada y entrega un producto al siguiente.

## Flujo principal

`Asignación → diagnóstico → investigación → actualización → resultados de aprendizaje → planificación → actividades → recursos → evaluación → calificación → retroalimentación → seguimiento → mejora`

## Agentes

1. `00_coordinador`: organiza el flujo y los puntos de aprobación.
2. `01_analista_asignacion`: interpreta el encargo, programa y contexto.
3. `02_diagnostico`: diseña y analiza la prueba diagnóstica.
4. `03_investigacion`: busca y verifica fuentes pertinentes.
5. `04_actualizacion_curricular`: propone cambios sustentados al contenido.
6. `05_resultados_bloom`: formula resultados observables y medibles.
7. `06_planificacion_unidad`: estructura la unidad y sus ciclos.
8. `07_diseno_actividades`: crea actividades de aula invertida.
9. `08_recursos_didacticos`: produce materiales y variantes.
10. `09_evaluacion_instrumentos`: diseña pruebas, rúbricas y listas de cotejo.
11. `10_calificacion_rubricas`: contrasta evidencias con criterios aprobados.
12. `11_retroalimentacion`: genera feedback y feedforward accionable.
13. `12_tutoria_seguimiento`: detecta necesidades y organiza apoyos.
14. `13_inclusion_accesibilidad`: revisa barreras y adaptaciones.
15. `14_integridad_etica_ia`: protege autoría, privacidad y uso responsable.
16. `15_analitica_mejora_agile`: facilita revisión, retrospectiva y mejora.
17. `16_comunicacion_docente`: prepara instrucciones, anuncios y recordatorios.

Todos los agentes deben cumplir el contrato de `_comun/CONTRATO_AGENTES.md` y el marco de `../METODOLOGIA.md`.

## Base normativa UASD

Los agentes también deben aplicar `_comun/MATRIZ_NORMATIVA_UASD.md`, elaborada a partir del Estatuto Orgánico, el Reglamento de Rendimiento Académico Estudiantil y el Reglamento de Carrera Académica.

Cada salida debe indicar si contiene:

- una obligación normativa;
- una decisión de Cátedra, Escuela o Facultad pendiente de comprobar;
- una recomendación pedagógica; o
- una propuesta generada por IA pendiente de validación docente.

## Estado protegido

Esta carpeta queda congelada. No debe modificarse por solicitudes relacionadas con programas, clases o unidades concretas. Cada caso nuevo se desarrolla en `../06_Trabajo_Docentes/`, conforme a sus reglas de trabajo. Solo una instrucción explícita de la propietaria autoriza cambios en estos agentes.
