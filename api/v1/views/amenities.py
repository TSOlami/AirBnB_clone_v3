#!/usr/bin/python3
"""
Creates a new view for Amenity objects
"""
from flask import jsonify, make_response, request, abort
from models import storage
from models.amenity import Amenity
from api.v1.views import app_views


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def get_amenities():
    """ Retrieves the list of all Amenity objects"""
    all_list = [obj.to_dict() for obj in storage.all(Amenity).values()]
    """Returns a dict"""
    return jsonify(all_list)


@app_views.route('/amenities/<string:amenity_id>', methods=['GET'],
                 strict_slashes=False)
def get_amenity(amenity_id):
    """ Retrieves a Amenity object"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
        """Returns a dict"""
    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<string:amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def del_amenity(amenity_id):
    """ Deletes a Amenity object"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    amenity.delete()
    storage.save()
    """Returns an empty dict"""
    return jsonify({})


@app_views.route('/amenities/', methods=['POST'],
                 strict_slashes=False)
def create_amenity():
    """ Creates a Amenity """
    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    if 'name' not in request.get_json():
        return make_response(jsonify({"error": "Missing name"}), 400)
    js = request.get_json()
    obj = Amenity(**js)
    obj.save()
    """Returns the new Amenity with the status code 201"""
    return (jsonify(obj.to_dict()), 201)


@app_views.route('/amenities/<string:amenity_id>', methods=['PUT'],
                 strict_slashes=False)
def post_amenity(amenity_id):
    """ Updates a Amenity"""
    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    obj = storage.get(Amenity, amenity_id)
    if obj is None:
        abort(404)
    for key, value in request.get_json().items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(obj, key, value)
    storage.save()
    """Returns the Amenity object with the status code 200"""
    return jsonify(obj.to_dict())
