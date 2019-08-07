#!/usr/bin/env python3
"""
Copyright (c) 2019 nsomeya.

All rights reserved.
"""

import iterm2
# To install, update, or remove packages from PyPI, use Scripts > Manage > Manage Dependencies...
status_count = 0
def get_count() -> int:
    global status_count
    if status_count > 30:
        status_count = 0
    status_count += 1
    return status_count

async def main(connection):
    knobs = []
    component = iterm2.StatusBarComponent(
        short_description="Sushi Status Bar",
        detailed_description="This is my first iterm2 status bar using python api",
        knobs=knobs,
        exemplar="Sushi Emoji",
        update_cadence=0.5,
        identifier="com.github.n-someya.sushi-status-bar")

    # This function gets called whenever any of the paths named in defaults (below) changes
    # or its configuration changes.
    @iterm2.StatusBarRPC
    async def coro(knobs) -> str:
        l_status_count : int = get_count()
        l_space : str = ""
        for i in range(0, l_status_count):
            l_space += " "

        return l_space + "🍣"

    # Register the component.
    await component.async_register(connection, coro)

# This instructs the script to run the "main" coroutine and to keep running even after it returns.
iterm2.run_forever(main)
