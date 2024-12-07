from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
import logging

# Укажите токен вашего бота
API_TOKEN = 'YOUR_BOT_TOKEN'  # Замените YOUR_BOT_TOKEN на токен, выданный @BotFather

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создание объектов Bot, Dispatcher и хранилища состояний
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# Определение состояний
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


# Обработчик команды "Calories"
@dp.message_handler(text="Calories")
async def set_age(message: types.Message):
    """
    Начинает цепочку вопросов. Запрашивает возраст.
    """
    await message.answer("Введите свой возраст:")  # Сообщение пользователю
    await UserState.age.set()  # Устанавливаем состояние age


# Обработчик состояния UserState.age
@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    """
    Обрабатывает возраст и запрашивает рост.
    """
    await state.update_data(age=message.text)  # Сохраняем возраст
    await message.answer("Введите свой рост:")  # Сообщение пользователю
    await UserState.growth.set()  # Устанавливаем состояние growth


# Обработчик состояния UserState.growth
@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    """
    Обрабатывает рост и запрашивает вес.
    """
    await state.update_data(growth=message.text)  # Сохраняем рост
    await message.answer("Введите свой вес:")  # Сообщение пользователю
    await UserState.weight.set()  # Устанавливаем состояние weight


# Обработчик состояния UserState.weight
@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    """
    Обрабатывает вес, рассчитывает норму калорий и завершает состояние.
    """
    await state.update_data(weight=message.text)  # Сохраняем вес

    # Получаем данные из состояния
    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    # Формула Миффлина - Сан Жеора для мужчин
    calories = 10 * weight + 6.25 * growth - 5 * age + 5

    # Отправляем результат пользователю
    await message.answer(f"Ваша норма калорий: {calories} ккал")

    # Завершаем состояние
    await state.finish()


# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
