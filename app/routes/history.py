from flask import jsonify, request
from datetime import datetime
from app import app
from app.models import weather_history

@app.route('/history', methods=['GET'])
def history():
    # Consulta todos os registros de histórico de clima no banco de dados
    history_data = weather_history.find({})
    
    # Lista para armazenar os dados formatados
    formatted_data = []
    
    # Parâmetros de consulta para filtrar por data e cidade, se fornecidos
    start_date_str = request.args.get('start_date')
    end_date_str = request.args.get('end_date')
    city = request.args.get('city')
    
    # Se as datas de início e fim forem fornecidas, converte-as para objetos de data
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d') if start_date_str else None
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d') if end_date_str else None
    
    # Formata os dados para retornar apenas as informações relevantes e filtra por data e cidade, se fornecido
    for record in history_data:
        # Verifica se o campo "forecasts" está presente no registro
        if "forecasts" in record:
            if (not city or record["city"] == city):
                filtered_forecasts = []
                for forecast in record["forecasts"]:
                    forecast_date = datetime.strptime(forecast["date"], '%Y-%m-%d')
                    if (not start_date or forecast_date >= start_date) and (not end_date or forecast_date <= end_date):
                        filtered_forecasts.append(forecast)
                if filtered_forecasts:
                    formatted_data.append({
                        "city": record["city"],
                        "forecasts": filtered_forecasts
                    })
        else:
            # Se o campo "forecasts" estiver ausente, registra um aviso e continua para o próximo registro
            print("Warning: 'forecasts' field not found in record:", record)
    
    return jsonify(formatted_data)

@app.route('/history/delete', methods=['DELETE'])
def delete_history():
    # Deleta todos os registros de histórico de previsão do tempo
    deleted_count = weather_history.delete_many({})
    
    return jsonify({"message": f"Deleted {deleted_count.deleted_count} records from history"})
