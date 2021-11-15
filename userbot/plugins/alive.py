import time
import random
import time
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot
from userbot.Config import Config
from telethon import version
import time
from userbot import ALIVE_NAME, LEGENDversion
from LEGENDBOT.utils import admin_cmd, edit_or_reply, sudo_cmd, time_formatter
from userbot.cmdhelp import CmdHelp
from . import *

uptime = get_readable_time((time.time() - StartTime))
DEFAULTUSER = ALIVE_NAME or "𝖑𝖊ɠêɳ̃dẞø✞︎ 🇮🇳"
LEGEND_IMG = "https://telegra.ph/file/153977a71b928874151a5.jpg"
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "ℓєgєи∂ Choice 𝖑𝖊ɠêɳ̃dẞø✞︎"
CUSTOM_YOUR_GROUP =Config.YOUR_GROUP or "@Legend_Userbot"

Legend = bot.uid
mention = f"[{DEFAULTUSER}](tg://user?id={Legend})"

@bot.on(admin_cmd(outgoing=True, pattern="legend$"))
@bot.on(sudo_cmd(pattern="legend$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)

    if  LEGEND_IMG:
        LEGEND_caption = f"**{CUSTOM_ALIVE_TEXT}**\n"
        
        LEGEND_caption += f"~~~~~~~~~~~~~~~~~~~~~~~\n"
        LEGEND_caption += f"        **✘𝕭𝖔† 𝕾𝖙𝖆𝖙𝖚𝖘✘** \n"
        LEGEND_caption += f"•🔥• **Oաղ̃ҽ̈ɾ**          ~ {ALIVE_NAME}\n\n"
        LEGEND_caption += f"•🌟• **𝖑𝖊ɠêɳ̃dẞø†**   ~ {LEGENDversion}\n"
        LEGEND_caption += f"•🌟• **†ҽ̀lҽ́thøղ̃**     ~ `{version.__version__}`\n"
        LEGEND_caption += f"•🌟• **𝚄ρtime**         ~ `{uptime}`\n"
        LEGEND_caption += f"•🌟• **𝙶𝚛𝚘𝚞𝚙**           ~ [𝙶𝚛𝚘𝚞𝚙](t.me/Legend_Userbot)\n"
        LEGEND_caption += f"•🌟• **𝙼𝚢 𝙶𝚛𝚘𝚞𝚙**  ~ {CUSTOM_YOUR_GROUP}\n"   

        await alive.client.send_file(
            alive.chat_id, LEGEND_IMG, caption=LEGEND_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"~~~~~~~~~~~~~~~~~~~~~~~ \n"
            f"         \n"
            f"•⚡• 𝕿єℓєτнοи    : `{version.__version__}`\n"
            f"🇮🇳 ℓєgєи∂ϐοτ  : `{LEGENDversion}`\n"
            f"🇮🇳 υρτιмє        : `{uptime}`\n"
            f"🔱 ɱαรƭεɾ        : {mention}\n"
            f"🔱 σωɳεɾ         : [ℓєgєи∂](t.me/The_LegendBoy)\n"
        )


msg = f"""
**  ⚜️ Lêɠêɳ̃dẞø† ιѕ σиℓιиє ⚜️**

       {Config.ALIVE_MSG}
    **  Bø✞︎ ẞ✞︎α✞︎µѕ **
**•⚜️•Øաղ̃ҽ̈r     :** **{mention}**
**•🌹•𝖑𝖊ɠêɳ̃dẞø✞︎  :** {LEGENDversion}
**•🌹•✞︎ҽ̀lҽ́ƭhøղ  :** {version.__version__}
**•🌹•Ãbûßê     :**  {abuse_m}
**•🌹•ßudø      :**  {is_sudo}
**•🌹•Bøt.      :** {Config.BOY_OR_GIRL}
"""
botname = Config.BOT_USERNAME

@bot.on(admin_cmd(pattern="alive$"))
@bot.on(admin_cmd(pattern="alive$", allow_sudo=True))
async def legend_a(event):
    try:
        legend = await bot.inline_query(botname, "alive")
        await legend[0].click(event.chat_id)
        if event.sender_id == The_LegendBoy:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)

CmdHelp("alive").add_command(
    "bot", None, "υѕє αи∂ ѕєє"
).add_command(
    "legend", None, "Its Same Like Alive"
).add_command(
    "alive", None, "Its Show ur Alive Template"
).add_warning(
    "Harmless Module✅"
).add_info(
     "Checking Alive"
).add_type(
    "Official"
).add()
