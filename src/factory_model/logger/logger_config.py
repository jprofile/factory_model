from decouple import config as _config

LOGGING_DIR=_config("LOGGING_DIR", "logs")
LOGGING_FILE=_config("LOGGING_FILE", "model-factory.log")
LOGGING_WHEN=_config("LOGGING_WHEN", "midnight")
LOGGING_INTERVAL=_config("LOGGING_INTERVAL", 1)
LOGGING_TITLE=_config("LOGGING_TITLE", "model-factory")
LOGGING_LEVEL=_config("LOGGING_LEVEL", "INFO")
LOGGING_HANDLERS=_config("LOGGING_HANDLERS", "console,file_handlers")
LOGGING_FORMATTER=_config("LOGGING_FORMATTER", 
                          "%(asctime)s - [%(name)s] - %(levelname)-5s - %(message)s")