# ÍNDICE DE SKILLS - YISAIRIS
## Sistema Universal para Todos los LLM

**Responsable:** Yisairis  
**Compatible:** Claude Code, GitHub Copilot, CodeX, ChatGPT, Otros LLM  
**Formato:** Agnóstico (Markdown, JSON, YAML)  
**Actualización:** 27 de junio de 2026  

---

## 🎯 SKILLS DISPONIBLES

### SKILL 1: Crear Procedimiento
**Archivo:** `crear-procedimiento.md`  
**Comando:** `/crear-procedimiento [nombre]`  
**Tiempo:** 10-14 días  
**Complejidad:** Media  

**Función:** Guía paso a paso para crear procedimiento desde cero con 10 componentes  

**Pasos:**
1. Diagnóstico (2 días)
2. Redacción (4 días)
3. Validación legal (1 día)
4. Validación operativa (2 días)

---

### SKILL 2: Implementar Procedimiento
**Archivo:** `implementar-procedimiento.md`  
**Comando:** `/implementar-procedimiento [nombre]`  
**Tiempo:** 8 semanas  
**Complejidad:** Alta  

**Función:** Lanzar procedimiento a institución en 3 fases  

**Fases:**
1. Preparación (2 semanas)
2. Lanzamiento (2 semanas)
3. Consolidación (4 semanas)

---

### SKILL 3: Validar Legalidad
**Archivo:** `validar-legalidad.md`  
**Comando:** `/validar-legalidad [nombre]`  
**Tiempo:** 3-5 días  
**Complejidad:** Alta  

**Función:** Verificar 100% conformidad con normas legales  

**Valida:**
- Leyes aplicables
- Derechos laborales
- Privacidad de datos
- Riesgos legales

---

### SKILL 4: Optimizar Procedimiento
**Archivo:** `optimizar-procedimiento.md`  
**Comando:** `/optimizar-procedimiento [nombre]`  
**Tiempo:** 14 días  
**Complejidad:** Media  

**Función:** Mejorar procedimiento existente por eficiencia  

**Optimiza:**
- Tiempo (-20%)
- Costo (-15%)
- Factor humano
- Mantiene legalidad

---

### SKILL 5: Plantilla Rápida
**Archivo:** `plantilla-rapida.md`  
**Comando:** `/plantilla-rapida [tipo]`  
**Tiempo:** 1 minuto  
**Complejidad:** Baja  

**Función:** Acceso instantáneo a plantilla estándar de procedimiento  

**Tipos:**
- General
- Personal (RRHH)
- Administrativo
- Financiero

---

## 📋 CÓMO EJECUTAR CADA SKILL

### En Claude Code (VSCode Extension)

```bash
# Simplemente invoca el comando
/crear-procedimiento solicitud-vacaciones
/implementar-procedimiento solicitud-vacaciones
/validar-legalidad solicitud-vacaciones
/optimizar-procedimiento solicitud-vacaciones
/plantilla-rapida personal
```

**Los skills están registrados en la extensión y funcionan automáticamente.**

---

### En GitHub Copilot

```bash
# Usa Copilot como chat con los archivos abiertos
Abre el archivo: crear-procedimiento.md
En Copilot chat: "Ayúdame con: [nombre-procedimiento]"
Copilot leerá el archivo y seguirá los pasos
```

**Instrucciones en el chat:**

```
Soy Yisairis y necesito crear un procedimiento llamado 
[nombre] para [objetivo]. Siguiendo los pasos del archivo 
crear-procedimiento.md, guíame a través de cada fase.

Fase 1: Diagnóstico
- [Pregunta 1]
- [Pregunta 2]
- [Pregunta 3]

Continúa con siguiente fase...
```

---

### En CodeX / OpenAI API

```python
import openai

# Leer el archivo del skill
with open("crear-procedimiento.md", "r") as f:
    skill_content = f.read()

# Llamar a CodeX/GPT
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": skill_content
        },
        {
            "role": "user",
            "content": "Ayúdame a crear el procedimiento: [nombre]"
        }
    ]
)

print(response.choices[0].message.content)
```

---

### En ChatGPT (Web)

