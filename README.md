# Azure Web App Deployment Using GitHub Actions — Azure DevOps Project

Azure App Service | GitHub Actions | Python Flask | CI/CD | Azure CLI | GitHub OIDC

Build and deploy a modern, responsive Python Flask web application to Microsoft Azure App Service using GitHub Actions. Every push to the `main` branch will automatically trigger a CI/CD pipeline.

Beginner to Intermediate

Hands-on Project

Portfolio Ready

## 1. Project overview

| Field          | Details                                 |
| -------------- | --------------------------------------- |
| Project title  | Azure Web App CI/CD with GitHub Actions |
| Repository     | `azure-webapp-github-actions`           |
| Cloud          | Microsoft Azure                         |
| Application    | Python Flask                            |
| Frontend       | HTML5, CSS3, JavaScript                 |
| Hosting        | Azure App Service (Linux)               |
| CI/CD          | GitHub Actions                          |
| Authentication | OpenID Connect (OIDC)                   |
| Monitoring     | Azure App Service Logs                  |
| Deployment     | Automatic on push to `main`             |

Objective: Develop a modern web application, store its source code in GitHub, configure a secure GitHub Actions pipeline, and automatically deploy the application to Azure App Service.

## 2. CI/CD architecture

Push code → Trigger workflow → Build and test → Deploy → Access website

## 3. Prerequisites

| Tool               | Purpose                           |
| ------------------ | --------------------------------- |
| Azure Subscription | Host the web application          |
| GitHub Account     | Source control and CI/CD          |
| Azure CLI          | Create and manage Azure resources |
| Git                | Version control                   |
| Python 3.11+       | Run Flask locally                 |
| VS Code            | Develop application               |

Install the required tools on macOS:

```
brew install azure-cli
brew install git
brew install python
```

Verify installation:

```
az version
git --version
python3 --version
```

Login to Azure:

```
az login

az account show --output table
```

## 4. Project folder structure

```
azure-webapp-github-actions/
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
├── tests/
│   └── test_app.py
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

Create the structure:

```
mkdir azure-webapp-github-actions
cd azure-webapp-github-actions

mkdir -p .github/workflows
mkdir -p templates
mkdir -p static/css
mkdir -p static/js
mkdir -p tests

touch app.py requirements.txt
touch templates/index.html
touch static/css/style.css
touch static/js/script.js
touch tests/test_app.py
touch .github/workflows/deploy.yml
touch README.md .gitignore

code .
```

## 5. Application source code

The application will provide a modern cloud dashboard, responsive layout, deployment status, technology cards, and a health-check API.

File: `app.py`

```
from flask import Flask, jsonify, render_templatefrom datetime import datetime, timezoneimport osapp = Flask(__name__)@app.route("/")def home():    return render_template(        "index.html",        app_name="Azure Cloud Dashboard",        environment=os.getenv("APP_ENV", "Production")    )@app.route("/health")def health():    return jsonify({        "status": "healthy",        "service": "azure-webapp",        "timestamp": datetime.now(timezone.utc).isoformat()    }), 200@app.route("/api/info")def info():    return jsonify({        "application": "Azure Cloud Dashboard",        "platform": "Azure App Service",        "framework": "Flask",        "cicd": "GitHub Actions",        "version": "1.0.0"    })if __name__ == "__main__":    app.run(        host="0.0.0.0",        port=int(os.getenv("PORT", 8000))    )
```

File: `requirements.txt`

```

Flask>=3.1,<4.0
gunicorn>=23,<24
pytest>=8,<10

