from aiogram.fsm.state import State, StatesGroup

class Form(StatesGroup):
    name  = State()
    age = State
    like_bots = State()

class Faivourites(StatesGroup):
    color = State()
    food = State()