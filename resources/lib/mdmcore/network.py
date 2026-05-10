# -*- coding: utf-8 -*-

import json
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

from .constants import DEFAULT_TIMEOUT, TEXT_ENCODING
from .logger import exception


DEFAULT_HEADERS = {
    "User-Agent": "MDM-Kodi-Addons/0.0.1"
}


def http_get(url, timeout=DEFAULT_TIMEOUT, headers=None):
    try:
        request_headers = DEFAULT_HEADERS.copy()

        if headers:
            request_headers.update(headers)

        request = Request(url, headers=request_headers)

        with urlopen(request, timeout=timeout) as response:
            return response.read()

    except (HTTPError, URLError):
        exception("HTTP request failed: {}".format(url))
        return None

    except Exception:
        exception("Unexpected HTTP error: {}".format(url))
        return None


def download_text(url, timeout=DEFAULT_TIMEOUT, headers=None):
    data = http_get(url, timeout=timeout, headers=headers)

    if data is None:
        return None

    try:
        return data.decode(TEXT_ENCODING)

    except Exception:
        exception("Failed to decode text response: {}".format(url))
        return None


def download_json(url, timeout=DEFAULT_TIMEOUT, headers=None):
    text = download_text(url, timeout=timeout, headers=headers)

    if text is None:
        return None

    try:
        return json.loads(text)

    except Exception:
        exception("Failed to parse JSON response: {}".format(url))
        return None


def test_url(url, timeout=DEFAULT_TIMEOUT):
    return http_get(url, timeout=timeout) is not None