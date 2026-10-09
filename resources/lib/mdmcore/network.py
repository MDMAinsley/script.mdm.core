# -*- coding: utf-8 -*-

import json
from urllib.request import Request, urlopen
from urllib.parse import urlsplit
from urllib.error import HTTPError

from .constants import CORE_VERSION, DEFAULT_TIMEOUT, TEXT_ENCODING
from .logger import error


DEFAULT_HEADERS = {
    "User-Agent": "MDM-Kodi-Addons/{}".format(CORE_VERSION)
}


def _safe_location(url):
    """Only log the origin; credentials may appear anywhere else in a URL."""
    try:
        parsed = urlsplit(url)
        if parsed.scheme not in ("http", "https") or not parsed.hostname:
            return "<invalid URL>"
        host = parsed.hostname
        if ":" in host:
            host = "[{}]".format(host)
        port = ":{}".format(parsed.port) if parsed.port is not None else ""
        return "{}://{}{}".format(parsed.scheme, host, port)
    except (TypeError, ValueError):
        return "<invalid URL>"


def _log_failure(operation, url, failure):
    # Do not include exception text or a traceback: either can contain secrets.
    detail = type(failure).__name__
    if isinstance(failure, HTTPError) and isinstance(failure.code, int):
        detail += " (status {})".format(failure.code)
    error("{} failed at {}: {}".format(operation, _safe_location(url), detail))


def http_get(url, timeout=DEFAULT_TIMEOUT, headers=None):
    try:
        request_headers = DEFAULT_HEADERS.copy()

        if headers:
            request_headers.update(headers)

        request = Request(url, headers=request_headers)

        with urlopen(request, timeout=timeout) as response:
            return response.read()

    except Exception as failure:
        _log_failure("HTTP request", url, failure)
        return None


def download_text(url, timeout=DEFAULT_TIMEOUT, headers=None):
    data = http_get(url, timeout=timeout, headers=headers)

    if data is None:
        return None

    try:
        return data.decode(TEXT_ENCODING)

    except Exception as failure:
        _log_failure("Text decoding", url, failure)
        return None


def download_json(url, timeout=DEFAULT_TIMEOUT, headers=None):
    text = download_text(url, timeout=timeout, headers=headers)

    if text is None:
        return None

    try:
        return json.loads(text)

    except Exception as failure:
        _log_failure("JSON parsing", url, failure)
        return None


def test_url(url, timeout=DEFAULT_TIMEOUT):
    return http_get(url, timeout=timeout) is not None
