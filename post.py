""" generates fake air temperatures for fake stations in stations.json
and posts them to a restful API restful.py """

import requests
import time
import json
import random
import datetime

time_string = "2021-09-03 07:00:00"
start_date = datetime.datetime.strptime(time_string, '%Y-%d-%m %H:%M:%S')

temp1 = random.uniform(-5.0, 12.0)
temp2 = random.uniform(temp1, temp1+8.0)

measured = 0

url = 'http://127.0.0.1:5000/'

while measured < 12:
    with open('sos\stations.json', 'r', encoding='utf-8') as stations:
        json_dict = json.load(stations)
        for station in json_dict['stations']:
            #print(station['id'])
            station_id = station['id']
            time = start_date + datetime.timedelta(hours=7)
            if '04:' in time.strftime('%Y-%d-%m %H:%M:%S'):
                time = time + datetime.timedelta(hours=3)
            start_date = time
            value = random.uniform(temp1, temp2)
            measured += 1

            data = {
                "id": station_id,
                "time": time.strftime('%Y-%d-%m %H:%M:%S'),
                "value": '{:.2f}'.format(value)
            }
            response = requests.post(url, json=data)
