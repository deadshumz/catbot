<<<<<<< HEAD
from asyncore import dispatcher
import logging
from aiogram import Bot, Dispatcher, executor, types
import pickle
import os

API_TOKEN = '5220834594:AAEK0KPc7bTq_1YY89Wi2IydiZZb1ukUFyc'


# logging
logging.basicConfig(level=logging.INFO)

# init
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# User_DATA

user_data = 0


# Функции
def reply_btns():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(types.InlineKeyboardButton(text='Ещё 🤩', callback_data='again'))
    return keyboard

def newUser(chatid, username):
    # data = [
    #     {
    #         'chatid' : 123123,
    #         'username' : '@test'
    #     }
    # ]
    # with open('bd.pickle', 'wb') as f:
    #     pickle.dump(data, f)
    #     return ''
    with open('bd.pickle', 'rb') as f:
        pickle_obj = pickle.load(f)
        if(next((x for x in pickle_obj if x["chatid"] == chatid), 0) == 0):
            print(next((x for x in pickle_obj if x["chatid"] == chatid), 0))
            newData = {
                'chatid' : chatid,
                'username' : username
            }
            pickle_obj += [newData]
            with open('bd.pickle', 'wb') as f:
                pickle.dump(pickle_obj, f)
                return 'Новый пользователь: ' + username
        else:
            return 'Пользователь существует'
        
    
    


# Асинки
@dp.message_handler(commands=['start'])
async def pong(message: types.Message):
    await message.answer('Привет, этот бот отслыает котов, просто напишите cat или кот!\n\n ' + newUser(message.chat.id, '@' + message.from_user['username']) + '\n\nРазработчик - @deadshumz \n\n' + os.environ['BOT_TOKEN'])

@dp.message_handler()
async def cat(message: types.Message):
    if(message.text.lower() == 'cat' or message.text.lower() == 'кот'):
        await bot.send_photo(chat_id=message.chat.id, photo='https://www.dogtime.com/assets/uploads/2011/01/file_23020_dachshund-dog-breed.jpg', caption=message.text, reply_markup=reply_btns())




# CALLBACK
@dp.callback_query_handler(text="again")
async def again(call: types.CallbackQuery):
    await bot.send_photo(chat_id=call.message.chat.id, photo='https://www.dogtime.com/assets/uploads/2011/01/file_23020_dachshund-dog-breed.jpg', caption=call.message.text, reply_markup=reply_btns())
    await call.answer()


# Старт
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

=======
from asyncore import dispatcher
import logging
from aiogram import Bot, Dispatcher, executor, types
import pickle

API_TOKEN = '5220834594:AAEK0KPc7bTq_1YY89Wi2IydiZZb1ukUFyc'

# БД


# logging
logging.basicConfig(level=logging.INFO)


# init
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# User_DATA

user_data = 0


# Функции
def reply_btns():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(types.InlineKeyboardButton(text='Ещё 🤩', callback_data='again'))
    return keyboard

def newUser(chatid, username):
    # data = [
    #     {
    #         'chatid' : 123123,
    #         'username' : '@test'
    #     }
    # ]
    # with open('bd.pickle', 'wb') as f:
    #     pickle.dump(data, f)
    #     return ''
    with open('bd.pickle', 'rb') as f:
        pickle_obj = pickle.load(f)
        if(next((x for x in pickle_obj if x["chatid"] == chatid), 0) == 0):
            print(next((x for x in pickle_obj if x["chatid"] == chatid), 0))
            newData = {
                'chatid' : chatid,
                'username' : username
            }
            pickle_obj += [newData]
            with open('bd.pickle', 'wb') as f:
                pickle.dump(pickle_obj, f)
                return 'Новый пользователь: ' + username
        else:
            return 'Пользователь существует'
        
    
    


# Асинки
@dp.message_handler(commands=['start'])
async def pong(message: types.Message):
    await message.answer('Привет, этот бот отслыает котов, просто напишите cat или кот!\n\n ' + newUser(message.chat.id, '@' + message.from_user['username']) + '\n\nРазработчик - @deadshumz')

@dp.message_handler()
async def cat(message: types.Message):
    if(message.text.lower() == 'cat' or message.text.lower() == 'кот'):
        await bot.send_photo(chat_id=message.chat.id, photo='https://www.dogtime.com/assets/uploads/2011/01/file_23020_dachshund-dog-breed.jpg', caption=message.text, reply_markup=reply_btns())




# CALLBACK
@dp.callback_query_handler(text="again")
async def again(call: types.CallbackQuery):
    await bot.send_photo(chat_id=call.message.chat.id, photo='https://www.dogtime.com/assets/uploads/2011/01/file_23020_dachshund-dog-breed.jpg', caption=call.message.text, reply_markup=reply_btns())
    await call.answer()


# Старт
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

>>>>>>> 9232d88 (1)
