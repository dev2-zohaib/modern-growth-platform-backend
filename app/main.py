import logging
import uuid

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router as api_router
from app.core.config import get_settings
from app.core.errors import register_exception_handlers
from app.core.logging import configure_logging

settings = get_settings()
configure_logging(settings.log_level)
logger = logging.getLogger(__name__)

app = FastAPI(title=settings.app_name, version='0.1.0', docs_url='/docs', redoc_url='/redoc')
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.middleware('http')
async def add_request_context(request: Request, call_next):
    request_id = request.headers.get('x-request-id', str(uuid.uuid4()))
    response = await call_next(request)
    response.headers['x-request-id'] = request_id
    logger.info('request_completed', extra={'path': request.url.path, 'method': request.method, 'request_id': request_id})
    return response


@app.get('/health')
def health() -> dict:
    return {'status': 'ok', 'service': settings.app_name, 'environment': settings.app_env, 'version': '0.1.0'}


app.include_router(api_router, prefix=settings.api_prefix)
register_exception_handlers(app)
