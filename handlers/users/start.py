from aiogram.types import ContentType, Message
from aiogram import types
from keyboards.inline.start_inline import get_menu_markup
from keyboards.inline.menu_inline import get_about_keyboard,getkeyboard

from loader import dp

#Добавлени фотки

lang = {
    'ru': {
        'greeting': '🇷🇺Здравствуйте! Добро пожаловать в нашего чат бота. Пожалуйста выберите язык:\n🇬🇧Hello! Welcome to our chatbot. Please select a language:',
        'selected': 'Вы выбрали русский язык.',
        'menu': 'Пожалуйста выберите:',
    },
    'en': {
        'greeting': '🇷🇺Здравствуйте! Добро пожаловать в нашего чат бота. Пожалуйста выберите язык:\n🇬🇧Hello! Welcome to our chatbot. Please select a language:',
        'selected': 'You have selected English language.',
        'menu': 'Please choose:',
    }
}

# Словарь для хранения выбранного языка для каждого пользователя
user_language = {}



@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    chat_id = message.chat.id

    # Проверяем, выбран ли уже язык для данного пользователя
    if chat_id in user_language:
        language = user_language[chat_id]
        await message.reply(lang[language]['selected'])
        await show_menu(message, language)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Русский")
        item2 = types.KeyboardButton('English')
        markup.add(item1, item2)

        await message.reply(lang['en']['greeting'], reply_markup=markup)




@dp.message_handler(content_types=['text'])
async def handle_message(message: types.Message):
    chat_id = message.chat.id
    text = message.text

    if text == "Русский":
        user_language[chat_id] = 'ru'

        await show_menu(message, 'ru')

    elif text == "English":
        user_language[chat_id] = 'en'

        await show_menu(message, 'en')




async def show_menu(message: types.Message, language: str):
    menu_text = lang[language]['menu']
    markup = get_menu_markup(language)
    await message.reply(menu_text, reply_markup=markup)






@dp.callback_query_handler(lambda c: c.data == 'cosmetology')
async def handle_cosmetology(callback_query: types.CallbackQuery):

    chat_id = callback_query.message.chat.id
    language = user_language.get(chat_id, 'en')

    # Отправляем фотографию

    image_url = 'https://cloud.mail.ru/public/5RXh/Pkd6X2eQC'  # Замените это на реальный URL изображения
    caption = 'Это ваше изображение'

    # Отправляем описание
    description = '🌼 Hello! 🌼\n'\
                  'Welcome to my chatbot! \n'\
                  '👩‍⚕️My name is Katerina, and I am a professional cosmetologist and dentist with more than 20 years of experience.\n' \
                  'Through this bot you can make an appointment with me . Together we will find the best solutions for your beauty and health. Feel free to ask questions and seek help.\n' \
                  '🌟 I will be glad to help you! 🌟'
    if language == 'ru':
        description =  '🌼 Здравствуйте! 🌼\n' \
                  'Добро пожаловать в мой чат-бот ! \n' \
                  '👩‍⚕️Меня зовут Катерина, и я профессиональный косметолог и стоматолог с более чем 20-летним опытом.\n' \
                  'Через этого бота вы можете записаться ко мне на запись. Вместе мы найдем лучшие решения для вашей красоты и здоровья. Не стесняйтесь задавать вопросы и обращаться за помощью.\n' \
                  '🌟 Рады видеть вас здесь! 🌟'
    await dp.bot.send_photo(chat_id, caption=description,reply_markup=get_about_keyboard(language),photo=image_url)
    await callback_query.message.delete()



