from telegram.ext import *
from telegramBot.to_do_session import ToDoSession
from telegramBot import responses, constants

sessions_dict = {}


def handle_message(update, context):
    """
       Ez a függvény kezeli a felhasználótól kapott üzeneteket.

       Args:
           update: Az üzenet és az üzenetküldő tulajdonságai.
           context: A kontextus.
    """
    text = str(update.message.text)
    username = update.message.from_user.username
    if username in sessions_dict:
        current_session = sessions_dict[username]
    else:
        current_session = ToDoSession()
        sessions_dict[username] = current_session

    response = responses.sample_responses(text, username, current_session)
    update.message.reply_text(response)


def start_command(update, context):
    """
       Ez a függvény kezeli a /start parancsot.

       Args:
           update: Az üzenet és az üzenetküldő tulajdonságai.
           context: A kontextus.
    """
    update.message.reply_text(constants.START_TEXT)


def help_command(update, context):
    """
        Ez a függvény kezeli a /help parancsot.

        Args:
            update: Az üzenet és az üzenetküldő tulajdonságai.
            context: A kontextus.
    """

    update.message.reply_text(constants.HELP_TEXT)


def error(update, context):
    """
        Ez a függvény kezeli az error lehetőségeket.

        Args:
            update: Az üzenet és az üzenetküldő tulajdonságai.
            context: A kontextus, ebből vehető ki maga az error típusa.
    """
    print(f"ERROR: Update {update} caused error {context.error}")


def main():
    """
        A main függvény, ebből indul ki az összes segéd függvény.

    """
    print("Bot started...")
    updater = Updater(constants.API_KEY, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))

    dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
