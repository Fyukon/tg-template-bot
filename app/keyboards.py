from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def contact_kb() -> ReplyKeyboardMarkup:
    button = KeyboardButton(text = "Отправить номер телефона", request_contact=True)
    keyboard = ReplyKeyboardMarkup(keyboard = [[button]], resize_keyboard=True)
    return keyboard

def main_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Services", callback_data="services"))
    builder.row(InlineKeyboardButton(text="About", callback_data="about"))
    builder.row(InlineKeyboardButton(text="Оставить заявку", callback_data="request"))
    return builder.as_markup()


def services_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Service 1", callback_data="service_1"),
                    InlineKeyboardButton(text="Service 2", callback_data="service_2"))
    builder.row(InlineKeyboardButton(text="Service 3", callback_data="service_3"),
                    InlineKeyboardButton(text="Service 4", callback_data="service_4"))
    builder.row(InlineKeyboardButton(text="Назад", callback_data="main_menu"), )
    return builder.as_markup()

def back_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Назад", callback_data="main_menu"))
    return builder.as_markup()
