"""
Define some interface to the SQL household database
"""

from object_recognition_core.db.object_db import ObjectDbFactory, ObjectDbParameters
from object_recognition_tabletop.db_interface import ObjectDb as ObjectDbCpp

########################################################################################################################

class SqlHouseHoldDb(ObjectDbFactory):
    @classmethod
    def type_name(cls):
        return 'SqlHousehold'

    @classmethod
    def object_db(cls, db_params):
        db_params_copy = db_params
        db_params_copy['port'] = str(db_params['port'])
        return ObjectDbCpp(ObjectDbParameters(db_params_copy))
