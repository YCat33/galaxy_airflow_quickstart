# Base image
FROM apache/airflow:2.6.1

USER root

# Configure gcc
RUN apt-get -y update && apt-get install -y libzbar-dev

USER airflow

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install  -r requirements.txt

USER root

# Set working directory and copy python script
WORKDIR /usr/app/src 

COPY encode_special_chars.py ./

ARG HOST
ARG USER
ARG PASSWORD

CMD ["python", "encode_special_chars.py", "$HOST", "$USER", "$PASSWORD"]


