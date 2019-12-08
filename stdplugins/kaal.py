"""use cmd .kaal
aaahaaa you can edit this 😉"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 30)

    input_str = event.pattern_match.group(1)

    if input_str == "KAAL":

        await event.edit(input_str)

        animation_chars = [

            "👑KAAL👑👑👑👑KAAL👑👑KAAL👑👑KAAL👑\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑",

            "◼️👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑",

            "◼️◼️👑KAAL👑👑KAAL👑👑KAAL👑\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑",

            "◼️◼️◼️️👑KAAL👑👑KAAL👑\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑",

            "◼️◼️◼️◼️👑KAAL👑\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑",

            "‎◼️◼️◼️◼️◼️\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑",

            "◼️◼️◼️◼️◼️\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑◼️\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑",

            "◼️◼️◼️◼️◼️\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑◼️\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑◼️\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑",

            "◼️◼️◼️◼️◼️\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑◼️\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑◼️\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑◼️\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑",

            "◼️◼️◼️◼️◼️\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑◼️\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑◼️\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑◼️\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑◼️",

            "◼️◼️◼️◼️◼️\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑◼️\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑◼️\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑◼️\n👑KAAL👑👑KAAL👑👑KAAL👑◼️◼️",

            "◼️◼️◼️◼️◼️\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑◼️\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑◼️\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑◼️\n👑KAAL👑👑KAAL👑◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑◼️\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑◼️\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑◼️\n👑KAAL👑◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑◼️\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑◼️\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑◼️\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑◼️\n◼️👑KAAL👑👑KAAL👑👑KAAL👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑KAAL👑👑KAAL👑👑KAAL👑👑KAAL👑◼️\n◼️👑KAAL👑👑KAAL👑👑KAAL👑◼️\n◼️👑KAAL👑👑KAAL👑👑KAAL👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️👑KAAL👑👑KAAL👑👑KAAL👑◼️\n◼️👑KAAL👑👑KAAL👑👑KAAL👑◼️\n◼️👑KAAL👑👑KAAL👑👑KAAL👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️👑KAAL👑👑KAAL👑◼️\n◼️👑KAAL👑👑KAAL👑👑KAAL👑◼️\n◼️👑KAAL👑👑KAAL👑👑KAAL👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️👑KAAL👑◼️\n◼️👑KAAL👑👑KAAL👑👑KAAL👑◼️\n◼️👑KAAL👑👑KAAL👑👑KAAL👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑KAAL👑👑KAAL👑👑KAAL👑◼️\n◼️👑KAAL👑👑KAAL👑👑KAAL👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑KAAL👑👑KAAL👑◼️◼️\n◼️👑KAAL👑👑KAAL👑👑KAAL👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑KAAL👑👑KAAL👑◼️◼️\n◼️👑KAAL👑👑KAAL👑◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑KAAL👑👑KAAL👑◼️◼️\n◼️👑KAAL👑◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑KAAL👑👑KAAL👑◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️👑KAAL👑◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️",

            "◼️◼️◼️\n◼️◼️◼️\n◼️◼️◼️",

            "◼️◼️\n◼️◼️",

            "◼️",
            "👑 KAAL 👑"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 31])
