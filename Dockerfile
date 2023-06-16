# Base image
FROM apache/airflow:2.6.1

# Copy the requirements file
COPY requirements.txt .

USER root

# Configure gcc
RUN apt-get -y update && apt-get install -y libzbar-dev

USER airflow

ARG GALAXY_DOMAIN
ARG GALAXY_USER
ARG GALAXY_PASSWORD

ENV GALAXY_DOMAIN=${GALAXY_DOMAIN}
ENV GALAXY_USER=${GALAXY_USER}
ENV GALAXY_PASSWORD=${GALAXY_PASSWORD}

# Install the dependencies
RUN pip install  -r requirements.txt