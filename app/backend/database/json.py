#!/usr/bin/env python3
"""
JSON Encoder for BSON in Documents
Was for mongo
TODO(simonfong6): Need to check if this is needed anymore.
"""
from flask.json import JSONEncoder

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        return JSONEncoder.default(self, obj)
