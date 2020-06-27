from . import api_apex
from packages.parsers_api_apex import get_delta_kills


@api_apex.route('/get_statistics')
def get_statistics():

    delta, curr_total = get_delta_kills(3)
    return f'DELTA:{delta}, CURRENT:{curr_total}'
