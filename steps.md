Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

// Github Actions

azure-pipelines.yml
Jenkinsfile

/workflows/ci.yml

1. Create Github Repo azure-webapp-github-actions
https://github.com/atulkamble/azure-webapp-github-actions.git

2. Clone Repo
git clone https://github.com/atulkamble/azure-webapp-github-actions.git
cd azure-webapp-github-actions

3. mkdir .github
cd .github
mkdir workflows
touch azure-webapps-python.yml

4. create Procfile

gunicorn app:app

http://127.0.0.1:8000

5. Create Resource - Canada Central - webapp

6. Create Azure WebApp Service and Plan

7. Deployment Center >> CI/CD >> Github Actions >> Basic Security Option Select >> OIDC*

8. Deploy Pipeine from Azure WebApp to Github Actions

pythonwebappatul-d5b2hkgxdzabe9e9.canadacentral-01.azurewebsites.net



