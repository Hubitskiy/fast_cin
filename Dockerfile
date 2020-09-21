FROM python:3.8-alpine as builder

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    DOCKERIZE_VERSION=v0.6.1

RUN apk --no-cache add \
    bash \
    python3-dev \
    build-base \
    curl \
    gcc \
    g++ \
    libxslt-dev \
    gettext \
    git \
    libffi-dev \
    linux-headers \
    openssl \
    musl-dev \
    postgresql-dev \
    tini \
    jpeg-dev \
    zlib-dev \
    cairo-dev \
    pango-dev \
    gdk-pixbuf-dev \
    fontconfig \
    ttf-ubuntu-font-family

FROM builder as production_build

WORKDIR /app

COPY ./app/ /app/

RUN pip3 install -r requirements.txt