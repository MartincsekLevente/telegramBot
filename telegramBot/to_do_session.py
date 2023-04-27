import uuid
from telegramBot.to_do_handler import ToDoHandler
from telegramBot.to_do_task import ToDoTask
from telegramBot import constants


class ToDoSession:

    def __init__(self):
        self.state = 0
        self.current_to_do_task = ToDoTask()
        self.selected_task_id = ''

    def get_state(self):
        """
           Ez a függvény visszaadja az aktuális state-t
        """
        return self.state

    def start_add_new_task(self):
        """
           Ez a függvény példányosít egy feladatot, üres értékkel későbbi feltöltésre
        """
        self.current_to_do_task = ToDoTask()

    def set_state(self, state):
        """
           Ezzel a függvénnyel lehet beállítani a state aktuális értékét

           Args:
               state: A state amire be kell állítani a változót
        """
        self.state = state

    def set_selected_task_id(self, task_id):
        """
           Ezzel a függvénnyel lehet beállítani a kiválasztott feladat id-jét.

           Args:
               task_id: A kiválasztott feladat id-je
        """
        self.selected_task_id = task_id

    def start_session(self):
        """
           Ezzel a függvénnyel lehet elindítani a session-t, így a state is visszaállítódik 1-re
        """
        self.state = 1
        return constants.START_SESSION_TEXT

    def jump_to_state(self, to_jump, info1='', info2=''):
        """
           Ezzel a függvénnyel át lehet ugrani egy bizonyos
            paraméterben megadott state-re, ebben az aktív session-ben.

           Args:
               to_jump: A state id-je, ahova át kell ugrania ennek az aktív session-nek.
               info1: Az első nem kötelező, plusz információ átadásra fenttartott paraméter
               info2: Az második nem kötelező, plusz információ átadásra fenttartott paraméter
        """
        self.state = to_jump
        match to_jump:
            case 0:
                return 'Szia! Miben tudok segíteni? ' \
                       'A parancsok megtekintéséhez használd a /help funkciót!'
            case 1:
                return self.start_session()
            case 2:
                return 'A [Hozzáadás] funkciót választottad. \n\n' \
                       'Ahhoz, hogy hozzáadj egy elemet a ToDo listádhoz,' \
                       ' csak írd be kívánt ToDo feladatod nevét! '
            case 3:
                return 'Az általad választott név a következő: ' + info1 + '\n\n' \
                       'Most add meg kérlek milyen dátummal legyen' \
                       ' határidős az általad választott ToDo feladat.\n' \
                       'A dátumot így add meg: Év/Hónap/Nap \nPl: 2023/04/24'
            case 4:
                return 'Az általad választott dátum a következő: ' + info1 + '\n\n' \
                       'Most add meg kérlek milyen leírás ' \
                       'tartozzon általad választott ToDO feladathoz!\n'
            case 5:
                self.state = 1
                return 'A [Megjelenítés] funkciót választottad. \n' \
                       'Íme az összes eddig hozzáadott ToDo Taskod:\n\n' \
                       + ToDoHandler.to_do_list_show_all(info1) + \
                       '\nTovábbi funkciókért használd a /help parancsot!'
            case 6:
                return 'A [Kiválasztás] funkciót választottad. \n\n' \
                       'Ahhoz, hogy teljesítetté vagy törölté tegyél egy elemet a ToDo listádból,' \
                       ' csak írd be kívánt ToDo feladatod referencia ID-jét!' \
                       ' Ezek az álatlad felvett' \
                       ' ToDo feladatok:\n\n' \
                       + ToDoHandler.to_do_list_show_all(info1)
            case 7:
                return 'Az általad beírt referencia ID (' + info2 + ') alapján ' \
                       'ezt a feladatot választottad ki:\n\n' \
                       + ToDoHandler.to_do_list_select_task_by_id(info1, info2) + \
                       'A következő lépésben kérlek add meg, hogy hogyan szeretnéd ' \
                       'lezárni az adott ToDo feladatot!\n\n' \
                       'completed: Ezt a feladatot teljesítetted.\n' \
                       'failed: Ezt a feladatot nem teljesítetted.\n' \
                       'remove: Ez a feladat tévesen lett felvéve.\n'
            case 8:
                self.state = 1
                return 'A kiválasztott ToDo feladat elvégzett státusszal le lett zárva!\n\n' \
                       'További funkciókért használd a /help parancsot!'
            case 9:
                self.state = 1
                return 'A kiválasztott ToDo feladat nem teljesített státusszal le lett zárva!\n\n' \
                       'További funkciókért használd a /help parancsot!'
            case 10:
                self.state = 1
                return 'A kiválasztott ToDO feladat törölve lett!\n\n' \
                       'További funkciókért használd a /help parancsot!'
            case 11:
                self.state = 1
                return 'A [Teljesítmény] funkciót választottad. \n' \
                       'Íme az összes eddig hozzáadott ToDo Taskod:\n\n' \
                       + ToDoHandler.to_do_list_show_performance(info1) + \
                       '\n\nTovábbi funkciókért használd a /help parancsot!'

    @staticmethod
    def wrong_task_id(task_id):
        """
           Ez a függvény kezeli le azt az esetet,
           amikor nem megfelelő feladat id lett megadva a kiválasztáshoz

           Args:
               task_id: A feladat id-je, ami hibásan lett megadva
        """
        return 'A megadott ToDo feladat referencia ID (' + task_id + ') hibás!\n' \
               'Add meg helyesen az ID-t. Ha nincsen meg ez az ID,' \
               ' akkor visszalépve a show all parancsot használva megtudod találni.'

    def quit_session(self):
        """
           Ez a függvény kezeli le azt az esetet,
           amikor szeretne a felhasználó kilépni az aktív session-ből
        """
        self.state = 0
        return "Kilépés sikeres! Miben tudok még segíteni? " \
               "A parancsok megtekintéséhez használd a /help funkciót!"

    def task_added_successfully(self, username):
        """
           Ez a függvény kezeli le azt az esetet, amikor a feladat hozzáadása sikeres volt

           Args:
               username: Az aktuális beszélgető partner felhasználóneve
        """
        self.state = 1
        ToDoHandler.to_do_list_add(username, self.current_to_do_task)
        return "A ToDo feladat hozzáadása sikeres!\n\nItt a ToDo feladatod részletes leírása:\n" \
               "Cím: " + self.current_to_do_task.title + "\n" \
               "Dátum: " + self.current_to_do_task.date + "\n" \
               "Leírás: " + self.current_to_do_task.description + "\n\n" \
               "További parancsok megtekintéséhez használd a /help funkciót!"

    def reply(self, user_message, username):
        """
           Ez a függvény felelős minden válasz adásért.
           A statek alapján kikeresi, hogy a beszélgetési fában hol járnak
           a beszélgető partnerrel, és az alapján lépteti a funkciók között.

           Args:
               user_message: Az aktuális beszélgető partner üzenete
               username: Az aktuális beszélgető partner felhasználóneve
        """
        match self.state:
            # case 0: casual conversation
            case 0:
                if user_message.lower() in ("hello", "szia"):
                    return "Szia! Miben tudok segíteni? \n" \
                           "A parancsok megtekintéséhez használd a /help funkciót!"
                elif user_message.lower() in ("idő", "ido?", "mennyi az ido", "mennyi az idő?"):
                    return "A jelenlegi pontos idő: " + str(ToDoHandler.get_time())
                elif user_message.lower() in "todo":
                    return self.start_session()
                else:
                    return ToDoHandler.not_clear_text(username)
            # case 1: add, delete, show all commands root
            case 1:
                if user_message.lower() in ("kilépés", "kilepes"):
                    return self.quit_session()
                elif (user_message.lower() == "hozzáadás") or (user_message.lower() == "hozzaadas"):
                    self.start_add_new_task()
                    self.current_to_do_task.username = username
                    return self.jump_to_state(2)
                elif (user_message.lower() == "megjelenítés") or \
                        (user_message.lower() == "megjelenites"):
                    return self.jump_to_state(5, username)
                elif (user_message.lower() == "kiválasztás") or \
                        (user_message.lower() == "kivalasztas"):
                    return self.jump_to_state(6, username)
                elif (user_message.lower() == "teljesítmény") or \
                        (user_message.lower() == "teljesitmeny"):
                    return self.jump_to_state(11, username)
                else:
                    return ToDoHandler.not_clear_text(username)
            # case 2: add title
            case 2:
                if user_message.lower() in ("kilépés", "kilepes"):
                    return self.quit_session()
                else:
                    self.current_to_do_task.title = str(user_message)
                    return self.jump_to_state(3, user_message)
            # case 3: add date
            case 3:
                if user_message.lower() in ("kilépés", "kilepes"):
                    return self.quit_session()
                else:
                    self.current_to_do_task.date = str(user_message)
                    return self.jump_to_state(4, user_message)
            # case 4: add description
            case 4:
                if user_message.lower() in ("kilépés", "kilepes"):
                    return self.quit_session()
                else:
                    self.current_to_do_task.description = str(user_message)
                    self.current_to_do_task.task_id = str(uuid.uuid1())
                    return self.task_added_successfully(username)
            case 6:
                if user_message.lower() in ("kilépés", "kilepes"):
                    return self.quit_session()
                elif ToDoHandler.to_do_list_select_check(username, user_message):
                    self.set_selected_task_id(user_message)
                    return self.jump_to_state(7, username, user_message)
                else:
                    return self.wrong_task_id(user_message)
            case 7:
                if user_message.lower() in ("kilépés", "kilepes"):
                    return self.quit_session()
                elif user_message.lower() == "completed":
                    ToDoHandler.to_do_list_task_completed(username)
                    ToDoHandler.to_do_list_remove_task_by_id(username, self.selected_task_id)
                    return self.jump_to_state(8)
                elif user_message.lower() == "failed":
                    ToDoHandler.to_do_list_task_failed(username)
                    ToDoHandler.to_do_list_remove_task_by_id(username, self.selected_task_id)
                    return self.jump_to_state(9)
                elif user_message.lower() == "remove":
                    ToDoHandler.to_do_list_remove_task_by_id(username, self.selected_task_id)
                    return self.jump_to_state(10)
