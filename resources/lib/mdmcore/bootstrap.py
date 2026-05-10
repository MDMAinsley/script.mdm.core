# -*- coding: utf-8 -*-

from .logger import info
from .paths import ensure_core_directories
from .device import (
    get_platform,
    get_kodi_version,
    get_free_memory_mb,
    is_low_memory_device,
)


def initialise_core(log_device_info=True):
    """
    Prepare MDM Core for use.
    Keep this lightweight.
    """

    ensure_core_directories()

    info("MDM Core initialised")

    if log_device_info:
        info("Platform: {}".format(get_platform()))
        info("Kodi Version: {}".format(get_kodi_version()))
        info("Free Memory MB: {}".format(get_free_memory_mb()))
        info("Low Memory Device: {}".format(is_low_memory_device()))

    return True