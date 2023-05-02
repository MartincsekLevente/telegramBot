---
#ToDo Telegram Chatbot
##Készítette: Martincsek Levente

---

##A bot funkciói:
- Saját ToDo lista meneddzselése
- CRUD műveletek a felvett ToDo feladatokra
- Feladat megjelőlése sikeres vagy sikertelennek
- Statisztika készítése az elvégzett feladatok arányáról

##Szükséges csomagok:
- python-telegram-chatbot - 13.7
- `pip install -r requirements.txt` paranccsal lehet telepíteni a szükséges csomagokat

##A bot működése:
- Egyedi API kulcs alapján van bekonfigurálva, amit ki lehet cserélni ha a saját chatbotodat szeretnéd használni.
- A bot képes külön session-t kezelni minden beszélgető partner esetén
- Json fájlokban van eltárolva a felhasználók adatai.
- A kód jól struktúrált, dokumentált, konstansokba szervezett
- A kód moduláris megtervezése miatt bármikor bővíthető


##A bot használata:
- Ezen a linken megtalálható a project: https://github.com/MartincsekLevente/telegramBot
- Vagy pedig a projektet lehet telepíteni a dist/todo_telegram_chatbot-1.0.tar.gz fájl telepítésével
- A fájl könyvtárában a következő parancsal: pip install .\todo_telegram_chatbot-1.0.tar.gz
- A botot a Telegram felületén @ToDo420Bot felhasználónéven lehet elérni
- A bot használatához regisztrálni kell a Telegram felületén egy profilt.
- A botra csak rá kell köszönni, vagy akár bármit írni neki, és onnan már vezetni fog a parancsokkal