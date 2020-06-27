from . import api_apex
from packages.parsers_api_apex import current_kills as func_current_kills
from packages.parsers_api_apex import total_kills as func_total_kills
from flask import request
from datetime import datetime
from app.database.models import KillHistory


@api_apex.route('/current_kills')
def api_current_kills():
    init_mode = request.args.get('init', False)

    total_kills = KillHistory.get_total_kills()
    if not total_kills:
        total_kills = func_total_kills()

    curr_kills, curr_total = func_current_kills(total_kills, init_mode)
    KillHistory.create_or_update(select={'total_kills': str(total_kills)},
                                 insert={'time_stamp': datetime.now()},
                                 init_mode=init_mode
                                 )

    return f'<html><body><div style="color:#fff">За сегодня: {curr_kills}<br>Всего: {curr_total}</div><script>let timerId = setInterval(() => window.location.reload(false), 2000);</script></body></html>'
