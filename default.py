# -*- coding: utf-8 -*-

from resources.lib.mdmcore.cache import set_cache, get_cache

from resources.lib.mdmcore.logger import info


def main():
    info("MDM Core loaded successfully!")

    set_cache("test_cache", {"working": True}, ttl=60)

    value = get_cache("test_cache")

    info("Cache test value: {}".format(value))


if __name__ == "__main__":
    main()