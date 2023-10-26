from aiogram import types

def about(language):
    if language == 'ru':
        markup = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("Назад↩️",callback_data='back')
        markup.row(item1)
        return markup
    elif language == 'en':
        markup = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton('Back↩️',callback_data='back')

        markup.row(item1)
        return markup