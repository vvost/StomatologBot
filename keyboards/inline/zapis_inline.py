from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import types

def get_keyboards(language):
    if language=='ru':
        markup = ReplyKeyboardMarkup(
            keyboard=[

                    [KeyboardButton("-Профессиональная гигиеническая и пародонтологическая чистка зубов ."),],
                    [KeyboardButton("-Лечение кариеса,пульпита и периодонтита."),],
                    [KeyboardButton("-Удаление зубов."),],
                    [KeyboardButton("-Имплантация и протезирование на имплантатах ."),],
                    [KeyboardButton("-Протезирование металлокерамическими и безметалловыми коронками (imax,цирконий)."),],
                    [KeyboardButton("-Стемное протезирование."),],
                    [KeyboardButton("-Микропротезирование (вкладки)."),],
                    [KeyboardButton("-Лечение детей."),],
                    [KeyboardButton("-Удаление  молочных зубов."),],
                    [KeyboardButton("-Постановка коронок на молочные зубы."),],
                    [KeyboardButton("Ботулинотерапия."),],
                    [KeyboardButton("Коррекция:носогубных складок."),],
                    [KeyboardButton("Формы и объема губ."),],
                    [KeyboardButton("Коррекция скул,формы подбородка,углонижней челюсти филлерами."),],
                    [KeyboardButton("Лифтинг овала лица,работа со вторым подбородком и брылями."),],
                    [KeyboardButton("Коллагеновый лифтинг."),],
                    [KeyboardButton("Лечение целлюлита и коррекция."),],
                    [KeyboardButton("Работа с розацеей и гиперпигментацией."),],
                [
                    KeyboardButton("Розация и гиперпигментция."),
                ],

                ],


            resize_keyboard=True
        )
        return markup
    elif language=='en':
        markup = ReplyKeyboardMarkup(
            keyboard=[

                [
                    KeyboardButton("Professional hygienic and periodontal teeth cleaning.")
                ],
                [
                    KeyboardButton("-Treatment of caries, pulpitis and periodontitis."),],
                    [KeyboardButton("-Tooth extraction."),],
                    [KeyboardButton("-Implantation and prosthetics on implants."),],
                    [KeyboardButton("-Prosthetics with metal-ceramic and metal-free crowns (imax, zirconium)."),],
                    [KeyboardButton("-Stem prosthetics."),],
                    [KeyboardButton("-Microprosthetics (tabs)."),],
                    [KeyboardButton("-Treatment of children"),],
                    [KeyboardButton("-Removal of baby teeth."),],
                    [KeyboardButton("-Placing crowns on baby teeth."),],
                    [KeyboardButton("Botulinum therapy."),],
                    [KeyboardButton("Correction: nasolabial folds."),],
                    [KeyboardButton("Shape and volume of lips."),],
                    [KeyboardButton("Correction of cheekbones, chin shape, angles of the lower jaw with fillers."),],
                    [KeyboardButton("Lifting the oval of the face, working with a double chin and jowls."),],
                    [KeyboardButton("Collagen lifting."),],
                    [KeyboardButton("Cellulite treatment and body contouring."),],
                    [KeyboardButton("Working with rosacea and hyperpigmentation."),],


                [
                    KeyboardButton("Rosaria and hyperpigmentation.")
                ],
            ],
            resize_keyboard=True
        )
        return markup

def get_time():
    markup=ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton("8:30-10:00"),],
            [KeyboardButton("10:00-11:30"),],
            [KeyboardButton("11:30-13:00"),],
            [KeyboardButton("13:00-14:30"),],
            [KeyboardButton("14:30-16:00"),],
            [KeyboardButton("16:00-17:30"),],
            [KeyboardButton("17:30-19:00"),],
            [KeyboardButton("19:00-20:30"),],

        ],
        resize_keyboard=True
    )
    return markup

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