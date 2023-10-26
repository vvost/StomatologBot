from aiogram import types

def get_contacts(language):
    if language =='ru':
        markup = types.InlineKeyboardMarkup()
        inst=types.InlineKeyboardButton('🟣Instagram',callback_data='inst',url='https://www.instagram.com/dr.tofini/')
        tg=types.InlineKeyboardButton('🔵Telegram',callback_data='tg',url='https://t.me/KaterinaTofini')
        maps=types.InlineKeyboardButton('Наша локация🗺',callback_data='maps',url='https://www.google.com/maps/place/Ayiou+Dimitriou+146,+Paralimni+5281,+%D0%9A%D1%96%D0%BF%D1%80/@35.0522804,33.9839937,17z/data=!3m1!4b1!4m6!3m5!1s0x14dfc605b06f2585:0x34425d5d19fe9cfa!8m2!3d35.0522804!4d33.9839937!16s%2Fg%2F11js8nkpb6?hl=uk-UA&entry=ttu')
        back_button = types.InlineKeyboardButton('Назад↩️', callback_data='back_services')
        markup.row(inst,tg)
        markup.add(maps)
        markup.add(back_button)
        return markup
    elif language =='en':
        markup = types.InlineKeyboardMarkup()
        inst=types.InlineKeyboardButton('🟣Instagram',callback_data='inst',url='https://www.instagram.com/dr.tofini/')
        tg=types.InlineKeyboardButton('🔵Telegram',callback_data='tg',url='https://t.me/KaterinaTofini')
        maps = types.InlineKeyboardButton('Our location🗺', callback_data='maps',url='https://www.google.com/maps/place/Ayiou+Dimitriou+146,+Paralimni+5281,+%D0%9A%D1%96%D0%BF%D1%80/@35.0522804,33.9839937,17z/data=!3m1!4b1!4m6!3m5!1s0x14dfc605b06f2585:0x34425d5d19fe9cfa!8m2!3d35.0522804!4d33.9839937!16s%2Fg%2F11js8nkpb6?hl=uk-UA&entry=ttu')
        back_button = types.InlineKeyboardButton('Back↩️', callback_data='back_services')
        markup.row(inst,tg)
        markup.add(maps)
        markup.add(back_button)
        return markup