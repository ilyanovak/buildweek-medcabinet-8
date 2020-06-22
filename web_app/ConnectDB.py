from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine
import psycopg2
from psycopg2.extras import DictCursor
from dotenv import load_dotenv

load_dotenv()

class ConnectDB():
    def __init__(self, name, user, password, host, sql):
        self.connection = psycopg2.connect(
            dbname=name,
            user=user,
            password=password,
            host=host)
        self.cursor = self.connection.cursor(cursor_factory=DictCursor)
        self.engine = create_engine(sql)
