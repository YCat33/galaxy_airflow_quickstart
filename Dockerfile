# Base image
FROM apache/airflow:2.6.1

# Copy the requirements file
COPY requirements.txt .

USER root

# Configure gcc
RUN apt-get -y update && apt-get install -y libzbar-dev

USER airflow

ARG GALAXY_USERNAME
ARG GALAXY_PASSWORD
ARG GALAXY_HOST

ENV GALAXY_USERNAME=${GALAXY_USERNAME}
ENV GALAXY_PASSWORD=${GALAXY_PASSWORD}
ENV GALAXY_HOST=${GALAXY_HOST}

# Install the dependencies
RUN pip install  -r requirements.txt