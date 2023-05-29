#!/usr/bin/python3
"""
Creates a new view for User object
"""
from flask import jsonify, make_response, request, abort
from models import storage
from models.user import User
from api.v1.views import app_views


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """ Retrieves the list of all User objects"""
    all_list = [obj.to_dict() for obj in storage.all(User).values()]
    """ retrieve an object into a valid JSON"""
    return jsonify(all_list)


@app_views.route('/users/<string:user_id>', methods=['GET'],
                 strict_slashes=False)
def get_user(user_id):
    """ Retrieves a User object"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
        """ retrieve an object into a valid JSON"""
    return jsonify(user.to_dict())


@app_views.route('/users/<string:user_id>', methods=['DELETE'],
                 strict_slashes=False)
def del_user(user_id):
    """Deletes a User object"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    user.delete()
    storage.save()
    """Returns an empty dictionary with the status code 200"""
    return jsonify({})


@app_views.route('/users/', methods=['POST'],
                 strict_slashes=False)
def create_user():
    """ Creates a User"""
    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    if 'email' not in request.get_json():
        return make_response(jsonify({"error": "Missing email"}), 400)
    if 'password'not in request.get_json():
        return make_response(jsonify({"error": "Missing password"}), 400)
    js = request.get_json()
    obj = User(**js)
    obj.save()
    """Returns the new User with the status code 201"""
    return (jsonify(obj.to_dict()), 201)


@app_views.route('/users/<string:user_id>', methods=['PUT'],
                 strict_slashes=False)
def post_user(user_id):
    """ Updates a User object """
    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    obj = storage.get(User, user_id)
    if obj is None:
        abort(404)
    for key, value in request.get_json().items():
        if key not in ['id', 'email', 'created_at', 'updated']:
            setattr(obj, key, value)
    storage.save()
    """Returns the User object with the status code 200"""
    return jsonify(obj.to_dict())