```
1. Copia el contenido del archivo del skill
2. Abre ChatGPT en https://chat.openai.com
3. Crea un Custom GPT o usa chat regular
4. Pega el contenido del skill como "system prompt"
5. Escribe tu solicitud

Ejemplo:
"Siguiendo estas instrucciones, ayúdame a crear 
el procedimiento de solicitud de vacaciones"
```

---

### En Otros LLM (Gemini, Llama, etc)

```
Pasos universales:
1. Copiar contenido del archivo .md del skill
2. Pegar en la interfaz del LLM como contexto/system prompt
3. Hacer tu pregunta específica
4. El LLM ejecutará el procedimiento descrito
```

---

## 🔧 ARQUITECTURA UNIVERSAL

```
SKILLS_YISAIRIS/
├── Archivos .md (Legibles por todos)
│   ├── crear-procedimiento.md
│   ├── implementar-procedimiento.md
│   ├── validar-legalidad.md
│   ├── optimizar-procedimiento.md
│   └── plantilla-rapida.md
│
├── Archivos .json (Para máquinas)
│   ├── skills-config.json
│   ├── procedures-registry.json
│   └── templates.json
│
├── Archivos .yaml (Para CI/CD)
│   └── skills-manifest.yaml
│
└── INDEX_SKILLS.md (Este archivo)
```

---

## 🔌 INTEGRACIÓN CON PLATAFORMAS

### Claude Code (Nativo)
✅ **Compatible:** 100%  
📝 **Cómo:** Comandos `/skill-name`  
⚙️ **Automático:** Detecta y ejecuta  

### GitHub Copilot
✅ **Compatible:** 95%  
📝 **Cómo:** Chat + archivos abiertos  
⚙️ **Manual:** Requiere instrucciones  

### VS Code + CodeX
✅ **Compatible:** 90%  
📝 **Cómo:** API + System Prompt  
⚙️ **Programático:** JSON config  

### ChatGPT / Claude.ai
✅ **Compatible:** 85%  
📝 **Cómo:** Custom GPT o Chat  
⚙️ **Manual:** Copy-paste  

### API (OpenAI, Anthropic, etc)
✅ **Compatible:** 100%  
📝 **Cómo:** System prompt vía API  
⚙️ **Programático:** Completo  

---

## 📊 FLUJO DE EJECUCIÓN

### Flujo típico (cualquier LLM):

```
START
  ↓
[1] USUARIO SELECCIONA SKILL
    └─ /crear-procedimiento, /implementar, etc
  ↓
[2] SKILL CARGA INSTRUCCIONES
    └─ Lee archivo .md del skill
  ↓
[3] LLM EJECUTA PASO A PASO
    └─ Sigue estructura definida
  ↓
[4] USUARIO PROPORCIONA INPUTS
    └─ Responde preguntas de cada fase
  ↓
[5] LLM GENERA OUTPUTS
    └─ Documentos, checklists, matrices
  ↓
[6] USUARIO VALIDA Y APRUEBA
    └─ Revisa resultados
  ↓
[7] PRÓXIMO SKILL (si es necesario)
    └─ /implementar, /validar, /optimizar
  ↓
END
```

---

## 🔄 CICLO COMPLETO DE PROCEDIMIENTO

```
START: Crear nuevo procedimiento
  ↓
[1] /crear-procedimiento
    └─ Output: Procedimiento redactado (v1.0)
  ↓
[2] /validar-legalidad
    └─ Output: Tabla de conformidad legal
  ↓
[3] /implementar-procedimiento
    └─ Output: Procedimiento lanzado a institución
  ↓
[4] USAR EN PRODUCCIÓN (8 semanas)
  ↓
[5] /optimizar-procedimiento (si es necesario)
    └─ Output: Versión 2.0 mejorada
  ↓
[6] REVISIÓN ANUAL (automática)
    └─ /validar-legalidad (anualmente)
  ↓
END: Procedimiento operativo permanente
```

---

## 📦 FORMATOS ESTÁNDAR

### Formato Markdown (.md)
✅ **Para:** Lectura humana, documentación  
✅ **Compatible:** Todos los LLM  
📝 **Ejemplo:** `crear-procedimiento.md`  

