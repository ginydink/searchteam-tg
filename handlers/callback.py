import random
from random import randint
from handlers.database import add_user, get_name
from aiogram import Router,F
from aiogram.types import CallbackQuery
from keyboards.inline import next_user,like_player

callback_router = Router()


@callback_router.callback_query(F.data == "send_test")
async def send_test_text(callback: CallbackQuery):
    await callback.answer("ты прошел тест")
    await callback.message.answer(text ="обработали send_test callback")
@callback_router.callback_query(F.data == "helping")
async def helping(callback: CallbackQuery):
    await callback.answer("бог тебе в помощь ")
    await callback.message.answer_photo(photo="https://img16.rl0.ru/afisha/e375x235p1147x364f1670x1047q85i/s3.afisha.ru/mediastorage/a9/7f/7f1cf8f4ec4f41c5a62674107fa9.jpg",caption= "<span class=\"tg-spoiler\">@daniilgino</span> я тебе помогу",parse_mode="HTML")
@callback_router.callback_query(F.data == "team")
async def team(callback: CallbackQuery):
    await callback.answer("sorry")
    await callback.message.answer(text = "Команда пока что в разработке")
@callback_router.callback_query(F.data == "player")
async def player(callback:CallbackQuery):
    await callback.answer("Ищем игроков")
    t = get_name()
    player  = random.choice(t)
    await callback.message.answer(text = str(f"Nickname {player[0]},\nВозраст {player[1]}\nКол-во эло {player[2]}\nКонтакт для связи {player[3]}"),reply_markup=like_player)
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
@callback_router.callback_query(F.data == "no")
async def select(callback:CallbackQuery):
    await callback.answer("Не отчаивайся")
    t = get_name()
    player  = random.choice(t)
    await callback.message.edit_text(text = str(f"Nickname {player[0]},\nВозраст {player[2]}\nКол-во эло {player[1]}\nКонтакт для связи {player[3]}"),reply_markup=like_player)
@callback_router.callback_query(F.data == "yes")
async def yes(callback:CallbackQuery):
    await callback.answer("Спасибо за использование бота")
    await callback.message.answer_photo(photo="https://open-images.acast.com/shows/67282bf5ce5bc563cb7669da/1736127936400-01e65e0d-784e-4d66-9237-f99895fee5d8.jpeg?height=750",caption = "/menu чтобы перейти в меню или\n/search чтобы продолжить поиск")
@callback_router.callback_query(F.data == "antitilt")
async def tilt(callback:CallbackQuery):
    await callback.answer("у тебя все получится")
    await callback.message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQb0T-L32BhvgBV7-E4eUo5YoC6QdUEplVFog&s",caption = "Не тильтуй")

