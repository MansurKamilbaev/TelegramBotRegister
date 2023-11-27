from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def choice_buttons():
    buttons=ReplyKeyboardMarkup(resize_keyboard=True)

    service_button=KeyboardButton('Заказать услугу')

    buttons.add(service_button)

    return buttons

def number_buttons():
    buttons=ReplyKeyboardMarkup(resize_keyboard=True)

    num_button=KeyboardButton('Поделиться контактом',request_contact=True,)


    buttons.add(num_button)
    return buttons