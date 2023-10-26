from aiogram import types
from loader import dp
from handlers.users.start import user_language
from keyboards.inline.uslugi_inline import get_services_keyboard
from keyboards.inline.menu_inline import get_about_keyboard


@dp.callback_query_handler(lambda c: c.data == 'services1')
async def handle_services(callback: types.CallbackQuery):
    chat_id = callback.message.chat.id
    language = user_language.get(chat_id, 'en')
    image1 = 'https://cloud.mail.ru/public/wpNx/SJ2GBDm1p'


    description = 'Dental services:\n▫️Professional hygienic and periodontal teeth cleaning.\n' \
                  '▫️Treatment of caries, pulpitis and periodontitis.\n' \
                  '▫️Tooth extraction.\n▫️Implantation and prosthetics on implants.' \
                  '\n▫️Prosthetics with metal-ceramic and metal-free crowns (imax, zirconium).' \
                  '\n▫️Stem prosthetics.' \
                  '\n▫️Microprosthetics (tabs).' \
                  '\n▫️Treatment of children.' \
                  '\n▫️Removal of baby teeth.' \
                  '\n▫️Placing crowns on baby teeth.\n'  \
                  '\nCosmetology services:' \
                  '\n◾️Botulinum therapy.' \
                  '\n◾️Correction: nasolabial folds.' \
                  '\n◾️Shape and volume of lips.' \
                  '\n◾️Correction of cheekbones, chin shape, angles of the lower jaw with fillers.' \
                  '\n◾️Lifting the oval of the face, working with a double chin and jowls.' \
                  '\n◾️Collagen lifting.' \
                  '\n◾️Cellulite treatment and body contouring.' \
                  '\n◾️Working with rosacea and hyperpigmentation.' \
                  '\n◾️Rosaria and hyperpigmentation.'


    if language == 'ru':
        description = 'Стоматологические услуги:\n▫️Профессиональная гигиеническая и пародонтологическая чистка зубов .\n' \
                  '▫️Лечение кариеса,пульпита и периодонтита.\n' \
                  '▫️Удаление зубов.\n▫️Имплантация и протезирование на имплантатах .' \
                  '\n▫️Протезирование металлокерамическими и безметалловыми коронками (imax,цирконий).' \
                  '\n▫️Стемное протезирование.' \
                  '\n▫️Микропротезирование (вкладки).' \
                  '\n▫️Лечение детей.' \
                  '\n▫️Удаление  молочных зубов .' \
                  '\n▫️Постановка коронок на молочные зубы.\n'  \
                  '\nКосметологические услуги:' \
                  '\n◾️Ботулинотерапия.' \
                  '\n◾️Коррекция:носогубных складок.' \
                  '\n◾️Формы и объема губ.' \
                  '\n◾️Коррекция скул,формы подбородка,углонижней челюсти филлерами.' \
                  '\n◾️Лифтинг овала лица,работа со вторым подбородком и брылями.' \
                  '\n◾️Коллагеновый лифтинг.' \
                  '\n◾️Лечение целлюлита и коррекция.' \
                  '\n◾️Работа с розацеей и гиперпигментацией.' \
                  '\n◾️Розация и гиперпигментация.'

    await dp.bot.send_photo(chat_id,caption= description, reply_markup=get_services_keyboard(language),photo=image1)
    await callback.message.delete()


@dp.callback_query_handler(lambda c: c.data == 'back_services')
async def handle_back_services(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    language = user_language.get(chat_id, 'en')

    image_url = 'https://cloud.mail.ru/public/5RXh/Pkd6X2eQC '  # Замените это на реальный URL изображения
    caption = 'Это ваше изображение'

    # Отправляем описание
    description = '🌼 Hello! 🌼\n' \
                  'Welcome to my chatbot! \n' \
                  '👩‍⚕️My name is Katerina, and I am a professional cosmetologist and dentist with more than 20 years of experience.\n' \
                  'Through this bot you can make an appointment with me . Together we will find the best solutions for your beauty and health. Feel free to ask questions and seek help.\n' \
                  '🌟 I will be glad to help you! 🌟'
    if language == 'ru':
        description = '🌼 Здравствуйте! 🌼\n' \
                      'Добро пожаловать в мой чат-бот ! \n' \
                      '👩‍⚕️Меня зовут Катерина, и я профессиональный косметолог и стоматолог с более чем 20-летним опытом.\n' \
                      'Через этого бота Вы можете записаться ко мне на приём . Вместе мы найдем лучшие решения для вашей красоты и здоровья. Не стесняйтесь задавать вопросы и обращаться за помощью.\n' \
                      '🌟Буду рада Вам помочь! 🌟'
    await dp.bot.send_photo(chat_id, caption=description, reply_markup=get_about_keyboard(language), photo=image_url)
    await callback_query.message.delete()