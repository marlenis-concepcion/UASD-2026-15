# Caso práctico: actualización curricular continua con IA

## Ingeniería de Software I y II — Plan 14

**Asignaturas analizadas:** INF-5220 Ingeniería de Software I e INF-5250 Ingeniería de Software II.  
**Documentos comparados:** programas del Plan 14 elaborados en 2012 y programas rediseñados por competencias en 2023.

## 1. Pregunta de trabajo

> ¿Cómo mantener actualizadas Ingeniería de Software I y II sin rediseñar formalmente el plan de estudios cada vez que cambia una herramienta del mercado?

La propuesta conserva las competencias y fundamentos aprobados, pero introduce una capa de actualización continua para prácticas, casos, herramientas, evidencias y rúbricas. La IA ayuda a detectar y documentar cambios; la decisión permanece bajo control docente e institucional.

## 2. Hallazgos del análisis documental

### Plan 14 de 2012

- Ingeniería de Software I enfatizaba procesos, estándares, gestión de proyectos, UML, herramientas CASE, configuración, pruebas y ética profesional.
- Ingeniería de Software II profundizaba métricas, estimación de costos, requerimientos y diseño orientado a objetos.
- La evaluación combinaba exámenes, participación, investigaciones, ejercicios, casos y portafolios.
- Los programas reconocían la necesidad de adaptación tecnológica y desarrollo profesional continuo, pero no definían un mecanismo periódico para actualizar prácticas y herramientas.

### Rediseño por competencias de 2023

- Ingeniería de Software I incorporó Scrum, Kanban, XP, DevOps, gestión de requerimientos, trazabilidad, Git, API, bases de datos, UX, patrones y arquitecturas modernas.
- Ingeniería de Software II incorporó calidad continua, automatización de pruebas, rendimiento, CI/CD, nube, infraestructura como código, observabilidad, mantenimiento y DevSecOps.
- Los programas declaran resultados de aprendizaje y vinculan competencias fundamentales, transversales y específicas.
- Se integró colaboración de profesionales vinculados con tecnología y DevOps.

### Fortalezas que deben conservarse

1. Fundamentos de ciclo de vida, requerimientos, arquitectura, calidad, ética y seguridad.
2. Orientación a competencias y resultados de aprendizaje.
3. Agile, DevOps, automatización, nube y control de versiones.
4. Proyecto práctico, trabajo colaborativo y mejora continua.
5. Apertura a la experiencia profesional del docente y de especialistas del sector.

### Oportunidades de mejora

1. Los mismos RAE aparecen en ambas asignaturas y necesitan evidencias diferenciadas por nivel.
2. Los criterios de evaluación son generales; faltan productos observables, métricas y niveles de dominio.
3. Ingeniería de Software II presenta una inconsistencia documental: aparece la clave INF-5220 y se repite “Unidad 2”; debe validarse como INF-5250 y corregirse la secuencia.
4. Las listas de herramientas pueden envejecer rápidamente si se incorporan como contenido rígido.
5. Falta explicitar ingeniería de software asistida por IA, evaluación de sistemas con LLM, gobierno de datos y supervisión humana.
6. Falta un mecanismo institucional de revisión periódica basado en evidencia del mercado, egresados y desempeño estudiantil.

## 3. Modelo propuesto: currículo estable + capa actualizable

| Capa | Contenido | Frecuencia de cambio | Aprobación |
|---|---|---:|---|
| 1. Fundamentos | Competencias, ética, requerimientos, arquitectura, calidad y seguridad | 3–5 años | Rediseño formal |
| 2. Resultados y evidencias | RAE específicos, proyecto integrador, rúbricas y criterios de aceptación | Anual | Cátedra/Escuela |
| 3. Laboratorios | Herramientas, plataformas, casos, datasets y vacantes de referencia | Trimestral o semestral | Equipo docente |

Este modelo evita cambiar el programa por cada tecnología nueva. Por ejemplo, la competencia “automatizar pruebas de interfaz” permanece estable, mientras Playwright, Selenium o la herramienta vigente pueden cambiar en la guía docente.

## 4. Actualización propuesta para Ingeniería de Software I

### Propósito

Diseñar y justificar una solución de software a partir de necesidades reales, requisitos trazables y decisiones arquitectónicas defendibles.

### Evidencias mínimas

- Backlog versionado con historias, criterios de aceptación y requerimientos no funcionales.
- Repositorio Git con estrategia de ramas, issues, pull requests y registro de decisiones.
- Modelo arquitectónico y Architecture Decision Records (ADR).
- API funcional con persistencia SQL o NoSQL.
- Pruebas unitarias e integración básica ejecutadas automáticamente.
- Informe breve sobre privacidad, propiedad intelectual, accesibilidad y riesgos del uso de IA.

### Laboratorios actualizables

1. Requerimientos y criterios de aceptación asistidos por IA, con validación humana.
2. Comparación argumentada entre monolito modular, microservicios y arquitectura orientada a eventos.
3. Diseño de API, contratos y manejo de errores.
4. Git colaborativo, revisión de código y trazabilidad.
5. Uso responsable de asistentes de programación: atribución, revisión, pruebas y seguridad.

## 5. Actualización propuesta para Ingeniería de Software II

### Propósito

Convertir una solución construida en un producto verificable, desplegable, observable, seguro y mantenible.

### Evidencias mínimas

