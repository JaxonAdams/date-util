from datetime import datetime

def get_datetime(timestamp, fmt=None):
    date_obj = datetime.fromtimestamp(timestamp)

    datetime_requested = {
        'datetime': date_obj,
        'unix': timestamp
    }

    if fmt:
        datetime_requested['formatted'] = date_obj.strftime(fmt)
    
    return datetime_requested, 200