```

## 6. Modern application UI

[Nife Labs · GitHub](https://images.openai.com/static-rsc-4/lAJyNMhJ8pxEb6AsL9tj7SE04A4V9vJM2MAmrXfqwhnpPx0kxB6yUzcgk-gSEYSlwhXFAlK-l_XwPZubBcZ0YEHpd65tIqVU6c9Knc4QUanf0l_1cyBa3zWxZx3bQU9IjKV1JIhp00ek8e8iPkPCgjhjGB04X_-rSA6j7zd5f-M?purpose=inline)

[github.com](https://github.com/nifetency)

Visual design reference for the dashboard interface.

File: `templates/index.html`

```

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport"
        content="width=device-width, initial-scale=1">
  <title>Azure Cloud Dashboard</title>
  <link rel="stylesheet"
        href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
  <header class="navbar">
    <div class="brand">☁ Cloud Dashboard</div>
    <span class="pill">● Azure App Service</span>
  </header>

  <main class="container">
    <section class="hero">
      <span class="eyebrow">CLOUD DEVOPS PROJECT</span>
      <h1>Deploy Smarter.<br>
        <span>Scale Faster.</span>
      </h1>
      <p>
        A modern Python Flask application deployed to
        Microsoft Azure using GitHub Actions CI/CD.
      </p>
      <div class="actions">
        <a href="/health" class="button">Check Health ↗</a>
        <a href="/api/info" class="button secondary">
          View API ↗
        </a>
      </div>
    </section>

    <section class="stats">
      <article class="card">
        <div class="card-icon">☁</div>
        <h3>Cloud Platform</h3>
        <strong>Microsoft Azure</strong>
        <p>Managed App Service hosting</p>
      </article>

      <article class="card">
        <div class="card-icon">⚙</div>
        <h3>CI/CD Pipeline</h3>
        <strong>GitHub Actions</strong>
        <p>Automated build and deployment</p>
      </article>

      <article class="card">
        <div class="card-icon">🐍</div>
        <h3>Backend</h3>
        <strong>Python Flask</strong>
        <p>REST API and web application</p>
      </article>
    </section>

    <section class="status-panel">
      <div>
        <h2>Application Status</h2>
        <p>Live health check from Flask API</p>
      </div>
      <div>
        <span id="status" class="status">Checking...</span>
        <p id="checked-at"></p>
      </div>
    </section>

    <footer>
      <p>Azure Cloud Dashboard · DevOps Project</p>
      <p>Environment: {{ environment }}</p>
    </footer>
  </main>

  <script src="{{ url_for('static',
                         filename='js/script.js') }}"></script>
</body>
</html>

```

File: `static/css/style.css`

```

:root {
  --bg: #07111f;
  --card: #111e30;
  --border: #26384f;
  --text: #f1f5f9;
  --muted: #9caec5;
  --accent: #38bdf8;
}

* { box-sizing: border-box; }

body {
  margin: 0;
  background: radial-gradient(
    ellipse at top, #16345b, var(--bg) 65%
  );
  color: var(--text);
  font-family: Inter, system-ui, Arial, sans-serif;
  min-height: 100vh;
}

.navbar {
  max-width: 1180px;
  margin: auto;
  padding: 26px 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}

.brand {
  font-size: 20px;
  font-weight: 800;
}

.pill, .status {
  padding: 9px 15px;
  border-radius: 50px;
  background: #123b37;
  color: #65f2c2;
  font-size: 13px;
  font-weight: 700;
}

.container {
  max-width: 1180px;
  margin: auto;
  padding: 20px 24px;
}

.hero {
  text-align: center;
  padding: 85px 0 75px;
}

.eyebrow {
  color: var(--accent);
  letter-spacing: 3px;
  font-size: 12px;
  font-weight: 700;
}

h1 {
  font-size: clamp(42px, 7vw, 78px);
  line-height: 1.12;
  letter-spacing: -2px;
  margin: 20px 0;
}

h1 span {
  background: linear-gradient(90deg, #38bdf8, #818cf8);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.hero p {
  max-width: 620px;
  margin: 0 auto 30px;
  color: var(--muted);
  line-height: 1.8;
}

.actions {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 14px;
}

.button {
  background: var(--accent);
  color: #061525;
  padding: 14px 24px;
  border-radius: 10px;
  text-decoration: none;
  font-weight: 700;
}

.button.secondary {
  background: transparent;
  color: white;
  border: 1px solid var(--border);
}

.stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}

.card, .status-panel {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 28px;
}

.card-icon { font-size: 32px; }

.card h3 {
  color: var(--muted);
  font-size: 14px;
  margin-top: 24px;
}

.card strong { font-size: 21px; }

.card p, .status-panel p, footer {
  color: var(--muted);
}

.status-panel {
  margin-top: 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
}

footer {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  padding: 35px 0;
  font-size: 13px;
}

@media (max-width: 700px) {
  .stats { grid-template-columns: 1fr; }
  .status-panel, footer {
    flex-direction: column;
    align-items: flex-start;
  }
  .hero { padding: 55px 0; }
  .navbar { flex-wrap: wrap; }
}

```

File: `static/js/script.js`

```

