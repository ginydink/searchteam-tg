from random import randint

from aiogram import Router,F
from aiogram.types import CallbackQuery

from handlers.commands import command_router

callback_router = Router()


@callback_router.callback_query(F.data == "send_test")
async def send_test_text(callback: CallbackQuery):
    await callback.answer("ты прошел тест")
    await callback.message.answer(text ="обработали send_test callback")
@callback_router.callback_query(F.data == "helping")
async def helping(callback: CallbackQuery):
    await callback.answer("бог тебе в помощь ")
    await callback.message.answer(text= "<span class=\"tg-spoiler\">@daniilgino</span> я тебе помогу",parse_mode="HTML")
@callback_router.callback_query(F.data == "team")
async def team(callback: CallbackQuery):
    await callback.answer("Ищем команды")
    await callback.message.answer(text = "Выбирай какая команда нравится")
@callback_router.callback_query(F.data == "player")
async def player(callback:CallbackQuery):
    await callback.answer("Ищем игроков")
    await callback.message.answer(text="Удачи в поиске игрока")
@callback_router.callback_query(F.data == "knife")
async def luck(callback:CallbackQuery):
    b = randint(5000,15000)
    a = randint(0,10)
    if a > 8:
        await callback.answer("УРА ПОБЕДА")
        await callback.message.answer( f"А ты везунчик,тебе выпал нож за {b}р")
    else:
        await callback.answer("грустный додепчик")
        await callback.message.answer(text = "Не везет в кейсах повезет в любви")
@callback_router.callback_query(F.data == "skin")
async def luck(callback:CallbackQuery):

    await callback.answer("Unlucky")
    a = randint(0,10)
    if a > 4 :
        await callback.answer("Unlucky")
        await callback.message.answer("Анлаки,нужен додеп")
    else:
        b = randint(1, 2500)
        await callback.answer("lucky")
        await callback.message.answer(f"Скин за {b}р это солидный выигрыш")
