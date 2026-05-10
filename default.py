# -*- coding: utf-8 -*-

from resources.lib.mdmcore.network import test_url
from resources.lib.mdmcore.logger import info
from resources.lib.mdmcore.kodi import show_notification


def main():
    info("MDM Core script launched")

    show_notification(
        "MDM Core",
        "MDM Core initialized successfully",
        time_ms=3000,
    )

    info("Network test: {}".format(test_url("https://mdmainsley.github.io/repository.mdm.repo/")))


if __name__ == "__main__":
    main()