# from flask import Blueprint, jsonify
# import psycopg2
# from psycopg2.extras import DictCursor
# from sqlalchemy import create_engine
# import pandas
# from dotenv import load_dotenv
# load_dotenv()

# json_routes = Blueprint("json_routes", __name__)

# @json_routes.route("/leafly.json")
# def return_leefly():
#     connection = psycopg2.connect(
#         dbname=os.getenv("DB_NAME"),
#         user=os.getenv("DB_USER"),
#         password=os.getenv("DB_PASS"),
#         host=os.getenv("DB_HOST")
#     )
#     cursor = connection.cursor(cursor_factory=DictCursor)
#     engine = create_engine(os.getenv("SQL_URL"))

#     query = 'SELECT * FROM leafly'
#     cursor.execute(query)
#     result = cursor.fetchall()
#     print(result)

#     # df = pandas.read_sql_table('leafly', con=engine)
#     # connection.commit()
#     # connection.close()
#     # df.column = ['strain', 'type', 'rating',
#     #              'effects', 'flavor', 'description']
#     # print(df)

#     cursor.close()
#     connection.close()

#     return jsonify(result)
