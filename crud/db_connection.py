import sqlite3

from model import TimestampCreate


def create_connection():
    connection = sqlite3.connect("timestamps.db")
    return connection


def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS timestamps (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic TEXT NOT NULL,
    start TEXT NOT NULL,
    stop TIMESTAMP NOT NULL
    )
    """)
    connection.commit()
    connection.close()


create_table()


def create_timestamp(timestamp: TimestampCreate):
    connection = create_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO timestamps (topic, start, stop) VALUES (?, ?, ?) RETURNING id;"
    cursor.execute(sql, (timestamp.topic, timestamp.timestamp, timestamp.start))
    row = cursor.fetchone()
    (id,) = row if row else None
    connection.commit()
    connection.close()

    return id


def delete_timestamp(timestamp: TimestampCreate):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM timestamps WHERE id=?", (str(timestamp.id)))
    connection.commit()
    connection.close()


def update_timestamp(timestamp: TimestampCreate):
    sql = """ UPDATE timestamps
                  SET topic = ? ,
                      timestamp = ?,
                      start = ? ,
                  WHERE id = ?"""
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(sql, (timestamp.topic, timestamp.timestamp, timestamp.start, timestamp.id))
    connection.commit()
    connection.close()

    return timestamp


def read_timestamps():
    sql = """
    SELECT * FROM timestamps
    """
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    connection.commit()
    connection.close()

    return rows


def read_timestamp(id: int):
    sql = """
    SELECT * FROM timestamps where id=?
    """
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(sql, (str(id)))
    row = cursor.fetchone()
    connection.commit()
    connection.close()

    return row
