# SKILLS - SISTEMA UNIVERSAL
## Ejecutable en Cualquier LLM

**Responsable:** Yisairis  
**Compatible:** ✅ Claude Code | ✅ Copilot | ✅ CodeX | ✅ ChatGPT | ✅ APIs  
**Formato:** Agnóstico (Markdown, JSON, YAML)  
**Última actualización:** 27 de junio de 2026  

---

## 📚 SKILLS DISPONIBLES

### 1️⃣ CREAR PROCEDIMIENTO
**Archivo:** [`crear-procedimiento.md`](crear-procedimiento.md)  
**Tiempo:** 10-14 días  
**Para:** Crear procedimiento desde cero  

```bash
# En Claude Code:
/crear-procedimiento solicitud-vacaciones

# En GitHub Copilot:
"Ayúdame a crear un procedimiento siguiendo los pasos de crear-procedimiento.md"

# En API:
POST /skill/create-procedure
  nombre: "Solicitud de Vacaciones"
  area: "RRHH"
```

---

### 2️⃣ IMPLEMENTAR PROCEDIMIENTO
**Archivo:** [`implementar-procedimiento.md`](implementar-procedimiento.md)  
**Tiempo:** 8 semanas (3 fases)  
**Para:** Lanzar procedimiento a institución  

```bash
# En Claude Code:
/implementar-procedimiento solicitud-vacaciones

# En GitHub Copilot:
"Sigue los pasos de implementar-procedimiento.md para lanzar esto"

# En Chat Manual:
Copia contenido de implementar-procedimiento.md y pega como contexto
```

---

### 3️⃣ VALIDAR LEGALIDAD
**Archivo:** [`validar-legalidad.md`](validar-legalidad.md)  
**Tiempo:** 3-5 días  
**Para:** Revisar conformidad legal al 100%  

```bash
# En Claude Code:
/validar-legalidad solicitud-vacaciones

# En API:
POST /skill/validate-legal
  procedimiento: "solicitud-vacaciones.md"
```

---

### 4️⃣ OPTIMIZAR PROCEDIMIENTO
**Archivo:** [`optimizar-procedimiento.md`](optimizar-procedimiento.md)  
**Tiempo:** 14 días  
**Para:** Mejorar procedimiento existente  

```bash
# En Claude Code:
/optimizar-procedimiento solicitud-vacaciones

# En GitHub Copilot:
"Optimiza esto usando los criterios en optimizar-procedimiento.md"
```

---

### 5️⃣ PLANTILLA RÁPIDA
**Archivo:** [`plantilla-rapida.md`](plantilla-rapida.md)  
**Tiempo:** 1 minuto  
**Para:** Obtener plantilla lista para rellenar  

```bash
# En Claude Code:
/plantilla-rapida general
/plantilla-rapida personal
/plantilla-rapida administrativa
/plantilla-rapida financiera

# En Chat:
"Dame la plantilla de procedimiento para [tipo]"
```

---

## 🚀 GUÍA RÁPIDA POR PLATAFORMA

### CLAUDE CODE (VSCode Extension) ⭐ RECOMENDADO

**Instalación:**
1. Abrir VS Code
2. Instalar extensión "Claude Code"
3. Abrir esta carpeta en VS Code

**Uso:**
```
1. Escribir comando: /crear-procedimiento [nombre]
2. Claude ejecutará automáticamente los pasos
3. Responder preguntas cuando pregunte
4. Obtener procedimiento completo
```

**Ventajas:**
- ✅ Más fácil
- ✅ Automático
- ✅ Integrado con editor
- ✅ Historial guardado

---

### GITHUB COPILOT

**Instalación:**
1. Instalar extensión GitHub Copilot
2. Abrir esta carpeta

**Uso:**

