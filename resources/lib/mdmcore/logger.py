# -*- coding: utf-8 -*-

import traceback

import xbmc

from .constants import LOG_PREFIX
from .settings import get_bool


def _log(message, level=xbmc.LOGINFO):
    xbmc.log("{} {}".format(LOG_PREFIX, message), level)


def debug(message):
    if not get_bool("debug_logging", default=False):
        return

    _log(message, xbmc.LOGDEBUG)


def info(message):
    _log(message, xbmc.LOGINFO)


def warning(message):
    _log(message, xbmc.LOGWARNING)


def error(message):
    _log(message, xbmc.LOGERROR)


def exception(message):
    _log("{}\n{}".format(message, traceback.format_exc()), xbmc.LOGERROR)