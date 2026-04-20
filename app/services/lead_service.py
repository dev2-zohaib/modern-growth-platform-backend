import logging
from app.models.schemas import ContactRequest, LeadRequest

logger = logging.getLogger(__name__)

SERVICES = [
    {
        'slug': 'performance-marketing',
        'title': 'Performance Marketing',
        'summary': 'Paid media strategy and execution focused on measurable pipeline and revenue outcomes.',
        'audience': ['startups', 'ecommerce', 'saas'],
    },
    {
        'slug': 'analytics-attribution',
        'title': 'Analytics & Attribution',
        'summary': 'Measurement architecture, conversion tracking, and decision-ready reporting.',
        'audience': ['startups', 'ecommerce', 'saas', 'regional_service'],
    },
    {
        'slug': 'digital-infrastructure',
        'title': 'Scalable Digital Infrastructure',
        'summary': 'Cloud-native systems and automation foundations for growth operations.',
        'audience': ['saas', 'regional_service', 'ecommerce'],
    },
]


def get_services() -> list[dict]:
    return SERVICES


def handle_contact_submission(payload: ContactRequest) -> None:
    logger.info('contact_submission_received', extra={'email': payload.email, 'company': payload.company})


def handle_lead_submission(payload: LeadRequest) -> None:
    logger.info(
        'lead_submission_received',
        extra={
            'email': payload.email,
            'company': payload.company,
            'business_type': payload.business_type,
            'goals': payload.goals,
        },
    )
