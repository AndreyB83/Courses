# Обновите таблицу, заполнив поле email.
# Напишите запрос для нахождения дублей в поле email.

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


def update_email(conn, sql):
    try:
        c = conn.cursor()
        c.execute(sql)
        conn.commit()
    except Error as e:
        print(e)


def main():
    database = r"hometaskdb.db"

    sql_scripts = ["""
    UPDATE students 
    SET email = 'vanya@mail.ru' 
    WHERE stud_id = 1;
    """,
                   """
    UPDATE students 
    SET email = 'petya@gmail.com' 
    WHERE stud_id = 2;
    """,
                   """
    UPDATE students
    SET email = 'vasya@yandex.ru'
    WHERE stud_id = 3;
    """,
                   """
    UPDATE students
    SET email = 'student@gmail.com'
    WHERE stud_id = 4;
    """,
                   """
    UPDATE students
    SET email = 'kolya@bk.ru'
    WHERE stud_id = 5;
    """,
                   """
    UPDATE students
    SET email = 'sasha@mail.ru'
    WHERE stud_id = 6;
    """,
                   """
    UPDATE students
    SET email = 'volodya@yandex.ru'
    WHERE stud_id = 7;
    """,
                   """
    UPDATE students
    SET email = 'roman@gmail.com'
    WHERE stud_id = 8;
    """,
                   """
    UPDATE students
    SET email = 'student@gmail.com'
    WHERE stud_id = 9;
    """,
                   """
    UPDATE students
    SET email = 'jan@bk.ru'
    WHERE stud_id = 10;
    """]

    conn = create_connection(database)

    if conn is not None:
        for sql in sql_scripts:
            update_email(conn, sql)
        conn.close()
    else:
        print("Error! cannot create the database connection.")


def get_doubl_email_from_table(conn, sql):
    try:
        c = conn.cursor()
        c.execute(sql)

        rows = c.fetchall()

        for row in rows:
            print(row)
    except Error as e:
        print(e)


def get_doubl_email():
    database = r"hometaskdb.db"

    sql_select = """
    SELECT email 
    FROM students
    GROUP BY email
    HAVING COUNT(email) > 1;
    """

    conn = create_connection(database)

    if conn is not None:
        get_doubl_email_from_table(conn, sql_select)
        conn.close()
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
    get_doubl_email()
