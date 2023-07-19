from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)


with engine.connect() as connection:
    result = connection.execute(text('select "Hello World"'))
    print(result.all())
