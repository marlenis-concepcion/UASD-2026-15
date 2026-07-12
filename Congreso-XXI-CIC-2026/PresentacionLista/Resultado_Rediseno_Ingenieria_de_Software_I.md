# Resultado del análisis y propuesta de actualización: Ingeniería de Software I

## 1. Identificación

- **Asignatura:** Ingeniería de Software I
- **Clave vigente en el Plan 14:** INF-5220
- **Documento base:** programa del Plan 14, elaborado en 2012
- **Documento contrastado:** rediseño basado en competencias, actualizado el 26 de junio de 2023
- **Naturaleza de este documento:** propuesta académica para discusión; no sustituye el programa oficial ni la aprobación institucional

## 2. Pregunta aplicada

> “Analizaremos las asignaturas Ingeniería de Software I y II del Plan 14. Revisaremos el rediseño curricular basado en competencias realizado en 2023 y construiremos, desde cero, un plan de actualización con IA y agentes que permita mantener sus contenidos continuamente alineados con las tendencias del mercado.”

## 3. Evidencia revisada

1. Programa de Ingeniería de Software I del Plan 14 (2012).
2. Programa rediseñado por competencias en 2023.
3. Vacantes tecnológicas presentadas en el XXI CIC 2026: Applaudo, Origami Risk, Grupo Ramos, HiRise, AI Robotix, Perform y BairesDev.
4. Señales mostradas de LinkedIn Jobs y Google Trends sobre Python, JavaScript, Java, SQL, Docker, React, Git y nube.
5. Requisitos recurrentes observados: API, SQL/NoSQL, Git, pruebas, automatización, CI/CD, Docker, nube, seguridad, Agile, inglés, comunicación y portafolio.

Google Trends expresa interés de búsqueda, no demanda laboral directa. Por ello se utiliza como señal complementaria y se contrasta con vacantes, encuestas profesionales y resultados de aprendizaje demostrables.

## 4. Hallazgos del análisis

### Fortalezas del Plan 14

- Reconoce el software como producto que debe responder a calidad, costo, tiempo y valor para el cliente.
- Incluye procesos, estándares, gestión de proyectos, pruebas, configuración, herramientas CASE y ética profesional.
- Promueve trabajo en equipo, comunicación oral y escrita, documentación y aprendizaje continuo.

### Avances del rediseño de 2023

- Incorpora Scrum, Kanban, XP y DevOps.
- Amplía la gestión y trazabilidad de requerimientos funcionales y no funcionales.
- Integra SOLID, código limpio, patrones, UI/UX, accesibilidad, API, bases de datos y diferentes estilos arquitectónicos.
- Incluye Git, pruebas unitarias y de integración, gestión de dependencias y colaboración.
- Define un perfil docente con experiencia profesional y actualización continua.

### Brechas que todavía deben cerrarse mediante la práctica

- El programa enumera muchas arquitecturas y herramientas, pero no establece con suficiente precisión qué producto integrador debe construir el estudiante.
- Git, pruebas, seguridad y documentación aparecen hacia el final; deben utilizarse desde el inicio del proyecto.
- Se requiere evidencia observable de API, persistencia, trazabilidad, revisión de código y colaboración.
- Falta explicitar el uso responsable de asistentes de IA: trazabilidad de prompts, validación, pruebas, privacidad, propiedad intelectual y prohibición de aceptar código sin comprenderlo.
- La amplitud temática puede producir cobertura superficial. Conviene profundizar en una arquitectura principal y comparar las demás mediante decisiones justificadas.

## 5. Propósito actualizado

Ingeniería de Software I debe lograr que el estudiante transforme una necesidad real en un incremento de software funcional, documentado y verificable. El curso conservará los fundamentos de procesos, requisitos, diseño y arquitectura, pero los conectará mediante un proyecto desarrollado en equipo con Git, API, datos, pruebas y revisión continua.

## 6. Competencia integradora propuesta

> Diseña y construye colaborativamente una solución de software de alcance controlado a partir de necesidades verificables, aplicando gestión ágil, ingeniería de requisitos, principios de diseño, arquitectura, control de versiones, pruebas, seguridad básica y documentación, con uso crítico y trazable de herramientas de inteligencia artificial.

## 7. Resultados de aprendizaje propuestos

Al finalizar, el estudiante podrá:

1. Explicar el ciclo de vida del software y seleccionar un enfoque de trabajo según el contexto, los riesgos y las restricciones del proyecto.
2. Identificar stakeholders, descubrir necesidades y convertirlas en historias de usuario, criterios de aceptación y requisitos no funcionales verificables.
3. Mantener trazabilidad entre necesidad, requisito, diseño, código, prueba y evidencia.
4. Modelar una solución mediante diagramas útiles y decisiones arquitectónicas justificadas, evitando documentación ornamental.
5. Aplicar SOLID, separación de responsabilidades, patrones pertinentes y prácticas de código limpio.
6. Construir una aplicación con interfaz o cliente, API, lógica de negocio y persistencia SQL o NoSQL.
7. Usar Git y GitHub/GitLab mediante ramas, commits significativos, issues y revisión por pull request.
8. Diseñar y ejecutar pruebas unitarias y de integración vinculadas a los criterios de aceptación.
9. Identificar riesgos básicos de seguridad, privacidad, accesibilidad, deuda técnica y dependencia de terceros.
10. Utilizar IA para investigar, diseñar, programar o revisar sin delegar el juicio profesional, documentando y verificando sus aportes.
11. Presentar y defender públicamente el producto, sus decisiones, limitaciones y evidencias.

## 8. Organización propuesta por unidades

