#!/usr/bin/python3
"""
Creates a new view for City objects
"""
from flask import jsonify, make_response, request, abort
from models import storage
from models.state import State
from models.city import City
from api.v1.views import app_views


@app_views.route('/states/<string:state_id>/cities',
                 methods=['GET'], strict_slashes=False)
def get_cities(state_id):
    """ Retrieves the list of all City objects of a State """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    list_cities = [obj.to_dict() for obj in state.cities]
    return jsonify(list_cities)


@app_views.route('/cities/<string:city_id>', methods=['GET'],
                 strict_slashes=False)
def get_city(city_id):
    """ Retrieves a City"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
        """Returns JSON"""
    return jsonify(city.to_dict())


@app_views.route('/cities/<string:city_id>', methods=['DELETE'],
                 strict_slashes=False)
def del_city(city_id):
    """ Deletes a City"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    city.delete()
    storage.save()
    """Returns an empty dict"""
    return jsonify({})


@app_views.route('/states/<string:state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def create_city(state_id):
    """ Creates a City """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    if 'name' not in request.get_json():
        return make_response(jsonify({"error": "Missing name"}), 400)

    js = request.get_json()
    obj = City(**js)
    obj.state_id = state.id
    obj.save()
    """Returns a dict"""
    return jsonify(obj.to_dict()), 201


@app_views.route('/cities/<string:city_id>', methods=['PUT'],
                 strict_slashes=False)
def update_city(city_id):
    """ Updates a City """
    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    obj = storage.get(City, city_id)
    if obj is None:
        abort(404)
    for key, value in request.get_json().items():
        if key not in ['id', 'state_id', 'created_at', 'updated_at']:
            setattr(obj, key, value)
    storage.save()
    """Returns a dict"""
    return jsonify(obj.to_dict())
