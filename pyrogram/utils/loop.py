#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import annotations as _annotations

import asyncio


# The loop `get_event_loop()` builds for a caller that is inside none, so that the sync
#  bridge has something to drive. It is not a record of the loop any client runs on: a
#  client is asked for its own, and `pyrogram/sync.py` wraps every method at import time,
#  before there is a client or a loop to ask.
_loop: asyncio.AbstractEventLoop | None = None


def get_running_loop() -> asyncio.AbstractEventLoop | None:
    """Return the loop the calling thread is inside, or `None`. Never builds one."""
    try:
        return asyncio.get_running_loop()
    except RuntimeError:
        return None


def get_event_loop() -> asyncio.AbstractEventLoop:
    """Return the loop the caller is inside, building one when the caller is inside none."""
    global _loop  # noqa: PLW0603

    running = get_running_loop()

    if running is not None:
        return running

    if _loop is None or _loop.is_closed():
        _loop = asyncio.new_event_loop()
        asyncio.set_event_loop(_loop)

    return _loop
