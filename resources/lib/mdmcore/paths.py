# -*- coding: utf-8 -*-

import os

from .kodi import (
    get_profile_path,
    make_dirs,
    path_exists
)


PROFILE_PATH = get_profile_path()

CACHE_PATH = os.path.join(PROFILE_PATH, "cache")
TEMP_PATH = os.path.join(PROFILE_PATH, "temp")
LOG_PATH = os.path.join(PROFILE_PATH, "logs")
DATA_PATH = os.path.join(PROFILE_PATH, "data")


def ensure_directory(path):
    """
    Create directory if it does not exist.
    """

    if not path_exists(path):
        make_dirs(path)

    return path


def ensure_core_directories():
    """
    Ensure all core directories exist.
    """

    ensure_directory(PROFILE_PATH)
    ensure_directory(CACHE_PATH)
    ensure_directory(TEMP_PATH)
    ensure_directory(LOG_PATH)
    ensure_directory(DATA_PATH)


def get_cache_path(*parts):
    return os.path.join(CACHE_PATH, *parts)


def get_temp_path(*parts):
    return os.path.join(TEMP_PATH, *parts)


def get_log_path(*parts):
    return os.path.join(LOG_PATH, *parts)


def get_data_path(*parts):
    return os.path.join(DATA_PATH, *parts)