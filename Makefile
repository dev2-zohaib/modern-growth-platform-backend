.PHONY: install run test lint docker-build

install:
	python -m pip install --upgrade pip && pip install -r requirements.txt

run:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

test:
	pytest

docker-build:
	docker build -t modern-growth-platform-backend .
