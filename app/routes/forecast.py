from flask import request, jsonify
from app import app
from app.models import weather_history
from app.functions.weather_api import get_weather_forecast
from ..utils.jsonify import jsonify_mongo
from ..utils.filter_data import filter_forecast_data

@app.route('/forecast', methods=['GET'])
def forecast():
    city = request.args.get('city', 'London')
    units = request.args.get('units', 'metric')
    api_key = "e7f9fd1ff7dc4ce3fe4999a74ea8efd0"  # Substitua pela sua API Key do OpenWeatherMap
    if not city:
        return jsonify({"error": "City parameter is required"}), 400
    
    data = get_weather_forecast(api_key, city, units)

    filtered_data = filter_forecast_data(data, units)
    
    weather_history.insert_one({"city": city, "forecasts": filtered_data})
    
    return jsonify_mongo(filtered_data)
