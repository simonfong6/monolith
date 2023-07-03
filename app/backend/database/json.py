#!/usr/bin/env python3
"""
JSON Encoder for BSON in Mongo Documents
"""
from flask.json import JSONEncoder
from bson import ObjectId

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return JSONEncoder.default(self, obj)
