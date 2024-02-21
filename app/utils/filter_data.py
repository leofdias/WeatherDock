def filter_forecast_data(raw_data, units="metric"):
    city_name = raw_data["city"]["name"]
    
    # Determinar o símbolo de temperatura com base no parâmetro units
    if units == "metric":
        temp_symbol = "°C"
    elif units == "imperial":
        temp_symbol = "°F"

    # Dicionário para armazenar os dados agrupados por data
    daily_forecasts = {}

    for forecast in raw_data["list"]:
        # Extrai a data (ano-mês-dia) da previsão
        date = forecast["dt_txt"].split(" ")[0]
        
        if date not in daily_forecasts:
            daily_forecasts[date] = []

        daily_forecasts[date].append({
            "time": forecast["dt_txt"].split(" ")[1],
            "temp": f"{forecast['main']['temp']} {temp_symbol}",
            "temp_min": f"{forecast['main']['temp_min']} {temp_symbol}",
            "temp_max": f"{forecast['main']['temp_max']} {temp_symbol}",
            "humidity": str(forecast["main"]["humidity"]) + '%',
            "feels_like": f"{forecast['main']['feels_like']} {temp_symbol}",
            "description": forecast["weather"][0]["description"] if forecast["weather"] else "No description"
        })

    # Converter os dados agrupados em uma lista estruturada por dias
    structured_forecasts = []
    for date, forecasts in daily_forecasts.items():
        structured_forecasts.append({
            "city": city_name,
            "date": date,
            "forecasts": forecasts
        })

    return structured_forecasts
