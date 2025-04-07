# Dockerfile
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /code/website

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "website.wsgi:application", "--bind", "0.0.0.0:8000"]
