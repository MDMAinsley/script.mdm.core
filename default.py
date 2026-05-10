# -*- coding: utf-8 -*-

from resources.lib.mdmcore.files import (
    write_json,
    read_json
)

from resources.lib.mdmcore.paths import get_data_path

from resources.lib.mdmcore.logger import info


def main():

    test_file = get_data_path("test.json")

    data = {
        "name": "MDM Core",
        "working": True
    }

    write_json(test_file, data)

    loaded = read_json(test_file)

    info("Loaded JSON: {}".format(loaded))


if __name__ == "__main__":
    main()