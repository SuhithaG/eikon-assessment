import util
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--data_path", default='data')
    parser.add_argument("--postgres_user", required=True)
    parser.add_argument("--postgres_pwd", required=True)
    parser.add_argument("--postgres_db", required=True)
    parser.add_argument("--results_table", default='results')

    args = parser.parse_args()

    # Create the utility postgres operations object
    db_obj = util.PostgresUtils(db=args['postgres_db'], user=args['postgres_user'], pwd=args['postgres_pwd'])

    # Fetch the results
    res = db_obj.fetch_table_rows(table_name='results')

    # Download the results as a csv file
    db_obj.download_results()
