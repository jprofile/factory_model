import os
import json
import yaml
from jinja2 import Template

SEP_PATTERN = "--- message ---"


def load_from_file(file_path: str) -> dict:
    """Carga un archivo JSON o YAML y lo convierte en un diccionario."""

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"El archivo '{file_path}' no existe. ")
    _, ext = os.path.splitext(file_path)
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            if ext.lower() == ".json":
                return json.load(file)
            elif ext.lower() in {".yaml", ".yml"}:
                return yaml.safe_load(file)
            if ext.lower() == ".prompt":
                return file.read()
            else:
                raise ValueError(f"Formato de archivo no soportado: {ext}")
    except Exception as e:
        raise RuntimeError(f"Error al cargar el archivo '{file_path}': {e}")


def read_template(path, params: dict):
    prompt = Template(load_from_file(path), trim_blocks=True, lstrip_blocks=True).render(**params)
    system = prompt[0:prompt.find(SEP_PATTERN)-1]
    input = prompt[prompt.find(SEP_PATTERN) + len(SEP_PATTERN):]
    return (system, input)
