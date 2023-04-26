def sample_responses(input_text, username, current_session):
    user_message = str(input_text)

    if username == "None":
        return "Úgy néz ki, hogy a felhasználóneved None. Kérlek állíts be magadnak egy felhasználónevet!"

    return current_session.reply(user_message, username)


