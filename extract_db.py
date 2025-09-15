import sqlite3
import pandas as pd
import sys

def main(filename: str):
    try:
        with sqlite3.connect(filename) as connection:
            cursor = connection.cursor()

            cursor.execute('SELECT name FROM sqlite_master;')
            tables = cursor.fetchall()[0]

            for table in tables:
                print(f'extracting {table} to {table}.csv')
                df = pd.read_sql_query(f'SELECT * FROM {table}', connection)
                df.to_csv(table + '.csv', index=False)
            print('finished')
    except Exception as e:
        print('error:', e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f'usage: {sys.argv[0]} <filename>')
    else:
        try:
            with open(sys.argv[1], 'r'):
                pass
            main(sys.argv[1])
        except FileNotFoundError:
            print('this file does not exist.')

