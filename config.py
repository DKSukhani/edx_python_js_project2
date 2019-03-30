import os
import secret
import psycopg2
from os import environ

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Secret key for session management. You can generate random strings here:
# https://randomkeygen.com/
SECRET_KEY = secret.secret_key

# Connect to the database
connection = psycopg2.connect(
        user = secret.db_user,
        password = secret.db_password,
        host = secret.db_host,
        port = secret.db_port,
        database = secret.db_database)
    cursor = connection.cursor()



# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
