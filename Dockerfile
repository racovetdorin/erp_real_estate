# FROM python:3.11-slim

# ENV PYTHONUNBUFFERED=1

# RUN mkdir /app

# WORKDIR /app

# COPY requirements.txt /app

# RUN pip install --upgrade pip

# RUN pip install -r requirements.txt

# COPY . /app

# RUN flake8 
FROM python:3.9.2-buster

RUN mkdir /usr/local/app

WORKDIR /usr/local/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

RUN pip install --upgrade pip
RUN pip install virtualenv
RUN virtualenv /usr/local/venv

COPY ./entrypoint.sh /usr/local/

RUN chmod u+x /usr/local/entrypoint.sh

COPY . /usr/local/app/

RUN flake8

CMD ["/bin/bash", "/usr/local/entrypoint.sh"]