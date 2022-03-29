from telegram.ext import *
from telegram import *
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

filepath = "user.txt"

PORT = int(os.environ.get('PORT', 80))
TOKEN = os.environ["TOKEN"]


def start(update: Update, context: CallbackContext):
    buttons = [[InlineKeyboardButton("🔉English", callback_data="_english_")], [
        InlineKeyboardButton("🔉አማርኛ", callback_data="_amharic_")]]
    context.bot.send_message(
        chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons), text="Choose Language/ቋንቋ ይምረጡ")
    context.user_data["current"] = ""
    context.user_data["data"] = ""


def messageHandler(update: Update, context: CallbackContext):
    if context.user_data.get("current", "") == "1e":
        context.bot.send_message(
            chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⏭Skip", callback_data="_skip_")]]), text="📧What is your Email address?")
        context.user_data["current"] = "2e"
        context.user_data["data"] += update.message.text + "~"

    elif context.user_data.get("current", "") == "1a":
        context.bot.send_message(
            chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⏭እለፍ", callback_data="_skip_")]]), text="📧እባክዎ የኢሜል አድራሻዎን ይላኩ")
        context.user_data["current"] = "2a"
        context.user_data["data"] += update.message.text + "~"

    elif context.user_data.get("current", "") == "2e":
        context.bot.send_message(
            chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⏭Skip", callback_data="_skip_")]]), text="📱What is your Phone Number?")
        context.user_data["current"] = "3e"
        context.user_data["data"] += update.message.text + "~"

    elif context.user_data.get("current", "") == "2a":
        context.bot.send_message(
            chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⏭እለፍ", callback_data="_skip_")]]), text="📱እባክዎ ስልክ ቁጥርዎን ይላኩ")
        context.user_data["current"] = "3a"
        context.user_data["data"] += update.message.text + "~"

    elif context.user_data.get("current", "") == "3e":
        buttons = [[InlineKeyboardButton("💵Money", callback_data="_money_"), InlineKeyboardButton("⚙Knowladge", callback_data="_knowladge_")], [
            InlineKeyboardButton("🎯Other", callback_data="_other_")]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(
            buttons), text="💪In what way you want to contribute?")
        context.user_data["current"] = "4e"
        context.user_data["data"] += update.message.text + "~"

    elif context.user_data.get("current", "") == "3a":
        buttons = [[InlineKeyboardButton("💵በገንዘብ", callback_data="_money_"), InlineKeyboardButton("⚙በእውቀት", callback_data="_knowladge_")], [
            InlineKeyboardButton("🎯ሌላ", callback_data="_othera_")]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(
            buttons), text="💪ሃሳቡን በምን መልክ ማገዝ ይፈልጋሉ?")
        context.user_data["current"] = "4a"
        context.user_data["data"] += update.message.text + "~"

    elif context.user_data.get("current", "") == "4e1":
        context.user_data["current"] = "5e"
        context.user_data["data"] += update.message.text + "~"
        buttons = [[InlineKeyboardButton("Active World (Mindset)", callback_data="_mindset_"), InlineKeyboardButton("Art (Culture)", callback_data="_art_")], [
            InlineKeyboardButton("Medicine (Modern + Traditional)", callback_data="_medicine_"), InlineKeyboardButton("Technology and Inovation", callback_data="_tech_")]]
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 reply_markup=InlineKeyboardMarkup(buttons), text="Which Division are you interested in?")

    elif context.user_data.get("current", "") == "6e":
        context.user_data["current"] = ""
        context.user_data["data"] += update.message.text
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Thank You for your time.\n Your registration is Complete.\nHave a nice day.")
        with open(filepath, 'a') as fp:
        fp.write(str(datetime.now())+"~"+context.user_data["data"]+"\n")
        fp.close()

    elif context.user_data.get("current", "") == "4a1":
        context.user_data["current"] = "5a"
        context.user_data["data"] += update.message.text + "~"
        buttons = [[InlineKeyboardButton("Active World (Mindset)", callback_data="_mindset_"), InlineKeyboardButton("Art (Culture)", callback_data="_art_")], [
            InlineKeyboardButton("Medicine (Modern + Traditional)", callback_data="_medicine_"), InlineKeyboardButton("Technology and Inovation", callback_data="_tech_")]]
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 reply_markup=InlineKeyboardMarkup(buttons), text="Which Division are you interested in?")

    elif context.user_data.get("current", "") == "6a":
        context.user_data["current"] = "7a"
        context.user_data["data"] += update.message.text
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="ለትብብርዎ እናመሰግናለን።\n ምዝገባዎ ተጠናቋል።\nመልካም ቀን ይሁንልዎ።")
        with open(filepath, 'a') as fp:
        fp.write(str(datetime.now())+"~"+context.user_data["data"]+"\n")
        fp.close()



def queryHandler(update: Update, context: CallbackContext):
    query = update.callback_query
    text = query.data

    if text == "_english_":
        context.user_data["current"] = "1e"
        context.user_data["data"] = ""
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="👋Hello there \n😀What is your name?")

    elif text == "_amharic_":
        context.user_data["current"] = "1a"
        context.user_data["data"] = ""
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="👋ሰላም \n😀ስሞትን ማን ልበል?")

    elif text == "_money_" or text == "_knowladge_":
        if context.user_data.get("current", "") == "4e":
            context.user_data["current"] = "5e"
            context.user_data["data"] += text + "~"
            buttons = [[InlineKeyboardButton("Active World (Mindset)", callback_data="_mindset_"), InlineKeyboardButton("Art (Culture)", callback_data="_art_")], [
                InlineKeyboardButton("Medicine (Modern + Traditional)", callback_data="_medicine_"), InlineKeyboardButton("Technology and Inovation", callback_data="_tech_")]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(
                buttons), text="Which Division are you interested in?")

        elif context.user_data.get("current", "") == "4a":
            context.user_data["current"] = "5a"
            context.user_data["data"] += text + "~"
            buttons = [[InlineKeyboardButton("ንቁ ዓለም (Mindset)", callback_data="_mindset_"), InlineKeyboardButton("ጥበብ (ባህል)", callback_data="_art_")], [
                InlineKeyboardButton("ህክምና (ዘመናዊ + ባህላዊ)", callback_data="_medicine_"), InlineKeyboardButton("ተክኖሎጂ እና ኢኖቬሽን", callback_data="_tech_")]]
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     reply_markup=InlineKeyboardMarkup(buttons), text="ይበልጥ መሳተፍ የሚፈልጉበት ክፍል የትኛው ነው?")

    elif text == "_other_":
        context.user_data["current"] = "4e1"
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="How would you like to contribute to the cause?")

    elif text == "_othera_":
        context.user_data["current"] = "4a1"
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="ማህበሩን በምን መልኩ ማገዝ ይሻሉ?")

    elif context.user_data.get("current", "") == "5a":
        context.user_data["current"] = "6a"
        context.user_data["data"] += text + "~"
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="አስተያየት ካለዎ?")
    elif context.user_data.get("current", "") == "5e":
        context.user_data["current"] = "6e"
        context.user_data["data"] += text + "~"
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Do You have any comments?")

    elif text == "_skip_":

        if context.user_data.get("current", "") == "2e":
            context.bot.send_message(
                chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⏭Skip", callback_data="_skip_")]]), text="📱What is your Phone Number?")
            context.user_data["current"] = "3e"
            context.user_data["data"] += "Unknown" + "~"

        elif context.user_data.get("current", "") == "3e":
            buttons = [[InlineKeyboardButton("💵Money", callback_data="_money_"), InlineKeyboardButton("⚙Knowladge", callback_data="_knowladge_")], [
                InlineKeyboardButton("🎯Other", callback_data="_other_")]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(
                buttons), text="💪In what way you want to contribute?")
            context.user_data["current"] = "4e"
            context.user_data["data"] += "Unknown" + "~"

        elif context.user_data.get("current", "") == "2a":
            context.bot.send_message(
                chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⏭እለፍ", callback_data="_skip_")]]), text="📱እባክዎ ስልክ ቁጥርዎን ይላኩ")
            context.user_data["current"] = "3a"
            context.user_data["data"] += "Unknown" + "~"

        elif context.user_data.get("current", "") == "3a":
            buttons = [[InlineKeyboardButton("💵በገንዘብ", callback_data="_money_"), InlineKeyboardButton("⚙በእውቀት", callback_data="_knowladge_")], [
                InlineKeyboardButton("🎯ሌላ", callback_data="_other_")]]
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(
                buttons), text="💪ሃሳቡን በምን መልክ ማገዝ ይፈልጋሉ?")
            context.user_data["current"] = "4a"
            context.user_data["data"] += "Unknown" + "~"


def main():

    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(queryHandler))
    dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
