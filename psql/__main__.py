from pprint import pprint
from db import create_db


con, cu = create_db(':memory:')

query = cu.execute(
    'SELECT user_name FROM users WHERE gender = "Male" AND user_id  > 5')


pprint(query.fetchone())
