# Pull base image
FROM python:3.9 AS base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /Disfactory

RUN apt-get update
RUN apt-get install -y libproj-dev binutils curl
# RUN wget --quiet --output-document=- http://ftp.debian.org/debian/pool/main/c/curl/libcurl4_7.72.0-1_amd64.deb | dpkg --install -
ENV POETRY_HOME=/root/.poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH "${PATH}:/root/.poetry/bin"
RUN poetry config virtualenvs.create false
COPY pyproject.toml poetry.lock ./

# Dev image
FROM base AS dev
RUN poetry install --no-root
COPY . /Disfactory/

# Prod image
FROM base AS prod
RUN poetry install --only=main --no-root
COPY . /Disfactory/
