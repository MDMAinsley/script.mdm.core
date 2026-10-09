# -*- coding: utf-8 -*-

import os

from resources.lib.mdmcore.bootstrap import initialise_core
from resources.lib.mdmcore.logger import info
from resources.lib.mdmcore.kodi import show_notification, get_addon_path, get_core_addon


def main():
    if not initialise_core():
        show_notification(
            "MDM Core",
            get_core_addon().getLocalizedString(30005),
            time_ms=5000,
        )
        return False

    info("MDM Core script launched")

    icon_path = os.path.join(get_addon_path(), "icon.png")

    show_notification(
        "MDM Core",
        get_core_addon().getLocalizedString(30004),
        icon=icon_path,
        time_ms=3000,
    )
    

if __name__ == "__main__":
    main()
