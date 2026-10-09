# Azure Web App Deployment Using GitHub Actions

This project is a Python Flask dashboard application deployed to Azure App Service, with automated CI/CD through GitHub Actions.

## Technical stack

- Backend: Python 3.11, Flask 3.x
- Frontend: HTML5, CSS3, JavaScript
- Testing: Pytest
- Deployment target: Microsoft Azure App Service (Linux)
- CI/CD: GitHub Actions
- Authentication: Azure OIDC (OpenID Connect) for secure GitHub-to-Azure login
- Runtime packaging: Gunicorn
- Infrastructure tooling: Azure CLI

## Project overview

- Modern cloud dashboard UI with Azure-inspired styling
- Health-check endpoint for monitoring and status validation
- Metadata API endpoint for deployment information
- Automated build and deploy workflow triggered on pushes to `main`
- Azure-hosted deployment using App Service and GitHub Actions

## Project structure

- `app.py` — Flask application and routes
- `requirements.txt` — Python dependencies
- `templates/index.html` — dashboard layout
- `static/css/style.css` — custom styling
- `static/js/script.js` — frontend health-check logic
- `tests/test_app.py` — unit tests for application routes
- `.github/workflows/deploy.yml` — CI/CD workflow for Azure deployment
- `.gitignore` — ignore rules for local environment files

## Local development

1. Create and activate a virtual environment.
2. Install dependencies.
3. Run the app locally.
4. Open <http://localhost:8000>

Example commands:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Application endpoints:

- `/` — dashboard page
- `/health` — health-check API returning service status
- `/api/info` — deployment metadata JSON

## Validation

Run the following command from the project root:

```bash
python -m pytest -v
```

## Deployment notes

The GitHub Actions workflow builds the app, runs tests, packages the app, logs into Azure using OIDC, and deploys the artifact to Azure App Service.

This project was generated from the original tutorial and the long embedded code samples were removed from the README after the implementation files were created.
