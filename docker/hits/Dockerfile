FROM python:latest
COPY . /code
WORKDIR /code
RUN pip install pipenv \
    && pipenv install --deploy --system
CMD [ "./docker/hits/startup.sh" ]