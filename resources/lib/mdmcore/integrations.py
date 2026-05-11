# -*- coding: utf-8 -*-

import xbmc
import xbmcaddon

from .logger import exception


def addon_exists(addon_id):
    """
    Check whether an addon is installed.
    """

    try:
        xbmcaddon.Addon(addon_id)
        return True

    except Exception:
        return False


def get_addon_version(addon_id):
    """
    Get addon version safely.
    """

    try:
        addon = xbmcaddon.Addon(addon_id)
        return addon.getAddonInfo("version")

    except Exception:
        return None


def execute_addon(addon_id):
    """
    Launch another addon safely.
    """

    try:
        xbmc.executebuiltin(
            'RunAddon("{}")'.format(addon_id)
        )

        return True

    except Exception:
        exception("Failed to execute addon: {}".format(addon_id))
        return False