FROM python:3.6

ARG POSTGRES_USER
ARG POSTGRES_PASSWORD
ARG POSTGRES_DB
ARG POSTGRES_PORT
ARG DB_SERVICE_NAME

RUN mkdir /project
COPY . /project/
WORKDIR /project/db/

ENV PYTHONPATH="/project"

RUN pip3 install -r requirements.txt
CMD ["python3", "migration.py"]
