from flask import redirect
from date_util import app

# api routes
@app.route('/api/')
def base_route():
    return {
        'message': 'Hello, world!'
    }, 200

@app.route('/api/now')
def base_redirect():
    return redirect('/api/')
