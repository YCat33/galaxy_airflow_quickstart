# Galaxy Airflow Quickstart

This repository contains a quickstart guide for setting up Galaxy and Airflow using Docker. It provides instructions to clone the repository, set up the necessary environment variables, build the Docker images, and start the services.

## Prerequisites
Before getting started, ensure you have the following:

- [Docker]([url](https://docs.docker.com/get-docker/)) installed on your machine
- Access to a [Galaxy]([url](https://www.starburst.io/platform/starburst-galaxy/start/)) instance
- Cluster connection information (username, password, host name) from the Galaxy UI


## Installation

1. ```git clone https://github.com/YCat33/galaxy_airflow_quickstart.git```
2. ```cd galaxy_airflow_quickstart```
3. Leverage the Clusters page within the Galaxy UI ([Docs]((https://docs.starburst.io/starburst-galaxy/query/clients.html))) to locate your connection variables. 
4. Set up the environment variables. Replace <user_name>, <password>, and <host_name> with your actual values. 
  
  **Note: If your username or password includes the @ character, replace it with %40.

```
  export GALAXY_USERNAME=<user_name> GALAXY_PASSWORD=<password> GALAXY_HOST=<host_name>
```
  
  
  ## Example Dag (Galaxy Demo)
  
  1. Task 1 (select_star) uses the TrinoOperator to execute a SQL select statement. It counts the number of records in the "tpch.tiny.customer" table and stores the result.
  2. Task 2 (print_number) is a PythonOperator that calls the print_command method. It retrieves the return value from Task 1 and prints it to the logs.
  3. Task 3 (data_validation_check) is an SQLColumnCheckOperator that performs a data quality check. It verifies that the distinct values in the "custkey" column of the "tpch.tiny.customer" table are equal to 1500.
  
