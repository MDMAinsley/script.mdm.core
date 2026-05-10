# -*- coding: utf-8 -*-

import xbmc
import xbmcaddon

from .constants import CORE_ADDON_ID, LOG_PREFIX


def _log_settings_error(message):
    xbmc.log("{} {}".format(LOG_PREFIX, message), xbmc.LOGERROR)


def get_addon(addon_id=CORE_ADDON_ID):
    return xbmcaddon.Addon(addon_id)


def get_string(setting_id, addon_id=CORE_ADDON_ID, default=""):
    try:
        value = get_addon(addon_id).getSetting(setting_id)
        return value if value != "" else default
    except Exception:
        _log_settings_error("Failed to read string setting: {}".format(setting_id))
        return default


def get_bool(setting_id, addon_id=CORE_ADDON_ID, default=False):
    try:
        return get_addon(addon_id).getSettingBool(setting_id)
    except Exception:
        _log_settings_error("Failed to read bool setting: {}".format(setting_id))
        return default


def get_int(setting_id, addon_id=CORE_ADDON_ID, default=0):
    try:
        return get_addon(addon_id).getSettingInt(setting_id)
    except Exception:
        _log_settings_error("Failed to read int setting: {}".format(setting_id))
        return default


def get_float(setting_id, addon_id=CORE_ADDON_ID, default=0.0):
    try:
        return get_addon(addon_id).getSettingNumber(setting_id)
    except Exception:
        _log_settings_error("Failed to read float setting: {}".format(setting_id))
        return default


def set_string(setting_id, value, addon_id=CORE_ADDON_ID):
    try:
        get_addon(addon_id).setSetting(setting_id, str(value))
        return True
    except Exception:
        _log_settings_error("Failed to write string setting: {}".format(setting_id))
        return False


def set_bool(setting_id, value, addon_id=CORE_ADDON_ID):
    try:
        get_addon(addon_id).setSettingBool(setting_id, bool(value))
        return True
    except Exception:
        _log_settings_error("Failed to write bool setting: {}".format(setting_id))
        return False


def set_int(setting_id, value, addon_id=CORE_ADDON_ID):
    try:
        get_addon(addon_id).setSettingInt(setting_id, int(value))
        return True
    except Exception:
        _log_settings_error("Failed to write int setting: {}".format(setting_id))
        return False


def set_float(setting_id, value, addon_id=CORE_ADDON_ID):
    try:
        get_addon(addon_id).setSettingNumber(setting_id, float(value))
        return True
    except Exception:
        _log_settings_error("Failed to write float setting: {}".format(setting_id))
        return False