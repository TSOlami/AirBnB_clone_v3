#!/usr/bin/python3
"""
Index
"""
from flask import Flask, jsonify
from api.v1.views import api_views
from models import storage


@app_views.route('/status', strict_slashes=False)
def status():
    """returns a JSON"""
return jsonify({"status": "OK"})


@app_views.route('/api/v1/stats', strict_slashes=False)
def count():
    """
    retrieves the number of each objects by type
    """
    return jsonify({"amenities": storage.count("Amenity"),
                    "cities": storage.count("City)",
                    "places": storage.count("Place"),
                    "reviews": storage.count("Review"),
                    "states": storage.count("State"),
                    "users": storage.count("User")})
