# VisionIASST
IA Vision y LLM aplicado a la Seguridad y Salud en el Trabajo, Riesgos profesionales

Prototipo 

👁️‍🗨️ AI-SST Vision
Análisis automático de riesgos laborales mediante IA multimodal

📌 Descripción
AI-SST Vision es una aplicación que implementa inteligencia artificial multimodal para identificar, analizar y documentar situaciones de riesgo en entornos laborales, enfocada en la Seguridad y Salud en el Trabajo (SST). Utiliza modelos de visión y lenguaje para evaluar condiciones, detectar actos y factores inseguros, y generar alertas en función de los riesgos detectados.

La herramienta asiste en la supervisión de tareas, el análisis preventivo, y la generación automática de informes, convirtiéndose en un asistente experto en SST capaz de operar de forma autónoma o complementaria a la supervisión humana.

🎯 Objetivo
Aplicar IA para la detección de riesgos laborales.

Evaluar situaciones de trabajo mediante análisis de imágenes.

Guiar el análisis utilizando el método de las 6M aplicado a SST.

Emitir alertas inteligentes según la gravedad del riesgo.

Generar reportes descriptivos en lenguaje técnico especializado.

⚙️ Tecnologías Utilizadas
Python

LLM Studio

Modelos locales sobre GPU (RTX 3080 Ti 12 GB)

DAMO-NLP-SG/VideoLLaMA3-2B-Image (modelo de visión)

lmstudio-community/deepseek-r1-distill-qwen-14b (modelo de texto)

Método de análisis de causa raíz 6M

entorno local sin necesidad de conexión a la nube

🧠 ¿Cómo Funciona? resumen
Se carga una imagen del entorno de trabajo.

El modelo de visión responde a preguntas guiadas:

Descripción general

Análisis bajo el método de las 6M (Manpower, Método, Máquina, Materiales, Medio ambiente, Mediciones)

Todas las respuestas se concatenan y son analizadas por un modelo de lenguaje (LLM).

El LLM evalúa la situación y:

Describe el escenario.

Determina actos y condiciones inseguras.

Identifica riesgos potenciales.

Emite una alerta (Roja, Amarilla o Azul).

🚨 Tipos de Alerta
🔴 Roja: Riesgo inminente (muerte, amputación, lesiones graves).

🟡 Amarilla: Riesgo potencial (condiciones que deben atenderse).

🔵 Azul: Condiciones seguras (sin necesidad de detener la tarea).

👥 Público Objetivo
Inspectores y profesionales de Seguridad y Salud en el Trabajo

Consultores e ingenieros de seguridad industrial

Empresas interesadas en aplicar IA para prevención de riesgos

Desarrolladores e investigadores en IA aplicada a SST

✨ ¿Qué hace especial esta aplicación?
AI-SST Vision combina capacidades de visión por computadora con análisis experto en SST, integrando por primera vez el método 6M de forma guiada por IA. A diferencia de otras soluciones que se limitan a detección visual, esta herramienta analiza contextos laborales como lo haría un inspector experto y toma decisiones basadas en texto y evidencias visuales. Todo esto sin conexión a la nube, garantizando privacidad y velocidad en entornos industriales.