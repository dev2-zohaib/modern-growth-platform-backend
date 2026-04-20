from typing import Literal

from pydantic import BaseModel, EmailStr, Field, HttpUrl


class ServiceItem(BaseModel):
    slug: str
    title: str
    summary: str
    audience: list[str]


class ContactRequest(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    email: EmailStr
    company: str | None = Field(default=None, max_length=120)
    message: str = Field(min_length=10, max_length=2000)
    budget_range: str | None = Field(default=None, max_length=50)


class LeadRequest(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    email: EmailStr
    company: str = Field(min_length=2, max_length=120)
    website: HttpUrl | None = None
    business_type: Literal['startup', 'ecommerce', 'saas', 'regional_service']
    monthly_ad_spend: int | None = Field(default=None, ge=0)
    goals: list[str] = Field(default_factory=list, max_length=10)


class SubmissionResponse(BaseModel):
    status: str
    message: str
