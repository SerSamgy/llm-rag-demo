from typing import Annotated

from fastapi import Depends

from app.core.config import Settings, get_settings


def get_app_settings() -> Settings:
    return get_settings()


type SettingsDep = Annotated[Settings, Depends(get_app_settings)]
