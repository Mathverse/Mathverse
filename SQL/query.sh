#!/usr/bin/env bash

psql -h "chicagoboothanalytics.clloyfrn47sj.us-west-1.rds.amazonaws.com" -p "5432" -d "ChicagoBoothAnalytics" -U "BoothAnalytics" -f "query.sql"
