# -*- coding: utf-8 -*-

import json
import os

from .constants import TEXT_ENCODING
from .logger import exception
from .paths import ensure_directory


def ensure_parent_directory(file_path):
    """
    Ensure parent directory exists.
    """

    parent = os.path.dirname(file_path)

    if parent:
        ensure_directory(parent)


def read_text(file_path, default=""):
    """
    Read text file safely.
    """

    try:
        with open(file_path, "r", encoding=TEXT_ENCODING) as file:
            return file.read()

    except Exception:
        return default


def write_text(file_path, content):
    """
    Write text file safely.
    """

    try:
        ensure_parent_directory(file_path)

        with open(file_path, "w", encoding=TEXT_ENCODING) as file:
            file.write(content)

        return True

    except Exception:
        exception("Failed to write text file: {}".format(file_path))
        return False


def read_json(file_path, default=None):
    """
    Read JSON file safely.
    """

    if default is None:
        default = {}

    try:
        with open(file_path, "r", encoding=TEXT_ENCODING) as file:
            return json.load(file)

    except Exception:
        return default


def write_json(file_path, data, pretty=True):
    """
    Write JSON file safely.
    """

    try:
        ensure_parent_directory(file_path)

        with open(file_path, "w", encoding=TEXT_ENCODING) as file:

            if pretty:
                json.dump(data, file, indent=4, ensure_ascii=False)
            else:
                json.dump(data, file, ensure_ascii=False)

        return True

    except Exception:
        exception("Failed to write JSON file: {}".format(file_path))
        return False


def delete_file(file_path):
    """
    Delete file safely.
    """

    try:

        if os.path.exists(file_path):
            os.remove(file_path)

        return True

    except Exception:
        exception("Failed to delete file: {}".format(file_path))
        return False