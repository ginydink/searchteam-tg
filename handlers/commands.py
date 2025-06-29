

from aiogram.types import Message,InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Router,F
from aiogram.filters import Command,or_f


command_router = Router()
from keyboards.inline import search_kb, help_kb, training_kb,choicer_kb,back_menu,random_case
@command_router.message((Command("start")))
async def start_handler(message:Message):
    start_text = "Выбери что ты хочешь сделать,но для начала пройди /verify"
    await message.answer(text= start_text)

@command_router.message(Command("about"))
async def about_handler(message:Message):
    about_text = (
    "Устал сливать эло на фасике?\n"
    "Тогда этот бот идеальное решение для тебя,ведь здесь ты всегда можешь найти игроков по своему скилу и просто друзей \n"
    "Если хочешь еще играть и с красивыми скинчиками, то переходи в этого бота @skin_builds_bot закупапйся и кайфуй"
)
    await message.answer(text= about_text)
@command_router.message(F.text.lower().contains("привет"))
async def send_cute_message(message: Message):
    cute_text = "Дарова родник"
    await message.answer(photo = "https://blog.marathonbet.ru/wp-content/uploads/2025/01/m0NESY-HLTV-Awards.jpg",text = cute_text)
@command_router.message(F.text.lower().contains("ты урод"))
async def send_cute_message(message: Message):
    cute_text = "Ты милый 💋"
    await message.answer(text = cute_text)

@command_router.message(F.photo)
async def react_to_photo(photo:Message):
    text_to_photo = (
        "Прикольная фоточка"
    )
    await photo.reply(text = text_to_photo)

@command_router.message(F.reply_to_message & F.text.lower().contains("спасибки родник"))
async def react_to_reply(photo:Message):
    react_reply = ("Зачем ты меня тегаешь?")
    await photo.reply(text= react_reply)
@command_router.message(F.text == "❤️")
async def react_to_heart(message:Message):
    react_to_heart = (
        "Спасибо за сердечко)"
    )
    await message.reply(text = react_to_heart)
@command_router.message(F.text.lower().contains("пока"))
async def send_cute_message(message: Message):
    cute_text = "гуд бай"
    await message.answer(text = cute_text)
@command_router.message(F.sticker)
async def react_to_photo(photo:Message):
    text_to_photo = (
        "Классный стикер"
    )
    await photo.reply(text = text_to_photo)
@command_router.message(Command("search"))
async def search_tea( m: Message):
    search_tea = "Оставь заявку или перейди по ссылке"
    await m.answer_photo(photo = "https://blog.marathonbet.ru/wp-content/uploads/2025/01/m0NESY-HLTV-Awards.jpg",caption= search_tea,reply_markup=search_kb)
@command_router.message(Command("help"))
async def search_tea( m: Message):
    helping = "Возможно это тебе поможет"
    await m.answer(text= helping,reply_markup=help_kb)
@command_router.message(Command("training"))
async def trainig_wait(m:Message):
    trainig_wat = "Потренируйся пока ждешь игру"
    await m.answer_photo(photo = "https://cdn.steelfactor.ru/2014/1403081918.jpg",caption=trainig_wat,reply_markup=training_kb)
@command_router.message(Command("verify_name"))
async def get_name(m: Message):
    verificate = "Введи свой ник"
    await m.answer(text=verificate)
@command_router.message(Command("verify_elo"))
async def get_elo(m:Message):
        elo = "Напиши сколько у тебя эло?"
        await m.answer(text=elo)
@command_router.message(Command("verify_age"))
async def get_age(m:Message):
        age = "Сколько тебе лет?"
        await m.answer(text=age)
@command_router.message(Command("choice"))
async def choice(m:Message):
    what_choice = "Выбери кого ты хочешь найти"
    await m.answer(photo = "https://cs-config.ru/_ld/12/42477246.png",text=what_choice,reply_markup=choicer_kb)
@command_router.message(Command("verify"))
async def verify(m:Message):
    good_verify = "Спасибо теперь ты зарегистрирован, дальше используй /choice"
    await m.answer(text=good_verify)
@command_router.message(Command("menu"))
async def back(m:Message):
    back_men = "Выберите что вы хотите сделать"
    await m.answer_photo(photo = "https://media.istockphoto.com/id/1172427455/ru/%D1%84%D0%BE%D1%82%D0%BE/%D0%BA%D1%80%D0%B0%D1%81%D0%B8%D0%B2%D1%8B%D0%B9-%D0%B7%D0%B0%D0%BA%D0%B0%D1%82-%D0%BD%D0%B0%D0%B4-%D1%82%D1%80%D0%BE%D0%BF%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%BC-%D0%BC%D0%BE%D1%80%D0%B5%D0%BC.jpg?s=612x612&w=0&k=20&c=mMM_lQ6H5YKUc4vT87reiS8wGxhc66lEyrUuBm15J3M=",caption=back_men,reply_markup=back_menu)
@command_router.message(Command("case"))
async def case(m:Message):
        cases = "Выбери что тебе упадет с кейса,все максимально честно"
        await m.answer_photo(photo="https://jabka.skin/cdn/serviceitems/5bb360d9-c5e7-49cc-8021-bbbd16c51625-676bcf9650b37.webp",caption=cases,reply_markup=random_case)
@command_router.message(Command("favourite_maps"))
async def maps(m:Message):
    await m.answer_poll(
        question= "Какая твоя любимая карта?",
        options = ["Mirage","Dust 2","Nuke","Inferno","Anubis"],
        is_anonymous = False
    )
