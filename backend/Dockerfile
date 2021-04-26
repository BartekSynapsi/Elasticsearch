FROM python:3.9.4-alpine3.12

WORKDIR /usr/backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY requirements.txt requirements.txt

RUN python3 -m pip install --upgrade pip &&\
    pip install -r requirements.txt


CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]