import requests
import os


def parse_api_apex():
    response = requests.get(os.environ.get('API_PLAYER_INFO'))
    if response.status_code == 200:
        return response.json()


def get_total_kills():
    data = parse_api_apex()
    if data:
        current_kills = data['total']['kills']['value']
        return current_kills


def get_delta_kills(prev_kills, total_kills_mod=True):
    total_kills = get_total_kills()
    delta_kills = total_kills - prev_kills
    if total_kills_mod:
        return delta_kills, total_kills

    return delta_kills
