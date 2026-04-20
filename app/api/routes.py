from fastapi import APIRouter, Depends, status

from app.core.config import Settings, get_settings
from app.models.schemas import ContactRequest, LeadRequest, SubmissionResponse
from app.services.lead_service import get_services, handle_contact_submission, handle_lead_submission

router = APIRouter()


@router.get('/services')
def list_services() -> dict:
    return {'items': get_services()}


@router.post('/contact', response_model=SubmissionResponse, status_code=status.HTTP_202_ACCEPTED)
def create_contact(payload: ContactRequest) -> SubmissionResponse:
    handle_contact_submission(payload)
    return SubmissionResponse(status='accepted', message='Contact request received.')


@router.post('/lead', response_model=SubmissionResponse, status_code=status.HTTP_202_ACCEPTED)
def create_lead(payload: LeadRequest) -> SubmissionResponse:
    handle_lead_submission(payload)
    return SubmissionResponse(status='accepted', message='Lead captured successfully.')


@router.get('/config-preview')
def config_preview(settings: Settings = Depends(get_settings)) -> dict:
    return {'app_name': settings.app_name, 'environment': settings.app_env}
