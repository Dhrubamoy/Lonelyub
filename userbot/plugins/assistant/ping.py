# Copyright (C) Midhun KM
#
# Please Don't Kang Without Credits
# A Plugin For Assistant Bot
# x0x

from datetime import datetime

from telethon import events

from userbot import *
from userbot import ALIVE_NAME
from userbot.plugins import *
from userbot.utils import *

LEGEND_IMG = os.environ.get(
    "BOT_PING_PIC", "https://telegra.ph/file/a9f6a3c160977352dd595.jpg"
)


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


@tgbot.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    start = datetime.now()
    event = await edit_or_reply(event, "**(❛ ᑭσɳց ❜!**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    if LEGEND_IMG:
        legend_caption = (
            f"**꧁•⊹٭Ping٭⊹•꧂**\n\n   ⚜ {ms}\n   ⚜ ❝𝐌𝐲 𝐌𝐚𝐬𝐭𝐞𝐫❞ ~『{ALIVE_NAME}』"
        )
        await tgbot.send_message(event.chat_id, LEGEND_IMG, caption=legend_caption)