async function checkHealth() {
  const status = document.getElementById("status");
  const checkedAt = document.getElementById("checked-at");

  try {
    const response = await fetch("/health", {
      cache: "no-store"
    });

    if (!response.ok) throw new Error("Health check failed");

    const data = await response.json();
    status.textContent = data.status === "healthy"
      ? "● Healthy"
      : "● Degraded";

    checkedAt.textContent =
      "Last checked: " + new Date().toLocaleTimeString();
  } catch (error) {
    status.textContent = "● Unavailable";
    status.style.color = "#fca5a5";
  }
}

checkHealth();
setInterval(checkHealth, 30000);

```

## 7. Run application locally

Create and activate Python virtual environment:

```
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python app.py
```

Open:

[http://localhost:8000](http://localhost:8000)

Test the APIs:

```
curl http://localhost:8000/

curl http://localhost:8000/health

curl http://localhost:8000/api/info
```

Expected health response:

```
{
  "status": "healthy",
  "service": "azure-webapp",
  "timestamp": "2026-10-09T09:00:00+00:00"
}
```

## 8. Create automated application tests

File: `tests/test_app.py`

```
import pytestfrom app import app@pytest.fixturedef client():    app.config["TESTING"] = True    with app.test_client() as client:        yield clientdef test_home(client):    response = client.get("/")    assert response.status_code == 200    assert b"Cloud Dashboard" in response.datadef test_health(client):    response = client.get("/health")    assert response.status_code == 200    assert response.json["status"] == "healthy"def test_api_info(client):    response = client.get("/api/info")    assert response.status_code == 200    assert response.json["platform"] == "Azure App Service"
```

Run tests:

```
python -m pytest -v
```

## 9. Create Azure infrastructure

Choose a globally unique App Service name. The example below uses `cloudnautic-flask-webapp-98600`; replace it if unavailable.

Set project variables

```
export RESOURCE_GROUP="rg-github-actions-webapp"
export LOCATION="centralindia"
export APP_PLAN="asp-github-actions"
export WEBAPP_NAME="cloudnautic-flask-webapp-98600"
```

Create Resource Group

```
az group create \
  --name "$RESOURCE_GROUP" \
  --location "$LOCATION"
```

Create Linux App Service Plan

```
az appservice plan create \
  --name "$APP_PLAN" \
  --resource-group "$RESOURCE_GROUP" \
  --location "$LOCATION" \
  --sku B1 \
  --is-linux
```

Create Python Web App

```
az webapp create \
  --resource-group "$RESOURCE_GROUP" \
  --plan "$APP_PLAN" \
  --name "$WEBAPP_NAME" \
  --runtime "PYTHON:3.11"
```

Check supported Python runtimes if the requested runtime is unavailable:

```
az webapp list-runtimes --os linux
```

Configure application settings and startup

```
az webapp config appsettings set \
  --resource-group "$RESOURCE_GROUP" \
  --name "$WEBAPP_NAME" \
  --settings APP_ENV=Production SCM_DO_BUILD_DURING_DEPLOYMENT=true
```

```
az webapp config set \
  --resource-group "$RESOURCE_GROUP" \
  --name "$WEBAPP_NAME" \
  --startup-file "gunicorn --bind=0.0.0.0:8000 app:app"
```

Enable HTTPS-only:

```
az webapp update \
  --resource-group "$RESOURCE_GROUP" \
  --name "$WEBAPP_NAME" \
  --https-only true
```

Check application:

```
az webapp show \
  --resource-group "$RESOURCE_GROUP" \
  --name "$WEBAPP_NAME" \
  --query "{name:name,state:state,url:defaultHostName}" \
  --output table
```

The B1 tier is billable. You can remove the resource group after completing the lab.

## 10. Configure GitHub repository

Create a new repository on GitHub:

[Create GitHub repository](https://github.com/new)

Repository name: `azure-webapp-github-actions`

File: `.gitignore`

```

venv/
.venv/
__pycache__/
*.pyc
.pytest_cache/
.env
.DS_Store

```

Push your application:

```
git init
git branch -M main

git add .
git commit -m "Initial Flask Azure WebApp project"

git remote add origin \
  https://github.com/atulkamble/azure-webapp-github-actions.git

git push -u origin main
```

Create the GitHub repository first, and ensure the remote URL matches your repository.

## 11. Configure secure Azure authentication (OIDC)

Microsoft recommends OpenID Connect for GitHub Actions because it avoids storing long-lived Azure client secrets.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://learn.microsoft.com\&sz=32)

Microsoft Learn

+1



### Step A — Create a Microsoft Entra application

```
export GITHUB_OWNER="atulkamble"
export GITHUB_REPO="azure-webapp-github-actions"

