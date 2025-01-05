FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    python3-dev \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

COPY . .

RUN pip install --no-cache-dir -r requirements.txt