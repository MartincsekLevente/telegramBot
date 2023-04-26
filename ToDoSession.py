from ToDoHandler import ToDoHandler
from ToDoTask import ToDoTask
import uuid


class ToDoSession:

    def __init__(self):
        self.state = 0
        self.currentToDoTask = ToDoTask()
        self.selectedTaskID = ''

    def get_state(self):
        return self.state

    def start_add_new_task(self):
        self.currentToDoTask = ToDoTask()

    def set_state(self, state):
        self.state = state

    def set_selected_task_id(self, task_id):
        self.selectedTaskID = task_id

    def start_session(self):
        self.state = 1
        return "Üdvözöllek a ToDo opciónál! Válassz a megadott opciók közül: \n\n" \
               "Hozzáadás - Addj hozzá a ToDo listádhoz egy feladatot! \n\n" \
               "Kiválasztás - Válassz ki egy feladatot a saját ToDo listádról! \n\n" \
               "Megjelenítés -  Megjelenítem neked az összes ToDo feladatot a listádról! \n\n" \
               "Teljesítmény - Megjelenítem neked az eddig elért eredményeidet a teljesített feladataid alapján! \n"

    def jump_to_state(self, to_jump, info1='', info2=''):
        self.state = to_jump
        match to_jump:
            case 0:
                return 'Szia! Miben tudok segíteni? A parancsok megtekintéséhez használd a /help funkciót!'
            case 1:
                return self.start_session()
            case 2:
                return 'A [Hozzáadás] funkciót választottad. \n\n' \
                       'Ahhoz, hogy hozzáadj egy elemet a ToDo listádhoz, csak írd be kívánt ToDo feladatod nevét! '
            case 3:
                return 'Az általad választott név a következő: ' + info1 + '\n\n' \
                                                                          'Most add meg kérlek milyen dátummal legyen határidős az általad választott ToDo feladat.\n' \
                                                                          'A dátumot így add meg: Év/Hónap/Nap \nPl: 2023/04/24'
            case 4:
                return 'Az általad választott dátum a következő: ' + info1 + '\n\n' \
                                                                            'Most add meg kérlek milyen leírás tartozzon általad választott ToDO feladathoz!\n'
            case 5:
                self.state = 1
                return 'A [Megjelenítés] funkciót választottad. \n' \
                       'Íme az összes eddig hozzáadott ToDo Taskod:\n\n' \
                       + ToDoHandler.to_do_list_show_all(info1) + \
                       '\nTovábbi funkciókért használd a /help parancsot!'
            case 6:
                return 'A [Kiválasztás] funkciót választottad. \n\n' \
                       'Ahhoz, hogy teljesítetté vagy törölté tegyél egy elemet a ToDo listádból,' \
                       ' csak írd be kívánt ToDo feladatod referencia ID-jét! Ezek az álatlad felvett' \
                       ' ToDo feladatok:\n\n' \
                       + ToDoHandler.to_do_list_show_all(info1)
            case 7:
                return 'Az általad beírt referencia ID (' + info2 + ') alapján ezt a feladatot választottad ki:\n\n' \
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
        return 'A megadott ToDo feladat referencia ID (' + task_id + ') hibás!\n' \
               'Add meg helyesen az ID-t. Ha nincsen meg ez az ID,' \
               ' akkor visszalépve ' \
               'a show all parancsot használva megtudod találni.'

    def quit_session(self):
        self.state = 0
        return "Kilépés sikeres! Miben tudok még segíteni? " \
               "A parancsok megtekintéséhez használd a /help funkciót!"

    def task_added_successfully(self, username):
        self.state = 1
        ToDoHandler.to_do_list_add(username, self.currentToDoTask)
        return "A ToDo feladat hozzáadása sikeres!\n\nItt a ToDo feladatod részletes leírása:\n" \
               "Cím: " + self.currentToDoTask.title + "\n" \
                                                      "Dátum: " + self.currentToDoTask.date + "\n" \
                                                                                              "Leírás: " + self.currentToDoTask.description + "\n\n" \
                                                                                                                                              "További parancsok megtekintéséhez használd a /help funkciót!"

    def reply(self, user_message, username):
        match self.state:
            # case 0: casual conversation
            case 0:
                if user_message.lower() in ("hello", "szia"):
                    return "Szia! Miben tudok segíteni? \nA parancsok megtekintéséhez használd a /help funkciót!"
                elif user_message.lower() in ("idő", "ido?", "mennyi az ido", "mennyi az idő?"):
                    return "A jelenlegi pontos idő: "+ToDoHandler.get_time()
                elif user_message.lower() in "todo":
                    return self.start_session()
                else:
                    return ToDoHandler.not_clear_text(username)
            # case 1: add, delete, show all commands root
            case 1:
                if user_message.lower() in ("quit", "exit"):
                    return self.quit_session()
                elif (user_message.lower() == "hozzáadás") or (user_message.lower() == "hozzaadas"):
                    self.start_add_new_task()
                    self.currentToDoTask.username = username
                    return self.jump_to_state(2)
                elif (user_message.lower() == "megjelenítés") or (user_message.lower() == "megjelenites"):
                    return self.jump_to_state(5, username)
                elif (user_message.lower() == "kiválasztás") or (user_message.lower() == "kivalasztas"):
                    return self.jump_to_state(6, username)
                elif (user_message.lower() == "teljesítmény") or (user_message.lower() == "teljesitmeny"):
                    return self.jump_to_state(11, username)
                else:
                    return ToDoHandler.not_clear_text(username)
            # case 2: add title
            case 2:
                if user_message.lower() in ("quit", "exit"):
                    return self.quit_session()
                else:
                    self.currentToDoTask.title = str(user_message)
                    return self.jump_to_state(3, user_message)
            # case 3: add date
            case 3:
                if user_message.lower() in ("quit", "exit"):
                    return self.quit_session()
                else:
                    self.currentToDoTask.date = str(user_message)
                    return self.jump_to_state(4, user_message)
            # case 4: add description
            case 4:
                if user_message.lower() in ("quit", "exit"):
                    return self.quit_session()
                else:
                    self.currentToDoTask.description = str(user_message)
                    self.currentToDoTask.task_id = str(uuid.uuid1())
                    return self.task_added_successfully(username)
            case 6:
                if user_message.lower() in ("quit", "exit"):
                    return self.quit_session()
                elif ToDoHandler.to_do_list_select_check(username, user_message):
                    self.set_selected_task_id(user_message)
                    return self.jump_to_state(7, username, user_message)
                else:
                    return self.wrong_task_id(user_message)
            case 7:
                if user_message.lower() in ("quit", "exit"):
                    return self.quit_session()
                elif user_message.lower() == "completed":
                    ToDoHandler.to_do_list_task_completed(username)
                    ToDoHandler.to_do_list_remove_task_by_id(username, self.selectedTaskID)
                    return self.jump_to_state(8)
                elif user_message.lower() == "failed":
                    ToDoHandler.to_do_list_task_failed(username)
                    ToDoHandler.to_do_list_remove_task_by_id(username, self.selectedTaskID)
                    return self.jump_to_state(9)
                elif user_message.lower() == "remove":
                    ToDoHandler.to_do_list_remove_task_by_id(username, self.selectedTaskID)
                    return self.jump_to_state(10)

