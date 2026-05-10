# -*- coding: utf-8 -*-

import os

from resources.lib.mdmcore.device import (
    get_platform,
    get_kodi_version,
    get_free_memory_mb,
    is_low_memory_device
)

from resources.lib.mdmcore.logger import info
from resources.lib.mdmcore.kodi import (
    show_notification,
    get_addon_path
)


def main():
    info("MDM Core script launched")

    icon_path = os.path.join(get_addon_path(), "icon.png")

    show_notification(
        "MDM Core",
        "MDM Core initialized successfully",
        icon=icon_path,
        time_ms=3000,
    )

    info("Platform: {}".format(get_platform()))
    info("Kodi Version: {}".format(get_kodi_version()))
    info("Free Memory MB: {}".format(get_free_memory_mb()))
    info("Low Memory Device: {}".format(is_low_memory_device()))


if __name__ == "__main__":
    main()