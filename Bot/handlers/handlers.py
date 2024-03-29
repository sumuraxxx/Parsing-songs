from aiogram import types, Router
from aiogram.filters import Command, CommandStart
from aiogram.utils.markdown import hbold

from Bot.parsing.parsing_text_songs import *

router = Router()


@router.message(CommandStart())
async def cmd_start(msg: types.Message) -> None:
    first_name = hbold(msg.from_user.first_name)
    await msg.answer(
        text=f"<b>привет</b>, {first_name}!!!!\n<b>введи команду</b> /text {msg}"
    )


@router.message(Command('text'))
async def cmd_song_text(msg: types.Message) -> None:
    song_text = None
    while song_text is None:
        song_text = await display_cleaned_lyrics()
    await msg.answer(
        text=f'<b>{song_text[0]}\n<em>({song_text[1][1]} - {song_text[1][2]})</em></b>'
    )



