async def on_startup(dp):

    # from utils.notify_admins import notify_admins #При запуске включаються утилы
    # await notify_admins(dp)

    from utils.set_bot_commands import set_bot_commadns
    await set_bot_commadns(dp)

    print('Бот запущен')

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.INFO)
    from aiogram import executor
    from handlers import dp
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)