from setuptools import setup, find_packages

setup(
    name="todo_telegram_chatbot",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "python-telegram-bot",
        "datetime",
        "uuid"
    ],
)
