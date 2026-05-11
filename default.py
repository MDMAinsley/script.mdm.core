# -*- coding: utf-8 -*-

import os

from resources.lib.mdmcore.bootstrap import initialise_core
from resources.lib.mdmcore.logger import info, debug
from resources.lib.mdmcore.kodi import show_notification, get_addon_path

from resources.lib.mdmcore.cache import set_cache, get_cache
from resources.lib.mdmcore.logger import info

def main():
    initialise_core()

    info("MDM Core script launched")

    icon_path = os.path.join(get_addon_path(), "icon.png")

    show_notification(
        "MDM Core",
        "MDM Core initialized successfully",
        icon=icon_path,
        time_ms=3000,
    )

    set_cache("test_cache", {"working": True}, ttl=60)

    value = get_cache("test_cache")

    info("Cache test value: {}".format(value))

if __name__ == "__main__":
    main()