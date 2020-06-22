from flask import Flask, Blueprint, jsonify, render_template, request
from web_app.models.nlp_model import Predictor
from web_app.parser import parser
import pprint
import pandas
import os
from web_app.ConnectDB import ConnectDB

insert_routes = Blueprint("insert_routes", __name__)

@insert_routes.route("/insert_leafly")
def insert_leafly():
    connect_db = ConnectDB(
        os.getenv("DB_NAME"),
        os.getenv("DB_USER"),
        os.getenv("DB_PASS"),
        os.getenv("DB_HOST"),
        os.getenv("SQL_URL")
    )

    query = """CREATE TABLE IF NOT EXISTS
                leafly(id SERIAL PRIMARY KEY,
                strain VARCHAR(50),
                type VARCHAR(50),
                rating FLOAT,
                effects VARCHAR(50),
                flavor VARCHAR(50),
                description VARCHAR(3000));"""

    connect_db.cursor.execute(query)
    connect_db.connection.commit()

    DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "cannabis.csv")
    df = pandas.read_csv(DB_FILEPATH)
    df.to_sql('leafly', connect_db.engine, if_exists='replace',
              index=True, index_label='id')
    connect_db.connection.commit()
    connect_db.cursor.close()
    connect_db.connection.close()

    return ('Successfly Inserted CSV to Database')

@insert_routes.route("/get_leafly")
def get_leafly():
    connect_db = ConnectDB(
        os.getenv("DB_NAME"),
        os.getenv("DB_USER"),
        os.getenv("DB_PASS"),
        os.getenv("DB_HOST"),
        os.getenv("SQL_URL")
    )

    query = 'SELECT * FROM leafly'
    connect_db.cursor.execute(query)
    query_result = connect_db.cursor.fetchall()
    connect_db.cursor.close()
    connect_db.connection.close()

    return jsonify(parser(query_result))

@insert_routes.route("/user_data")
def get_data():
    return render_template('effects_flavors.html')

@insert_routes.route("/print_data", methods=["POST"])
def display_data():
    # Select data from dictionary
    user_data = request.form['Flavors/Effects']
    print("RAW USER DATA TYPE:", type(user_data))
    print("RAW USER DATA:", user_data)

    # Pass user_data into NLP model
    predictor = Predictor()
    results = predictor.predict(user_data, size=5)
    print("NLP RESULTS DATA:", results)
    print("NLP RESULTS DATA TYPE:", type(results))

    # Select rows from table
    connect_db = ConnectDB(
        os.getenv("DB_NAME"),
        os.getenv("DB_USER"),
        os.getenv("DB_PASS"),
        os.getenv("DB_HOST"),
        os.getenv("SQL_URL")
    )

    query = f'SELECT * FROM leafly WHERE id in {tuple(results)}'
    connect_db.cursor.execute(query)
    query_result = connect_db.cursor.fetchall()
    print("--- QUERY RESULT ---")
    print("QUERY RESULT TYPE:", type(query_result))
    pprint.pprint(query_result)
    print("--------------------")
    connect_db.cursor.close()
    connect_db.connection.close()

    return jsonify(parser(query_result))
