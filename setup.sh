#!/bin/bash

# Check if three arguments are provided
if [ "$#" -ne 3 ]; then
    echo "Error: Three arguments are required."
    echo "Usage: ./deploy.sh <host> <user> <password>"
    exit 1
fi

# Assign input arguments to variables
host=$1
user=$2
password=$3

# # Get the absolute path to the script's directory
# SCRIPT_DIR=$(dirname "$(readlink -f "$0")")

# # Change the working directory to the script's directory
# cd "$SCRIPT_DIR"

# Check if python3 is available
if command -v python3 &>/dev/null; then
    python_executable="python3"
else
    python_executable="python"
fi

# Run python script with input arguments
python3 encode_special_chars.py "$host" "$user" "$password"

# Build Docker images
docker-compose build

# Start Docker containers
docker-compose up -d

# Direct user to airflow UI
echo "Navigate to localhost:8080 to access the Airflow UI and login using "airflow" as the username and password"

