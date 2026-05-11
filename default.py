# -*- coding: utf-8 -*-

import os

from resources.lib.mdmcore.bootstrap import initialise_core
from resources.lib.mdmcore.logger import info
from resources.lib.mdmcore.kodi import show_notification, get_addon_path


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
    

if __name__ == "__main__":
    main()