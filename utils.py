from future.utils import raise_with_traceback
import json
import datetime
import uuid

class Storage(dict):
    """
    A Storage object is like a dictionary except `obj.foo` can be used 
    in addition to `obj['foo']`.

        >>> o = storage(a=1)
        >>> o.a
        1
        >>> o['a']
        1
        >>> o.a = 2
        >>> o['a']
        2
        >>> del o.a
        >>> o.a
        Traceback (most recent call last):
            ...
        AttributeError: 'a'

    """
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as k:
            raise_with_traceback(AttributeError(k))

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError as k:
            raise_with_traceback(AttributeError(k))

    def __repr__(self):
        return '<Storage ' + dict.__repr__(self) + '>'

storage = Storage

def json_default(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()
    if isinstance(o, uuid.UUID):
        return str(o)
    return json.JSONEncoder.default(self, o)

def publishjson(obj):
    return json.dumps(obj, default=json_default)
