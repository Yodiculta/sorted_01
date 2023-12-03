# @app.route('/api/', methods=['POST'])
# def handle_post_request():
#     # Получаем данные из POST-запроса
#     data = request.json
    
#     # Извлекаем значения из данных запроса
#     area_of_development = data.get('areaOfDevelopment')
#     experience_description = data.get('experienceDescription')
#     name = data.get('name')

#     # Выполняем необходимые операции с данными
#     # Например, вызываем API или выполняем другую логику
#     # В данном случае просто печатаем полученные значения
#     print('Area of Development:', area_of_development)
#     print('Experience Description:', experience_description)
#     print('Name:', name)
    
#     # Склеиваем строки через символ "_"
#     concatenated_string = area_of_development + "_" + name
    
#     # Возвращаем ответ
#     return concatenated_string