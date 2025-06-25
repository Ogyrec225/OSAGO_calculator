from typing import Any


def unification_handlers(cmd_handlers: dict[Any] = {}, query_handlers: dict[Any] = {}):
    return {**cmd_handlers, **query_handlers}
