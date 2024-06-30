from flask import Flask
from app.routes import initialize_routes

apps = Flask(__name__)
initialize_routes(apps)

# Any other initial setup can go here
