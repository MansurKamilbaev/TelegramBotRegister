import telebot

import buttons

bot = telebot.TeleBot("6867174864:AAEQInjC1JC6vc19pNRSXAcEp8ISwXOPb7E")

@bot.message_handler(commands=['start'])
def start(message):
    user_id=message.from_user.id
    bot.send_message(user_id,'Добро пожаловать в наш бот! Выберите кнопку:',reply_markup=buttons.choice_buttons())


@bot.message_handler(content_types=['text'])

def start_mybot_text(message):
    user_id = message.from_user.id
    if message.text =="Заказать услугу":
        bot.send_message(user_id,'Введите свое имя:',reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message,get_name)


def get_name(message):
    user_name=message.text
    user_id = message.from_user.id
    bot.send_message(user_id,"Отправьте теперь номер телефона: ",reply_markup=buttons.number_buttons())
    bot.register_next_step_handler(message,get_number,user_name)

def get_number(message,user_name):
    user_id = message.from_user.id
    if message.contact and message.contact.phone_number:
        user_number=message.contact.phone_number
        bot.send_message(user_id,'Напишите вашу услугу: ')
        bot.register_next_step_handler(message,get_service,user_name,user_number)


def get_service(message,user_name,user_number):
    user_id = message.from_user.id
    user_service=message.text
    bot.send_message(user_id,'Какие сроки?')
    bot.register_next_step_handler(message,get_deadline,user_name,user_number,user_service)

#-4023613416
def get_deadline(message,user_name,user_number,user_service):
    user_deadline=message.text
    user_id = message.from_user.id
    bot.send_message(-4023613416,f'Новая заявка!\n\nИмя:{user_name}\n'
                                 f'Номер телефона:{user_number}\n'
                                 f'Услуга{user_service}\n'
                                 f'Срок:{user_deadline}\n')
    bot.send_message(user_id,'Скоро админы вам позвонят!😂')
    bot.register_next_step_handler(message,start_mybot_text)



bot.infinity_polling()
