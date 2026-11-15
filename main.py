import os
import random
from dotenv import *
from vkbottle import *
from vkbottle.bot import *

load_dotenv()  # Загружаем секретные данные из файла .env

TOKEN = os.getenv("MY_TOKEN")  # Берём токен из окружения
bot = Bot(token=TOKEN)  # Создаём и авторизуем бота


@bot.on.message(text="Привет")  # Реагируем на сообщение "Привет"
async def greeting_handler(message: Message):
    print("кто-то написал мне")
    await message.answer("Привет!")  # Отправляем ответ

@bot.on.message(text="Пока")  # Реагируем на сообщение "Привет"
async def greeting_handler(message: Message):
    print("кто-то написал мне")
    await message.answer("До свидания")  # Отправляем ответ

@bot.on.message(text=["пицца", "пепперони", "сырная"])  # Реагируем на сообщение "Привет"
async def greeting_handler(message: Message):
    print("кто-то написал мне")
    await message.answer("Принято! Готовим пиццу")  # Отправляем ответ

@bot.on.message(text=["магия"])  # Реагируем на сообщение "Привет"
async def greeting_handler(message: Message):
    print("кто-то написал мне")
    a = ["Да", "Нет", "Возможно"]
    await message.answer (random.choice(a))  # Отправляем ответ

@bot.on.message(text="Вход")
async def greeting_handler(message: Message):
    print("кто-то пытается войти")
    
    if text == SECRET_PASS:
        await message.answer("Доступ разрешен")
    else:
        await message.answer("Неверно!")

@bot.on.message()  
async def spy_translator_handler(message: Message):
    print("кто-то написал мне")
    user_text = message.text
    reversed_text = user_text[::-1]
    await message.answer(reversed_text)

задание 1
@bot.on.message()
async def log_any_message(message: Message):
    print(f"От пользователя с ID: {message.from_id}")
    print(f"Текст сообщения: {message.text}")

задание 2
@bot.on.message()
async def log_any_message(message: Message):
    print("кто-то написал мне")
    text_length = len(message.text)
    await message.answer(f"Твой ID: {message.from_id}. А длина твоего сообщения: {text_length} символов")

задание 3
@bot.on.message()
async def log_any_message(message: Message):
    if not message.text:
        print(f"пользователь {message.from_id} прислал медиа")
    else:
        print(f"пользователь {message.from_id} написал { message.text}")

#задание 4
@bot.on.message()
async def log_any_message(message: Message):
    if "привет" in message.text.lover() or "здарова" in message.text.lover():
        await message.answer("Привет")
    elif "пока" in message.text.lover():
        await message.answer("До встречи")
    else:
        await message.answer("Я тебя не понимаю")

# @bot.on.message()
# async def time_helper_handler(message: Message):
#     text_lower = message.text.lower()
   
#     if "время" in text_lower or "который час" in text_lower:
#         await message.answer("Скоро обед! ")

        
print("Запуск бота...")
bot.run()  # Запускаем бесконечную работу бота


# message.text — сам текст сообщения (строка).
# message.from_id — ID автора (кто написал).
# message.peer_id — ID чата (где написал: в личке или в беседе).
