# -*- coding: utf-8 -*-

from resources.lib.mdmcore.logger import info
from resources.lib.mdmcore.paths import ensure_core_directories


def main():

    ensure_core_directories()

    info("MDM Core directories ensured")


if __name__ == "__main__":
    main()