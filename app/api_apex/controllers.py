from datetime import datetime

from flask import jsonify, render_template, request

from app.database.models import KillHistory
from packages.parsers_api_apex import current_kills as func_current_kills
from packages.parsers_api_apex import total_kills as func_total_kills
from packages.parsers_api_apex import change_total_kills as func_change_total
from . import api_apex


@api_apex.route('/stat_kills')
def statistics_kills():
    total_kills = KillHistory.get_total_kills()

    if total_kills:
        curr_kills, curr_total = func_current_kills(total_kills)
        return jsonify({'success': True,
                        'data':
                            {
                                'total_kills': curr_total,
                                'curr_kills': curr_kills,
                            }
                        })

    return jsonify({'success': False})


@api_apex.route('/stat_kills/start')
def start_statistics_kills():
    curr_total = func_total_kills()
    record = KillHistory.init_table(total_kills=curr_total, time_stamp=datetime.now())

    if record:
        return jsonify({'success': True,
                        'data':
                            {
                                'total_kills': record.total_kills,
                                'time': record.time_stamp,
                            }
                        })

    return jsonify(({'success': False}))


@api_apex.route('/stat_kills/change')
def change_statistics_kills():
    sign = request.args.get('sign')
    value = request.args.get('value')
    if value:
        value = int(value)
        old_total = KillHistory.get_total_kills()
        new_total = str(func_change_total(sign, value, old_total))
        record = KillHistory.update_record(total_kills=new_total, time_stamp=datetime.now())
        if record:
            return jsonify({'success': True,
                            'data':
                                {
                                    'new_total_kills': record.total_kills,
                                    'time': record.time_stamp
                                }
                            }
                           )
    return jsonify({'success': False})


@api_apex.route('/')
def index():
    return render_template('api_apex/index.html')
