from aiogram import types

def get_menu_markup(language):
    if language == 'ru':
        markup = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("▫️Начнем!", callback_data='cosmetology')

        markup.row(item1)
        return markup
    elif language == 'en':
        markup = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("▫️Go!", callback_data='cosmetology')

        markup.row(item1)
        return markup