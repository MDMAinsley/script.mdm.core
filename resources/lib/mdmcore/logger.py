# -*- coding: utf-8 -*-

import traceback

import xbmc

from .constants import LOG_PREFIX


def _log(message, level=xbmc.LOGINFO):
    xbmc.log("{} {}".format(LOG_PREFIX, message), level)


def debug(message):
    _log(message, xbmc.LOGDEBUG)


def info(message):
    _log(message, xbmc.LOGINFO)


def warning(message):
    _log(message, xbmc.LOGWARNING)


def error(message):
    _log(message, xbmc.LOGERROR)


def exception(message):
    _log("{}\n{}".format(message, traceback.format_exc()), xbmc.LOGERROR)