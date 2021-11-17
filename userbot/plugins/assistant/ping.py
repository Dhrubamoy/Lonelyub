import os
from datetime import datetime

from userbot import *
from userbot.Config import Config
from userbot.plugins import *

LEGEND_IMG = os.environ.get(
    "BOT_PING_PIC", "https://telegra.ph/file/a9f6a3c160977352dd595.jpg"
)


@tgbot.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    start = datetime.now()
    end = datetime.now()
    (end - start).microseconds / 1000
    if LEGEND_IMG:
        legend_caption = (
            f"**꧁•⊹٭Ping٭⊹•꧂**\n\n   ⚜ 4\n   ⚜ ❝𝐌𝐲 𝐌𝐚𝐬𝐭𝐞𝐫❞ ~『{Config.ALIVE_NAME}』"
        )
        await tgbot.send_message(event.chat_id, LEGEND_IMG, caption=legend_caption)
