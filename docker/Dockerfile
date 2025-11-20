FROM python:3.13-alpine
LABEL authors="requp"

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
COPY ../backend /backend
WORKDIR /backend
COPY ../pyproject.toml pyproject.toml

RUN python -m venv .venv
RUN . .venv/bin/activate
RUN uv sync

EXPOSE 8000