FROM python:latest
RUN apt update && \
    apt install -y postgresql-client && \
    rm -rf /var/lib/apt/lists/* && \
    pip install pipenv
COPY . /code/
WORKDIR /code/
RUN pipenv install --deploy --system
CMD ["./docker/init/wait-for-postgres.sh", "db", "./docker/init/startup.sh"]
