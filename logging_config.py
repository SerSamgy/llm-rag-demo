import os
from typing import Any

from dotenv import load_dotenv

load_dotenv()


class Dummy:
    pass


def my_json_default(obj: Any) -> Any:
    if isinstance(obj, Dummy):
        return "DUMMY"
    return obj


# def get_version_metadata():
#     # https://stackoverflow.com/a/78082532
#     version = importlib.metadata.version(PROJECT_NAME)
#     return version


PROJECT_NAME = os.environ.get("APP_NAME", "RAGDock")
# PROJECT_VERSION = get_version_metadata()
# TODO: Make the PROJECT_VERSION dynamic
PROJECT_VERSION = "0.0.1"
ENVIRONMENT = os.environ.get("ENV", "local")
