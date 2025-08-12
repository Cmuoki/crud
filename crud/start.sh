#!/usr/bin/env bash
gunicorn crud.crud_project.wsgi:application --bind 0.0.0.0:$PORT