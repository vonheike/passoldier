from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)

from telegram import InlineKeyboardButton, InlineKeyboardMarkup


from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,

                          ConversationHandler, CallbackQueryHandler)

from time import sleep

import os

FLOOD = range(1)



reply_keyboard = [['@Penitenziario', '@Penitenziario', '@Penitenziario', '@Penitenziaroo', '@Penitenziario'],

                      ['@Penitenziario', '@Penitenziario', '@Penitenziario', '@Penitenziario', '@Penitenziario'],

                      ['@Penitenziario', '@Penitenziario', '@Penitenziario', '@Penitenziario', '@Penitenziario']]

inline_keyboard = [

        [InlineKeyboardButton("👤", url='t.me/Penitenziario'), InlineKeyboardButton("👤", url='t.me/ouned')],

        [InlineKeyboardButton("👤", url='t.me/Penitenziario'), InlineKeyboardButton("👤", url='t.me/Penitenziario')],

        [InlineKeyboardButton("👤", url='t.me/Penitenziario'), InlineKeyboardButton("👤", url='t.me/Penitenziario')],

        [InlineKeyboardButton("👤", url='t.me/Penitenziario'), InlineKeyboardButton("👤", url='t.me/Penitenziario')],

        [InlineKeyboardButton("👤", url='t.me/diotrans'), InlineKeyboardButton("👤", url='t.me/diotrans')],

        [InlineKeyboardButton("👤", url='t.me/Penitenziario'), InlineKeyboardButton("👤", url='t.me/Penitenziario')]

    ]


def start(bot, update):

    global reply_keyboard, inline_keyboard

    if update.message.chat.type == "private":

        update.message.reply_text("Salve %s, per utilizzare questo bot, aggiungilo al tuo gruppo" % update.message.from_user.name)

    else:

        a = 0

        while a < 5:

            a = a + 1

            bot.sendMessage(chat_id=update.message.chat_id, text="Sei sotto attacco del grande Reich 👉👉\n\n\n👉👉👉\n\n👉👉👉\n" * 100,

                            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False))

            bot.sendMessage(chat_id=update.message.chat_id, text="Ops sei ancora sotto attacco 👉👉\n\n\n👏👏👏\n\n👏👏👏\n" * 100,

                            reply_markup=InlineKeyboardMarkup(inline_keyboard))

    return flood

def flood(bot, update):

    global reply_keyboard, inline_keyboard

    a = 0

    while a < 5:

        a = a + 1

        bot.sendMessage(chat_id=update.message.chat_id, text="IL REICH COLPISCE XD\n\n\n XD XD XD XD XD XD \n\n\n" * 100,

                        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False))

        bot.sendMessage(chat_id=update.message.chat_id, text="COLPISCE FORTE E GLORIOSO \n\n\n c: c: c: \n\n\n" * 100,

                        reply_markup=InlineKeyboardMarkup(inline_keyboard))


def cancel():

    print("SOS")

def on_join(bot, update):

    global reply_keyboard, inline_keyboard

    if update.message.new_chat_members:

        a = 0

        while a < 5:

            a = a + 1

            bot.sendMessage(chat_id=update.message.chat_id, text="Siamo consapevoli che il nostro bot sta cortesemente floddando  :’)\n\n\n :’] :’] [‘: [‘: \n\n\n" * 100,

                            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False))

            bot.sendMessage(chat_id=update.message.chat_id, text="lel 👺\n\n\n lel lel lel lel👺👺👺👺👺\n\n\n" * 140,

                            reply_markup=InlineKeyboardMarkup(inline_keyboard))

def main():

    updater = Updater("550184488:AAGn1Hux_LLphZpyFszGzxyyd2ggguSG1e0")

    dp = updater.dispatcher

    conv_handler = ConversationHandler(

        entry_points=[CommandHandler('start', start)],


        states={

            FLOOD: [RegexHandler('^(@penitenziario|@penitenziario|@penitenziario|@ouned|@ouned|@ouned|@ouned|@ouned|@ouned|@ouned|@ouned|@ouned|@ouned|@ouned|@ouned)$', flood)],

        },


        fallbacks=[CommandHandler('cancel', cancel)]

    )


    dp.add_handler(MessageHandler(Filters.status_update, on_join))

    dp.add_handler(conv_handler)

    updater.start_polling()

    updater.idle()



if __name__ == '__main__':

    main()
