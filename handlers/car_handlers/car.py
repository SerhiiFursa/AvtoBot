"""
    This module contains a finite state machine (FSM) mechanism for storing states between
    stages of dialogue with the bot (in this case, everything related to the choice of machine criteria).
    At each stage, the bot saves the user's choice and upon completion provides
    complete list of selected criteria. For a list with information,
    it is necessary to go through all the stages of the dialogue.
    The start_ad function is called by command in the bot and is the first stage of the FSM,
    each following function will work in strict order based on the answer
    user in the previous function.
    The come_back.py file implements the back button, while the incorrectly.py file handles
    possible incorrect user responses.
"""

import json

from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import ReplyKeyboardRemove
from aiogram import F
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from loader import dp
from scraping.create_url import create_url
from scraping.scraping_data import scraping_first_ad


with open(r'handlers/car_handlers/car_data.json') as file:
    car_data_dict = json.load(file)


# making lists of possible answers
alphabet = [x[0] for x in car_data_dict.items()]
marks_and_models = []
marks = []
models = []
transmission_list = ['Автомат', 'Ручная', 'Без разницы']
year_min_list = tuple(list(map(lambda x: str(x), list(range(1900, 2024)) + ['Без разницы'])))
year_max_list = tuple(list(map(lambda x: str(x), list(range(1900, 2024)) + ['Без разницы'])))
mileage_min_list = tuple(list(map(lambda x: str(x), list(range(0, 2000000)) + ['Без разницы'])))
mileage_max_list = tuple(list(map(lambda x: str(x), list(range(0, 2000000)) + ['Без разницы'])))
price_min_list = tuple(list(map(lambda x: str(x), list(range(0, 4000000)) + ['Без разницы'])))
price_max_list = tuple(list(map(lambda x: str(x), list(range(0, 4000000)) + ['Без разницы'])))

for a in car_data_dict.keys():
    cars = tuple(car_data_dict[a].items())
    marks_and_models.extend(tuple([m for m in cars]))
    marks.extend([mark[0] for mark in cars])
    models.extend([mark[1] for mark in cars])

list_of_models = []

for model in models:
    list_of_models.extend(model)


# creation of a mechanism of finite automata and their stages
class ChoiceCar(StatesGroup):
    choosing_letter = State()
    choosing_mark = State()
    choosing_model = State()
    choosing_transmission = State()
    choosing_year_min = State()
    choosing_year_max = State()
    choosing_mileage_min = State()
    choosing_mileage_max = State()
    choosing_price_min = State()
    choosing_price_max = State()


