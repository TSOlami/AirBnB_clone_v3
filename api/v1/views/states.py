#!/usr/bin/python3
"""
A new view for State objects
"""
from flask import jsonify, make_response, request, abort
from models import storage
from models.state import State
from api.v1.views import app_views


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_all():
    """ Retrieves the list of all State objects by id """
    all_states = [obj.to_dict() for obj in storage.all(State).values()]
    return jsonify(all_states)


@app_views.route('/states/<string:state_id>', methods=['GET'],
                 strict_slashes=False)
def get_state(state_id):
    """ Retrieves a State object"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
        """Returns a dict"""
    return jsonify(state.to_dict())


@app_views.route('/states/<string:state_id>', methods=['DELETE'],
                 strict_slashes=False)
def del_state(state_id):
    """ Deletes a State object"""
    state = storage.get(State, state_id)
    if state is None:
        """If the state_id is not linked to any State object, raise a 404 error"""
        abort(404)
    state.delete()
    storage.save()
    """Returns an empty dictionary"""
    return jsonify({})


@app_views.route('/states/', methods=['POST'],
                 strict_slashes=False)
def create_state():
    """ Creates a State """
    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    if 'name' not in request.get_json():
        return make_response(jsonify({"error": "Missing name"}), 400)
    js = request.get_json()
    obj = State(**js)
    obj.save()
    """Returns a dict"""
    return jsonify(obj.to_dict()), 201


@app_views.route('/states/<string:state_id>', methods=['PUT'],
                 strict_slashes=False)
def post_state(state_id):
    """ Updates a State"""
    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    obj = storage.get(State, state_id)
    if obj is None:
        abort(404)
    for key, value in request.get_json().items():
        if key not in ['id', 'created_at', 'updated']:
            setattr(obj, key, value)
    storage.save()
    """Returns a dict"""
    return jsonify(obj.to_dict())
