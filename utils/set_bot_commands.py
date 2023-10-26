#Установка команд для бота

from aiogram import types
async def set_bot_commadns(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('/start', 'Запуск бота')
    ])