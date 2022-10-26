import logging
from pydantic import BaseSettings, Field, validator


class Settings(BaseSettings):
    NAME: str = 'Redis like application'
    LOG_LEVEL: int = Field(env='APPLICATION_LOG_LEVEL', default=logging.DEBUG)
    ENVIRONMENT: str = Field(default="DEV", env='ENVIRONMENT')


    @validator('LOG_LEVEL')
    def application_log_level_values(cls, value):
        permitted_values = [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]
        if(value not in permitted_values):
            raise ValueError(
                f"Variable 'APPLICATION_LOG_LEVEL' must be one of this values: {', '.join(permitted_values)}"
            )
        return value
