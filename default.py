# -*- coding: utf-8 -*-

from resources.lib.mdmcore.settings import get_string

from resources.lib.mdmcore.logger import info


def main():

    info("Settings test value: {}".format(get_string("missing_setting", default="fallback")))

    info("Loaded JSON: {}".format(loaded))


if __name__ == "__main__":
    main()