from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

from handlers.callback import callback_router

search_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text = "search_team", url="https://t.me/newcsgo")],
    ]
)
help_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text= "help", callback_data="helping")]
    ]
)
training_kb = InlineKeyboardMarkup(
    inline_keyboard = [
    [InlineKeyboardButton(text="training💪🏿", url="https://www.3daimtrainer.com/cs2-guide-how-to-improve/")]]

)
choicer_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="найти команду😘", callback_data="team")],
        [InlineKeyboardButton(text="найти игрока💋",callback_data="player")]
    ]
)
back_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="найти команду😘", callback_data="team"),
        InlineKeyboardButton(text="найти игрока💋", callback_data="player")],
        [InlineKeyboardButton(text= "help🥺", callback_data="helping"),
         InlineKeyboardButton(text="tgk❤️", url="https://t.me/rishe1ie")]


    ]
)
random_case = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="knife🔪",callback_data="knife"),
         InlineKeyboardButton(text="skin🔫",callback_data="skin")]
    ]
)