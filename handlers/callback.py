import random
from codecs import replace_errors
from random import randint
from handlers.database import add_user, get_name,get_team
from aiogram import Router,F
from aiogram.types import CallbackQuery
from keyboards.inline import like_player,like_team

from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram import Router,F
from aiogram.filters import Command,or_f
from aiogram.fsm.state import State, StatesGroup

from handlers.database import add_user,add_team
command_router = Router()
from keyboards.inline import search_kb, help_kb, training_kb,choicer_kb,back_menu,random_case
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
    y = get_team()
    team = random.choice(y)
    await callback.message.answer(text = str(f"Название команды {team[0]}\nСредний возраст в команде {team[2]}\nО команде {team[1]}\nКонтакт для вступления в команду {team[3]}"),reply_markup = like_team)
@callback_router.callback_query(F.data == "player")
async def player(callback:CallbackQuery):
    await callback.answer("Ищем игроков")
    t = get_name()
    player  = random.choice(t)
    await callback.message.answer(text = str(f"Nickname {player[0]},\nВозраст {player[2]}\nКол-во эло {player[2]}\nКонтакт для связи {player[3]}"),reply_markup=like_player)
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
    await callback.message.delete()
    await callback.message.answer(text = str(f"Nickname {player[0]},\nВозраст {player[2]}\nКол-во эло {player[1]}\nКонтакт для связи {player[3]}"),reply_markup=like_player)
@callback_router.callback_query(F.data == "yes")
async def yes(callback:CallbackQuery):
    await callback.answer("Спасибо за использование бота")
    await callback.message.answer_photo(photo="https://open-images.acast.com/shows/67282bf5ce5bc563cb7669da/1736127936400-01e65e0d-784e-4d66-9237-f99895fee5d8.jpeg?height=750",caption = "/menu чтобы перейти в меню или\n/choice чтобы продолжить поиск")
@callback_router.callback_query(F.data == "antitilt")
async def tilt(callback:CallbackQuery):
    await callback.answer("у тебя все получится")
    await callback.message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQb0T-L32BhvgBV7-E4eUo5YoC6QdUEplVFog&s",caption = "Не тильтуй")
@callback_router.callback_query(F.data == "nos")
async def select(callback:CallbackQuery):
    await callback.answer("Не отчаивайся")
    a = get_team()
    team  = random.choice(a)
    await callback.message.delete()
    await callback.message.answer(text = str(f"Название команды {team[0]}\nСредний возраст в команде {team[2]}\nО команде {team[1]}\nКонтакт для вступления в команду {team[3]}"),reply_markup = like_team)
@callback_router.callback_query(F.data == "yes")
async def yes(callback:CallbackQuery):
    await callback.answer("Спасибо за использование бота")
    await callback.message.answer_photo(photo="https://open-images.acast.com/shows/67282bf5ce5bc563cb7669da/1736127936400-01e65e0d-784e-4d66-9237-f99895fee5d8.jpeg?height=750",caption = "/menu чтобы перейти в меню")
class Form(StatesGroup):
    team = State()
    mid_age = State()
    description = State()
    usernam = State()
    menu = State()
@callback_router.callback_query(F.data == "reg")
async def verify(m:Message,state:FSMContext):
    await m.answer("Напиши название команды")
    await state.set_state(Form.team)
@callback_router.callback_query(Form.team)
async def name_answer (m:Message,state:FSMContext):
    await state.update_data(team=m.text)
    await state.set_state(Form.mid_age)
    await m.answer(text = "Какой средний возраст игроков в вашей команде")
@callback_router.callback_query(Form.mid_age, F.text.isdigit())
async def age_answer (m:Message,state:FSMContext):
    await state.update_data(mid_age = m.text)
    data = await state.get_data()
    a = int(data['mid_age'])
    if a < 100:
        data = await state.get_data()
        await state.set_state(Form.description)
        await m.answer(text= f"Хорошое название, {data['team']}\nнапиши немного о своей команде")
    else:
        await m.answer(text="Некорректный возраст,введите свой реальный возраст")
@callback_router.callback_query(Form.description,F.text)
async def elo_answer (m:Message,state:FSMContext):
    await state.update_data(description = m.text)
    await m.answer(text = f"Введи свой юзернейм в тг")
    await state.set_state(Form.usernam)
@callback_router.callback_query(Form.usernam,F.text)
async def username_sys(m:Message,state:FSMContext):
    await state.update_data(usernam = m.text)
    data = await state.get_data()
    add_team(
        user_id = m.from_user.id,
        team = data['team'],
        mid_age = int(data['mid_age']),
        description = data['description'],
        usernam = data['usernam']
    )
    await state.set_state(Form.menu)
    await m.answer(text = f"Ваша заявка принята✅\nНазвание твоей команды {data['team']}\nСредний возраст в команде {data['mid_age']}\nКраткое описание команды {data['description']}\nКонтакт для связи {data['usernam']}\nНапиши что-то для продолжения работы бота")
@callback_router.callback_query(Form.menu)
async def menus_updat(m:Message,state:FSMContext):
    await state.update_data(menus = m.text)
    await m.answer_photo(photo = "https://media.istockphoto.com/id/1172427455/ru/%D1%84%D0%BE%D1%82%D0%BE/%D0%BA%D1%80%D0%B0%D1%81%D0%B8%D0%B2%D1%8B%D0%B9-%D0%B7%D0%B0%D0%BA%D0%B0%D1%82-%D0%BD%D0%B0%D0%B4-%D1%82%D1%80%D0%BE%D0%BF%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%BC-%D0%BC%D0%BE%D1%80%D0%B5%D0%BC.jpg?s=612x612&w=0&k=20&c=mMM_lQ6H5YKUc4vT87reiS8wGxhc66lEyrUuBm15J3M=",caption="выбери что ты хочешь сделать",reply_markup=back_menu)
    await state.clear()
