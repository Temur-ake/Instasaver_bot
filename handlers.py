import asyncio

from aiogram import Router, Bot
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"<i>Assalomu aleykum, <b>{message.from_user.full_name} 👋🏻</b> link yuboring !</i>")
    answer = await message.answer(text=f"👇🏻")


@router.message(Command(commands='help'))
async def help_command(message: Message) -> None:
    await message.answer('''Buyruqlar:
/start - Botni ishga tushirish
/help - Yordam''')


@router.message()
async def sent_to_video(message: Message, bot: Bot) -> None:
    try:
        copy = message.send_copy(chat_id=message.chat.id).text
        if copy and copy.startswith('https://www.instagram.com/') and len(copy) >= 42:
            copy = copy[:12] + "dd" + copy[12:]
            animation = await message.answer(text=f"⏳")
            await asyncio.sleep(1)
            # for i in ["3️⃣", "2️⃣", "1️⃣"]:
            #     await asyncio.sleep(1)
            #     await animation.edit_text(text=f"<strong>{i} ...</strong>")
            await bot.delete_message(chat_id=message.chat.id, message_id=animation.message_id)
            result = await message.answer(text=f"<strike>{copy}</strike>", parse_mode=ParseMode.HTML)
            await message.answer('@instasave_studiobot - Eng sevimli videolaringizni yuklab oling ✅!')
        else:
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            sent = await message.answer(text=f"<b> Link hato yoki Post topilmadi !!! </b>")
            await asyncio.sleep(3)
            await bot.delete_message(chat_id=message.chat.id, message_id=sent.message_id)
    except:  # noqa
        await message.answer("Yana urunib ko'ring !")




begin_router = Router()

begin_router.include_router(
    router,
)