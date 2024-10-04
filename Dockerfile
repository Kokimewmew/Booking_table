FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip install -r /app/requirements.txt --no-cache-dir


CMD ["sh", "-c", "python /app/manage.py migrate && python /app/manage.py runserver 0.0.0.0:8000"]