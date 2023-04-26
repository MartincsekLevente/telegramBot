import Constants as const
from telegram.ext import *
import Responses as R
from ToDoSession import ToDoSession

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

    response = R.sample_responses(text, username, current_session)
    update.message.reply_text(response)


def start_command(update, context):
    """
       Ez a függvény kezeli a /start parancsot.

       Args:
           update: Az üzenet és az üzenetküldő tulajdonságai.
           context: A kontextus.
    """
    update.message.reply_text(const.start_text)


def help_command(update, context):
    """
        Ez a függvény kezeli a /help parancsot.

        Args:
            update: Az üzenet és az üzenetküldő tulajdonságai.
            context: A kontextus.
    """

    update.message.reply_text(const.help_text)


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
    updater = Updater(const.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
