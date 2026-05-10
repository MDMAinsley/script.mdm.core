# -*- coding: utf-8 -*-


class MDMCoreError(Exception):
    """Base exception for MDM Core."""


class MDMSettingsError(MDMCoreError):
    """Raised when addon settings cannot be read or written."""


class MDMPathError(MDMCoreError):
    """Raised when a path cannot be resolved or created."""


class MDMCacheError(MDMCoreError):
    """Raised when cache operations fail."""


class MDMNetworkError(MDMCoreError):
    """Raised when network operations fail."""