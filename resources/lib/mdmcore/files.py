# -*- coding: utf-8 -*-

import json
import os
import tempfile

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
        _write_atomic(file_path, content.encode(TEXT_ENCODING))

        return True

    except Exception:
        exception("Failed to write text file: {}".format(file_path))
        return False


def _write_atomic(file_path, content):
    """Replace a local file only after the complete encoded content is written."""
    destination = os.path.abspath(file_path)
    ensure_parent_directory(destination)
    temporary = None
    try:
        descriptor, temporary = tempfile.mkstemp(
            prefix=".mdm-write-", dir=os.path.dirname(destination)
        )
        with os.fdopen(descriptor, "wb") as file:
            file.write(content)
            file.flush()
            os.fsync(file.fileno())
        os.replace(temporary, destination)
        temporary = None
    finally:
        if temporary is not None:
            try:
                os.remove(temporary)
            except OSError:
                exception("Failed to remove temporary write file")


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
        content = json.dumps(data, indent=4 if pretty else None, ensure_ascii=False)
        _write_atomic(file_path, content.encode(TEXT_ENCODING))

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
