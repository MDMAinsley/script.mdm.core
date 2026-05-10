# -*- coding: utf-8 -*-

import platform

import xbmc


def get_platform():
    """
    Return simplified platform name.
    """

    system = platform.system().lower()

    if "windows" in system:
        return "windows"

    if "linux" in system:
        return "linux"

    if "darwin" in system:
        return "macos"

    if "android" in system:
        return "android"

    return "unknown"


def is_android():
    """
    Detect Android-based Kodi devices.
    """

    return xbmc.getCondVisibility("System.Platform.Android")


def is_windows():
    return xbmc.getCondVisibility("System.Platform.Windows")


def is_linux():
    return xbmc.getCondVisibility("System.Platform.Linux")


def is_macos():
    return xbmc.getCondVisibility("System.Platform.OSX")


def get_kodi_version():
    """
    Return Kodi build version string.
    """

    return xbmc.getInfoLabel("System.BuildVersion")


def get_free_memory_mb():
    """
    Return free memory estimate in MB.
    """

    try:
        memory = xbmc.getInfoLabel("System.Memory(free)")

        memory = memory.upper().replace("MB", "").strip()

        return int(float(memory))

    except Exception:
        return 0


def is_low_memory_device(threshold_mb=500):
    """
    Determine if device is likely low-end.
    """

    free_memory = get_free_memory_mb()

    if free_memory <= 0:
        return False

    return free_memory < threshold_mb