#!/bin/bash

# Verwenden Sie das von GitHub Actions bereitgestellte Token
GITHUB_TOKEN=${GITHUB_TOKEN}

# Setzen Sie den Benutzernamen und den Repository-Namen
GITHUB_REPO="knutdF/DocumentSystem"

# Pfad zur JSON-Datei
JSON_FILE=".github/doc.json"

# Lesen Sie Titel und Body aus der JSON-Datei
ISSUE_TITLE=$(jq -r '.title' "$JSON_FILE")
ISSUE_BODY=$(jq -r '.body' "$JSON_FILE")

# Erstellen Sie das Issue
curl -s -X POST -H "Authorization: token $GITHUB_TOKEN" \
     -H "Accept: application/vnd.github.v3+json" \
     https://api.github.com/repos/$GITHUB_REPO/issues \
     -d "{\"title\":\"$ISSUE_TITLE\", \"body\":\"$ISSUE_BODY\"}"
