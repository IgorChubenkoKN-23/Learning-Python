from aiogram import Bot, Dispatcher, asyncio , types


TOKEN = "8517058719:AAFEjFQXOlMsKq57pI7MafDd15a-tF8_YXo"



bot=Bot(token=TOKEN)
dp=Dispatcher()

@dp.message(commands=["start"])

async def start_handler(message: types.Message):
    await message.answer("Привіт! Я бот")


    if __name__ == "__main__":
          asyncio.run(main())