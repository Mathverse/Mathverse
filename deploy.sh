#!/usr/bin/env bash

python ChicagoBoothAnalytics_project/manage.py makemigrations
python ChicagoBoothAnalytics_project/manage.py migrate
python ChicagoBoothAnalytics_project/manage.py collectstatic

git add --all
git commit -m "deploy changes to AWS EB Django app"
git push --all

eb deploy --no-verify-ssl
