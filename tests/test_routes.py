from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_services_endpoint_returns_catalog():
    response = client.get('/api/v1/services')
    assert response.status_code == 200
    data = response.json()
    assert len(data['items']) >= 3


def test_contact_endpoint_accepts_valid_payload():
    response = client.post('/api/v1/contact', json={
        'name': 'Alex Founder',
        'email': 'alex@example.com',
        'company': 'Example SaaS',
        'message': 'We need help with growth analytics and media buying.',
        'budget_range': '$5k-$10k'
    })
    assert response.status_code == 202
    assert response.json()['status'] == 'accepted'


def test_contact_endpoint_rejects_invalid_payload():
    response = client.post('/api/v1/contact', json={'name': 'A', 'email': 'bad-email', 'message': 'short'})
    assert response.status_code == 422


def test_lead_endpoint_accepts_valid_payload():
    response = client.post('/api/v1/lead', json={
        'name': 'Taylor',
        'email': 'taylor@example.com',
        'company': 'Regional Services Co',
        'website': 'https://example.com',
        'business_type': 'regional_service',
        'monthly_ad_spend': 12000,
        'goals': ['lead generation', 'dashboarding']
    })
    assert response.status_code == 202
    assert response.json()['status'] == 'accepted'
