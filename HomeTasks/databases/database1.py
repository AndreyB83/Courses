# Создайте таблицу учеников (ФИО + номер группы).
# Заполните таблицу 10-ю записями. Выберите записи только с четными id.

import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection(r"hometaskdb.db")


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)


def main():
    database = r"hometaskdb.db"

    sql_create_projects_table = """
    create table students 
    ( 
      stud_id integer PRIMARY KEY not null,  
      stud_name TEXT not null, 
      group_num integer not null 
    );
    """

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_projects_table)
        conn.close()
    else:
        print("Error! cannot create the database connection.")


def modify_table(conn, sql):
    try:
        c = conn.cursor()
        c.execute(sql)
        conn.commit()
    except Error as e:
        print(e)


def modify():
    database = r"hometaskdb.db"

    sql_insert = """
    INSERT INTO students VALUES
      (1, 'Ваня', 11),
      (2, 'Петя', 11),
      (3, 'Вася', 11),
      (4, 'Игорь', 11),
      (5, 'Коля', 11),
      (6, 'Саша', 12),
      (7, 'Володя', 12),
      (8, 'Роман', 12),
      (9, 'Женя', 12),
      (10, 'Ян', 12
    );
    """

    conn = create_connection(database)

    if conn is not None:
        modify_table(conn, sql_insert)
        conn.close()
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    modify()


def get_data_from_table(conn, sql):
    try:
        c = conn.cursor()
        c.execute(sql)

        rows = c.fetchall()

        for row in rows:
            print(row)
    except Error as e:
        print(e)


def get_data():
    database = r"hometaskdb.db"

    sql_select = """
    SELECT *
    FROM students 
    WHERE stud_id % 2 == 0;
    """

    conn = create_connection(database)

    if conn is not None:
        get_data_from_table(conn, sql_select)
        conn.close()
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    get_data()
