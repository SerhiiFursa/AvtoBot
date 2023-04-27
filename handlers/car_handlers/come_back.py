from aiogram import types, F
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from .car import ChoiceCar, transmission_list, marks_and_models, alphabet
from loader import dp


@dp.message(
    ChoiceCar.choosing_mark,
    F.text == 'Назад'
)
async def mark_back(message: types.Message, state: FSMContext):
    kb = ReplyKeyboardBuilder()
    for alpha in alphabet:
        kb.add(types.KeyboardButton(text=alpha))
    await state.update_data(letter=message.text)
    await state.set_state(ChoiceCar.choosing_letter)
    await message.answer(
        text="Выберите на какую букву начинается марка:",
        reply_markup=kb.as_markup(resize_keyboard=True)
    )


@dp.message(
    ChoiceCar.choosing_model,
    F.text == 'Назад'
)
async def model_back(message: types.Message, state: FSMContext):
    kb = ReplyKeyboardBuilder()
    count = 0
    for model in marks_and_models:
        user_data = await state.get_data()
        if model[0][0] == user_data['letter']:
            count += 1
            kb.add(types.KeyboardButton(text=model[0]))
    kb.add(types.KeyboardButton(text='Назад'))
    kb.add(types.KeyboardButton(text='Отменить'))
    if count >= 2:
        kb.adjust(2)
    await state.update_data(mark=message.text)
    await state.set_state(ChoiceCar.choosing_mark)
    await message.answer(
        text="Выберите марку:",
        reply_markup=kb.as_markup(resize_keyboard=True)
    )


@dp.message(
    ChoiceCar.choosing_transmission,
    F.text == 'Назад'
)
async def transmission_back(message: types.Message, state: FSMContext):
    kb = ReplyKeyboardBuilder()
    count = 0
    user_data = await state.get_data()
    for model in marks_and_models:
        if model[0] == (user_data["mark"]):
            count += 1
            for mod in model[1]:
                kb.add(types.KeyboardButton(text=mod))
            kb.add(types.KeyboardButton(text='Назад'))
            kb.add(types.KeyboardButton(text='Отменить'))
            kb.adjust(2)
    if count >= 2:
        kb.adjust(2)
    await state.update_data(model=message.text)
    await state.set_state(ChoiceCar.choosing_model)
    await message.answer(
        text="Выберите модель:",
        reply_markup=kb.as_markup(resize_keyboard=True)
    )


@dp.message(
    ChoiceCar.choosing_year_min,
    F.text == 'Назад'
)
async def year_min_back(message: types.Message, state: FSMContext):
    kb = ReplyKeyboardBuilder()
    for trans in transmission_list:
        kb.add(types.KeyboardButton(text=trans))
    kb.add(types.KeyboardButton(text='Назад'))
    kb.add(types.KeyboardButton(text='Отменить'))
    kb.adjust(2)
    await state.update_data(transmission=message.text)
    await state.set_state(ChoiceCar.choosing_transmission)
    await message.answer(
        text="Выберите коробку передач",
        reply_markup=kb.as_markup(resize_keyboard=True)
    )


@dp.message(
    ChoiceCar.choosing_year_max,
    F.text == 'Назад'
)
async def year_max_back(message: types.Message, state: FSMContext):
    kb = ReplyKeyboardBuilder()
    kb.add(types.KeyboardButton(text='Без разницы'))
    kb.add(types.KeyboardButton(text='Назад'))
    kb.add(types.KeyboardButton(text='Отменить'))
    kb.adjust(2)
    await state.update_data(year_min=message.text)
    await state.set_state(ChoiceCar.choosing_year_min)
    await message.answer(
        text="Впишите минимальный год поиска машин:\n(не раньше 1900, например, 1998, 2005 и т.д.)",
        reply_markup=kb.as_markup(resize_keyboard=True)
    )


@dp.message(
    ChoiceCar.choosing_mileage_min,
    F.text == 'Назад'
)
async def mileage_min_back(message: types.Message, state: FSMContext):
    kb = ReplyKeyboardBuilder()
    kb.add(types.KeyboardButton(text='Без разницы'))
    kb.add(types.KeyboardButton(text='Назад'))
    kb.add(types.KeyboardButton(text='Отменить'))
    kb.adjust(2)
    await state.update_data(year_max=message.text)
    await state.set_state(ChoiceCar.choosing_year_max)
    await message.answer(
        text="Впишите максимальный год поиска машин:\n(не позже 2023, например, 1998, 2005 и т.д.)",
        reply_markup=kb.as_markup(resize_keyboard=True)
    )


@dp.message(
    ChoiceCar.choosing_mileage_max,
    F.text == 'Назад'
)
async def mileage_max_back(message: types.Message, state: FSMContext):
    kb = ReplyKeyboardBuilder()
    kb.add(types.KeyboardButton(text='Без разницы'))
    kb.add(types.KeyboardButton(text='Назад'))
    kb.add(types.KeyboardButton(text='Отменить'))
    kb.adjust(2)
    await state.update_data(mileage_min=message.text)
    await state.set_state(ChoiceCar.choosing_mileage_min)
    await message.answer(
        text="Впишите минимальный пробег желаемой машины:\n(например, 50000, 175000 и т.д.)",
        reply_markup=kb.as_markup(resize_keyboard=True)
    )


@dp.message(
    ChoiceCar.choosing_price_min,
    F.text == 'Назад'
)
async def price_min_back(message: types.Message, state: FSMContext):
    kb = ReplyKeyboardBuilder()
    kb.add(types.KeyboardButton(text='Без разницы'))
    kb.add(types.KeyboardButton(text='Назад'))
    kb.add(types.KeyboardButton(text='Отменить'))
    kb.adjust(2)
    await state.update_data(mileage_max=message.text)
    await state.set_state(ChoiceCar.choosing_mileage_max)
    await message.answer(
        text="Впишите максимальный пробег желаемой машины:\n(например, 150000, 275000 и т.д.)",
        reply_markup=kb.as_markup(resize_keyboard=True)
    )


@dp.message(
    ChoiceCar.choosing_price_max,
    F.text == 'Назад'
)
async def price_max_back(message: types.Message, state: FSMContext):
    kb = ReplyKeyboardBuilder()
    kb.add(types.KeyboardButton(text='Без разницы'))
    kb.add(types.KeyboardButton(text='Назад'))
    kb.add(types.KeyboardButton(text='Отменить'))
    kb.adjust(2)
    await state.update_data(price_min=message.text)
    await state.set_state(ChoiceCar.choosing_price_min)
    await message.answer(
        text="Впишите минимальную цену машины:\n(например, 5000, 20000 и т.д.)\nВнимаение! Валюта бота - польский злотый!",
        reply_markup=kb.as_markup(resize_keyboard=True)
    )
