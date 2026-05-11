# -*- coding: utf-8 -*-

import xbmc


_MONITOR = xbmc.Monitor()


def abort_requested():
    """
    Return True if Kodi is shutting down or script should stop.
    """

    return _MONITOR.abortRequested()


def wait_for_abort(timeout_seconds):
    """
    Wait up to timeout_seconds.
    Returns True if abort was requested.
    """

    return _MONITOR.waitForAbort(timeout_seconds)