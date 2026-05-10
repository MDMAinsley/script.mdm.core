# -*- coding: utf-8 -*-

import xbmc
import xbmcaddon
import xbmcgui
import xbmcvfs

from .constants import CORE_ADDON_ID


_CORE_ADDON = xbmcaddon.Addon(CORE_ADDON_ID)


def get_core_addon():
    return _CORE_ADDON


def get_addon(addon_id):
    return xbmcaddon.Addon(addon_id)


def get_kodi_version():
    return xbmc.getInfoLabel("System.BuildVersion")


def get_profile_path():
    return translate_path(_CORE_ADDON.getAddonInfo("profile"))


def get_addon_path():
    return translate_path(_CORE_ADDON.getAddonInfo("path"))


def translate_path(path):
    return xbmcvfs.translatePath(path)


def path_exists(path):
    return xbmcvfs.exists(path)


def make_dirs(path):
    return xbmcvfs.mkdirs(path)


def show_notification(title, message, icon=None, time_ms=3000):
    xbmcgui.Dialog().notification(
        heading=title,
        message=message,
        icon=icon or xbmcgui.NOTIFICATION_INFO,
        time=time_ms
    )


def dialog_ok(title, message):
    return xbmcgui.Dialog().ok(title, message)


def dialog_yesno(title, message):
    return xbmcgui.Dialog().yesno(title, message)


def execute_builtin(command):
    xbmc.executebuiltin(command)


def sleep(milliseconds):
    xbmc.sleep(milliseconds)