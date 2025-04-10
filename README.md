# LLM

**LLM** es una librería Python modular orientada a la integración con múltiples modelos de lenguaje (LLMs), proveedores cloud y utilidades auxiliares para desarrollo e infraestructura.

Esta librería está diseñada para facilitar la interacción con LLMs de OpenAI, Azure, Google y Ollama, integrando además autenticación, configuración externa, plantillas Jinja2, y componentes reutilizables.

## Características

- Soporte para múltiples modelos LLM:
  - OpenAI (chat y embeddings)
  - Azure OpenAI
  - Google Generative AI
  - Ollama
  - LangChain y variantes
- Módulos para configuración (`decouple`, `YAML`)
- Autenticación vía Azure Identity
- Generación de contenido vía plantillas Jinja2
- Separación clara de responsabilidades con módulos como:
  - `logger`
  - `security`
  - `auth_clients`
  - `utils`
  - `model_*` (interfaces para distintos LLMs)

## Instalación

Desde PyPI (una vez publicado):

```bash
pip install llm
```

Desde un repositorio:

```bash
pip install git+https://github.com/tu_usuario/mi_libreria.git
```

Instalación local (modo editable para desarrollo):

```bash
git clone https://github.com/tu_usuario/mi_libreria.git
cd llm
pip install -e .
```

## Uso básico

```python
from model_factory.model_OpenAIChat import OpenAIChatModel

modelo = OpenAIChatModel()
respuesta = modelo.chat("¿Cuál es la capital de Francia?")
print(respuesta)
```

> ⚠️ Sustituye `model_factory` por el nombre del submódulo real si cambia.

## Estructura del proyecto

```
mi_libreria/
├── model_factory/
│   ├── __init__.py
│   ├── logger.py
│   ├── utils.py
│   ├── security.py
│   ├── ...
├── pyproject.toml
└── README.md
```

## Requisitos y dependencias

Este paquete requiere las siguientes librerías externas:

- `python-decouple`
- `PyYAML`
- `openai`
- `jinja2`
- `azure-identity`
- `langchain`
- `langchain-openai`
- `langchain-google-genai`
- `langchain-community`
- `langchain-azure-ai`
- `langchain-ollama`

Las dependencias se instalarán automáticamente con `pip`.

## Requisitos del sistema
- Python 3.12 o superior
- Acceso a credenciales/API keys para los proveedores usados (OpenAI, Azure, etc.)
