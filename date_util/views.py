from datetime import datetime

from flask import request

import date_util.utils.dates as d_utils
from date_util import app


# API ROUTES

# base / current date / current time
@app.route('/api/')
def base_route():
    date_obj = datetime.now()

    # query strings?
    fmt = request.args.get('fmt')
    
    return d_utils.get_datetime(date_obj.timestamp(), fmt=fmt)
