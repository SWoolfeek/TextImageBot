#!/usr/bin/env py
import MySQLDB
import telebot
import keys
from telebot import types
import picture
import os

token = keys.telegram_token
bot = telebot.TeleBot(token)



@bot.message_handler(commands=['start'])
def start(message):
    try:
        MySQLDB.add_new(message.chat.id, message.chat.first_name)
    except:
        pass
    bot.send_message(message.chat.id,
                     'Hi, write the text and take a picture.\n',
                     reply_markup=starting_keyboard())


@bot.message_handler(commands=['background_color'])
def text_black(message):
    bot.send_message(message.chat.id,
                     'Here you can change background color.\n',
                     reply_markup=background_keyboard())


@bot.message_handler(commands=['text_color'])
def text_black(message):
    bot.send_message(message.chat.id,
                     'Here you can change text color.\n',
                     reply_markup=text_keyboard())


# Text colors
@bot.message_handler(commands=['t_red'])
def text_black(message):
    try:
        MySQLDB.text_color(message.chat.id, '#CC0000')
    except:
        pass
    bot.send_message(message.chat.id,
                     'Now, text color is red.\n',
                     reply_markup=starting_keyboard())


@bot.message_handler(commands=['t_black'])
def text_black(message):
    try:
        MySQLDB.text_color(message.chat.id, '#000000')
    except:
        pass
    bot.send_message(message.chat.id,
                     'Now, text color is black.\n',
                     reply_markup=starting_keyboard())


@bot.message_handler(commands=['t_white'])
def text_black(message):
    try:
        MySQLDB.text_color(message.chat.id, '#FFFFFF')
    except:
        pass
    bot.send_message(message.chat.id,
                     'Now, text color is white.\n',
                     reply_markup=starting_keyboard())


@bot.message_handler(commands=['t_blue'])
def text_black(message):
    try:
        MySQLDB.text_color(message.chat.id, '#0000CC')
    except:
        pass
    bot.send_message(message.chat.id,
                     'Now, text color is blue.\n',
                     reply_markup=starting_keyboard())


@bot.message_handler(commands=['t_green'])
def text_black(message):
    try:
        MySQLDB.text_color(message.chat.id, '#006600')
    except:
        pass
    bot.send_message(message.chat.id,
                     'Now, text color is green.\n',
                     reply_markup=starting_keyboard())


@bot.message_handler(commands=['t_yellow'])
def text_black(message):
    try:
        MySQLDB.text_color(message.chat.id, '#FFFF00')
    except:
        pass
    bot.send_message(message.chat.id,
                     'Now, text color is yellow.\n',
                     reply_markup=starting_keyboard())


# Background colors
@bot.message_handler(commands=['b_red'])
def back_red(message):
    try:
        MySQLDB.background_color(message.chat.id, '#990000')
    except:
        pass
    bot.send_message(message.chat.id,
                     'Now, background color is red.\n'
                     , reply_markup=starting_keyboard())

@bot.message_handler(commands=['b_black'])
def back_red(message):
    try:
        MySQLDB.background_color(message.chat.id, '#000000')
    except:
        pass
    bot.send_message(message.chat.id,
                     'Now, background color is black.\n'
                     , reply_markup=starting_keyboard())


@bot.message_handler(commands=['b_white'])
def back_red(message):
    try:
        MySQLDB.background_color(message.chat.id, '#FFFFFF')
    except:
        pass
    bot.send_message(message.chat.id,
                     'Now, background color is white.\n'
                     , reply_markup=starting_keyboard())


@bot.message_handler(commands=['b_blue'])
def back_red(message):
    try:
        MySQLDB.background_color(message.chat.id, '#009999')
    except:
        pass
    bot.send_message(message.chat.id,
                     'Now, background color is blue.\n'
                     , reply_markup=starting_keyboard())


@bot.message_handler(commands=['b_green'])
def back_red(message):
    try:
        MySQLDB.background_color(message.chat.id, '#339933')
    except:
        pass
    bot.send_message(message.chat.id,
                     'Now, background color is green.\n'
                     , reply_markup=starting_keyboard())


@bot.message_handler(commands=['b_yellow'])
def back_red(message):
    try:
        MySQLDB.background_color(message.chat.id, '#FFFF66')
    except:
        pass
    bot.send_message(message.chat.id,
                     'Now, background color is yellow.\n'
                     , reply_markup=starting_keyboard())

@bot.message_handler(content_types=['text'])
def handle_text(message):
    text = message.text
    if len(text) > 500:
        bot.send_message(message.chat.id, 'Ups, the message is too big.',
                       reply_markup=starting_keyboard())
    else:
        t_color, b_color = MySQLDB.query(message.chat.id)
        photo_path = picture.create_picture(text, b_color, t_color, message.chat.id)
        photo = open(photo_path, 'rb')
        bot.send_photo(message.chat.id, photo,
                       reply_markup=starting_keyboard())

    # Deleting picture from folder
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), photo_path)
        os.remove(path)

# Keyboards
def starting_keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    btn1 = types.KeyboardButton('/background_color')
    btn2 = types.KeyboardButton('/text_color')
    markup.add(btn1, btn2)
    return markup


def background_keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    btn1 = types.KeyboardButton('/b_red')
    btn2 = types.KeyboardButton('/b_black')
    btn3 = types.KeyboardButton('/b_white')
    btn4 = types.KeyboardButton('/b_blue')
    btn5 = types.KeyboardButton('/b_green')
    btn6 = types.KeyboardButton('/b_yellow')
    markup.add(btn1, btn2, btn3)
    markup.add(btn4, btn5, btn6)
    return markup


def text_keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    btn1 = types.KeyboardButton('/t_red')
    btn2 = types.KeyboardButton('/t_black')
    btn3 = types.KeyboardButton('/t_white')
    btn4 = types.KeyboardButton('/t_blue')
    btn5 = types.KeyboardButton('/t_green')
    btn6 = types.KeyboardButton('/t_yellow')
    markup.add(btn1, btn2, btn3)
    markup.add(btn4, btn5, btn6)
    return markup

bot.polling(none_stop=True, interval=0)
