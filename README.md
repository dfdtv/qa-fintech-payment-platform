# QA FinTech Payment Platform

Pet-project that simulates a FinTech payment platform and demonstrates QA Automation skills (API + UI + contracts + CI).

## Tech stack
- Python, Pytest
- HTTPX, Pydantic
- Playwright
- Docker, docker-compose
- PostgreSQL, Redis, Kafka
- GitHub Actions, Allure

## How to run tests locally
```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install pytest
pytest -q
