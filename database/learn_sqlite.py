# db_utils.py
import os
import sqlite3
import pandas as pd


# create a default path to connect to and create (if necessary) a database
# called 'database.sqlite3' in the same directory as this script
project_path = os.path.dirname(__file__)
db_path = os.path.join(project_path, 'database.sqlite3')


class dbopen(object):
    """
    Simple CM for sqlite3 databases. Commits everything at exit.
    """
    def __init__(self, path):
        self.path = path
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.path)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_class, exc, traceback):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    with dbopen(db_path) as c:
        # The execute method only allows you to execute a single SQL sentence. If you need to execute several different SQL
        # sentences you should use executescript method
        with open(os.path.join(project_path, 'Sample-SQL-File-1000-Rows.sql'), encoding='utf8') as sqlfile:
            c.executescript(sqlfile.read())

        sql_string = r'SELECT * FROM user_details limit 5;'
        c.execute(sql_string)
        df = pd.read_sql_query(sql_string, c.connection)
        print(df)
        result = c.fetchall()
        print(result)
        for row in c:
            print(row)
