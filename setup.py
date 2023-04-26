from setuptools import setup

setup(
    name="todo_telegram_chatbot",
    version="1.0.0",
    author='Martincsek Levente',
    readme="README.md",
    author_email='martincsekl@gmail.com',
    packages=['telegramBot'],
    install_requires=[
        "python-telegram-bot",
        "datetime",
        "uuid"
    ],
)
