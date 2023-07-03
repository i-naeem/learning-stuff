import sqlite3

connection = sqlite3.connect(':memory:')
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE users_table(
        user_id text
        user_name text
        last_name text
        first_name text
    )
    """
)