```
PASO 1: Abre el archivo del skill
Archivo → Abrir: crear-procedimiento.md

PASO 2: Abre Copilot Chat (Ctrl+Shift+L)

PASO 3: Escribe prompt que incluya el skill:
"Siguiendo las instrucciones en crear-procedimiento.md,
 ayúdame a crear un procedimiento para solicitud de 
 permisos especiales. Aquí está el contexto:
 - Área: RRHH
 - Usuarios: 80
 - Complejidad: Media"

PASO 4: Copilot leerá el archivo y ejecutará paso a paso
```

**Ventajas:**
- ✅ Integrado en VS Code
- ✅ Acceso a archivos locales
- ✅ Historial en contexto

---

### CHATGPT / CLAUDE.AI

**Método 1: Manual (Copiar-Pegar)**

```
PASO 1: Copiar contenido del skill
Abre: crear-procedimiento.md → Copiar todo (Ctrl+A)

PASO 2: Ir a ChatGPT (https://chat.openai.com)

PASO 3: Crear Custom GPT o usar chat:
- Crear nuevo chat
- Pegar el contenido del skill como primer mensaje
- Escribir tu solicitud:

"Siguiendo estas instrucciones, ayúdame a crear
 un procedimiento para [nombre]. Aquí está mi contexto:
 [detalles específicos]"

PASO 4: ChatGPT ejecutará los pasos
```

**Método 2: Crear Custom GPT (Reusable)**

```
1. ChatGPT → Explore → Create a GPT
2. Name: "Yisairis Procedimientos"
3. Description: "Crea procedimientos eficientes para sector público"
4. Instructions: Pegar contenido de skills-config.json
5. Archivo de conocimiento: Subir todos los .md
6. Save as "Only me" o "Anyone" según necesidad
7. Usar el GPT en futuro sin copiar-pegar
```

---

### OPENAI API / CODEX

**Python:**

```python
import json
import os
from openai import OpenAI

# Cargar configuración de skills
with open("skills-config.json") as f:
    config = json.load(f)

# Cargar instrucciones del skill
with open("crear-procedimiento.md") as f:
    skill_instructions = f.read()

# Crear cliente
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Llamada a la API
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": skill_instructions
        },
        {
            "role": "user",
            "content": f"""
            Crear procedimiento:
            - Nombre: Solicitud de Permisos
            - Área: RRHH
            - Usuarios: 80
            - Complejidad: Media
            """
        }
    ],
    temperature=0.7,
    max_tokens=2000
)

print(response.choices[0].message.content)
```

**JavaScript:**

```javascript
const fs = require('fs');
const OpenAI = require('openai');

const skillContent = fs.readFileSync('crear-procedimiento.md', 'utf-8');

const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});

async function runSkill() {
  const response = await client.chat.completions.create({
    model: 'gpt-4',
    messages: [
      { role: 'system', content: skillContent },
      { role: 'user', content: 'Crear procedimiento: Solicitud de Vacaciones' }
    ]
  });
  
  console.log(response.choices[0].message.content);
}

runSkill();
```

---

### OTROS LLM (Gemini, Llama, etc)

**Paso universal:**

```
1. Copiar contenido del archivo .md del skill
2. Usarlo como "system prompt" en la API del LLM:

system_prompt = open("crear-procedimiento.md").read()

response = llm.generate(
    system=system_prompt,
    user_input="Crear procedimiento: [nombre]"
)
```

---

## 🔄 FLUJO DE TRABAJO RECOMENDADO

### Para Crear Nuevo Procedimiento:

```
┌─────────────────────────────────────────────┐
│  START: Necesito crear un procedimiento    │
└────────────┬────────────────────────────────┘
             │
             ▼
    ┌──────────────────────┐
    │ /plantilla-rapida    │ (1 min)
    │ Obtener template     │
    └──────────┬───────────┘
             │
             ▼
    ┌──────────────────────┐
    │ /crear-procedimiento │ (10-14 días)
    │ Redactar completo    │
    └──────────┬───────────┘
             │
             ▼
    ┌──────────────────────┐
    │ /validar-legalidad   │ (3-5 días)
    │ Revisar legal        │
    └──────────┬───────────┘
             │
             ▼
    ┌──────────────────────┐
    │ /implementar-proc    │ (8 semanas)
    │ Lanzar a institución │
    └──────────┬───────────┘
             │
             ▼
┌────────────────────────────────────────┐
│  END: Procedimiento operativo          │
└────────────────────────────────────────┘
```

