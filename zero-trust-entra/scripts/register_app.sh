#!/usr/bin/env bash
set -euo pipefail
echo "Creating app registration (you will need to set CLIENT_SECRET output as env var)..."
APP_NAME="zero-trust-demo-app"
az ad app create --display-name "$APP_NAME" --reply-urls "http://localhost:8080/getAToken" --available-to-other-tenants false > /tmp/app.json
APP_ID=$(jq -r '.appId' /tmp/app.json)
echo "AppId: $APP_ID"
SECRET_JSON=$(az ad app credential reset --id $APP_ID --append --credential-description "dev-secret" --years 1)
CLIENT_SECRET=$(echo $SECRET_JSON | jq -r '.password')
echo "Client secret created. Set CLIENT_ID=$APP_ID and CLIENT_SECRET accordingly."
