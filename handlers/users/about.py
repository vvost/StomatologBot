from aiogram import types
from loader import dp
from handlers.users.start import user_language
from keyboards.inline.about_inline import about
from keyboards.inline.menu_inline import get_about_keyboard


@dp.callback_query_handler(lambda c: c.data == 'about')
async def handle_about(callback: types.CallbackQuery):
    chat_id = callback.message.chat.id
    language = user_language.get(chat_id, 'en')
    # Получение инлайн-клавиатуры "О-нас"
    photo='https://cloud.mail.ru/public/pWDw/dZQ5ihugu'
    description = '🏨More than 20 years ago I started my professional career in medicine and dentistry.  ' \
                      'Today, with the accumulated experience and passion for work, I offer you my services in modern dentistry and cosmetology.\n\n' \
                      '☎️Our phone numbers: +357 9913 0144\n \n' \
                      '🗺We are located at: Giorgi Papadopoulou 2,grafio 2 Paralimni 5290\n \n' \
                      '❇️Trust us and we will help you achieve the desired results, maintain your health and self-confidence. We are proud of our work and look forward to seeing you'
    if language == 'ru':
        description = '🏨Более 20 лет назад я начала свой профессиональный путь в медицине и стоматологии. ' \
                      'Сегодня, с накопленным опытом и страстью к работе, я предлагаю вам мои услуги в современной стоматологии и косметологии.\n \n' \
                      '☎️Наши телефоны: +357 9913 0144\n \n' \
                      '🗺Мы находимся по адресу: Giorgi Papadopoulou 2,grafio 2 Paralimni 5290\n \n' \
                      '❇️Доверьтесь нам, и мы поможем вам достичь желаемых результатов, сохранить здоровье и уверенность в себе. Мы гордимся нашей работой и с нетерпением ждем, чтобы увидеть вас'
    await dp.bot.send_photo(chat_id,caption=description, reply_markup=about(language),photo=photo)
    await callback.message.delete()



@dp.callback_query_handler(lambda c: c.data == 'back')
async def handle_back_services(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    language = user_language.get(chat_id, 'en')

    image_url = 'https://cloud.mail.ru/public/5RXh/Pkd6X2eQC '  # Замените это на реальный URL изображения


    # Отправляем описание
    description = '🌼 Hello! 🌼\n' \
                  'Welcome to my chatbot! \n' \
                  '👩‍⚕️My name is Katerina, and I am a professional cosmetologist and dentist with more than 20 years of experience.\n' \
                  'Through this bot you can make an appointment with me . Together we will find the best solutions for your beauty and health. Feel free to ask questions and seek help.\n' \
                  '🌟I will be glad to help you! 🌟'
    if language == 'ru':
        description = '🌼 Здравствуйте! 🌼\n' \
                      'Добро пожаловать в мой чат-бот ! \n' \
                      '👩‍⚕️Меня зовут Катерина, и я профессиональный косметолог и стоматолог с более чем 20-летним опытом.\n' \
                      'Через этого бота Вы можете записаться ко мне на приём . Вместе мы найдем лучшие решения для вашей красоты и здоровья. Не стесняйтесь задавать вопросы и обращаться за помощью.\n' \
                      '🌟Буду рада Вам помочь! 🌟'
    await dp.bot.send_photo(chat_id, caption=description, reply_markup=get_about_keyboard(language), photo=image_url)
    await callback_query.message.delete()