export SUBSCRIPTION_ID=$(az account show --query id -o tsv)
export TENANT_ID=$(az account show --query tenantId -o tsv)

export CLIENT_ID=$(az ad app create \
  --display-name "github-actions-azure-webapp" \
  --query appId -o tsv)

az ad sp create --id "$CLIENT_ID"
```

### Step B — Assign Azure RBAC permissions

```
export WEBAPP_ID=$(az webapp show \
  --resource-group "$RESOURCE_GROUP" \
  --name "$WEBAPP_NAME" \
  --query id -o tsv)

export SP_OBJECT_ID=$(az ad sp show \
  --id "$CLIENT_ID" \
  --query id -o tsv)

az role assignment create \
  --assignee-object-id "$SP_OBJECT_ID" \
  --assignee-principal-type ServicePrincipal \
  --role "Website Contributor" \
  --scope "$WEBAPP_ID"
```

Your Azure account needs permission to create app registrations and role assignments.

### Step C — Configure GitHub federated credential

```
cat > federated-credential.json <<EOF
{
  "name": "github-main",
  "issuer": "https://token.actions.githubusercontent.com",
  "subject": "repo:${GITHUB_OWNER}/${GITHUB_REPO}:ref:refs/heads/main",
  "description": "GitHub Actions main branch deployment",
  "audiences": [
    "api://AzureADTokenExchange"
  ]
}
EOF

az ad app federated-credential create \
  --id "$CLIENT_ID" \
  --parameters federated-credential.json

rm federated-credential.json
```

### Step D — Add GitHub Actions secrets

Open your GitHub repository:

Settings → Secrets and variables → Actions → New repository secret

| Secret                  | Value              |
| ----------------------- | ------------------ |
| `AZURE_CLIENT_ID`       | `$CLIENT_ID`       |
| `AZURE_TENANT_ID`       | `$TENANT_ID`       |
| `AZURE_SUBSCRIPTION_ID` | `$SUBSCRIPTION_ID` |

Display the values locally:

```
echo "AZURE_CLIENT_ID=$CLIENT_ID"
echo "AZURE_TENANT_ID=$TENANT_ID"
echo "AZURE_SUBSCRIPTION_ID=$SUBSCRIPTION_ID"
```

These three identifiers are not passwords. The federated trust determines which GitHub repository and branch can authenticate.

## 12. Create GitHub Actions CI/CD pipeline

File: `.github/workflows/deploy.yml`

This pipeline performs automated testing before deploying. It uses `azure/login@v2` and `azure/webapps-deploy@v3`, following Microsoft's App Service deployment pattern.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub

+1



```

name: Azure WebApp CI/CD

on:
  push:
    branches:
      - main
  workflow_dispatch:

permissions:
  contents: read
  id-token: write

env:
  AZURE_WEBAPP_NAME: cloudnautic-flask-webapp-98600
  PYTHON_VERSION: "3.11"

jobs:
  build-and-test:
    name: Build and Test
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: ${{ env.PYTHON_VERSION }}

      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run Unit Tests
        run: python -m pytest -v

      - name: Package Application
        run: |
          zip -r app.zip \
            app.py requirements.txt templates static \
            -x "*/__pycache__/*"

      - name: Upload Build Artifact
        uses: actions/upload-artifact@v4
        with:
          name: flask-app
          path: app.zip

  deploy:
    name: Deploy to Azure
    runs-on: ubuntu-latest
    needs: build-and-test

    steps:
      - name: Download Build Artifact
        uses: actions/download-artifact@v4
        with:
          name: flask-app

      - name: Azure Login using OIDC
        uses: azure/login@v2
        with:
          client-id: ${{ secrets.AZURE_CLIENT_ID }}
          tenant-id: ${{ secrets.AZURE_TENANT_ID }}
          subscription-id: ${{ secrets.AZURE_SUBSCRIPTION_ID }}

      - name: Deploy to Azure App Service
        uses: azure/webapps-deploy@v3
        with:
          app-name: ${{ env.AZURE_WEBAPP_NAME }}
          package: app.zip

      - name: Verify Deployment
        run: |
          URL="https://${{ env.AZURE_WEBAPP_NAME }}.azurewebsites.net/health"

          for attempt in {1..12}; do
            if curl --fail --silent --show-error "$URL"; then
              exit 0
            fi
            echo "Waiting for application startup..."
            sleep 10
          done

          echo "Health check failed"
          exit 1

