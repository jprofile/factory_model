# Model Factory

**Model Factory** es una librería Python modular orientada a la integración con múltiples modelos de lenguaje (LLMs), proveedores cloud y utilidades auxiliares para desarrollo e infraestructura.

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
  - `model_*` (interfaces para distintos LLMs)

## Instalación

Desde PyPI (una vez publicado):

```bash
pip install llm
```

Desde un repositorio:

```bash
pip install git+https://github.com/jprofile/model_factory.git
```

Instalación local (modo editable para desarrollo):

```bash
git clone https://github.com/jprofile/model_factory.git
cd llm
pip install -e .
```

## Puesta a punto
Para poder hacer uso de la factoría de modelos es necesario definir una serie de variables de entorno, que permiten la conexión a los distintos servicios de alojamiento de modelos:

```python
AZURE_TENANT_ID = <id_tenant_azure>
AZURE_CLIENT_ID = <id_client_azure>
AZURE_CLIENT_SECRET = <secret_passphrase_azure_client>
AZURE_TOKEN_URL = <azure_url_token_generator>
```

Para un mayor nivel de seguridad, se cuenta con conexión a KeyVault. Para definir la conexión al almacén de claves correspondiente, se debe usar:
```python
KV_NAME = <kv_name>
KV_TENANT_ID = <id_kv_tenant>
KV_CLIENT_ID = <id_kv_client>
KV_SECRET = <secret_passphrase_kv>
```

Con la conexión a KeyVault establecida, los valores que se deben recuperar desde el almacén de claves deben especificarse siguiendo la siguiente nomenclatura:
```
VARIABLE_SECRET = kv{name-of-secret-at-kv}
```

De esta forma, por ejemplo:
```python
# Pasamos de tener el secreto en raw
AZURE_CLIENT_SECRET = <secret_passphrase_azure_client>

# A recuperarlo desde el KV
AZURE_CLIENT_SECRET = kv{<name_secret_azure_client>}
```

Además, si contamos con un fichero en el que tenemos las distintas configuraciones de modelos que deseamos utilizar, debemos indicarlo con su correspondiente variable.
```
MODELS_CONFIG_FILE = <path_to_models_declarations_file>
```

## Uso básico

```python
from factory_model import ModelFactory

model = ModelFactory.get_model('gpt-4o')
respuesta = modelo.invoke("¿Cuál es la capital de Francia?")
print(respuesta)
```

## Estructura del proyecto

```
factory_model/
├── factory_model/
│   ├── __init__.py
│   ├── config/
│   ├── llm/
│   ├── logger/
│   ├── security/
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Requisitos y dependencias

Este paquete requiere las siguientes librerías externas:

- `python-decouple`
- `PyYAML`
- `openai`
- `jinja2`
- `azure-core`
- `azure-identity`
- `azure-keyvault-secrets`
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
