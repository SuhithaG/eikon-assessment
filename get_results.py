import util

if __name__ == "__main__":
    args = {"data_path": r'data', "postgres_user": 'docker',
            "postgres_pwd": "docker", "postgres_db": "exampledb",
            "results_table": "results"}
    db_obj = util.PostgresUtils(db=args['postgres_db'], user=args['postgres_user'], pwd=args['postgres_pwd'])
    res = db_obj.fetch_table_rows(table_name='results')
    db_obj.download_results()
