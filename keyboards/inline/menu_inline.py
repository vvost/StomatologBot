from aiogram import types

# Функция для получения инлайн клавиатуры "О нас"
def get_about_keyboard(language):
    if language == 'ru':
        markup = types.InlineKeyboardMarkup()
        item = types.InlineKeyboardButton('О нас👩🏻‍⚕️🦷', callback_data='about')
        item1 = types.InlineKeyboardButton('Услуги📋', callback_data='services1')
        item2 = types.InlineKeyboardButton('Контакты📞', callback_data='contacts')
        item3 = types.InlineKeyboardButton('Запись📋', callback_data='appointment')
        markup.add(item,item1,item2, item3)
        return markup
    elif language == 'en':
        markup = types.InlineKeyboardMarkup()
        item = types.InlineKeyboardButton('About Us👩🏻‍⚕️🦷', callback_data='about')
        item1 = types.InlineKeyboardButton('Services📋', callback_data='services1')
        item2 = types.InlineKeyboardButton('Contacts📞', callback_data='contacts')
        item3 = types.InlineKeyboardButton('Appointment📋', callback_data='appointment')
        markup.add(item,item1,item2,item3)
        return markup

def getkeyboard(language):
    if language == 'ru':
        markup = types.InlineKeyboardMarkup()
        item = types.InlineKeyboardButton('О нас👩🏻‍⚕️🦷', callback_data='about')
        item11 = types.InlineKeyboardButton('Услуги📋', callback_data='services1')
        item22 = types.InlineKeyboardButton('Контакты📞', callback_data='contacts')
        item33 = types.InlineKeyboardButton('Запись📋', callback_data='appointment')
        markup.row(item)
        markup.row(item11, item22, item33)
        return markup
    elif language == 'en':
        markup = types.InlineKeyboardMarkup()
        item = types.InlineKeyboardButton('About Us👩🏻‍⚕️🦷', callback_data='about')
        item1 = types.InlineKeyboardButton('Services📋', callback_data='services1')
        item2 = types.InlineKeyboardButton('Contacts📞', callback_data='contacts')
        item3 = types.InlineKeyboardButton('Appointment📋', callback_data='appointment')
        markup.row(item)
        markup.row(item1, item2, item3)
        return markup



