from flask import Flask
from web_app.routes.home_routes import home_routes
from web_app.routes.insert_routes import insert_routes

app = Flask(__name__)

app.config["SECRET_KEY"] = "temporary secret key"

app.register_blueprint(home_routes)
app.register_blueprint(insert_routes)

app.run(debug=True)
