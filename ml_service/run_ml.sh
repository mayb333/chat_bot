#!/bin/bash

poetry run uvicorn src.app.app:app --reload --host 127.0.0.1 --port 1111
