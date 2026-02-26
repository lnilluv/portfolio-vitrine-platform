FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app/src

WORKDIR /app

COPY services/portfolio-api/src src
COPY data/projects /app/data/projects

EXPOSE 8000

CMD ["python", "-m", "portfolio_api.adapters.http.server"]
