from telegramBot import constants


def sample_responses(input_text, username, current_session):
    """
       Ez a függvény kezeli a felhasználótól kapott üzeneteket.

       Args:
           input_text: Az aktuális beszélgető partner jelenlegi üzenete
           username: Az aktuális beszélgető partner felhasználóneve
           current_session: Az aktuális beszélgető partnerhez tartozó session.
    """
    user_message = str(input_text)

    if username == "None":
        return constants.NONE_USER_NAME_TEXT

    return current_session.reply(user_message, username)
