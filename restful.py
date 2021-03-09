""" restful API that recieves fake air temperatures generated in post.py
and saves them to temperatures.json
get method returns all or filtered data """

from flask import Flask, request, send_file
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

temp_data = 'data\\temperatures.json'

class Index(Resource):
    def get(self):
        return send_file(temp_data)
    
    def post(self):
        some_json = request.get_json()
        with open ('sos\\data\\temperatures.json', 'r+', encoding='utf-8') as file_1:
            data = json.load(file_1)
            temp = data['readings']
            temp.append(some_json)
            
        with open('sos\\data\\temperatures.json', 'w', encoding='utf-8') as file_2:
            json.dump(data, file_2, indent=4)

        return {'you_sent': some_json}, 201
    
class FilterData(Resource):
    def get(self, id):
        found = 0
        filtered = {}
        with open('sos\\data\\temperatures.json', 'r', encoding='utf-8') as temps:
            json_dict = json.load(temps)
            for reading in json_dict['readings']:
                if reading['id'] == id:
                    filtered[found] = reading
                    found += 1
        return filtered
        
api.add_resource(Index, '/')
api.add_resource(FilterData, '/Filter/<id>')

if __name__ == '__main__':
    app.run(debug=True)
