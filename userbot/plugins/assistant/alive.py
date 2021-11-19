from telethon import events

from userbot import *

from . import *

PM_IMG = "https://telegra.ph/file/c26fc61e904476083baa7.jpg"
pm_caption = f"⚜『LONELY』Is Ôñĺîne⚜ \n\n"
pm_caption += f"MASTER ~ 『{legend_mention}』\n"
pm_caption += f"**╭───────────**\n"
pm_caption += f"┣Ťêlethon ~ `1.15.0` \n"
pm_caption += f"┣『Lonely Version』~ `{LEGENDversion}` \n"
pm_caption += f"┣Çhâññel ~ [Channel](https://t.me/lonely_userbot)\n"
pm_caption += f"┣**License** ~ [License v3.0](github.com/The-LegendBot/LEGENBOT/blob/master/LICENSE)\n"
pm_caption += f"┣Copyright ~ By [『Lêɠêɳ̃dẞø†』 ](https://t.me/Legend_Userbot)\n"
pm_caption += f"┣Creator ~ By [『Dhruba』 ](https://t.me/Dhruba_XD)\n"
pm_caption += f"┣Assistance ~ By [『Akki』 ](https://t.me/Akki_ThePro)\n"
pm_caption += f"╰────────────\n"
pm_caption += f"       »»» [『⪨Lonelyboτ⪩』](https://t.me/lonely_Userbot) «««"


@tgbot.on(events.NewMessage(pattern="^/alive"))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
