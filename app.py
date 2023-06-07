import os
import pandas as pd
from datetime import datetime
from collections import Counter
from flask import Flask
import util

app = Flask(__name__)


# This is the function to calculate the highest used compound by each user
def find_most_common_compound(values):
    res = []

    compounds = [compound for row in values for compound in row.split(";")]
    count_common = Counter(compounds)
    most_common_count = max(count_common.values())

    for compound, count in count_common.items():
        if most_common_count == count:
            res.append(compound)

    return sorted(res)[0]


# The main etl function starting the feature derivation
def etl(args):
    # Load CSV files
    compounds_df = pd.DataFrame()
    users_df = pd.DataFrame()
    user_experiments_df = pd.DataFrame()
    # print("data path: ", args['data_path'])

    # Going through all the files in the data directory and fetching the data from the right files
    for filename in os.listdir(args['data_path']):
        # print("filename: ", filename)
        if filename.endswith(".csv") and "compounds" in filename.lower():
            compounds_df = pd.read_csv(os.path.join(args['data_path'], filename), sep=",\s+")

        elif filename.endswith(".csv") and "user_experiments" in filename.lower():
            user_experiments_df = pd.read_csv(os.path.join(args['data_path'], filename), sep=",\s+")

        elif filename.endswith(".csv") and "users" in filename.lower():
            users_df = pd.read_csv(os.path.join(args['data_path'], filename), sep=",\s+")

    # Process files to derive features
    # Eliminations the users who haven't signed up up yet
    today_date = datetime.now().date().strftime("%Y-%m-%d")
    users_df = users_df[users_df['signup_date'] <= today_date]
    user_experiments_df = user_experiments_df[user_experiments_df['user_id'].isin(users_df['user_id'])]

    # Total number of experiments per user
    f1 = user_experiments_df.groupby('user_id').size().reset_index(name='total_experiments')

    # Average runtime of experiments per user
    f2 = user_experiments_df.groupby('user_id')['experiment_run_time'].mean().reset_index(name='avg_runtime')

    # Compound experimented with highest number of times
    f3 = user_experiments_df.groupby('user_id')['experiment_compound_ids'].apply(find_most_common_compound).reset_index(
        name='most_common_compound_id')

    # Merging all the features into a single result
    res_df = pd.merge(f1, f2, on='user_id')
    res_df = pd.merge(res_df, f3, on='user_id')
    # print(res_df)

    # Upload processed data into a database

    # Create the utility postgres operations object
    db_obj = util.PostgresUtils(db=args['postgres_db'], user=args['postgres_user'], pwd=args['postgres_pwd'])

    # Create a database
    # db_obj.create_database(db_name=args['postgres_db'])

    # Create the table if needed
    db_obj.create_table(table_name=args['results_table'])

    # Write the final results into the table
    util.insert_into_table(res_df, table_name=args['results_table'])


# This functions is to get the parameters needed for this application
def get_params():
    # args = {"data_path": os.getenv('DATA_DIR_PATH'), "postgres_user": os.environ.get('POSTGRES_USER'),
    #         "postgres_pwd": os.getenv('POSTGRES_PWD'), "postgres_db": os.getenv('POSTGRES_DB'),
    #         "results_table": os.getenv('RESULTS_TABLE')}

    args = {"data_path": r'data', "postgres_user": 'docker',
            "postgres_pwd": "docker", "postgres_db": "test_db",
            "results_table": "results"}

    return args


# Your API that can be called to trigger your ETL process
# Hit this endpoint when the https://localhost:5000 is hit
# @app.route('/')
def trigger_etl():
    args = get_params()
    # Trigger your ETL process here
    etl(args)
    return 'hello world!'


if __name__ == "__main__":
    trigger_etl()
    # Start the server and run the app
    # app.run(host='0.0.0.0', port=5000, threaded=True)