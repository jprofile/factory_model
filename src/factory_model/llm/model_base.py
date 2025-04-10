from abc import ABC, abstractmethod
import datetime
import re
from decouple import config
from ..logger import info
from ..config import get_var, kwargs_decouple
from .model_utils import read_template


REGEX_VAR = r"{(.+?)}"


class BaseModel(ABC):
    def __init__(self, config: dict[str, str]):
        self.config = config
        # import os
        # self.model_name = config.get("model_name").format(**os.environ)
        # self.version = config.get("model_version").format(**os.environ)
        # self.api_key = config.get("api_key").format(**os.environ)
        # self.api_auth = config.get("api_auth").format(**os.environ)
        # self.endpoint = config.get("api_endpoint").format(**os.environ)
        # self.params = config.get("model_params", {})

        self.model_name = self.render_var("model_name")
        self.version = self.render_var("model_version")
        if "api_key" in config:
            self.api_key = self.render_var("api_key", cast=str)
        if "api_endpoint" in config:
            self.endpoint = self.render_var("api_endpoint")
        self.api_auth = self.render_var("api_auth", default="service_principal")
        self.params = self.render_var("model_params", default={})

    @abstractmethod
    def initialize_model(self):
        """Implementa la inicialización del modelo de IA."""
        pass

    def prompt(self, params):

        system = params[0]
        input = params[1]

        init = datetime.datetime.now()
        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": input}
        ]

        response = self.client.invoke(messages).content
        info(f"Duración: {str((datetime.datetime.now() - init).total_seconds())} segundos")
        # clean_response = re.sub(r"<think>.*?</think>", "", response, flags=re.DOTALL)
        return response

    def prompt_template(self, path, params: dict):
        return self.prompt(read_template(path, params))

    def embedding(self, text: str):
        raise Exception(f"Model {self.model_name} does not allow embedding")

    def render_var(self, var_name, *args, **kwargs):
        """
        Render environment variable using decouple and applying conventions in value as {kv:VARIABLE}
        """
        # Get decouple arguments
        decouple_kwargs = kwargs_decouple(*args, **kwargs)
        # Property has to exist
        if var_name in self.config:
            property_value: str = self.config.get(var_name)
            if isinstance(property_value, str):
                # Only render string templates
                return self.render_property(property_value, **decouple_kwargs)
            return property_value
        else:
            # Get value using decouple, will throw a ValueError if the variable doesn't exist
            # and it is not configurated a default value
            return config(var_name, **decouple_kwargs)

    def render_property(self, property_value: str, **decouple_kwargs) -> str:
        """
        Render property value or template
        """
        values_list: dict[str, str] = {}
        var_names = re.findall(REGEX_VAR, property_value)
        if var_names:
            # Template found
            for var_name in var_names:
                # Add values from environment variables using decouple
                values_list[var_name] = get_var(var_name=var_name, **decouple_kwargs)
        value = property_value.format(**values_list)
        return value
