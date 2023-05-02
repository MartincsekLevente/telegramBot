from datetime import datetime
import json


class ToDoHandler:

    @staticmethod
    def get_time():
        """
           Ez a függvény visszaadja az aktuális időt.

           Returns:
                datetime: Az aktuális idő.
        """
        return datetime.now().strftime("%d/%m/%y, %H:%M:%S")

    @staticmethod
    def not_clear_text(username):
        """
           Ez a függvény visszaadja azt az opciót, hogyha a beírt szöveg nem felismerhető

           Args:
               username: Az aktuális beszélgető partner felhasználóneve
        """
        return "Bocsi, " + username + ", nem ismerem fel ezt a parancsot. " \
                                      "Használd a /help funkciót ha elakadnál.\n" \
                                      "Amennyiben szeretnél belépni a ToDo Hub-ba, " \
                                      "akkor írd be azt, hogy todo"

    @staticmethod
    def to_do_list_add(username, current_to_do_task):
        """
           Ez a függvény hozzáad egy feladatot a felhasználó listájához

           Args:
               username: Az aktuális beszélgető partner felhasználóneve
               current_to_do_task: A feladat, amit hozzá kell adni a listához

           Raises:
               FileNotFoundError: Ha a fájl nem található
               json.JSONDecodeError: Ha nem sikerül dekódolni a json fájlt
        """
        try:
            with open("ToDoData.json", "r", encoding="utf-8") as json_file:
                todo_data = json.load(json_file)

            task_dict = {
                "id": current_to_do_task.task_id,
                "username": current_to_do_task.username,
                "title": current_to_do_task.title,
                "date": current_to_do_task.date,
                "description": current_to_do_task.description
            }

            if username in todo_data:
                todo_data[username].append(task_dict)
            else:
                todo_data[username] = [task_dict]

            with open("ToDoData.json", "w", encoding="utf-8") as json_file:
                json.dump(todo_data, json_file)

                print("New ToDo task added: username: {}, task_id: {}, title: {}, "
                      "date: {}, description: {}".format(
                    username,
                    current_to_do_task.task_id,
                    current_to_do_task.title,
                    current_to_do_task.date,
                    current_to_do_task.description))
        except FileNotFoundError:
            print("A ToDoData.json fájl nem található.")
        except json.JSONDecodeError:
            print("Hiba történt a JSON fájl dekódolása közben.")

    @staticmethod
    def to_do_list_show_all(username):
        """
           Ez a függvény megjeleníti az összes adott felhasználónévhez tartozó feldatot

           Args:
               username: Az aktuális beszélgető partner felhasználóneve

           Raises:
               FileNotFoundError: Ha a fájl nem található
               json.JSONDecodeError: Ha nem sikerül dekódolni a json fájlt
        """
        try:
            with open('ToDoData.json', 'r', encoding="utf-8") as json_file:
                todo_data = json.load(json_file)
                if username in todo_data:
                    tasks = todo_data[username]
                    result = ""
                    for task in tasks:
                        result += f"Cím:  {task['title']}\n"
                        result += f"Teljesítési dátum:  {task['date']}\n"
                        result += f"Feladat leírása:  {task['description']}\n"
                        result += f"Feladat kiválasztásához tartozó " \
                                  f"referencia ID:  {task['id']}\n\n"
                    return result
                else:
                    return "Nincsenek felvett ToDo feladatok" + username + " felhasználóhoz."

        except FileNotFoundError:
            print("A ToDoData.json fájl nem található.")
        except json.JSONDecodeError:
            print("Hiba történt a JSON fájl dekódolása közben.")

    @staticmethod
    def to_do_list_select_check(username, task_id):
        """
           Ez a függvény megnézi, hogy a paraméterben beadott feladat id kiválasztható-e

           Args:
               username: Az aktuális beszélgető partner felhasználóneve
               task_id: Az aktuális paraméterben megadott feladat id-je

           Raises:
               FileNotFoundError: Ha a fájl nem található
               json.JSONDecodeError: Ha nem sikerül dekódolni a json fájlt
        """
        try:
            with open('ToDoData.json', 'r', encoding="utf-8") as json_file:
                todo_data = json.load(json_file)
            tasks = todo_data[username]
            for task in tasks:
                if task['id'] == task_id:
                    return True
            return False
        except FileNotFoundError:
            print("A ToDoData.json fájl nem található.")
        except json.JSONDecodeError:
            print("Hiba történt a JSON fájl dekódolása közben.")

    @staticmethod
    def to_do_list_select_task_by_id(username, task_id):
        """
           Ez a függvény elvégzi a paraméterben beadott feladat id alapján a kiválasztást

           Args:
               username: Az aktuális beszélgető partner felhasználóneve
               task_id: Az aktuális paraméterben megadott feladat id-je

           Raises:
               FileNotFoundError: Ha a fájl nem található
               json.JSONDecodeError: Ha nem sikerül dekódolni a json fájlt
        """
        try:
            with open('ToDoData.json', 'r', encoding="utf-8") as json_file:
                todo_data = json.load(json_file)
            tasks = todo_data[username]
            for task in tasks:
                if task['id'] == task_id:
                    result = ""
                    result += f"Cím:  {task['title']}\n"
                    result += f"Teljesítési dátum:  {task['date']}\n"
                    result += f"Feladat leírása:  {task['description']}\n\n"
                    return result
            return "Nem található rögzített feladatod a megadott referencia ID alapján!"
        except FileNotFoundError:
            print("A ToDoData.json fájl nem található.")
        except json.JSONDecodeError:
            print("Hiba történt a JSON fájl dekódolása közben.")

    @staticmethod
    def to_do_list_remove_task_by_id(username, task_id):
        """
           Ez a függvény elvégzi a paraméterben beadott feladat id alapján a feladat törlését

           Args:
               username: Az aktuális beszélgető partner felhasználóneve
               task_id: Az aktuális paraméterben megadott feladat id-je

           Raises:
               FileNotFoundError: Ha a fájl nem található
               json.JSONDecodeError: Ha nem sikerül dekódolni a json fájlt
        """
        try:
            with open('ToDoData.json', 'r', encoding="utf-8") as json_file:
                todo_data = json.load(json_file)
                tasks = todo_data[username]
                for task in tasks:
                    if task['id'] == task_id:
                        tasks.remove(task)
                todo_data[username] = tasks
            with open("ToDoData.json", "w", encoding="utf-8") as json_file:
                json.dump(todo_data, json_file)
        except FileNotFoundError:
            print("A ToDoData.json fájl nem található.")
        except json.JSONDecodeError:
            print("Hiba történt a JSON fájl dekódolása közben.")

    @staticmethod
    def to_do_list_task_completed(username):
        """
           Ez a függvény elvégzi a paraméterben megadott
           felhasználónév alapján a teljesítettnek jelölést

           Args:
               username: Az aktuális beszélgető partner felhasználóneve

           Raises:
               FileNotFoundError: Ha a fájl nem található
               json.JSONDecodeError: Ha nem sikerül dekódolni a json fájlt
        """
        try:
            with open("ToDoStat.json", "r", encoding="utf-8") as json_file:
                todo_stat = json.load(json_file)
            if username in todo_stat:
                if 'completed_tasks' in todo_stat[username]:
                    todo_stat[username]['completed_tasks'] += 1
                else:
                    todo_stat[username]['completed_tasks'] = 1
            else:
                todo_stat[username] = {'completed_tasks': 1}
            with open("ToDoStat.json", "w", encoding="utf-8") as json_file:
                json.dump(todo_stat, json_file)
        except FileNotFoundError:
            print("A ToDoStat.json fájl nem található.")
        except json.JSONDecodeError:
            print("Hiba történt a JSON fájl dekódolása közben.")

    @staticmethod
    def to_do_list_task_failed(username):
        """
           Ez a függvény elvégzi a paraméterben megadott felhasználónév
            alapján a teljesítettlennek jelölést

           Args:
               username: Az aktuális beszélgető partner felhasználóneve

           Raises:
               FileNotFoundError: Ha a fájl nem található
               json.JSONDecodeError: Ha nem sikerül dekódolni a json fájlt
        """
        try:
            with open("ToDoStat.json", "r", encoding="utf-8") as json_file:
                todo_stat = json.load(json_file)
            if username in todo_stat:
                if 'failed_tasks' in todo_stat[username]:
                    todo_stat[username]['failed_tasks'] += 1
                else:
                    todo_stat[username]['failed_tasks'] = 1
            else:
                todo_stat[username] = {'failed_tasks': 1}
            with open("ToDoStat.json", "w", encoding="utf-8") as json_file:
                json.dump(todo_stat, json_file)
        except FileNotFoundError:
            print("A ToDoStat.json fájl nem található.")
        except json.JSONDecodeError:
            print("Hiba történt a JSON fájl dekódolása közben.")

    @staticmethod
    def to_do_list_show_performance(username):
        """
           Ez a függvény elvégzi a paraméterben megadott felhasználónév
           alapján a statisztika kiszámolását és kiiratását

           Args:
               username: Az aktuális beszélgető partner felhasználóneve

           Raises:
               FileNotFoundError: Ha a fájl nem található
               json.JSONDecodeError: Ha nem sikerül dekódolni a json fájlt
        """
        try:
            with open('ToDoStat.json', 'r', encoding="utf-8") as json_file:
                todo_stat = json.load(json_file)
                if username in todo_stat:
                    result = ""
                    if 'completed_tasks' in todo_stat[username]:
                        result += f"Sikeresen elvégzett feladatok száma: {todo_stat[username]['completed_tasks']}\n"
                    else:
                        result += "Sikeresen elvégzett feladatok száma: 0\n"

                    if 'failed_tasks' in todo_stat[username]:
                        result += f"Sikertelenül elvégzett feladatok száma: {todo_stat[username]['failed_tasks']}\n"
                    else:
                        result += "Sikertelenül elvégzett feladatok száma: 0\n"

                    if 'failed_tasks' in todo_stat[username] and 'completed_tasks' in todo_stat[username]:
                        completed_num = int(todo_stat[username]['completed_tasks'])
                        failed_num = int(todo_stat[username]['failed_tasks'])
                        total_num = completed_num + failed_num
                        rate = round(((completed_num / total_num) * 100), 2)
                        result += f"Az általad elvégzett feladatok sikerességi aránya: {rate}%\n"
                    return result
                else:
                    return "Nincsenek teljesített ToDo feladatok" + username + " felhasználóhoz," \
                                                                               " így nem tudok eredményeket" \
                                                                               " megjeleníteni!"
        except FileNotFoundError:
            print("A ToDoStat.json fájl nem található.")
        except json.JSONDecodeError:
            print("Hiba történt a JSON fájl dekódolása közben.")