---

### Para Optimizar Procedimiento Existente:

```
┌─────────────────────────────────────────────┐
│  START: Mejorar procedimiento existente    │
└────────────┬────────────────────────────────┘
             │
             ▼
    ┌──────────────────────┐
    │ /optimizar-proc      │ (14 días)
    │ Mejorar eficiencia   │
    └──────────┬───────────┘
             │
             ▼
    ┌──────────────────────┐
    │ /validar-legalidad   │ (3-5 días)
    │ Revisar cambios      │
    └──────────┬───────────┘
             │
             ▼
    ┌──────────────────────┐
    │ /implementar-proc    │ (8 semanas)
    │ Lanzar versión 2.0   │
    └──────────┬───────────┘
             │
             ▼
┌────────────────────────────────────────┐
│  END: Procedimiento mejorado            │
└────────────────────────────────────────┘
```

---

## 📋 ARCHIVOS DE CONFIGURACIÓN

### `skills-config.json`
**Qué es:** Configuración de todos los skills en formato máquina  
**Para qué:** APIs, integraciones automatizadas  
**Contiene:**
- Lista de skills
- Parámetros entrada/salida
- Dependencias
- Flujos de ejecución

---

### `skills-manifest.yaml`
**Qué es:** Manifiesto para herramientas CI/CD  
**Para qué:** Deployment, automatización  
**Contiene:**
- Versión del sistema
- Dependencias
- Health checks

---

## ✅ CHECKLIST: LISTA PARA USAR

- [x] Skill 1: Crear Procedimiento - Operativo
- [x] Skill 2: Implementar Procedimiento - Operativo
- [x] Skill 3: Validar Legalidad - Operativo
- [x] Skill 4: Optimizar Procedimiento - Operativo
- [x] Skill 5: Plantilla Rápida - Operativo
- [x] Configuración JSON - Completa
- [x] Documentación - Completa
- [x] Compatible Claude Code - ✅
- [x] Compatible GitHub Copilot - ✅
- [x] Compatible ChatGPT/Claude.ai - ✅
- [x] Compatible APIs - ✅

---

## 🎯 PRÓXIMOS PASOS

**Inmediato (Esta semana):**
1. Prueba cada skill en tu LLM favorito
2. Ajusta según tus necesidades
3. Comienza con primer procedimiento

**Corto plazo (Este mes):**
1. Crea 2-3 procedimientos prioritarios
2. Capacita a tu equipo
3. Implementa en institución

**Mediano plazo (Este trimestre):**
1. Optimiza procedimientos existentes
2. Expande a 5+ procedimientos
3. Automatiza flujos si es posible

---

## 📞 SOPORTE

**Responsable:** Yisairis  
**Problemas:** Email a Yisairis  
**Tiempo respuesta:** Máximo 24 horas  

**Información de contacto:**
- Email: [Email]
- Teléfono: [Teléfono]
- Horario: Lunes-Viernes 9am-5pm

---

## 📚 DOCUMENTACIÓN RELACIONADA

| Documento | Propósito |
|-----------|-----------|
| `README.md` | Introducción general |
| `REFERENCIA_RAPIDA.md` | Preguntas frecuentes |
| `FILOSOFIA_EFICIENCIA.md` | Principios de diseño |
| `MATRIZ_LEGALIDAD.md` | Validación legal |
| `HOJA_DE_RUTA.md` | Planificación 12 meses |
| `skills-config.json` | Configuración técnica |

---

*Sistema de Skills Universal - Yisairis*  
*Funciona en todos los LLM existentes*
