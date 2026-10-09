# MDM Core

Shared backend utilities and foundational systems for the MDM Kodi Addons ecosystem.

## 1.0.0 development candidate

This candidate covers the shared backend helpers and initialization script.
Windows/Kodi and Firestick acceptance is pending; 1.0.0 is not yet a public release.

The helper names remain unchanged. File writes return True only after a complete
temporary file replaces the destination; encoding, serialization, write or
replacement failures return False and preserve the previous file. These helpers
accept local paths, including translated Kodi profile paths, rather than remote
VFS URLs. Atomic replacement is not a guarantee against every power-loss scenario.

Cache keys are strings and map to deterministic SHA256 filenames prefixed with
`v2-`. Include the caller's addon/provider namespace in keys when sharing Core.
Legacy cache files are left untouched and are not read or migrated, because their
old names could represent multiple keys. Temporary cached data will be rebuilt
on a miss. Permanent data and settings are unaffected by this cache transition.
Malformed cache payloads return the caller's default. TTL <= 0 expires immediately;
positive TTL expires when current time reaches creation time plus TTL. Invalid
timestamps and future creation times are treated as misses. cache_exists reports
stored None and other falsy values as present while their entries remain valid.

ensure_directory returns the directory path or raises MDMPathError if a local
directory cannot be established. initialise_core returns False for that failure;
the runnable script displays a failure notification instead of reporting success.
Android detection prioritizes Kodi's platform condition over a Linux kernel name.

HTTP failures retain their None return value. Logs include only the server origin,
error class and HTTP status where available. User info, paths, queries, fragments,
response bodies, exception text and tracebacks are omitted from HTTP diagnostics.
The hostname is still logged; do not put secrets in hostnames.

Automated validation uses simulated Kodi APIs. Actual Kodi and Firestick acceptance
of these repairs is still required before publication or compatibility sign-off.

### Helper contracts and examples

Settings getters return the Kodi value, or the caller's default if the API raises;
the string getter also uses its default for an empty string. Typed Kodi getters can
return False/0 for missing settings without raising. Setters retain their original
coercion behaviour: callers should pass bool to set_bool (the string "false" is
truthy in Python), integer-compatible values to set_int and numeric values to
set_float. Setters return False when conversion or the Kodi API raises.

JSON-RPC execute returns the response result, or None for error/malformed responses
and API failures. execute_addon returns True when RunAddon dispatch does not raise;
it does not confirm installation, startup or completion. Use a trusted addon ID.
Monitor helpers directly expose Kodi abortRequested and waitForAbort; use them
instead of a busy polling loop. Unreadable free memory returns 0, which is treated
as unknown rather than automatically classifying the device as low-memory.

```python
import mdmcore

if mdmcore.initialise_core(log_device_info=False):
    mdmcore.logger.info("Backend ready")

key = "plugin.video.mdm.flix:metadata:example"
if mdmcore.cache.set_cache(key, {"title": "Example"}, ttl=300):
    metadata = mdmcore.cache.get_cache(key, default={})
```

Core does not run a background service. Repeated initialization is safe for existing
directories, but each call logs initialization and optionally device details.
Core has no third-party Python dependency; xbmc.python 3.0.0 is the manifest
requirement. This is a declaration, not evidence of testing every Kodi version.

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
