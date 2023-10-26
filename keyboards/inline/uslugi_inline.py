from aiogram import types


def get_services_keyboard(language):
    if language == 'ru':
        markup = types.InlineKeyboardMarkup()

        back_button = types.InlineKeyboardButton('Назад↩️', callback_data='back_services')

        markup.add(back_button)
        return markup
    elif language == 'en':
        markup = types.InlineKeyboardMarkup()

        back_button = types.InlineKeyboardButton('Back↩️', callback_data='back_services')

        markup.add(back_button)
        return markup