### Unidad 1. Ingeniería de software, valor y responsabilidad

- Software como producto y servicio.
- Ciclo de vida, calidad, costo, riesgo y valor.
- Ética, privacidad, accesibilidad, propiedad intelectual e IA responsable.
- Formación de equipos y selección del problema.

**Evidencia:** acta del proyecto, problema validado, stakeholders y riesgos iniciales.

### Unidad 2. Agile y planificación basada en evidencia

- Scrum, Kanban y selección contextual del marco de trabajo.
- Product backlog, historias, criterios de aceptación y Definition of Done.
- Estimación, priorización, riesgos y retrospectiva.

**Evidencia:** backlog priorizado y tablero con historial de decisiones.

### Unidad 3. Requisitos y trazabilidad

- Elicitación, requisitos funcionales y no funcionales.
- Casos de uso, historias, reglas de negocio, datos e integraciones.
- Validación con stakeholders y control de cambios.

**Evidencia:** especificación ligera y matriz requisito–criterio–prueba.

### Unidad 4. Diseño y arquitectura

- SOLID, cohesión, acoplamiento, patrones y código limpio.
- Arquitectura por capas, hexagonal o Clean Architecture como opción principal.
- Comparación con monolito modular, microservicios, eventos y serverless.
- UI/UX, accesibilidad, API y modelo de datos.

**Evidencia:** ADR, diagramas esenciales, contrato de API y modelo de datos.

### Unidad 5. Construcción colaborativa

- Git desde el primer incremento.
- Flujo de ramas, commits, revisión de código y gestión de dependencias.
- Implementación de interfaz, API, negocio y persistencia.
- Manejo de errores, configuración y secretos.

**Evidencia:** repositorio con historial verificable y primer incremento funcional.

### Unidad 6. Calidad integrada y seguridad básica

- Pruebas unitarias, de integración y de API.
- Análisis estático, linters, cobertura con interpretación crítica.
- OWASP básico, validación de entradas, autenticación y autorización.
- Registro de defectos y deuda técnica.

**Evidencia:** suite ejecutable, reporte de calidad y corrección documentada de defectos.

### Unidad 7. Producto mínimo demostrable

- Integración del incremento final.
- Documentación técnica y de usuario.
- Evaluación de mantenibilidad y retrospectiva.
- Defensa ante audiencia académica y profesional.

**Evidencia:** demostración, repositorio, documentación y defensa individual y grupal.

## 9. Proyecto integrador mínimo

Cada equipo construirá desde cero una solución pequeña pero completa que incluya:

- problema y usuario claramente definidos;
- backlog y criterios de aceptación;
- API documentada;
- persistencia SQL o NoSQL;
- interfaz o cliente funcional;
- arquitectura justificable;
- Git con issues y pull requests;
- pruebas unitarias, de integración y de API;
- controles básicos de seguridad;
- documentación para ejecutar el proyecto;
- registro del uso de IA y de las verificaciones realizadas;
- demostración pública y portafolio.

No se exige que todos los equipos utilicen el mismo lenguaje. La evaluación se concentra en competencias transferibles, decisiones justificadas y evidencia reproducible.

## 10. Evaluación sugerida

| Evidencia | Porcentaje |
|---|---:|
| Diagnóstico, problema, stakeholders y ética | 10 % |
| Backlog, requisitos y trazabilidad | 15 % |
| Diseño, arquitectura y datos | 20 % |
| Incrementos de implementación y colaboración en Git | 20 % |
| Pruebas, seguridad y calidad del código | 15 % |
| Producto final, documentación y reproducibilidad | 10 % |
| Defensa individual, coevaluación y retrospectiva | 10 % |

La calificación individual se apoyará en commits, revisiones, decisiones explicadas y defensa oral; no solo en el producto colectivo.

## 11. Uso de IA con criterios de aceptación

Se permite IA para ideación, comparación de alternativas, generación de borradores, revisión y apoyo a la programación cuando el estudiante:

- protege datos, credenciales y propiedad intelectual;
- registra la herramienta, el propósito y el aporte relevante;
- verifica resultados mediante fuentes, compilación, pruebas y revisión humana;
- puede explicar y modificar lo entregado;
- identifica errores, sesgos, riesgos y limitaciones;
- conserva autoría sobre las decisiones finales.

## 12. Mecanismo de actualización continua

1. Mantener un backlog curricular en GitHub/GitLab.
2. Revisar trimestralmente una muestra de vacantes locales e internacionales.
3. Incorporar egresados de niveles junior, mid, senior, lead y gerencial a la revisión.
4. Mapear cada señal: vacante → competencia → resultado → actividad → evidencia.
5. Probar cambios pequeños en una sección antes de modificar el programa oficial.
6. Revisar métricas de aprendizaje, retroalimentación y portafolios.
7. Aprobar cambios mediante revisión docente e institucional, con historial de versión.

## 13. Prioridades para el próximo ciclo

- **Mantener:** fundamentos, requisitos, diseño, ética, gestión y comunicación.
- **Fortalecer:** API, Git, pruebas, seguridad, datos y proyecto integrador.
- **Introducir con control:** Docker básico, nube conceptual e IA asistida verificable.
- **Reservar para Software II:** CI/CD avanzado, infraestructura como código, observabilidad, pruebas avanzadas, despliegue y operación.

## 14. Fuentes internas utilizadas

- `Plan 14 - 5220 Ingenieria de Software I.pdf`.
- `Fixed_INF522-Ingenieria de Software I_Programa de Clase.docx`.
- `Transformacion_Perfil_Profesional_Automatizacion_IA_CIC2026_FINAL.pptx`.