```

Replace `AZURE_WEBAPP_NAME` with the exact name of your deployed Azure Web App. The workflow assumes that App Service build automation has been enabled in Step 9.

## 13. Execute CI/CD deployment

Commit the workflow:

```
git add .
git commit -m "Configure Azure GitHub Actions CI/CD"
git push origin main
```

Go to:

[GitHub Actions workflow dashboard](https://github.com/atulkamble/azure-webapp-github-actions/actions)

Expected pipeline execution

1. Build and Test

   Checkout → Python Setup → Dependencies → Unit Tests → Package → Artifact
2. Deploy to Azure

   Download Artifact → Azure OIDC Login → App Service Deployment → Health Check

Both jobs should finish successfully before considering deployment complete.

## 14. Verify Azure Web App

EXPECTED WEBSITE URL

[https://cloudnautic-flask-webapp-98600.azurewebsites.net](https://cloudnautic-flask-webapp-98600.azurewebsites.net)

&#x20;Copy

This URL will work once the named App Service is successfully created and deployed.

Test deployment:

```
curl -I "https://${WEBAPP_NAME}.azurewebsites.net"

curl "https://${WEBAPP_NAME}.azurewebsites.net/health"

curl "https://${WEBAPP_NAME}.azurewebsites.net/api/info"
```

Check application status:

```
az webapp show \
  --resource-group "$RESOURCE_GROUP" \
  --name "$WEBAPP_NAME" \
  --query "{name:name,state:state,host:defaultHostName}" \
  -o table
```

## 15. Enable monitoring and troubleshoot

Enable application logs:

```
az webapp log config \
  --resource-group "$RESOURCE_GROUP" \
  --name "$WEBAPP_NAME" \
  --application-logging filesystem \
  --level information
```

Stream logs:

```
az webapp log tail \
  --resource-group "$RESOURCE_GROUP" \
  --name "$WEBAPP_NAME"
```

Restart application:

```
az webapp restart \
  --resource-group "$RESOURCE_GROUP" \
  --name "$WEBAPP_NAME"
```

| Error                                   | Possible cause                  | Solution                                     |
| --------------------------------------- | ------------------------------- | -------------------------------------------- |
| 403 during deployment                   | Missing Azure RBAC permission   | Verify Website Contributor assignment        |
| OIDC login failure                      | Incorrect federated credential  | Verify GitHub repository and branch subject  |
| 502 / 503                               | Application failed to start     | Check Gunicorn startup and logs              |
| `ModuleNotFoundError`                   | Dependencies not installed      | Verify `requirements.txt` and build settings |
| Deployment successful, site not updated | Startup or deployment issue     | Review deployment and application logs       |
| Health check failed                     | App still starting or unhealthy | Review logs and test `/health`               |

## 16. Demonstrate continuous deployment

Update the application title in `templates/index.html`:

```
<h1>Azure DevOps Deployment<br>
  <span>Version 2.0</span>
</h1>
```

Commit and push:

```
git add .
git commit -m "Release v2.0 dashboard"
git push origin main
```

GitHub Actions will automatically build, test, and deploy the new version.

## 17. Project completion checklist

Deployment progress

0 / 10

Flask application runs locally

All unit tests pass

Azure Resource Group created

Linux App Service Plan created

Azure Web App created

GitHub repository configured

OIDC federation and RBAC configured

GitHub Actions secrets configured

CI/CD pipeline succeeds

Website and health endpoint verified

## 18. Cleanup Azure resources

After completing the lab, delete the resource group to stop App Service charges:

```
az group delete \
  --name "$RESOURCE_GROUP" \
  --yes \
  --no-wait
```

This deletes all Azure resources in that resource group. The GitHub repository remains intact.

## 19. Resume-ready project description

Project: Automated Azure App Service Deployment using GitHub Actions

Technologies: Microsoft Azure, App Service, Python, Flask, GitHub Actions, Git, Azure CLI, OIDC, Microsoft Entra ID, Azure RBAC.

Developed and deployed a responsive Python Flask web application on Azure App Service. Implemented an automated CI/CD pipeline using GitHub Actions with unit testing, build artifact packaging, and deployment verification. Configured secure, secretless Azure authentication using OpenID Connect and Microsoft Entra ID, with role-based access control and application health monitoring.

Official references: [Azure App Service GitHub Actions documentation](https://learn.microsoft.com/en-us/azure/app-service/deploy-github-actions) and [Deploy Python to Azure using GitHub Actions](https://learn.microsoft.com/en-us/azure/developer/python/python-web-app-github-actions-app-service).
