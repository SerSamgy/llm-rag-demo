import logging

import anyio
import fastapi
import starlette
import uvicorn
from rich.logging import RichHandler


def setup_logging(level: str):
    handler = RichHandler(
        level=level,
        rich_tracebacks=True,
        tracebacks_suppress=[fastapi, uvicorn, starlette, anyio],
    )
    # TODO: Make the ReachHandler to be used for local env only,
    #       use StreamHandler with JSON formatter for the rest of envs.
    #       Check [this](https://nhairs.github.io/python-json-logger/latest/) for out-of-the-box solution.
    # handler.setFormatter(JsonFormatter())

    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    root_logger.handlers = [handler]
