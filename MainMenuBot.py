"""""
BotApplication
"""""
"""""
def main_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="Приветствие", callback_data="greet")
    builder.button(text="Описание", callback_data="description")
    return builder.as_markup()

# Меню после нажатия "Описание"
def description_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="Вернуться", callback_data="back")
    return builder.as_markup()

# Обработчик команды /start
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Главное меню:", reply_markup=main_menu())

# Обработчик кнопки "Приветствие"
@dp.callback_query(lambda c: c.data == "greet")
async def greet(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text("Привет! Это приветственное сообщение.", reply_markup=main_menu())

# Обработчик кнопки "Описание"
@dp.callback_query(lambda c: c.data == "description")
async def show_description(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text("Здесь находится описание бота.", reply_markup=description_menu())

# Обработчик кнопки "Вернуться"
@dp.callback_query(lambda c: c.data == "back")
async def back_to_menu(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text("Главное меню:", reply_markup=main_menu())
"""""
import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.methods.get_file import GetFile
from Projects import Project, projects, add_project
from Version import BotUpdate

# Загрузите переменные окружения из .env
load_dotenv("TEST.env")

# Получите токен
API_TOKEN =  os.getenv("TELEGRAM_BOT_TOKEN")
debug_mode = os.getenv("DEBUG")
print(f"Debug mode: {debug_mode}")

# Обновление
bot_version = "0.0.1"
date_version = "22.05.2025"
bot_update = BotUpdate(version=bot_version, update=date_version)

#___________________________________________________________________
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
# ___________________________________________--- Функции к окнам ---
def main_menu():
    keyboard = [
        [types.KeyboardButton(text="Проекты")],
        [types.KeyboardButton(text="Описание")]
    ]
    return types.ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

def back_menu():
    keyboard = [[types.KeyboardButton(text="Вернуться")]]
    return types.ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

def project_list():
    keyboard = [[types.KeyboardButton(text = "Выгрузить шаблон таблицы")], [types.KeyboardButton(text = "Вернуться")]]
    return types.ReplyKeyboardMarkup(keyboard = keyboard, resize_keyboard = True)

# ___________________________________________________________--- Обработчики ---
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Добро, пожаловать! Главное меню:", reply_markup=main_menu())

@dp.message(lambda msg: msg.text == "Проекты")
async def greet(message: types.Message):
    await message.answer(f"Существующие проекты на данный момент: {projects}", reply_markup=main_menu())
@dp.message(lambda msg: msg.text == "Описание")
async def show_description(message: types.Message):
    await message.answer("Систематически улучшаемый бот")
    await message.answer(bot_update.last_update())
    await message.answer("Приятного пользования!", reply_markup=back_menu())

@dp.message(lambda msg: msg.text == "Вернуться")
async def go_back(message: types.Message):
    await message.answer("Главное меню:", reply_markup=main_menu())

@dp.message(lambda msg: msg.text == "Выгрузить шаблон таблицы")
async def xl_file(message: types.Message):
    await message.answer("Выгрузка таблицы:", reply_markup=project_list())
    file = os.path.()

# __________________________________________________________--- Запуск бота ---
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())