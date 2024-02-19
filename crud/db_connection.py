import sqlite3

from model import TimestampCreate


def create_connection():
    connection = sqlite3.connect("timestamps.db")
    connection.row_factory = sqlite3.Row
    return connection


def rows_to_list_of_dicts(rows):
    dicts = [{k: item[k] for k in item.keys()} for item in rows]
    return dicts


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
    sql = "INSERT INTO timestamps (topic, start, stop) VALUES (?, ?, ?) RETURNING *"
    cursor.execute(sql, (timestamp.topic, timestamp.timestamp, timestamp.start))
    row = cursor.fetchall()
    connection.commit()
    connection.close()

    return rows_to_list_of_dicts(row)


def delete_timestamp(timestamp_id: int):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM timestamps WHERE id=?", (str(timestamp_id)))
    connection.commit()
    connection.close()
    return timestamp_id


def update_timestamp(timestamp: TimestampCreate):
    sql = """ UPDATE timestamps
                  SET topic = ? ,
                      timestamp = ?,
                      start = ? ,
                  WHERE id = ?
                  RETURNING *"""
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(sql, (timestamp.topic, timestamp.timestamp, timestamp.start, timestamp.id))
    rows = cursor.fetchall()
    connection.commit()
    connection.close()

    return rows_to_list_of_dicts(rows)


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

    return rows_to_list_of_dicts(rows)


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

    return rows_to_list_of_dicts(row)
