<<<<<<< HEAD
#!/usr/bin/python3
"""
"""
from api.v1.views.places_amenities import *
from api.v1.views.places_reviews import *
from api.v1.views.places import *
from api.v1.views.users import *
from api.v1.views.amenities import *
from api.v1.views.cities import *
from api.v1.views.states import *
from flask import Blueprint
from api.v1.views.index import *


app_views = Blueprint(app_views, __name__, url_prefix='/api/v1')
=======
#!/usr/bin/python3
"""
Init file
"""
from api.v1.views.places_amenities import *
from api.v1.views.places_reviews import *
from api.v1.views.places import *
from api.v1.views.users import *
from api.v1.views.amenities import *
from api.v1.views.cities import *
from api.v1.views.states import *
from flask import Blueprint
from api.v1.views.index import *


app_views = Blueprint(app_views, __name__, url_prefix='/api/v1')
>>>>>>> 7f43dbc (AirBnB_clone_v3)
