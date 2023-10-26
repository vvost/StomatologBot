#Предупржедалка для админов

# from aiogram import Dispatcher, types
# from data.config import admins
# import logging
#
# async def notify_admins(dp: Dispatcher):
#     for admin in admins: #Отправка по всем админам текст
#         try:
#             text = 'OHAYO!'
#             await dp.bot.send_message(chat_id=admin, text=text)
#         except Exception as err:
#             logging.exception(err)