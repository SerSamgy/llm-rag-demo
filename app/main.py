from fastapi import FastAPI

from app.api.routes_health import router as health_router
from app.core.config import get_settings
from app.core.logging import setup_logging

settings = get_settings()
setup_logging(settings.log_level)

is_debug = True if settings.log_level == "DEBUG" else False

app = FastAPI(title=settings.app_name, debug=is_debug)

app.include_router(health_router)
