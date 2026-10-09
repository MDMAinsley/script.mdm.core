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
        created = int(created_ts)
        ttl = int(ttl_seconds)
        current = now_ts()
        return ttl <= 0 or created < 0 or created > current or current >= created + ttl
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
