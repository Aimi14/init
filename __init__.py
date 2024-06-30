from flask import Flask
from app.routes import initialize_routes

app = Flask(__name__)
initialize_routes(app)

# Any other initial setup can go here
