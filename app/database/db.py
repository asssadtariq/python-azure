import psycopg2


def init_db():
    conn = psycopg2.connect(
        database="",
        host="",
        user="",
        password="",
        port="",
    )

    # cursor is an object used to interact with a database by executing SQL queries
    cursor = conn.cursor()

    return conn, cursor
