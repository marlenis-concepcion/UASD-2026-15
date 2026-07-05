# Guion de presentación

## Diapositiva 1: Portada e introducción

Buenos días. Mi nombre es Marlenis Judith Concepción Cuevas y les doy la bienvenida a este taller sobre rediseño académico con inteligencia artificial. Hoy no vamos a mirar la IA solamente como una herramienta para escribir textos o preparar una presentación. Vamos a pensarla como una oportunidad para reorganizar el trabajo docente completo.

Tenemos un grupo multidisciplinario. Esto es una fortaleza, porque la necesidad de simplificar el trabajo cotidiano no pertenece a una sola carrera. Una persona puede enseñar programación, otra salud, derecho, ingeniería, idiomas, ciencias sociales o administración; todas deben investigar, planificar, crear actividades, evaluar evidencias y retroalimentar. Cambian los contenidos y los criterios profesionales, pero muchas tareas del flujo docente son comunes.

Nuestro propósito será partir de una asignatura real, revisar sus contenidos, relacionarla con las competencias profesionales y producir actividades, evaluaciones y retroalimentaciones más pertinentes. Trabajaremos con la Taxonomía de Bloom revisada, aula invertida y ciclos Agile para docentes.

También presentaré NotebookLM utilizando varios programas de asignaturas de programación. Veremos cómo una colección de fuentes institucionales puede convertirse en preguntas, cuestionarios, presentaciones y materiales de apoyo. Aunque el ejemplo sea de programación, el procedimiento puede transferirse a cualquier disciplina sustituyendo las fuentes y los criterios correspondientes.

Mi intención es que cada persona salga de aquí con al menos una idea concreta para simplificar su trabajo del día a día. Finalmente, conectaremos la demostración con una arquitectura de agentes especializados. La idea central es sencilla: la IA realiza y organiza buena parte del trabajo repetitivo, mientras el docente conserva el propósito pedagógico, el vínculo humano y la decisión final.

## Diapositiva 2: La IA redefine el trabajo docente

Quiero comenzar con una afirmación: la inteligencia artificial está redefiniendo el trabajo docente. No se trata simplemente de agregar otra aplicación a nuestra lista de herramientas. Se trata de revisar cómo distribuimos nuestro tiempo y cuáles tareas requieren realmente nuestro juicio profesional.

Durante años hemos dedicado muchas horas a comenzar actividades desde una página en blanco, adaptar instrucciones, elaborar preguntas similares, revisar entregas una por una y repetir comentarios. Con IA, buena parte de ese trabajo puede prepararse, clasificarse o compararse de manera asistida.

Eso no significa sacar al docente del proceso. Significa moverlo hacia donde aporta más valor: definir qué se debe aprender, observar cómo aprende el estudiante, interpretar dificultades, acompañar decisiones y validar la evaluación. A este principio lo llamamos **human in the loop**, o ser humano dentro del ciclo. La IA ejecuta una tarea, organiza datos o propone una respuesta; el docente revisa la evidencia, corrige cuando sea necesario y aprueba el resultado antes de utilizarlo.

Los agentes que propondremos no tomarán el control de la asignatura. Cada uno realizará una función delimitada y entregará evidencia para que el docente revise. El verdadero beneficio no es solamente producir más rápido; es recuperar tiempo para enseñar, conversar y atender las diferencias del grupo. Al escuchar los ejemplos, quiero que cada participante piense: ¿cuál tarea repetitiva de mi día a día podría delegar parcialmente a un agente sin delegar mi responsabilidad?

## Diapositiva 3: Problema y demostración de NotebookLM

Aquí planteamos el problema que queremos resolver. Actualizar una asignatura exige revisar programas, fuentes nuevas y necesidades del mercado laboral. Luego debemos transformar esos hallazgos en actividades coherentes, revisar las evidencias y explicar a cada estudiante cómo mejorar. Cuando el grupo es numeroso, este ciclo puede convertirse en una carga difícil de sostener.

En este momento haré la demostración de NotebookLM. He cargado varios programas relacionados con asignaturas de programación, entre ellos documentos de INF-510 a INF-515, incluyendo asignaturas y laboratorios, además de planes académicos. Es importante señalar que NotebookLM responde apoyándose en las fuentes seleccionadas. Por eso primero debemos revisar cuáles documentos cargamos y cuáles tenemos activados.

[Mostrar NotebookLM]. Señalaré el panel de fuentes, el chat y el área Studio. A partir de esos programas podemos preguntar qué contenidos se repiten, cuáles competencias aparecen, qué temas podrían estar desactualizados y cómo se relacionan las asignaturas. También podemos producir un cuestionario sobre programación, una presentación, tarjetas didácticas o una guía. La herramienta genera un borrador fundamentado; el docente verifica y decide si es pedagógicamente adecuado.

