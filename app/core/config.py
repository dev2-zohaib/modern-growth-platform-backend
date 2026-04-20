from functools import lru_cache
from typing import List

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = Field(default="Modern Growth Platform API", alias="APP_NAME")
    app_env: str = Field(default="development", alias="APP_ENV")
    app_debug: bool = Field(default=False, alias="APP_DEBUG")
    app_host: str = Field(default="0.0.0.0", alias="APP_HOST")
    app_port: int = Field(default=8000, alias="APP_PORT")
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")
    api_prefix: str = Field(default="/api/v1", alias="API_PREFIX")
    allowed_origins_raw: str = Field(default="http://localhost:3000", alias="ALLOWED_ORIGINS")
    contact_email: str = Field(default="hello@example.com", alias="CONTACT_EMAIL")
    lead_webhook_url: str | None = Field(default=None, alias="LEAD_WEBHOOK_URL")
    aws_region: str = Field(default="us-east-1", alias="AWS_REGION")
    aws_account_id: str = Field(default="123456789012", alias="AWS_ACCOUNT_ID")
    s3_bucket_name: str = Field(default="modern-growth-platform-assets-example", alias="S3_BUCKET_NAME")

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', case_sensitive=False)

    @property
    def allowed_origins(self) -> List[str]:
        return [origin.strip() for origin in self.allowed_origins_raw.split(',') if origin.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()
