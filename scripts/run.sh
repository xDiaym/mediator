#!/usr/bin/env bash

uvicorn mediator.main:app --host 0.0.0.0 --port 8000 "$@"
