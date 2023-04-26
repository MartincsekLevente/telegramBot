import Constants as keys
from telegram.ext import *
import Responses as R
from ToDoSession import ToDoSession

sessions_dict = {}


def handle_message(update, context):
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
    update.message.reply_text('Szia! Miben tudok segíteni? A parancsok megtekintéséhez használd a /help funkciót!')


def help_command(update, context):
    update.message.reply_text('Én egy olyan bot vagyok, aki a te ToDo listádat tudja vezérelni!\n\n'
                              'Hogyha még soha nem használtál, lépj be a ToDo Hub-ba és '
                              'próbáld ki a következő parancsok egyikét:\n\n'
                              'todo - Belépsz a ToDo Hub-ba, ahonnan elérhető az összes jelenleg elérhető funkcióm!\n\n'
                              'Hozzáadás - Addj hozzá a ToDo listádhoz egy saját feladatot! \n\n'
                              'Kiválasztás - Válassz ki egy feladatot a saját ToDo listádról! \n\n'
                              'Megjelenítés - Megjelenítem neked az összes ToDo feladatodat a listádról!\n\n'
                              'Teljesítmény - Megjelenítem neked az eddig elért eredményeidet a '
                              'teljesített feladataid alapján!\n\n')


def error(update, context):
    print(f"ERROR: Update {update} caused error {context.error}")


def main():
    print("Bot started...")
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
