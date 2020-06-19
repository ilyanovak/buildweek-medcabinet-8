from flask import Blueprint, jsonify
import psycopg2
from psycopg2.extras import DictCursor
from sqlalchemy import create_engine

import pandas

json_routes = Blueprint("json_routes", __name__)

DB_NAME = 'cyarxgrz'
DB_USER = 'cyarxgrz'
DB_PASS = '2QQLDECBgrYioavOEavWO5X2Uv3VGu5A'
DB_HOST = 'ruby.db.elephantsql.com'
SQL_URL = 'postgres://cyarxgrz:2QQLDECBgrYioavOEavWO5X2Uv3VGu5A@ruby.db.elephantsql.com:5432/cyarxgrz'

@json_routes.route("/leafly.json")
def return_leefly():
    connection = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST
    )
    cursor = connection.cursor(cursor_factory=DictCursor)
    engine = create_engine(SQL_URL)

    query = 'SELECT * FROM leafly'
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)

    # df = pandas.read_sql_table('leafly', con=engine)
    # connection.commit()
    # connection.close()
    # df.column = ['strain', 'type', 'rating',
    #              'effects', 'flavor', 'description']
    # print(df)

    cursor.close()
    connection.close()

    return jsonify(result)
