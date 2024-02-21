from flask import Flask

# Cria uma instância do Flask
app = Flask(__name__)

from app.routes import forecast, history