from flask import jsonify

def jsonify_mongo(data):
    # Verifica se data é uma lista
    if isinstance(data, list):
        # Processa cada entrada se data for uma lista
        for entry in data:
            if '_id' in entry:
                entry['_id'] = str(entry['_id'])
    elif isinstance(data, dict) and '_id' in data:
        # Trata data como um dicionário único se não for uma lista
        data['_id'] = str(data['_id'])
    return jsonify(data)