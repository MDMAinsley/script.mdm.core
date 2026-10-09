# -*- coding: utf-8 -*-

import hashlib

from .timeutils import now_ts, has_expired
from .constants import DEFAULT_CACHE_TTL
from .files import read_json, write_json, delete_file
from .paths import get_cache_path


def _cache_file(key):
    if not isinstance(key, str):
        raise TypeError("Cache keys must be strings")
    # A new namespace avoids interpreting ambiguous legacy filenames as new keys.
    digest = hashlib.sha256(key.encode("utf-8")).hexdigest()
    return get_cache_path("v2-{}.json".format(digest))


def set_cache(key, data, ttl=DEFAULT_CACHE_TTL):
    try:
        payload = {"created": now_ts(), "ttl": int(ttl), "data": data}
        return write_json(_cache_file(key), payload, pretty=False)
    except (TypeError, ValueError, OverflowError, UnicodeError):
        return False


def get_cache(key, default=None):
    try:
        filename = _cache_file(key)
    except (TypeError, UnicodeError):
        return default
    payload = read_json(filename, default=None)

    if not payload:
        return default

    if not isinstance(payload, dict):
        delete_file(filename)
        return default
    created = payload.get("created")
    ttl = payload.get("ttl")
    if (type(created) is not int or type(ttl) is not int or
            "data" not in payload or has_expired(created, ttl)):
        delete_file(filename)
        return default

    return payload.get("data", default)


def delete_cache(key):
    try:
        return delete_file(_cache_file(key))
    except (TypeError, UnicodeError):
        return False


def cache_exists(key):
    missing = object()
    return get_cache(key, default=missing) is not missing
