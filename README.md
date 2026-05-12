# MDM Core

Shared backend utilities and foundational systems for the MDM Kodi Addons ecosystem.

---

# Purpose

`script.mdm.core` provides reusable backend functionality shared across:

- `plugin.video.mdm.flix`
- `script.mdm.link`
- `script.mdm.conf`
- `skin.mdm.skin`

The goal is to centralise common logic and avoid duplicated systems across addons.

---

# Responsibilities

MDM Core is responsible for:

- Logging
- Settings helpers
- Filesystem/path helpers
- Cache helpers
- Network helpers
- Device/platform detection
- Kodi wrapper utilities
- JSON-RPC helpers
- Time utilities
- Addon integration helpers
- Shared bootstrap/initialisation

---

# Non-Responsibilities

MDM Core should NOT contain:

- Scrapers/providers
- Playback menus
- Skin layouts/UI ownership
- Media browsing logic
- Business-specific addon logic
- Repository build logic
- Heavy service daemons
- Provider-specific behaviour

Core should remain generic and reusable.

---

# Architecture Principles

- Keep systems modular and loosely coupled
- Prefer maintainability over shortcuts
- Optimise for low-end devices and Firesticks
- Avoid unnecessary dependencies
- Avoid overengineering early
- Prefer lightweight synchronous systems initially
- Fail safely and gracefully

---

# Dependency Direction

Allowed:

```
core -> nothing
flix -> core
link -> core
conf -> core
skin -> core
```

Forbidden:

```
core -> flix
core -> link
core -> conf
core -> skin
```

MDM Core must remain independent.

---

# Logging Rules

All logging should go through:

```python
from mdmcore.logger import (
    debug,
    info,
    warning,
    error,
    exception
)
```

Do not call `xbmc.log()` directly in addons.

---

# Cache Rules

Cache should only store temporary or rebuildable data.

Examples:

- Provider responses
- Metadata
- Artwork paths
- Speed tests
- Temporary network results

Do NOT store:

- Permanent settings
- Secrets/authentication data
- Critical user data

---

# Path Rules

Never hardcode platform paths.

Always use:

- `paths.py`
- Kodi path translation helpers

Kodi platforms behave differently across:

- Windows
- Linux
- Android
- Fire OS

---

# Performance Considerations

Target hardware includes:

- Older Firesticks
- Low-memory Android devices
- Weak CPUs

Avoid:

- Large in-memory datasets
- Excessive filesystem writes
- Aggressive threading
- Heavy background polling
- Unnecessary dependencies

Prefer:

- Lazy loading
- Small caches
- Lightweight helpers
- Safe fallbacks

---

# Current Module Structure

```text
mdmcore/
├── __init__.py
├── bootstrap.py
├── cache.py
├── constants.py
├── device.py
├── exceptions.py
├── files.py
├── integrations.py
├── jsonrpc.py
├── kodi.py
├── logger.py
├── monitor.py
├── network.py
├── paths.py
├── settings.py
└── timeutils.py
```

---

# Future Expansion Areas

Potential future modules:

- playback/
- api/
- provider abstraction
- artwork management
- bandwidth detection
- adaptive playback helpers
- service management