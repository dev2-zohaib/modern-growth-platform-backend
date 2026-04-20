# Modern Growth Platform Backend

Production-ready starter repository for an AWS-based informational business website backend. The system is designed for startups, e-commerce brands, SaaS companies, and regional service businesses, with future-ready foundations for analytics, campaign reporting, CRM/ad platform integrations, automation workflows, and internal APIs.

## Highlights

- FastAPI backend with structured validation, error handling, and logging
- Informational and lead-capture endpoints: `/health`, `/api/v1/services`, `/api/v1/contact`, `/api/v1/lead`
- Environment-based configuration via `.env`
- Dockerized local/runtime packaging
- Terraform infrastructure for AWS networking, security, compute, S3, IAM, and CloudWatch logging
- Deployment helper scripts for local setup and AWS deployment
- Unit tests and API test scaffolding with `pytest`
- Developer-facing docs and architecture notes

## Repository Structure

```text
app/
  api/routes.py
  core/config.py
  core/errors.py
  core/logging.py
  main.py
  models/schemas.py
  services/lead_service.py
infra/
  terraform/
docs/
scripts/
tests/
```

## Architecture Summary

- **Application**: FastAPI service with versioned API routes
- **Validation**: Pydantic request/response schemas
- **Observability**: JSON logging plus request correlation middleware
- **Infrastructure**: Terraform provisions a practical AWS starter footprint:
  - VPC with public subnets
  - Security group for application ingress
  - ECS Fargate service and ECR repository for container deployment
  - CloudWatch log group
  - S3 bucket for assets/uploads
  - IAM execution/task roles
  - Route53/ACM placeholders for future domain/TLS wiring

## Assumptions

- Branding, exact service list, and domain values are not finalized, so placeholders are used.
- Initial deployment target uses **ECS Fargate** for scalable container hosting.
- Contact and lead submission persistence is currently implemented as structured logging and optional webhook forwarding placeholder, ready for future integrations with CRMs or messaging systems.
- Terraform uses placeholder CIDRs and domain variables that should be adjusted per environment.

## Local Setup

1. Create and activate a Python 3.12 virtual environment.
2. Copy environment template:
   ```bash
   cp .env.example .env
   ```
3. Install dependencies:
   ```bash
   make install
   ```
4. Run locally:
   ```bash
   make run
   ```
5. Open docs at [http://localhost:8000/docs](http://localhost:8000/docs).

## Testing

Run:

```bash
make test
```

## Docker

Build and run:

```bash
docker build -t modern-growth-platform-backend .
docker run --rm -p 8000:8000 --env-file .env modern-growth-platform-backend
```

## AWS Deployment

### Main entry points

- Application entry point: `app/main.py`
- Infrastructure entry point: `infra/terraform`
- Deploy helper: `scripts/deploy.sh`

### Deployment workflow

1. Ensure AWS CLI, Docker, and Terraform are installed and authenticated.
2. Update `.env` and Terraform variables.
3. Build and push the application image to ECR.
4. Apply Terraform.
5. Update ECS service to use the new image.

Example:

```bash
cd infra/terraform
cp terraform.tfvars.example terraform.tfvars
terraform init
terraform plan
terraform apply
```

Then:

```bash
bash scripts/deploy.sh
```

## Environment Variables

See `.env.example` for defaults. Key settings include:

- `APP_ENV`
- `APP_DEBUG`
- `APP_HOST`
- `APP_PORT`
- `LOG_LEVEL`
- `API_PREFIX`
- `ALLOWED_ORIGINS`
- `CONTACT_EMAIL`
- `LEAD_WEBHOOK_URL`
- `AWS_REGION`
- `AWS_ACCOUNT_ID`
- `S3_BUCKET_NAME`

## API Overview

- `GET /health` - service health and environment metadata
- `GET /api/v1/services` - service catalog for the website
- `POST /api/v1/contact` - contact form submission
- `POST /api/v1/lead` - lead capture submission with business context

Detailed API docs are available in `docs/api.md` and via Swagger UI.

## Future Extensions

- CRM sync (HubSpot, Salesforce)
- ad platform connectors (Meta Ads, Google Ads, LinkedIn Ads)
- analytics/reporting ingestion pipelines
- admin authentication and internal dashboards
- async processing with SQS/EventBridge/Lambda
