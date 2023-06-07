# eikon-assessment
Contains needed solution files for the initial tech assessment

<h2>Assumptions for the Deriverables</h2>
<h3>Feature Derivation </h3>
I have made few assumptions while doing the feature derivation and folowing are the features dervied and the assumptions made:

- Total experiments a user ran -> computed the total number of experiments a user ran
- Average experiments amount per user -> Computed the average run time of experiments per user
- User's most commonly experimented compound -> Found the compound experimented maximum number of times per user, in case of multiple compound used maximum times, the compound with least compound id is returned. 


<h3>Other Assumptions</h3>

1. In the users.csv, there is field "signup_date" and I have used this field to eliminate the users who are not signed up yet i.e., whose signup date greater than tody's date, which means these user's future experiments are not considered while computing the feature extraction.
2. Assummed that the data file names contain 'users', 'user_experiments' and 'compounds' in the names of the files (case insensitive), given as input to the application.
3. The data directory is the same directory as the scripts and the input files are present in it.

<h2> Deliverables</h2>
<h3>Files</h3>

1. app.py -> The main python script which performs the needed operations to get the results
2. util.py -> An utility file which has postgres functions in a class needed to perform the operations
3. get_results.py -> A python which downloads the results as a .csv file when executed
4. docker-compose.yml -> Docker compose file to create postgres database service and flask application service for the execution of the application
5. Dockerfile -> Dockerfile with commands to support execution of python scripts

<h2>How to Execute</h2>
<h3>Local execution</h3>

Prereqs:
This solution needs a postgres db to be installed on the local machine
Please look at "local_execution" folder to find the scripts for local execution. It has 3 python scripts in it. These are the same scripts as described above and they can be executed by a simple "python app.py" with the following command line arguments needed for postgres login:

- data_path -> The path of the data directory, not a required parameter, defaults to the data directory present in the cur folder
- postgres_user -> username for the postgres db, required param
- postgres_pwd -> password for the postgres db, required param
- postgres_db -> database name to connect to, required param
- results_table -> name of the table to store the results, defaults to the name 'results' 

> Execute python app.py with the above mentioned paramters to execute the script

And then to see the results, simply execute python get_results.py with the same parameters os above to download the results into a csv file.

<h3> Dockerized Version </h3>
This docker version doesn't have any prereqs and can simply be executed by the following commands sequentially:

```
docker-compose build
docker-compose run --rm database
docker-compose run --rm flaskapp 
```

The last two commands should be executed in two different terminals

My solution to the docker approach does not execute successfully. I am able to start the two services successfully but my flask app simply return "This page is not working" error. I think it's to docker and local machine port binding but I was not able figure it out. I also tried just using the python script instead of a python flask but the database is throwing an authentication error and I couldn't figure it.

I have all the code and the respective files with comments in the directories.

<h3>Results</h3>
Please find the results in results.csv file for the data given.
