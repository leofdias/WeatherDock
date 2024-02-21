from pymongo import MongoClient

# Conexão ao MongoDB (ajuste as configurações conforme necessário)
client = MongoClient('mongodb://mongo:27017/')
db = client.weather_database

# Coleção para armazenar histórico de previsões
weather_history = db.weather_history
