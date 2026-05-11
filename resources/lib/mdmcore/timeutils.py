# -*- coding: utf-8 -*-

import time
from datetime import datetime, timezone


def now_ts():
    """
    Current Unix timestamp.
    """

    return int(time.time())


def now_utc_iso():
    """
    Current UTC time as ISO string.
    """

    return datetime.now(timezone.utc).isoformat()


def has_expired(created_ts, ttl_seconds):
    """
    Check whether a timestamp + TTL has expired.
    """

    try:
        return now_ts() > int(created_ts) + int(ttl_seconds)
    except Exception:
        return True


def age_seconds(created_ts):
    """
    Return age in seconds from timestamp.
    """

    try:
        return max(0, now_ts() - int(created_ts))
    except Exception:
        return 0