# Resultado del análisis y propuesta de actualización: Ingeniería de Software II

## 1. Identificación

- **Asignatura:** Ingeniería de Software II
- **Clave vigente en el Plan 14:** INF-5250
- **Prerrequisito:** INF-5220, Ingeniería de Software I
- **Documento base:** programa del Plan 14, elaborado en 2012
- **Documento contrastado:** rediseño basado en competencias, actualizado el 28 de agosto de 2023
- **Naturaleza de este documento:** propuesta académica para discusión; no sustituye el programa oficial ni la aprobación institucional

### Correcciones formales recomendadas al documento de 2023

Antes de oficializar una nueva versión deben corregirse dos aspectos:

1. La cabecera identifica la asignatura con la clave `INF-5220`; debe validarse y sustituirse por `INF-5250`.
2. La numeración contiene dos unidades llamadas “Unidad 2”; “Fundamentos para el despliegue” debe renumerarse dentro de la secuencia definitiva.

## 2. Pregunta aplicada

> “Analizaremos las asignaturas Ingeniería de Software I y II del Plan 14. Revisaremos el rediseño curricular basado en competencias realizado en 2023 y construiremos, desde cero, un plan de actualización con IA y agentes que permita mantener sus contenidos continuamente alineados con las tendencias del mercado.”

## 3. Evidencia revisada

1. Programa de Ingeniería de Software II del Plan 14 (2012).
2. Programa rediseñado por competencias en 2023.
3. Vacantes presentadas en el XXI CIC 2026 en QA, automatización, datos, desarrollo, nube e IA.
4. Requisitos recurrentes: Playwright, Selenium, API testing, rendimiento, seguridad, Python, SQL/NoSQL, Docker, AWS, Terraform, CI/CD, observabilidad, agentes y evaluación de modelos.
5. Señales de Google Trends y encuestas profesionales de QA utilizadas en la presentación.

Las herramientas concretas cambian. El currículo debe evaluar capacidades transferibles y utilizar las herramientas como medios para producir evidencia, no como listas para memorizar.

## 4. Hallazgos del análisis

### Fortalezas del Plan 14

- Profundiza en métricas, estimación, calidad, verificación, mantenimiento y gestión.
- Reconoce la negociación, el liderazgo, la comunicación y la responsabilidad profesional.
- Plantea un proyecto final y la entrega de artefactos de software de calidad.

### Avances del rediseño de 2023

- Reorienta la asignatura hacia calidad, DevOps, automatización, despliegue, mantenimiento y seguridad.
- Incluye pruebas funcionales y no funcionales, Selenium, JUnit, TestNG, JMeter, k6, análisis estático y gestión de defectos.
- Incorpora CI/CD, nube, GitHub Actions, GitLab, Jenkins, infraestructura como código, monitoreo y logging.
- Integra DevSecOps, seguridad de API, aplicaciones web y móviles, gestión de incidentes y mejora continua.

### Brechas que todavía deben cerrarse

- Se presentan muchas herramientas sin definir una cadena mínima obligatoria que todos los estudiantes deban integrar.
- Debe actualizarse el énfasis desde “automatizar casos” hacia ingeniería de calidad basada en riesgo, estrategia y valor de negocio.
- Faltan contract testing, calidad de datos, confiabilidad, SRE básico, supply-chain security y evaluación de sistemas que incorporan IA.
- Deben incorporarse Playwright y pruebas modernas de API sin convertir el programa en un catálogo dependiente de marcas.
- Hace falta exigir un pipeline reproducible, despliegue observable, evidencia de seguridad y respuesta a incidentes.
- El uso de IA requiere controles de determinismo, privacidad, evaluación, trazabilidad y revisión humana.

## 5. Propósito actualizado

Ingeniería de Software II debe tomar el producto desarrollado en Software I —o una base equivalente— y convertirlo en un sistema confiable, seguro, automatizado, desplegable, observable y mantenible. La asignatura conecta calidad, DevSecOps y operación mediante evidencia ejecutable en un pipeline.

## 6. Competencia integradora propuesta

> Diseña, automatiza y gobierna el proceso de calidad, entrega y operación de un sistema de software, aplicando pruebas basadas en riesgo, CI/CD, contenedores, nube, observabilidad, seguridad, mantenimiento e inteligencia artificial responsable para demostrar confiabilidad y mejora continua.

## 7. Resultados de aprendizaje propuestos

Al finalizar, el estudiante podrá:

