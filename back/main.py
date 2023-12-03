from flask import Flask, request
from flask_cors import CORS, cross_origin
from typing import Optional
from app.gig_chat import get_giga_responce

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
@cross_origin()
def handle_post_request():
    if request.method == 'OPTIONS':
    # Обработка предварительных запросов OPTIONS
        return '', 200
    data: Optional[dict] = request.json  # Объявляем data как Optional[dict]
    if data is None:
        return "No data received"
    
    area_of_development = data.get('areaOfDevelopment')
    name = data.get('name')
    experienceDescription = data.get('experienceDescription')
    if area_of_development is None or name is None or experienceDescription is None:
        return "No all data received"
    prompt = "Пользователь " + name + " хотел бы начать обучение в сфере "+ area_of_development+ " и на текущий момент имеет такие знания: " + experienceDescription
    giga_response = get_giga_responce(prompt)
    return giga_response

@app.route('/api/', methods=['GET'])
def handle_get_request():
    if request.method == 'OPTIONS':
    # Обработка предварительных запросов OPTIONS
        return '', 200
    data: Optional[dict] = request.json  # Объявляем data как Optional[dict]
    if data is None:
        return "No data received"
    experienceDescription = data.get('experienceDescription')
    area_of_development = data.get('areaOfDevelopment')
    name = data.get('name')
    
    if area_of_development is None:
        return "No area_of_development received"
    if name is None:
        return "No name received"
    prompt = "Пользователь " + name + " хотел бы начать обучение в сфере "+ area_of_development+ "и на текущий момент имеет такие знания: " + experienceDescription
    giga_response = get_giga_responce(prompt)
    return giga_response


if __name__ == '__main__':
    app.run(debug=True)