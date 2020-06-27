import requests
import os
from flask import jsonify

from . import api_apex


@api_apex.route('/get_kills')
def get_kills():
    """API для выдачи текущего значения kills"""
    response = requests.get(os.environ.get('API_PLAYER_INFO'))
    if response.status_code == 200:
        data = response.json()
        trackers = data['legends']['selected']['data']
        for tracker in trackers:
            if tracker['key'] == 'kills':
                count_kills = tracker['value']
                return f'{count_kills}'

        return jsonify({'message': 'Kills not founded'})

    raise ConnectionError