# option to undo all replies
@dp.message(Command("cancel"))
@dp.message(F.text == "Отменить")
async def cancel_handler(message: types.Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.clear()
    await message.answer(
        "Выбор машины отменён.",
        reply_markup=ReplyKeyboardRemove(),
    )


@dp.message(Command(commands=['car']))
@dp.message(F.text == 'Выбор машины')
async def start_ad(message: types.Message, state: FSMContext):
    kb = ReplyKeyboardBuilder()
    for alpha in alphabet:
        kb.add(types.KeyboardButton(text=alpha))
    await state.set_state(ChoiceCar.choosing_letter)
    await message.answer(
        text="Выберите на какую букву начинается марка:",
        reply_markup=kb.as_markup(resize_keyboard=True)
    )


@dp.message(
    ChoiceCar.choosing_letter,
    F.text.in_(alphabet)
)
async def choice_mark(message: types.Message, state: FSMContext):
    kb = ReplyKeyboardBuilder()
    count = 0
    for model in marks_and_models:
        if model[0][0] == message.text:
            count += 1
            kb.add(types.KeyboardButton(text=model[0]))
    kb.add(types.KeyboardButton(text='Назад'))
    kb.add(types.KeyboardButton(text='Отменить'))
    if count >= 2:
        kb.adjust(2)
    await state.update_data(letter=message.text)
    await state.set_state(ChoiceCar.choosing_mark)
    await message.answer(
        text="Выберите марку:",
        reply_markup=kb.as_markup(resize_keyboard=True)
    )


@dp.message(
    ChoiceCar.choosing_mark,
    F.text.in_(marks)
)
async def choice_model(message: types.Message, state: FSMContext):
    kb = ReplyKeyboardBuilder()
    count = 0
    for model in marks_and_models:
        if model[0] == message.text:
            count += 1
            for mod in model[1]:
                kb.add(types.KeyboardButton(text=mod))
            kb.add(types.KeyboardButton(text='Назад'))
            kb.add(types.KeyboardButton(text='Отменить'))
            kb.adjust(2)
    if count >= 2:
        kb.adjust(2)
    await state.update_data(mark=message.text)
    await state.set_state(ChoiceCar.choosing_model)
    await message.answer(
        text="Выберите модель:",
        reply_markup=kb.as_markup(resize_keyboard=True)
    )


@dp.message(
    ChoiceCar.choosing_model,
    F.text.in_(list_of_models)
)
async def choice_transmission(message: types.Message, state: FSMContext):
    kb = ReplyKeyboardBuilder()
    for trans in transmission_list:
        kb.add(types.KeyboardButton(text=trans))
    kb.add(types.KeyboardButton(text='Назад'))
    kb.add(types.KeyboardButton(text='Отменить'))
    kb.adjust(2)
    await state.update_data(model=message.text)
    await state.set_state(ChoiceCar.choosing_transmission)
    await message.answer(
        text="Выберите коробку передач",
        reply_markup=kb.as_markup(resize_keyboard=True)
    )


@dp.message(
    ChoiceCar.choosing_transmission,
    F.text.in_(transmission_list)
)
async def choice_year_min(message: types.Message, state: FSMContext):
    kb = ReplyKeyboardBuilder()
    kb.add(types.KeyboardButton(text='Без разницы'))
    kb.add(types.KeyboardButton(text='Назад'))
    kb.add(types.KeyboardButton(text='Отменить'))
    kb.adjust(2)
    await state.update_data(transmission=message.text)
    await state.set_state(ChoiceCar.choosing_year_min)
    await message.answer(
        text="Впишите минимальный год поиска машин:\n(не раньше 1900, например, 1998, 2005 и т.д.)",
        reply_markup=kb.as_markup(resize_keyboard=True)
    )


@dp.message(
    ChoiceCar.choosing_year_min,
    F.text.in_(year_min_list)
)
async def choice_year_max(message: types.Message, state: FSMContext):
    kb = ReplyKeyboardBuilder()
    kb.add(types.KeyboardButton(text='Без разницы'))
    kb.add(types.KeyboardButton(text='Назад'))
    kb.add(types.KeyboardButton(text='Отменить'))
    kb.adjust(2)
    await state.update_data(year_min=message.text)
    await state.set_state(ChoiceCar.choosing_year_max)
    await message.answer(
        text="Впишите максимальный год поиска машин:\n(не позже 2023, например, 1998, 2005 и т.д.)",
        reply_markup=kb.as_markup(resize_keyboard=True)
    )


@dp.message(
    ChoiceCar.choosing_year_max,
    F.text.in_(year_max_list)
)
async def choice_mileage_min(message: types.Message, state: FSMContext):
    kb = ReplyKeyboardBuilder()
    kb.add(types.KeyboardButton(text='Без разницы'))
    kb.add(types.KeyboardButton(text='Назад'))
    kb.add(types.KeyboardButton(text='Отменить'))
    kb.adjust(2)
    await state.update_data(year_max=message.text)
    await state.set_state(ChoiceCar.choosing_mileage_min)
    await message.answer(
        text="Впишите минимальный пробег желаемой машины:\n(например, 50000, 175000 и т.д.)",
        reply_markup=kb.as_markup(resize_keyboard=True)
    )


@dp.message(
    ChoiceCar.choosing_mileage_min,
    F.text.in_(mileage_min_list)
)
async def choice_mileage_max(message: types.Message, state: FSMContext):
    kb = ReplyKeyboardBuilder()
    kb.add(types.KeyboardButton(text='Без разницы'))
    kb.add(types.KeyboardButton(text='Назад'))
    kb.add(types.KeyboardButton(text='Отменить'))
    kb.adjust(2)
    await state.update_data(mileage_min=message.text)
    await state.set_state(ChoiceCar.choosing_mileage_max)
    await message.answer(
        text="Впишите максимальный пробег желаемой машины:\n(например, 150000, 275000 и т.д.)",
        reply_markup=kb.as_markup(resize_keyboard=True)
    )


@dp.message(
    ChoiceCar.choosing_mileage_max,
    F.text.in_(mileage_max_list)
)
async def choice_price_min(message: types.Message, state: FSMContext):
    kb = ReplyKeyboardBuilder()
    kb.add(types.KeyboardButton(text='Без разницы'))
    kb.add(types.KeyboardButton(text='Назад'))
    kb.add(types.KeyboardButton(text='Отменить'))
    kb.adjust(2)
    await state.update_data(mileage_max=message.text)
    await state.set_state(ChoiceCar.choosing_price_min)
    await message.answer(
        text="Впишите минимальную цену машины:\n(например, 5000, 20000 и т.д.)\n"
             "Внимаение! Валюта бота - польский злотый!",
        reply_markup=kb.as_markup(resize_keyboard=True)
    )


@dp.message(
    ChoiceCar.choosing_price_min,
    F.text.in_(price_min_list)
)
async def choice_price_max(message: types.Message, state: FSMContext):
    kb = ReplyKeyboardBuilder()
    kb.add(types.KeyboardButton(text='Без разницы'))
    kb.add(types.KeyboardButton(text='Назад'))
    kb.add(types.KeyboardButton(text='Отменить'))
    kb.adjust(2)
    await state.update_data(price_min=message.text)
    await state.set_state(ChoiceCar.choosing_price_max)
    await message.answer(
        text="Впишите максимальную цену машины:\n(например, 30000, 55000 и т.д.)\n"
             "Внимаение! Валюта бота - польский злотый!",
        reply_markup=kb.as_markup(resize_keyboard=True)
    )


@dp.message(
    ChoiceCar.choosing_price_max,
    F.text.in_(price_max_list)
)
async def final(message: types.Message, state: FSMContext):
    await state.update_data(price_max=message.text)

    user_data = await state.get_data()
    user_data['id_user'] = message.from_user.id

    with open('scraping/data_for_scraping.json', 'w') as file:
        json.dump(user_data, file, indent=4, ensure_ascii=False)

    await message.answer(
        text=f'Сделано! Ваш выбор: \nМарка - {user_data["mark"]}\nМодель - {user_data["model"]}\n'
             f'Коробка - {user_data["transmission"]}\nМинимальный год - {user_data["year_min"]}\nМаксимальный год - {user_data["year_max"]}\n'
             f'Минимальный пробег - {user_data["mileage_min"]}\nМаксимальный пробег - {user_data["mileage_max"]}\n'
             f'Минимальная цена - {user_data["price_min"]}\nМаксимальная цена - {user_data["price_max"]}\n',

        reply_markup=ReplyKeyboardRemove()
    )

    await create_url(user_data)
    await scraping_first_ad(id_user=message.from_user.id)
    await state.clear()
