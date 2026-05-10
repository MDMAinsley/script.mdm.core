# -*- coding: utf-8 -*-

from resources.lib.mdmcore.logger import info
from resources.lib.mdmcore.kodi import show_notification


def main():
    info("MDM Core script launched")

    show_notification(
        "MDM Core",
        "Kodi wrapper test successful"
    )


if __name__ == "__main__":
    main()