from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from .car import ChoiceCar, transmission_list, marks_and_models
from loader import dp


@dp.message(ChoiceCar.choosing_mark)
async def mark_incorrectly(message: types.Message):
    kb = ReplyKeyboardBuilder()
    count = 0
    for model in marks_and_models:
        if model[0][0] == message.text:
            count += 1
            kb.add(types.KeyboardButton(text=model[0]))
    if count >= 2:
        kb.adjust(2)
    await message.answer(
        text="Марку не найденно!\n\n"
             "Пожалуйста, выберите марку из списка ниже:",
        reply_markup=kb.as_markup(resize_keyboard=True)
    )


@dp.message(ChoiceCar.choosing_model)
async def model_incorrectly(message: types.Message):
    kb = ReplyKeyboardBuilder()
    count = 0
    for model in marks_and_models:
        if model[0] == message.text:
            count += 1
            for mod in model[1]:
                kb.add(types.KeyboardButton(text=mod))
            kb.adjust(2)
            kb.add(types.KeyboardButton(text='Назад'))
            kb.add(types.KeyboardButton(text='Отменить'))
    if count >= 2:
        kb.adjust(2)
    await message.answer(
        text="Модель не найденно!\n\n"
             "Пожалуйста, выберите модель из списка ниже:",
        reply_markup=kb.as_markup(resize_keyboard=True)
    )


@dp.message(ChoiceCar.choosing_transmission)
async def transmission_incorrectly(message: types.Message):
    kb = ReplyKeyboardBuilder()
    for trans in transmission_list:
        kb.add(types.KeyboardButton(text=trans))
    kb.add(types.KeyboardButton(text='Назад'))
    kb.add(types.KeyboardButton(text='Отменить'))
    kb.adjust(2)
    await message.answer(
        text="Пожалуйста, выберите коробку передач из списка ниже",
        reply_markup=kb.as_markup(resize_keyboard=True)
    )


@dp.message(ChoiceCar.choosing_year_min)
async def year_min_incorrectly(message: types.Message):
    kb = ReplyKeyboardBuilder()
    kb.add(types.KeyboardButton(text='Без разницы'))
    kb.add(types.KeyboardButton(text='Назад'))
    kb.add(types.KeyboardButton(text='Отменить'))
    kb.adjust(2)
    await message.answer(
        text="Год введён неверно!\nПожалуйста, впишите минимальный год поиска машин:\n"
             "(не раньше 1900, например, 1998, 2005 и т.д.)",
        reply_markup=kb.as_markup(resize_keyboard=True)
    )


@dp.message(ChoiceCar.choosing_year_max)
async def year_max_incorrectly(message: types.Message):
    kb = ReplyKeyboardBuilder()
    kb.add(types.KeyboardButton(text='Без разницы'))
    kb.add(types.KeyboardButton(text='Назад'))
    kb.add(types.KeyboardButton(text='Отменить'))
    kb.adjust(2)
    await message.answer(
        text="Год введён неверно!\nПожалуйста, впишите максимальный год поиска машин:\n"
             "(не позже 2023, например, 1998, 2005 и т.д.)",
        reply_markup=kb.as_markup(resize_keyboard=True)
    )


@dp.message(ChoiceCar.choosing_mileage_min)
async def mileage_min_incorrectly(message: types.Message):
    kb = ReplyKeyboardBuilder()
    kb.add(types.KeyboardButton(text='Без разницы'))
    kb.add(types.KeyboardButton(text='Назад'))
    kb.add(types.KeyboardButton(text='Отменить'))
    kb.adjust(2)
    await message.answer(
        text="Пробег введён некорректно!\nПожалуйста, впишите минимальный пробег желаемой машины:\n"
             "(например, 50000, 175000 и т.д.)",
        reply_markup=kb.as_markup(resize_keyboard=True)
    )


@dp.message(ChoiceCar.choosing_mileage_max)
async def mileage_max_incorrectly(message: types.Message):
    kb = ReplyKeyboardBuilder()
    kb.add(types.KeyboardButton(text='Без разницы'))
    kb.add(types.KeyboardButton(text='Назад'))
    kb.add(types.KeyboardButton(text='Отменить'))
    kb.adjust(2)
    await message.answer(
        text="Пробег введён некорректно!\nПожалуйста, впишите максимальный пробег желаемой машины:\n"
             "(например, 150000, 275000 и т.д.)",
        reply_markup=kb.as_markup(resize_keyboard=True)
    )


@dp.message(ChoiceCar.choosing_price_min)
async def price_min_incorrectly(message: types.Message):
    kb = ReplyKeyboardBuilder()
    kb.add(types.KeyboardButton(text='Без разницы'))
    kb.add(types.KeyboardButton(text='Назад'))
    kb.add(types.KeyboardButton(text='Отменить'))
    kb.adjust(2)
    await message.answer(
        text="Цена введена некорректно!\nПожалуйста, впишите минимальную цену машины:\n"
             "(например, 5000, 20000 и т.д.)\nВнимаение! Валюта бота - польский злотый!",
        reply_markup=kb.as_markup(resize_keyboard=True)
    )


@dp.message(ChoiceCar.choosing_price_max)
async def price_max_incorrectly(message: types.Message):
    kb = ReplyKeyboardBuilder()
    kb.add(types.KeyboardButton(text='Без разницы'))
    kb.add(types.KeyboardButton(text='Назад'))
    kb.add(types.KeyboardButton(text='Отменить'))
    kb.adjust(2)
    await message.answer(
        text="Цена введена некорректно!\nПожалуйста, впишите максимальную цену машины:\n"
             "(например, 30000, 55000 и т.д.)\nВнимаение! Валюта бота - польский злотый!",
        reply_markup=kb.as_markup(resize_keyboard=True)
    )
