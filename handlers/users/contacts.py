from aiogram import types
from loader import dp
from handlers.users.start import user_language
from keyboards.inline.menu_inline import get_about_keyboard
from keyboards.inline.contacts_inline import get_contacts

@dp.callback_query_handler(lambda c: c.data == 'contacts')
async def handle_contacts(callback: types.CallbackQuery):
    chat_id = callback.message.chat.id
    language = user_language.get(chat_id, 'en')

    img='https://cloud.mail.ru/public/Fj6c/M2dnhyzq3'

    description = 'Our address Giorgi Papadopoulou 2,grafio 2 \n Paralimni 5290 \n Our phone number: +357 9913 0144'
    if language == 'ru':
        description = 'Наш адресс Giorgi Papadopoulou 2,grafio 2 \n Paralimni 5290 \n Наш номер:+357 9913 0144'

    await dp.bot.send_photo(chat_id,caption= description, reply_markup=get_contacts(language),photo=img)
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
                  'Through this bot you can make an appointment with me. Together we will find the best solutions for your beauty and health. Feel free to ask questions and seek help.\n' \
                  '🌟I will be glad to help you! 🌟'
    if language == 'ru':
        description = '🌼 Здравствуйте! 🌼\n' \
                      'Добро пожаловать в мой чат-бот ! \n' \
                      '👩‍⚕️Меня зовут Катерина, и я профессиональный косметолог и стоматолог с более чем 20-летним опытом.\n' \
                      'Через этого бота Вы можете записаться ко мне на приём . Вместе мы найдем лучшие решения для вашей красоты и здоровья. Не стесняйтесь задавать вопросы и обращаться за помощью.\n' \
                      '🌟Буду рада Вам помочь! 🌟'
    await dp.bot.send_photo(chat_id, caption=description, reply_markup=get_about_keyboard(language), photo=image_url)
    await callback_query.message.delete()