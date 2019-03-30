import psycopg2
from sqlalchemy import create_engine
import os
from os import environ
import secret

# There are two different manners in which python can connect to the postgres db.  One of them is psycopg2 and the other is sqlalchemy.  There are minor differences to both of them.

# This is the psycopg2 method

try:
    connection = psycopg2.connect(
        user = secret.db_user,
        password = secret.db_password,
        host = secret.db_host,
        port = secret.db_port,
        database = secret.db_database)
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print("Connection is successful")
    print('PostgreSQL database version:')
    cursor.execute('SELECT version()')
    db_version = cursor.fetchone()
    print(f"db_version is {db_version}")
    cursor.close()
    connection.close()
    print('Database connection closed.')

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)


# This is the sqlalchemy method

# user_database_url = environ.get('DATABASE_URL', secret.user_database_url)
# engine = create_engine(user_database_url)
# connection = engine.connect()
# print("Connection using sqlalchemy is also successful")
# result = connection.execute("select * from users")
# for row in result:
#     print("users:", row['email'])
# connection.close()
