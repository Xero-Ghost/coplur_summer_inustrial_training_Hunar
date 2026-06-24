# Dockerized Python Application

This project contains a simple Python application that runs inside a Docker container using the `python:3.12-slim` base image.

## Features
- Prints the current Python version running inside the container
- Prints the current date and time
- Automatically runs when the container starts

## Files
- `app.py` - Python script
- `Dockerfile` - Docker image definition
- `requirements.txt` - No external dependencies required

## Build the Docker Image
```bash
docker build -t python-version-time .
```

## Run the Docker Container
```bash
docker run --rm python-version-time
```
