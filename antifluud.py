import time
from mailbox import Message

from aiogram import BaseMiddleware
from aiogram.types import Message
from collections import defaultdict

class AntiFloodMiddleware(BaseMiddleware):

    def __init__(self,delay:float = 0.5):
       self.delay = delay
       self.last_time = defaultdict(lambda :0)

    async def __call__(self, handler,event:Message,data):
        user_id = event.from_user.id
        current_time = time.time()

        if current_time - self.last_time[user_id] < self.delay:
            await event.answer("ИДИ ОТДОХНИ")
            return
        else:
            self.last_time[user_id] = current_time
            return await handler(event,data)