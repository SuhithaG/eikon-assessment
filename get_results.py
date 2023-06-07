import util

if __name__ == "__main__":
    args = {"data_path": r'data', "postgres_user": 'docker',
            "postgres_pwd": "docker", "postgres_db": "test_db",
            "results_table": "results"}
    print(args)

    # Create the utility postgres operations object
    db_obj = util.PostgresUtils(db=args['postgres_db'], user=args['postgres_user'], pwd=args['postgres_pwd'])

    # Fetch the results
    res = db_obj.fetch_table_rows(table_name='results')

    # Download the results as a csv file
    db_obj.download_results()
