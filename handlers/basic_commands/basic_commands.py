from aiogram import types, F
from aiogram.filters import Command

from database.execute import clear_cell
from loader import dp


@dp.message(Command(commands=["start"]))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Выбор машины")],
        [types.KeyboardButton(text="Удалить запрос")],
        [types.KeyboardButton(text="Поддержать проект")],
        [types.KeyboardButton(text="Помощь")],
        [types.KeyboardButton(text="Жалобы")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.answer(
        f"Рад видеть, {message.from_user.full_name}",
        reply_markup=keyboard)


@dp.message(Command(commands=["help"]))
@dp.message(F.text == "Помощь")
async def command_start_handler(message: types.Message) -> None:
    await message.answer(
        "Для навигации в боте вы можете воспользоваться коммандным меню (находится слева) или же "
        "кнопками в главном меню (вызывается коммандой /start).\n\n"
        "Чтобы начать выбор машины, нажмите на кнопку 'Выбор машины' или воспользуйтесь коммандой /car. "
        "Затем по очереди выбирайте нужные вам критерии, по окончанию бот запишет ваш запрос и будет присылать,"
        "в соответствии с запросом, новые объявления.\n\nЕсли вы хотите убрать рассылку, "
        "нажмите на кнопку 'Удалить запрос' или воспользуйтесь коммандой /delete.\n\nОбъявления приходят только по "
        "одному составленному запросу. Если вы задали новый запрос, то старый сразу стирается.\n\n"
        "Запрос считается составленным, как только вы выбрали все критерии и "
        "бот прислал сообщение с подитоживанием вашего выбора")


@dp.message(Command(commands=["report"]))
@dp.message(F.text == "Жалобы")
async def command_report_handler(message: types.Message) -> None:
    await message.answer(
        "Если вы хотите сообщить об ошибке или составить жалобу, то напишите на почту:\navtobot.report@gmail.com")


@dp.message(Command(commands=["delete"]))
@dp.message(F.text == "Удалить запрос")
async def command_clear_handler(message: types.Message) -> None:
    await clear_cell(message.from_user.id)
    await message.answer(
        "Ваш запрос успешно удалён!")


@dp.message(Command(commands=['donate']))
@dp.message(F.text == "Поддержать проект")
async def buy(message: types.Message):
    await message.answer(
        text='Буду признателен за любую поддержку проекта ;)\n\n'
             'https://www.buymeacoffee.com/AvtoBot'
    )
