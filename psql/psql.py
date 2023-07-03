import sqlite3
import json

connection = sqlite3.connect(':memory:')
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE users(
        user_id text
        user_name text
        first_name text
        last_name text
        email text
        gender text
    )
    """
)


with open(file='fake_users.json', mode='r', encoding='utf-8') as _file:
    for user in json.load(_file):
        cursor.execute('INSERT INTO users VALUES (?)')
