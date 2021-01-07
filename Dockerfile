FROM kennethreitz/pipenv

ENV DOCKERIZE_VERSION v0.6.1
RUN apt-get update && apt-get install -y wget \
 && wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
 && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
 && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

WORKDIR /app
COPY Pipfile* /app/
COPY docms/. /app/

CMD [ "python3", "./manage.py", "runserver", "0.0.0.0:8000" ]