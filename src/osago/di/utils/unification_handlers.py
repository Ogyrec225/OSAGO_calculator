from typing import Any


def unification_handlers(
    cmd_handlers: dict[Any] | None = None, query_handlers: dict[Any] | None = None
):
    return {**(cmd_handlers or {}), **(query_handlers or {})}
