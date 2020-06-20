from flask import Flask, Blueprint, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine
import psycopg2
from psycopg2.extras import DictCursor
import pandas
import os
from web_app.models.nlp_model import Predictor
from dotenv import load_dotenv
load_dotenv()

insert_routes = Blueprint("insert_routes", __name__)

@insert_routes.route("/insert_leafly")
def insert_leafly():
    connection = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        host=os.getenv("DB_HOST")
        )
    cursor = connection.cursor(cursor_factory=DictCursor)
    engine = create_engine(os.getenv("SQL_URL"))

    query = """CREATE TABLE IF NOT EXISTS
                leafly(id SERIAL PRIMARY KEY,
                strain VARCHAR(50),
                type VARCHAR(50),
                rating FLOAT,
                effects VARCHAR(50),
                flavor VARCHAR(50),
                description VARCHAR(3000));"""

    cursor.execute(query)
    connection.commit()

    DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "cannabis.csv")
    df = pandas.read_csv(DB_FILEPATH)
    df.to_sql('leafly', engine, if_exists='replace', index=True, index_label='id')
    connection.commit()
    cursor.close()
    connection.close()

    return ('Successfly Inserted CSV to Database')

@insert_routes.route("/get_leafly")
def get_leafly():
    connection = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        host=os.getenv("DB_HOST")
        )
    cursor = connection.cursor(cursor_factory=DictCursor)
    engine = create_engine(os.getenv("SQL_URL"))

    query = "SELECT * FROM leafly"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()

    return jsonify(result)

@insert_routes.route("/user_data")
def get_data():
    return render_template('effects_flavors.html')

@insert_routes.route("/print_data", methods=["POST"])
def display_data():
    # converts data from from into a dictionary
    data = dict(request.form)
    print("RAW USER DATA:", data)
    print("RAW USER DATA TYPE:", type(data))

    # extracts the list of flavors and effects from the dictionary
    user_data = data['Flavors/Effects'].split(sep=',')
    print("MODIFIED USER DATA:", user_data)
    print("MODIFIED USER DATA TYPE:", type(user_data))

    # you can pass user_data to ruby's model
    predictor = Predictor()
    results = predictor.predict(user_data, size=5)
    print("NLP RESULTS DATA:", results)
    print("NLP RESULTS DATA TYPE:", type(results))

    return "TODO"
