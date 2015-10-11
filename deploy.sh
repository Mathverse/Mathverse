#!/usr/bin/env bash

python ChicagoBoothAnalytics_project/manage.py makemigrations
python ChicagoBoothAnalytics_project/manage.py migrate
python ChicagoBoothAnalytics_project/manage.py collectstatic

git add --all

getopts m: git_commit_message
git commit -m "$git_commit_message"

git push --all

eb deploy --no-verify-ssl