- Estrategia de calidad basada en riesgos.
- Automatización de pruebas web y API; pruebas de regresión y rendimiento.
- Pipeline CI/CD con controles de calidad y seguridad.
- Aplicación contenerizada y desplegada en un entorno reproducible.
- Infraestructura como código o configuración automatizada.
- Observabilidad mediante logs estructurados, métricas, alertas y tablero.
- Evaluación de vulnerabilidades, dependencias y secretos.
- Plan de mantenimiento, respuesta a incidentes y recuperación.
- Experimento opcional con LLM o agente que incluya dataset de evaluación, métricas y supervisión humana.

### Laboratorios actualizables

1. Playwright o Selenium para pruebas E2E; Postman/Newman o equivalente para API.
2. GitHub Actions, GitLab CI, Jenkins o plataforma institucional equivalente.
3. Docker, nube e infraestructura como código.
4. SAST, DAST, análisis de dependencias y DevSecOps.
5. Evaluación de aplicaciones con IA: exactitud, seguridad, costo, latencia y resultados no deterministas.

## 6. Proyecto integrador entre ambas asignaturas

**Ingeniería de Software I:** descubrir, especificar, diseñar y construir el producto mínimo.  
**Ingeniería de Software II:** probar, asegurar, desplegar, observar y mantener el mismo producto.

### Definición de terminado

1. Requerimientos vinculados con código y pruebas.
2. Decisiones arquitectónicas documentadas.
3. Revisión mediante pull request.
4. Pipeline ejecutado correctamente.
5. Evidencias de calidad, seguridad y rendimiento.
6. Despliegue reproducible.
7. Demostración y defensa ante docentes, egresados y profesionales invitados.

## 7. Sistema de agentes para la actualización continua

| Agente | Entradas | Función | Salida |
|---|---|---|---|
| Radar de mercado | Vacantes, encuestas, Google Trends, informes y aportes de egresados | Extraer competencias y detectar cambios | Informe mensual de señales |
| Mapeador curricular | Programas, RAE, contenidos y evidencias | Comparar señales con el currículo | Matriz cubierto/parcial/ausente |
| Diseñador de actualización | Brechas priorizadas y restricciones académicas | Proponer laboratorios, casos y rúbricas | Borrador de cambio mínimo |
| Auditor de evidencia | Repositorios, rúbricas y resultados estudiantiles | Verificar si la competencia se demuestra | Reporte de cobertura y calidad |
| Guardián de gobernanza | Normas, privacidad, PI, seguridad y accesibilidad | Identificar riesgos y requisitos regulatorios | Lista de controles y alertas |

### Regla de control

Ningún agente modifica por sí solo el programa oficial. Toda propuesta debe incluir fuente, fecha, justificación, impacto, responsable y aprobación humana.

## 8. Flujo de trabajo versionado

```text
Señal del mercado
        ↓
Issue con fuente y fecha
        ↓
Análisis de brecha por IA
        ↓
Validación: docente + egresado + empresa
        ↓
Pull request con laboratorio/rúbrica
        ↓
Piloto con estudiantes
        ↓
Evidencia y retrospectiva
        ↓
Aprobar, ajustar o descartar
```

### Estructura sugerida del repositorio

```text
curriculo/
  INF-5220/
  INF-5250/
radar-mercado/
propuestas/
rubricas/
evidencias/
decisiones/
```

Cada actualización debe conservar historial, autoría y comparación entre versiones.

## 9. Participación de egresados

- **Junior y Mid:** barreras de entrada, entrevistas, herramientas y prácticas iniciales.
- **Senior y Lead:** arquitectura, calidad, decisiones técnicas y mentoría.
- **Gerencia, CEO y VP:** estrategia, capacidades futuras, regulación y necesidades organizacionales.
- **Cadencia:** encuesta corta mensual, mesa trimestral y revisión semestral de evidencias.

La experiencia del egresado complementa, pero no sustituye, el criterio pedagógico ni la regulación académica.

## 10. Plan piloto de 90 días

| Periodo | Acción | Resultado |
|---|---|---|
| Semanas 1–2 | Constituir mesa docente–egresados–empresa y definir fuentes | Criterios y responsables |
| Semanas 3–4 | Ejecutar agentes Radar y Mapeador | Matriz de brechas priorizada |
| Semanas 5–6 | Diseñar un laboratorio para INF-5220 y otro para INF-5250 | Pull requests y rúbricas |
| Semanas 7–10 | Pilotar con una sección | Evidencias y observaciones |
| Semanas 11–12 | Evaluar, ajustar y documentar decisión | Versión aprobada o descartada |

## 11. Indicadores de éxito

- Porcentaje de competencias de mercado mapeadas a evidencias del curso.
- Porcentaje de estudiantes que completa el pipeline y despliegue.
- Cobertura y confiabilidad de pruebas.
- Vulnerabilidades críticas abiertas al cierre.
- Calidad de ADR, pull requests y trazabilidad.
- Valoración de egresados y empresas sobre el portafolio.
- Tiempo transcurrido desde la detección de una brecha hasta su piloto.
- Número de propuestas aceptadas, ajustadas o descartadas con justificación.

## 12. Primera acción recomendada

Pilotar únicamente dos cambios:

1. **INF-5220:** requerimientos, ADR y revisión de código asistidos por IA con trazabilidad completa.
2. **INF-5250:** pipeline CI/CD con pruebas web/API, seguridad básica, despliegue y observabilidad.

Al finalizar el semestre, la evidencia permitirá decidir si estos cambios se mantienen en la guía docente, se convierten en microcredenciales o requieren un nuevo proceso formal de rediseño.

