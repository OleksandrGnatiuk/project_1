from aiogram import types, Router
from aiogram.filters import CommandStart, Command, or_f
from aiogram import F

user_private_router = Router()


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(text="Привіт, я віртуальний помічник.")


@user_private_router.message(or_f(Command('menu'), F.text.lower().contains('меню')))
async def menu_cmd(message: types.Message):
    await message.answer(text='Ось меню:')


@user_private_router.message(Command('about'))
async def about_cmd(message: types.Message):
    await message.answer(text='Ми дуже відома компанія')


@user_private_router.message(Command('schedule'))
async def schedule_cmd(message: types.Message):
    await message.answer(text='Працюємо з 8,00 - 20,00 (Без вихідних)')


@user_private_router.message(F.photo | F.audio | F.sticker)
async def photo_cmd(message: types.Message):
    await message.answer(text='Мені також подобається')


@user_private_router.message(F.Audio)
async def photo_cmd(message: types.Message):
    await message.answer(text='Божественні звуки')


@user_private_router.message(F.Sticker | F.Emoji)
async def photo_cmd(message: types.Message):
    await message.answer(text='pizza')


@user_private_router.message(F.text.lower().contains("ціни"))
async def magic_price_cmd(message: types.Message):
    await message.answer(text='Актуальні ціни буде відправлено на вашу пошту')


# @user_private_router.message(F.text)
# async def magic_cmd(message: types.Message):
#     await message.answer(text='Це вже робота магічного фільтру')
