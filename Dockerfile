FROM kennethreitz/pipenv

COPY . /app

WORKDIR /app/docms
ENTRYPOINT [ "python3", "./manage.py" ]
CMD [ "runserver", "0.0.0.0:8000" ]