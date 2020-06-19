from flask import Flask
from web_app.routes.home_routes import home_routes
from web_app.routes.json_routes import json_routes
from web_app.routes.insert_routes import insert_routes
from web_app.routes.search_routes import search

app = Flask(__name__)

app.register_blueprint(home_routes)
app.register_blueprint(json_routes)
app.register_blueprint(insert_routes)
app.reguster_blueprint(search_routes)

app.run(debug=True)
