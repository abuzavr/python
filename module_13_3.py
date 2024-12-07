from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging

# Токен бота
API_TOKEN = 'token'

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создание объектов Bot и Dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    """
    Обрабатывает команду /start.
    """
    await message.answer("Привет! Я бот помогающий твоему здоровью.")  # Ответ в чат


# Обработчик всех остальных сообщений
@dp.message_handler()
async def all_messages(message: types.Message):
    """
    Обрабатывает все остальные сообщения.
    """
    await message.answer("Введите команду /start, чтобы начать общение.")  # Ответ в чат


# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
