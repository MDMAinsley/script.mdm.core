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
    Dispatch RunAddon for an addon ID. True means dispatch did not raise;
    it does not confirm the addon exists, starts successfully or completes.
    """

    try:
        xbmc.executebuiltin(
            'RunAddon("{}")'.format(addon_id)
        )

        return True

    except Exception:
        exception("Failed to execute addon: {}".format(addon_id))
        return False
