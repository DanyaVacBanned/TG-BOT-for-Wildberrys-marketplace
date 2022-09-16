from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ContentTypes
import logging
import cfg
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from data import FSMAdmin
from db import Database
import keyboard as nav
from selenium_action import execute, feedback
import time
#STORAGE
storage = MemoryStorage()
#BOT INITIALIZING
logging.basicConfig(level=logging.INFO)
TOKEN = cfg.get_token()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
#YOOUTOKEN
YOOUTOKEN = cfg.get_yooukassa()
#DATABASE
db = Database('wb_db.db')

#BODY
@dp.message_handler(commands=['start'])
async def startapp(meesage: types.Message):
    await bot.send_message(meesage.from_user.id, cfg.read_file(), reply_markup=nav.Keyboard)

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, cfg.read_help_file())

#USER INPUT
@dp.message_handler(text = 'Приступить', state=None)
async def letsgo(message: types.Message):
     await FSMAdmin.articul.set()
     await bot.send_message(message.from_user.id, "Введите артикул товара")


@dp.message_handler(state=FSMAdmin.articul)
async def load_articul(message: types.Message, state: FSMContext):
    async with state.proxy() as sp:
        sp['articul'] = message.text
        await FSMAdmin.next()
        await bot.send_message(message.from_user.id,'Идёт отправка ключевого запроса...')
        time.sleep(3)
        await bot.send_message(message.from_user.id, "Введите количество дней для выкупа")

@dp.message_handler(state=FSMAdmin.days)
async def load_days(message: types.Message, state=FSMContext):
    async with state.proxy() as sp:
        sp['days'] = message.text
        await FSMAdmin.next()
        await bot.send_message(message.from_user.id, cfg.pvz_text())

@dp.message_handler(state=FSMAdmin.punkt)
async def load_punkt(message: types.Message, state=FSMContext):
    async with state.proxy() as sp:
        sp['punkt'] = message.text
        sp_articul = sp['articul']
        sp_days = sp['days']
        sp_punkt = sp['punkt']
        db.save_slovar(sp_articul, sp_days, sp_punkt)
        await bot.send_message(message.from_user.id,'Теперь произведите оплату',reply_markup=nav.btnPay_inline)
        i = int(db.get_days())
        while i != 0:
            execute()
            i -= 1
            time.sleep(1 * 60 * 60 * 24)

        while i !=0:
            feed_text = cfg.feed_text_func()
            feedback(feed_text)
            i -=1
        db.delete_curent_data() #Отзывы

    await state.finish()


@dp.callback_query_handler(text='payment')
async def payment(call: types.CallbackQuery):
    await bot.send_invoice(chat_id=call.from_user.id, title='Начать продвижение', description='После оплаты начнется продвижение указанного товара', payload='payment', provider_token=YOOUTOKEN, currency='RUB', start_parameter='wb_bot', prices=({'label': 'Руб', 'amount': int(cfg.get_price())*int(db.get_days())*100}))

@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.message_handler(content_types=ContentTypes.SUCCESSFUL_PAYMENT)
async def process_pay(message: types.Message):
    if message.successful_payment.invoice_payload == 'payment':
        await bot.send_message(message.from_user.id, 'Услуга оплаченна!')





#POLLING
if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)
