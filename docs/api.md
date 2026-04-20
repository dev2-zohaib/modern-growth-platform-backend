# API Documentation

## Health

### `GET /health`
Returns application status, environment, and version metadata.

## Services

### `GET /api/v1/services`
Returns a curated list of service offerings presented on the website.

## Contact

### `POST /api/v1/contact`
Accepts a website contact form payload.

Example payload:

```json
{
  "name": "Alex Founder",
  "email": "alex@example.com",
  "company": "Example SaaS",
  "message": "We need performance marketing and analytics support.",
  "budget_range": "$5k-$10k"
}
```

## Lead

### `POST /api/v1/lead`
Captures a more detailed lead suitable for future CRM/ad platform workflows.

Example payload:

```json
{
  "name": "Taylor",
  "email": "taylor@example.com",
  "company": "Regional Services Co",
  "website": "https://example.com",
  "business_type": "regional_service",
  "monthly_ad_spend": 12000,
  "goals": ["lead generation", "attribution", "dashboarding"]
}
```
