# Architecture Notes

## Backend

The backend uses FastAPI with a clean modular structure:

- `api/` for routes
- `core/` for configuration, logging, middleware, and exception handling
- `models/` for request/response schemas
- `services/` for business logic

## Infrastructure

Terraform provisions a scalable AWS foundation around ECS Fargate so the backend can evolve without replatforming.

## Security and Reliability

- Environment-based configuration
- Minimal input acceptance with Pydantic validation
- Structured JSON logs for operational tooling
- Principle-of-least-privilege IAM roles
- Security group restricted to HTTP ingress placeholder
- S3 public access blocked by default
