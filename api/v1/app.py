#!/usr/bin/python3
"""
"""
from flask import Flask, jsonify, make_response
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def close():
    """calls the storage close method"""
    storage.close()


@app.errorhandler(404)
def not_found():
    """creates a 404 page"""
    return make_response(jsonify({"error": "NOt Found"}), 404)


if __name__ == "__main__":

    host = getenv('HBNB_API_HOST', default='0.0.0.0')
    port = getenv('HBNB_API_PORT', default='5000')

    app.run(host, int(port), threaded=True)
