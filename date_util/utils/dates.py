from datetime import datetime

def get_datetime(timestamp, fmt=None):
    date_obj = datetime.fromtimestamp(timestamp)

    datetime_requested = {
        'datetime': date_obj,
        'unix': timestamp,
        'iso': date_obj.isoformat()
    }

    if fmt:
        datetime_requested['formatted'] = date_obj.strftime(fmt).replace("'", '')
    
    return datetime_requested, 200
