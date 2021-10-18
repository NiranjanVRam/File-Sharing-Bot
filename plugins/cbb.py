#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : <a href='tg://user?id={OWNER_ID}'>LiqWid</a>\n\n○ Language : <code>Python3</code>\n\n○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n\n○ MOVIES : <a href='https://t.me/fhmoviechat'>FH MOVIES</a>\n\n\n\n○ SERIES : <a href='https://t.me/fhserieschat'>FH SERIES</a>\n\n○ CHANNEL : <a href='https://t.me/fileshomeofficial'>FH GROUP</a>\n\n○ SUPPORT : <a href='https://t.me/fhhelperbot'>Click Here</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
