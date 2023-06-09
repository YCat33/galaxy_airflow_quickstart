# Galaxy Airflow Quickstart

This repository contains a quickstart guide for setting up Galaxy and Airflow using Docker. It provides instructions to clone the repository, set up the necessary environment variables, build the Docker images, and start the services.

## Prerequisites
Before getting started, ensure you have the following:

- [Docker](https://docs.docker.com/get-docker/) installed on your machine
- Access to a [Galaxy](https://www.starburst.io/platform/starburst-galaxy/start/) instance
- Cluster connection information (username, password, host name) from the Galaxy UI


## Installation

1. ```git clone https://github.com/YCat33/galaxy_airflow_quickstart.git```
2. ```cd galaxy_airflow_quickstart```
3. Navigate to your Galaxy Domain
4. Leverage the Clusters page within the [Galaxy UI](https://docs.starburst.io/starburst-galaxy/query/clients.html) to locate your connection variables.
5. Run the below to allow the bash setup script to be executable:
```
  chmod +x setup.sh
```
   
6. Run the bash script below by leveraging the connection variables in step 4: 

```
  ./setup.sh '<host>' '<user>' '<password>'
```
  *This script performs the follwing steps
  
    1. Runs the encode_special_chars script that sets the connection parameters to the necessary format (e.g. replacing "@' with "%40").
    2. Runs the DockerFile to build the image, which involves installing the "apache-airflow-providers-trino" package and setting up the Galaxy Connection (These variables are used within the Docker-Compose.yaml file to instantiate a connection to Starburst Galaxy (see line 75 [here](https://github.com/YCat33/galaxy_airflow_quickstart/blob/31b28bbf9237b26cddbab380f416e80384e65cd3/docker-compose.yaml#L75)))
    3. Deploys the necessary Docker containers based off the docker-compose file

  
7. Navigate to ```localhost:8080``` in your Browser and login using "airflow" as the username and password.

  ## Example Dag (starburst-galaxy-example)
  
  1. Task 1 (select_star) uses the TrinoOperator to execute a SQL select statement. It counts the number of records in the "tpch.tiny.customer" table and stores the result.
  2. Task 2 (print_number) is a PythonOperator that calls the print_command method. It retrieves the return value from Task 1 and prints it to the logs.
  3. Task 3 (data_validation_check) is an SQLColumnCheckOperator that performs a data quality check. It verifies that the distinct values in the "custkey" column of the "tpch.tiny.customer" table are equal to 1500.

  ## Running the Example DAG
  1. From the Airflow UI home screen, you should see a single DAG titled "starburst-galaxy-example".
<img width="623" alt="image" src="https://github.com/YCat33/galaxy_airflow_quickstart/assets/115039992/dfdc5a3b-0087-4803-829c-f6a73a5367e5">


  2. Trigger the DAG by clicking the “play” button on the right-hand side of the screen
<img width="608" alt="image" src="https://github.com/YCat33/galaxy_airflow_quickstart/assets/115039992/8d8c7bb7-9132-427a-88b2-dada3abff574">


  3. View the Logs for each task

     
<img width="617" alt="image" src="https://github.com/YCat33/galaxy_airflow_quickstart/assets/115039992/6f248a1f-4572-411e-bbf0-7438e862646e">
<img width="615" alt="image" src="https://github.com/YCat33/galaxy_airflow_quickstart/assets/115039992/d4abe2ea-f4fa-4e8d-b0c3-f532433c0092">
<img width="616" alt="image" src="https://github.com/YCat33/galaxy_airflow_quickstart/assets/115039992/d130ed8b-2e8c-4909-9049-4e99fb485464">
<img width="624" alt="image" src="https://github.com/YCat33/galaxy_airflow_quickstart/assets/115039992/782a3fba-1c62-4c53-8694-c56caa85d3ec">
<img width="623" alt="image" src="https://github.com/YCat33/galaxy_airflow_quickstart/assets/115039992/08ff7c5a-8764-4070-8432-838ce63b7e59">
<img width="615" alt="image" src="https://github.com/YCat33/galaxy_airflow_quickstart/assets/115039992/acc8e2ec-73f7-43d9-981e-dca524b63e87">
<img width="618" alt="image" src="https://github.com/YCat33/galaxy_airflow_quickstart/assets/115039992/b653e215-6ca5-45be-89e8-f95691b0bf98">
