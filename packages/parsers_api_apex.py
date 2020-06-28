import os

import requests


def parse_api_apex() -> dict:
    response = requests.get(os.environ.get('API_PLAYER_INFO'))
    if response.status_code == 200:
        return response.json()


def total_kills() -> int:
    data = parse_api_apex()
    if data:
        total = data['total']['kills']['value']
        return int(total)


def current_kills(prev_kills: int, init: bool = False, return_total: bool = True) -> int or tuple:
    total = total_kills()
    if init:
        curr_kills = 0
    else:
        curr_kills = total - prev_kills

    if return_total:
        return curr_kills, total

    return curr_kills
