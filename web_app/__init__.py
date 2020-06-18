from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine
import psycopg2
from psycopg2.extras import DictCursor
import pandas
import os

from web_app.routes.home_routes import home_routes
from web_app.routes.json_routes import json_routes

# from dotenv import load_dotenv
# load_dotenv()
# DB_NAME = os.getenv("DB_NAME")
# DB_USER = os.getenv("DB_USER")
# DB_PASS = os.getenv("DB_PASS")
# DB_HOST = os.getenv("DB_HOST")
# SQL_URL = os.getenv("SQL_URL")
DB_NAME = 'cyarxgrz'
DB_USER = 'cyarxgrz'
DB_PASS = '2QQLDECBgrYioavOEavWO5X2Uv3VGu5A'
DB_HOST = 'ruby.db.elephantsql.com'
SQL_URL = 'postgres://cyarxgrz:2QQLDECBgrYioavOEavWO5X2Uv3VGu5A@ruby.db.elephantsql.com:5432/cyarxgrz'

app = Flask(__name__)
app.register_blueprint(home_routes)
app.register_blueprint(json_routes)

def insert_leafly():
    connection = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST
        )
    cursor = connection.cursor(cursor_factory=DictCursor)
    engine = create_engine(SQL_URL)

    query = "CREATE TABLE IF NOT EXISTS leafly(strain VARCHAR(50), type VARCHAR(50), rating FLOAT, effects VARCHAR(50), flavor VARCHAR(50), description VARCHAR(3000));"
    cursor.execute(query)
    connection.commit()

    DB_FILEPATH = os.path.join(os.path.dirname(__file__), "cannabis.csv")
    df = pandas.read_csv(DB_FILEPATH)
    df.to_sql('leafly', engine, if_exists='replace', index=False)
    connection.commit()

    connection.close()

if __name__ == "__main__":
#     breakpoint()
