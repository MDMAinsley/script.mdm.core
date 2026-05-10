# -*- coding: utf-8 -*-

import time

from .constants import DEFAULT_CACHE_TTL
from .files import read_json, write_json, delete_file
from .paths import get_cache_path


def _cache_file(key):
    safe_key = key.replace("/", "_").replace("\\", "_").replace(":", "_")
    return get_cache_path("{}.json".format(safe_key))


def set_cache(key, data, ttl=DEFAULT_CACHE_TTL):
    payload = {
        "created": int(time.time()),
        "ttl": int(ttl),
        "data": data
    }

    return write_json(_cache_file(key), payload, pretty=False)


def get_cache(key, default=None):
    payload = read_json(_cache_file(key), default=None)

    if not payload:
        return default

    created = payload.get("created", 0)
    ttl = payload.get("ttl", DEFAULT_CACHE_TTL)

    if int(time.time()) > created + ttl:
        delete_cache(key)
        return default

    return payload.get("data", default)


def delete_cache(key):
    return delete_file(_cache_file(key))


def cache_exists(key):
    return get_cache(key, default=None) is not None