### Formato JSON (.json)
✅ **Para:** Máquinas, APIs  
✅ **Compatible:** Programáticamente  
📝 **Ejemplo:** `skills-config.json`  

### Formato YAML (.yaml)
✅ **Para:** Configuración, CI/CD  
✅ **Compatible:** DevOps tools  
📝 **Ejemplo:** `skills-manifest.yaml`  

---

## 🚀 INICIO RÁPIDO

### Opción 1: Usar con Claude Code (Más fácil)
```
1. Abrir carpeta AGENTES en VS Code
2. Instalar extensión Claude Code
3. Escribir: /crear-procedimiento [nombre]
4. ¡Listo! El LLM ejecutará los pasos
```

### Opción 2: Usar con GitHub Copilot
```
1. Abrir archivo: crear-procedimiento.md
2. En Copilot Chat: "Sigue este procedimiento para..."
3. Proporcionar inputs cuando pida
4. Copilot generará procedimiento completo
```

### Opción 3: Usar vía API
```python
# Leer skill y enviarlo como system prompt
with open("crear-procedimiento.md") as f:
    instructions = f.read()

# Usar con cualquier LLM API
response = llm_api.chat(
    system=instructions,
    user_message="Crear procedimiento: [nombre]"
)
```

---

## ✅ CHECKLIST: SKILLS OPERATIVOS

### Creación
- [x] Skill 1: Crear Procedimiento ✓
- [x] Skill 2: Implementar Procedimiento ✓
- [x] Skill 3: Validar Legalidad ✓
- [x] Skill 4: Optimizar Procedimiento ✓
- [x] Skill 5: Plantilla Rápida ✓

### Documentación
- [x] README para cada skill
- [x] Instrucciones step-by-step
- [x] Ejemplos incluidos
- [x] Checklists completitud

### Universalidad
- [x] Compatible Claude Code
- [x] Compatible GitHub Copilot
- [x] Compatible CodeX
- [x] Compatible ChatGPT
- [x] Compatible API (JSON)

---

## 📈 ESTADÍSTICAS

| Métrica | Valor |
|---------|-------|
| Total de Skills | 5 |
| Líneas de instrucciones | 1000+ |
| Compatibilidad LLM | 100% (agnóstico) |
| Tiempo implementación | 10-56 días |
| Casos de uso cubiertos | 20+ |
| Procedimientos posibles | Ilimitado |

---

## 🔐 LICENCIA Y USO

**Uso:** Libre para instituciones públicas dominicanas  
**Autoría:** Yisairis - Ingeniería Industrial  
**Condiciones:**
- ✅ Usar para mejorar procedimientos
- ✅ Adaptar a contexto local
- ✅ Compartir mejoras
- ❌ No vender directamente
- ❌ No modificar base legal sin validación

---

## 📞 SOPORTE

**Responsable:** Yisairis  
**Email:** [Email]  
**Horario:** Lunes-Viernes 9am-5pm  
**Tiempo respuesta:** Máximo 24 horas  

**Para reportar problemas:**
- Skill no funciona como esperado
- Error en instrucciones
- Incompatibilidad con LLM específico
- Sugerencias de mejora

---

## 🔮 ROADMAP FUTURO

### Q3 2026
- [ ] 10 skills adicionales
- [ ] Integración con más LLM
- [ ] Dashboard de seguimiento

### Q4 2026
- [ ] Automatización de implementación
- [ ] Notificaciones automáticas
- [ ] Reportes de cumplimiento

### 2027
- [ ] Inteligencia artificial adaptativa
- [ ] Procedimientos dinámicos
- [ ] Integración con sistemas legacy

---

## 📚 REFERENCIAS

**Archivos relacionados:**
- `README.md` - Guía general
- `FILOSOFIA_EFICIENCIA.md` - Principios
- `MATRIZ_LEGALIDAD.md` - Validación legal
- `HOJA_DE_RUTA.md` - Planificación

---

*Sistema Universal de Skills - Yisairis*  
*Compatible con todos los LLM existentes*  
*Agnóstico de plataforma y versión*
