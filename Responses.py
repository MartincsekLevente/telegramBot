import Constants as const


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
        return const.none_user_name_text

    return current_session.reply(user_message, username)