## Diapositiva 4: Agentes para las tareas docentes

En lugar de pedirle todo a una sola IA con un único mensaje, proponemos agentes especializados. El agente de diagnóstico identifica conocimientos previos y brechas. El investigador busca información actual y verifica sus fuentes. El diseñador convierte resultados de aprendizaje en actividades. El evaluador compara evidencias con una rúbrica. El agente de calificación propone una valoración justificada y el de retroalimentación explica cómo mejorar.

Estos agentes son útiles para un grupo multidisciplinario porque la arquitectura se conserva aunque cambie la materia. En programación, un agente puede analizar código y criterios de funcionamiento. En salud, puede organizar un caso clínico educativo sin utilizar datos personales. En derecho, puede contrastar una argumentación con los criterios de la actividad. En idiomas, puede clasificar errores y proponer práctica diferenciada. En administración, puede revisar un estudio de caso o un proyecto. En todos los ejemplos, las fuentes, la rúbrica y la validación humana deben pertenecer a la disciplina.

Esta separación es importante porque cada tarea requiere instrucciones, fuentes y controles distintos. Un agente que investiga no debe inventar criterios de evaluación. Un agente que califica no debe cambiar la rúbrica después de ver el trabajo del estudiante. Y un agente de retroalimentación no debe limitarse a felicitar o señalar errores; debe ofrecer acciones concretas.

En la demostración de NotebookLM vimos productos como preguntas, cuestionarios y presentaciones. Aquí damos un paso adicional: convertimos esos productos en partes de un flujo docente. Cada salida debe tener una finalidad pedagógica y un responsable de validarla. Así evitamos acumular materiales bonitos que no contribuyen realmente al aprendizaje.

## Diapositiva 5: Funcionamiento del equipo de agentes

Este es el flujo general del equipo de agentes. Primero se diagnostica. Después se investiga qué debe actualizarse. Con la evidencia recopilada se actualizan los contenidos. Solo entonces se diseñan actividades, instrumentos y productos. Cuando el estudiante entrega su evidencia, el agente evaluador la contrasta con la rúbrica y el agente de retroalimentación prepara orientaciones para la siguiente versión.

Sobre todos ellos se encuentra el agente coordinador. Su función no es enseñar ni calificar, sino conservar el contexto, comprobar que cada etapa recibió los productos anteriores y detener el proceso cuando falta información. También identifica los puntos donde debe intervenir el docente.

Por ejemplo, si la rúbrica pide argumentación, pero la actividad solo solicita marcar respuestas, el coordinador debe señalar que existe una desalineación. Si un estudiante no cumplió un criterio, el sistema no debe improvisar un castigo ni cambiar la regla. Debe mostrar qué evidencia falta, proponer una retroalimentación y remitir la decisión definitiva al docente.

Aquí opera nuevamente el principio human in the loop. No significa que el docente tenga que rehacer manualmente todo lo producido por la IA. Significa que existen puntos de control proporcionales al riesgo: aprobar las competencias, validar las fuentes, revisar la rúbrica, examinar casos dudosos y confirmar la calificación. Los agentes realizan el trabajo operativo; el docente supervisa y responde por la decisión. Cada agente asiste; ninguno sustituye la responsabilidad profesional.

## Diapositiva 6: Marco metodológico

La rapidez de la IA solo es valiosa cuando está gobernada por una metodología. Nuestro primer marco es la Taxonomía de Bloom revisada. Los resultados deben utilizar acciones observables: recordar, comprender, aplicar, analizar, evaluar y crear. No basta con decir que el estudiante conocerá un tema; debemos determinar qué hará para demostrarlo.

El segundo marco es el aula invertida. Antes del encuentro, el estudiante explora fuentes, responde un diagnóstico y prepara preguntas. Durante la clase aplicamos, analizamos y resolvemos problemas. Después de la clase consolidamos, producimos una evidencia y mejoramos a partir de la retroalimentación.

El tercer marco es Agile para docentes: trabajamos en ciclos cortos, con una lista priorizada, un producto verificable, una revisión y una retrospectiva. Finalmente, la IA educativa exige transparencia, verificación de fuentes, protección de datos y supervisión humana. Los agentes no diseñan en el vacío. Sus decisiones deben obedecer a estos principios y mantener la alineación entre lo que prometemos enseñar y lo que realmente evaluamos.

## Diapositiva 7: Prueba diagnóstica

Toda unidad comienza con una prueba diagnóstica. Su finalidad no es castigar ni asignar una nota sumativa. Buscamos conocer el punto de partida: qué recuerda el estudiante, qué comprende, qué puede aplicar y cuáles conceptos erróneos podrían dificultar el nuevo aprendizaje.

