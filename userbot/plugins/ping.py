# rewritten by @saravanakrish

from telethon import events
from datetime import datetime

from userbot import ALIVE_NAME, CMD_HELP
from userbot.utils import admin_cmd
from userbot.manager.utils import edit_or_reply

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "TamilBotð®ð³"


@command(pattern="^.ping")
async def _(event):
    if event.fwd_from:
        return
    IMSID = bot.uid
    start = datetime.now()
    event = await edit_or_reply(event, "__**ð´ð»ââï¸ Pong!__**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(
        f"__**ð´ð»ââï¸ á´á´É´É¢!__**\nâ¥__**á´ÉªÉ´É¢ ê±á´á´á´á´**__ {ms}\nâ¥ __**Êá´á´**__ __**á´ê°**__ [{DEFAULTUSER}](tg://user?id={IMSID})"
    )

CMD_HELP.update(
    {
        "Ping":

        """â¼â¢â ð²ð¼ð½ð³ ââ¢â¾  :`.ping`\
\nâ¼â¢â ððð°ï¸ð¶ð´ ââ¢â¾  Check your bot status.\
"""
    }
)