1. Diseñar una estrategia de calidad basada en riesgos, usuarios, arquitectura y objetivos de negocio.
2. Seleccionar niveles y tipos de prueba evitando duplicación y automatización sin valor.
3. Implementar pruebas unitarias, de integración, contrato, API, interfaz y end-to-end.
4. Automatizar pruebas web con Playwright, Selenium o una alternativa justificada y mantenible.
5. Ejecutar pruebas de rendimiento, seguridad, accesibilidad y calidad de datos con criterios medibles.
6. Construir un pipeline CI/CD que compile, analice, pruebe, empaquete y despliegue el sistema.
7. Empaquetar aplicaciones con Docker y gestionar configuración, secretos, artefactos y dependencias.
8. Desplegar en un entorno cloud o equivalente y documentar la estrategia de rollback y recuperación.
9. Implementar logs, métricas, trazas, alertas y objetivos básicos de confiabilidad.
10. Aplicar DevSecOps, análisis de dependencias y controles de seguridad en el pipeline.
11. Diagnosticar incidentes, priorizar defectos y realizar análisis de causa raíz.
12. Evaluar el uso de IA en desarrollo y pruebas mediante métricas, casos adversos, trazabilidad y supervisión humana.
13. Comunicar resultados técnicos y riesgos a audiencias de negocio, desarrollo y operación.

## 8. Organización propuesta por unidades

### Unidad 1. Estrategia de calidad y riesgo

- Calidad de producto y proceso; ISO/IEC 25010 como marco de análisis.
- Riesgo, impacto, probabilidad y costo de fallo.
- Pirámide o trofeo de pruebas y criterios de automatización.
- Métricas útiles: cobertura de riesgo, tiempo de retroalimentación, escape de defectos y confiabilidad.

**Evidencia:** estrategia de calidad y matriz de riesgos del producto.

### Unidad 2. Automatización por capas

- Pruebas unitarias, integración, contrato, API, UI y E2E.
- Playwright, Selenium o alternativa equivalente.
- Datos de prueba, dobles, ambientes, flakiness y mantenibilidad.
- Patrones de automatización y revisión de código de pruebas.

**Evidencia:** framework automatizado ejecutable y justificación de cobertura.

### Unidad 3. Pruebas no funcionales y calidad ampliada

- Rendimiento, carga, estrés y capacidad.
- Seguridad de web, API y dependencias.
- Accesibilidad y experiencia de usuario.
- Calidad, privacidad y gobierno de datos.

**Evidencia:** informe de riesgos no funcionales, resultados reproducibles y plan de mejora.

### Unidad 4. CI/CD, contenedores y supply chain

- Integración continua, quality gates y artefactos.
- Docker, registros y versionamiento.
- Gestión segura de secretos y configuración.
- SBOM, análisis de dependencias y controles de la cadena de suministro.

**Evidencia:** pipeline que ejecuta análisis, pruebas y empaquetado en cada cambio.

### Unidad 5. Despliegue e infraestructura

- Entornos, nube, redes y almacenamiento a nivel aplicado.
- Infraestructura como código con Terraform o alternativa.
- Estrategias rolling, blue/green, canary, rollback y recuperación.
- Costos, escalabilidad, disponibilidad y cumplimiento.

**Evidencia:** despliegue automatizado en ambiente de prueba con plan de reversión.

### Unidad 6. Observabilidad, operación y mantenimiento

- Logs estructurados, métricas, trazas y tableros.
- SLI, SLO y alertas básicas.
- Gestión de incidentes, causa raíz y postmortem sin culpa.
- Mantenimiento, deuda técnica, versiones, backup y retiro.

**Evidencia:** tablero observable, alerta demostrable y simulación de incidente.

### Unidad 7. IA aplicada a ingeniería y calidad

- Generación y mantenimiento asistido de pruebas.
- Priorización por riesgo y detección de flakiness.
- LLM, RAG, agentes, MCP y tool calling como objetos de prueba.
- Evaluación de modelos: exactitud, consistencia, seguridad, costo, latencia y comportamiento adverso.
- Límites: resultados no deterministas, prompt injection, fuga de datos y dependencia excesiva.

**Evidencia:** experimento comparativo con criterios, conjunto de evaluación y revisión humana.

### Unidad 8. Entrega y defensa profesional

- Auditoría de trazabilidad requisito–código–prueba–pipeline–despliegue.
- Informe ejecutivo de calidad y riesgo residual.
- Portafolio, documentación y defensa ante panel académico-profesional.
- Retrospectiva y backlog de mejora.

**Evidencia:** sistema desplegado, dossier técnico y defensa individual y grupal.

