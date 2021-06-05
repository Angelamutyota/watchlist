from flask import Flask
from .config import config_options


# Initializing application
config_name = 'development'

app = Flask(__name__)
app.config.from_object(config_options[config_name])


from app import views