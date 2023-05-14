# pull official base image
#FROM python:3.9.5-slim-buster
FROM python:3.10.7-slim-buster


# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV FLASK_APP=main.py 
ENV FLASK_RUN_HOST=0.0.0.0

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN export LDFLAGS="-L/usr/local/opt/openssl/lib"
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/

EXPOSE 5000

#CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]


#RUN ls -la app/
#ENTRYPOINT ["app/docker-entrypoint.sh"]