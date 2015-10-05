#!/usr/bin/env bash

python DjangoProject/manage.py makemigrations
python DjangoProject/manage.py migrate
python DjangoProject/manage.py collectstatic

git add --all
git commit -m "deploy changes to AWS EB Django app"
git push --all

eb deploy --no-verify-ssl