El agente de diagnóstico puede ayudarnos a crear preguntas en varios niveles de Bloom, organizar las respuestas y detectar patrones. En el ejemplo de la gráfica, el grupo tiene mejores resultados en recordar y comprender, pero presenta mayor dificultad al aplicar y analizar. Esa información cambia nuestra planificación: quizá debamos dedicar menos tiempo a repetir definiciones y más tiempo a casos guiados.

Aquí también podemos utilizar NotebookLM para generar un primer banco de preguntas basadas en los programas y materiales seleccionados. Sin embargo, el docente debe comprobar el nivel cognitivo, la claridad y la pertinencia de cada pregunta. Los resultados del diagnóstico alimentan el primer ciclo Agile: permiten priorizar contenidos, formar grupos, preparar apoyos y ajustar el ritmo. Al final compararemos una evidencia equivalente para observar el progreso real.

## Diapositiva 8: Aula invertida e IA

La IA puede acompañar las tres etapas del aula invertida. Antes de la clase, puede preparar una lectura guiada, un video breve, tarjetas, preguntas de anticipación y el diagnóstico. El estudiante llega con una primera aproximación al contenido y el docente recibe información sobre las dificultades del grupo.

Durante la clase no queremos usar el tiempo para repetir lo que el estudiante pudo revisar previamente. Queremos resolver casos, programar, analizar errores, comparar soluciones y tomar decisiones. La IA puede proponer variantes de un problema o brindar apoyos diferenciados, pero el encuentro debe favorecer la discusión, la colaboración y el acompañamiento docente.

Después de la clase, el estudiante entrega un producto, explica su proceso y recibe retroalimentación. El agente evaluador organiza la evidencia según la rúbrica y el agente de retroalimentación propone próximos pasos. El estudiante mejora su trabajo y el docente observa qué debe cambiar en el siguiente ciclo. De esta forma, la tecnología no reduce la interacción humana; libera tiempo del encuentro para hacerla más profunda.

## Diapositiva 9: Evaluación, rúbrica y retroalimentación

Una de las tareas que más agota al docente es corregir trabajos cuando algunos estudiantes no cumplen la rúbrica. El problema no es solamente colocar una puntuación. Debemos identificar qué criterio se cumplió, cuál evidencia lo demuestra, qué falta y cómo puede mejorar el estudiante.

Nuestro flujo conecta diagnóstico, competencia, resultado de aprendizaje, nivel de Bloom, actividad, evidencia, rúbrica y retroalimentación. El agente evaluador compara la entrega con cada criterio aprobado. No puede penalizar algo que nunca fue solicitado ni modificar los criterios después de recibir el trabajo. Cuando no encuentra evidencia suficiente, debe decirlo claramente y remitir el caso al docente.

El agente puede preparar una propuesta como esta: criterio, evidencia encontrada, nivel alcanzado, puntuación sugerida y justificación. Luego el agente de retroalimentación convierte ese análisis en un mensaje respetuoso y accionable. El docente revisa los casos dudosos y valida la calificación. Así dejamos de repetir comentarios manualmente, pero mantenemos una evaluación justa, trazable y humana.

## Diapositiva 10: Cierre

Para cerrar, no estamos proponiendo que el docente haga más tareas con una herramienta nueva. Estamos proponiendo una manera distinta de trabajar. Los agentes especializados pueden investigar, organizar información, producir variantes, comparar evidencias y preparar retroalimentaciones. El docente aporta lo que ninguna automatización debe decidir por sí sola: el propósito de la asignatura, la lectura del contexto, la relación con el estudiante y el juicio profesional.

Como somos un grupo multidisciplinario, no espero que todos salgamos con el mismo agente. Una persona puede comenzar con un agente para crear actividades; otra, con uno para revisar una rúbrica; otra, con un agente para organizar retroalimentaciones frecuentes. Lo importante es identificar una tarea real que consume tiempo, definir qué información necesita la IA, establecer qué producto debe entregar y decidir dónde intervendrá el ser humano para validarlo.

La invitación es comenzar con una asignatura y una unidad, no automatizarlo todo de inmediato. Cargamos las fuentes confiables, aplicamos un diagnóstico, seleccionamos una tarea repetitiva y diseñamos un agente con límites claros. Revisamos sus resultados, recogemos evidencia y mejoramos el siguiente ciclo.

Quiero que nos quedemos con esta idea: la IA puede hacer por nosotros gran parte del trabajo operativo y repetitivo, pero trabaja dentro de límites definidos por el docente. Nosotros validamos los resultados mediante human in the loop. La meta es que cada participante salga con una idea aplicable para simplificar su día a día y recuperar tiempo para acompañar mejor a sus estudiantes.

Nuestro próximo paso será tomar una asignatura real y construir esta cadena de agentes desde la investigación hasta la retroalimentación. Muchas gracias. Ahora podemos conversar sobre cuál tarea docente desean transformar primero.
