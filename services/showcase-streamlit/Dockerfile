FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY services/showcase-streamlit/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY services/showcase-streamlit/app.py app.py
COPY services/showcase-streamlit/pages pages

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
