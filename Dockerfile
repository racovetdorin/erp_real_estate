FROM python:3

ENV PYTHONUNBUFFERED=1

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /app
#RUN ./manage.py makemigrations
#RUN ./manage.py migrate

#CMD ["./bin/run"]