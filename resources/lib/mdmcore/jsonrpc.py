# -*- coding: utf-8 -*-

import json

import xbmc

from .logger import exception


def execute(method, params=None):
    """
    Execute a Kodi JSON-RPC method safely.
    """

    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
    }

    if params is not None:
        payload["params"] = params

    try:
        raw_response = xbmc.executeJSONRPC(json.dumps(payload))
        response = json.loads(raw_response)

        if "error" in response:
            return None

        return response.get("result")

    except Exception:
        exception("JSON-RPC call failed: {}".format(method))
        return None


def get_application_properties(properties=None):
    if properties is None:
        properties = ["version", "name"]

    return execute(
        "Application.GetProperties",
        {"properties": properties}
    )


def get_player_active_players():
    return execute("Player.GetActivePlayers")