## 9. Proyecto integrador mínimo

El equipo evolucionará una solución de Software I o un producto equivalente. La entrega debe incluir:

- estrategia de calidad basada en riesgo;
- suite unitaria, integración, API y E2E;
- automatización web o móvil cuando corresponda;
- prueba de rendimiento y revisión básica de seguridad;
- pipeline CI/CD;
- imagen Docker y gestión segura de configuración;
- despliegue en nube o entorno equivalente;
- infraestructura como código en alcance controlado;
- logs, métricas y alerta;
- simulación de fallo, rollback o recuperación;
- issue tracking, pull requests y trazabilidad;
- evaluación explícita de cualquier componente o asistencia de IA;
- documentación reproducible y defensa pública.

## 10. Stack de referencia, no obligatorio

| Capacidad | Opciones de laboratorio |
|---|---|
| Lenguaje | Python, Java, JavaScript/TypeScript, C# o Go |
| API | REST o GraphQL con contrato documentado |
| Datos | PostgreSQL/MySQL y una comparación justificada con NoSQL |
| Automatización | Playwright, Selenium, Cypress o Appium |
| API testing | Postman/Newman, pytest, REST Assured u opción equivalente |
| Rendimiento | k6 o JMeter |
| CI/CD | GitHub Actions, GitLab CI, Jenkins o Azure DevOps |
| Contenedores | Docker |
| IaC | Terraform o alternativa equivalente |
| Observabilidad | OpenTelemetry, Prometheus, Grafana o servicios cloud equivalentes |
| Seguridad | SAST, análisis de dependencias y OWASP ZAP en alcance académico |

La institución puede escoger un stack soportado para el laboratorio, pero los resultados de aprendizaje no deben depender de una marca.

## 11. Evaluación sugerida

| Evidencia | Porcentaje |
|---|---:|
| Estrategia de calidad y riesgos | 10 % |
| Automatización por capas | 20 % |
| Pruebas no funcionales y seguridad | 15 % |
| Pipeline CI/CD y contenedores | 20 % |
| Despliegue, IaC y observabilidad | 15 % |
| Operación, incidente y mejora | 10 % |
| Informe, portafolio y defensa individual | 10 % |

No se otorgará la totalidad de la calificación por una demostración manual. El pipeline y las evidencias deben poder ejecutarse o verificarse nuevamente.

## 12. Uso responsable de IA

Cuando se utilice IA para producir código, pruebas, infraestructura o documentación, el equipo deberá:

- declarar herramientas y propósitos;
- proteger secretos, datos y propiedad intelectual;
- versionar prompts o decisiones relevantes cuando aporten trazabilidad;
- ejecutar pruebas y revisión humana;
- medir utilidad, errores, costo y tiempo;
- demostrar que puede diagnosticar y modificar el resultado;
- aplicar pruebas adversas si el producto incorpora LLM o agentes;
- mantener una alternativa operativa ante fallos del proveedor o del modelo.

## 13. Mecanismo de actualización continua

1. Revisar trimestralmente vacantes de QA, desarrollo, datos, nube, DevOps, seguridad e IA.
2. Consultar a egresados y profesionales junior, mid, senior, lead y gerenciales.
3. Mantener un radar: adoptar, probar, observar o retirar.
4. Registrar cada propuesta en el backlog curricular con evidencia y responsable.
5. Pilotar cambios en laboratorios o microcredenciales antes de incorporarlos al programa.
6. Evaluar portafolios, pipelines, empleabilidad y retroalimentación de empresas.
7. Versionar decisiones y obtener aprobación institucional.

## 14. Secuencia con Ingeniería de Software I

| Ingeniería de Software I | Ingeniería de Software II |
|---|---|
| Descubre y especifica necesidades | Define riesgos y estrategia de calidad |
| Diseña arquitectura y datos | Verifica arquitectura, confiabilidad y seguridad |
| Construye API y producto mínimo | Automatiza pruebas y entrega |
| Usa Git y revisión colaborativa | Implementa CI/CD y quality gates |
| Prueba unidades e integraciones | Añade E2E, rendimiento, seguridad y contratos |
| Documenta y demuestra | Despliega, observa, opera y mejora |

## 15. Fuentes internas utilizadas

- `Plan 14 - 5250 Ingenieria de Software II.pdf`.
- `Fixed_INF525-Ingenieria de Software II_Programa de Clase.docx`.
- `Transformacion_Perfil_Profesional_Automatizacion_IA_CIC2026_FINAL.pptx`.
