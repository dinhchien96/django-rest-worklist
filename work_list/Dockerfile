# syntax=docker/dockerfile:1
FROM python:3.8

# ENV PYTHONUNBUFFERED=1

EXPOSE 8000

WORKDIR /code

COPY requirements.txt /code

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]

