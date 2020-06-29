import os

import requests


def parse_api_apex() -> dict:
    response = requests.get(os.environ.get('API_PLAYER_INFO'))
    if response.status_code == 200:
        return response.json()


def change_total_kills(sign: str, value: int, old_total: int) -> int:
    if sign == '+':
        new_total = old_total - value
    else:
        new_total = old_total + value

    if new_total < 0:
        new_total = 0
    return new_total


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
