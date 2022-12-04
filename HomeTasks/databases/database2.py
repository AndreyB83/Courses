# Измените таблицу учеников, добавив поле email.

import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def alter_table(conn, sql):
    try:
        c = conn.cursor()
        c.execute(sql)
        conn.commit()
    except Error as e:
        print(e)


def main():
    database = r"hometaskdb.db"

    sql_alter_projects_table = """
    ALTER TABLE students 
    ADD COLUMN email TEXT;
    """

    conn = create_connection(database)

    if conn is not None:
        alter_table(conn, sql_alter_projects_table)
        conn.close()
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
