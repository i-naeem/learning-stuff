import sqlite3
import json

connection = sqlite3.connect(':memory:')
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE users(
        first_name text,
        user_name text,
        last_name text,
        user_id text,
        email text,
        gender text
    )
    """
)

# Populating database with fake users.
with open(file='fake_users.json', mode='r', encoding='utf-8') as _file:
    cursor.executemany(
        'INSERT INTO users(user_id, user_name, first_name, last_name, email, gender) VALUES (:user_id, :user_name, :first_name, :last_name, :email, :gender)', json.load(_file))

    connection.commit()
