import os
import json
import random

import getpass
import hashlib

#  erstellen eines Speicherortes für Variablen, ohne diese fest zu definiren
import secrets
import string

data = {}

#  abspeichern des Dateipfades, wo sich die main.py befindet
path = os.getcwd()


def change_voc_new() -> None:
    """
    Funktion, that shows up the dialog for the creation of a new set, as well as the creation of the set
    :return: None
    """
    category_input = "_"
    name_input = "_"

    #  Nutzereingabe, welche ohne '_' sein muss. Dies könnte später wichtig werden
    while "_" in category_input or "_" in name_input:
        category_input = input("In welche Kategorie soll das Set eingefügt werden?\n")
        name_input = input("Wie soll das Set heißen?\n")

    #  erstellen des Dateinamens aus den Nutzereingaben z.B. en_unit1.json
    file_name = f"{category_input}_{name_input}.json"

    #  überpfüfen, ob dieses Set shon existirt. Genauer gesagt wird geschaut, ob die Datei schon vorhanden ist.
    if os.path.isfile(f"{path}/data/{data['user_id']}/voc/{file_name}"):
        print("Leider existirt dieses Set schon!")
    else:
        #  erstellen der Daten, welche Abgespeichert werden sollen
        data_set = {
            "vocs": {

            },
            "stats": {
                "all_time_lerned": 0,
                "all_time_right": 0
            }
        }

        #  erstellen der Datei für das Set
        with open(f"{path}/data/{data['user_id']}/voc/{file_name}", "w") as file:
            #  abspeichern der Daten in der Datei
            json.dump(data_set, file)
        print("Das Set wurde angelegt!")

    set_site("change_voc_menu")


def change_voc_remove() -> None:
    """
    Funktion, that's shows up the dialog for removing a set, as well as the removing prosses
    :return: None
    """
    #  mit einer comprehension wird hier eine Liste aller Datein in dem Vokabelordner der Person erstellt
    sets = [file for file in os.listdir(f"{path}/data/{data['user_id']}/voc/")]

    #  die erstellte Liste wird ausgegeben
    for i, set_name in enumerate(sets):
        print(f"{i + 1} -> {set_name.replace('.json', '')}")

    #  der Nutzer wird gefragt, welches Set er löschen möchte.
    #  Ebenfalls wird überprüft, ob diese Setnummer überhaubt möglich ist
    set_nummer = 0

    while set_nummer > len(sets) or set_nummer <= 0:
        set_nummer = int(input("Welche Setnummer soll gelöscht werden?\n"))

    #  auslesen des Dateinamens, anhand der eingegebenen Nummer
    file_name = f"{sets[set_nummer - 1]}"

    #  Überprüfung, ob das Set existirt(Ist nicht wirklich notwendig, habe es aber aus Sicherheitsgründen gemacht)
    if os.path.isfile(f"{path}/data/{data['user_id']}/voc/{file_name}"):
        #  entfernen des Sets
        os.remove(f"{path}/data/{data['user_id']}/voc/{file_name}")
        print("Das Set wurde gelöscht!")
    else:
        print("Das Set ist nicht zu finden")

    set_site("change_voc_menu")


def change_voc_edit() -> None:
    """
    Dialog to Select, which set is to edit
    :return: None
    """
    #  mit einer comprehension wird hier eine Liste aller Datein in dem Vokabelordner der Person erstellt
    sets = [file for file in os.listdir(f"{path}/data/{data['user_id']}/voc/")]

    #  die erstellte Liste wird ausgegeben
    for i, set_name in enumerate(sets):
        print(f"{i + 1} -> {set_name.replace('.json', '')}")

    set_nummer = 0

    #  der Nutzer wird gefragt, welches Set er löschen möchte.
    #  Ebenfalls wird überprüft, ob diese Setnummer überhaubt möglich ist
    while set_nummer > len(sets) or set_nummer <= 0:
        set_nummer = int(input("Welche Setnummer soll bearbeitet werden?\n"))

    #  abspeichern des ausgewählten Sets
    data["set_for_edit"] = f"{sets[set_nummer - 1]}"
    print("Das Set wurde erfolgreich ausgewählt!")

    set_site("change_voc_edit_set")


def change_voc_edit_set() -> None:
    """
    Dialog, that shows up every vocabulary in a set. The set must be set in data under 'set_for_edit'
    :return: None
    """
    #  öffnet die Datei und liest die Daten aus
    with open(f"{path}/data/{data['user_id']}/voc/{data['set_for_edit']}", "r") as file:
        set_data = json.load(file)

    print("0 -> Vokabel hinzufügen\n"
          "Vokabelnummer -> Vokabel - Übersetzung")

    #  erstellt eine eigene Liste für die Vokabeln des Sets
    vocs = [voc for voc in set_data["vocs"]]

    #  nutzt die erstellte Liste zur Ausgabe der Vokabeln
    for i, voc_key in enumerate(vocs):
        print(f"{i + 1} -> {voc_key} - {set_data['vocs'][voc_key]}")

    print(f"{len(set_data['vocs']) + 1} -> Zurück\n")

    #  Nutzereigabe mit überprüfung, ob die Eingabe gültig ist.
    voc_numer = -1

    while voc_numer > len(set_data["vocs"]) + 1 or voc_numer < 0:
        voc_numer = int(input("Welche Vokabel soll gelöscht werden oder welche Aktion soll ausgeführt werden?\n"))

    #  nutzen der Nutzereingabe, um zu entscheiden, was gemacht werden soll
    if voc_numer == 0:
        set_site("change_voc_edit_set_add")
    elif voc_numer == len(set_data["vocs"]) + 1:
        set_site("change_voc_menu")
    else:
        #  löschen der angegebenen Vokabel in der Variable im Programm
        del set_data["vocs"][vocs[voc_numer - 1]]
        #  öffnen der Datei und überschreiebn der Daten aus der Datei mit der Variable im Programm
        with open(f"{path}/data/{data['user_id']}/voc/{data['set_for_edit']}", "w") as file:
            json.dump(set_data, file, indent=4)
        print("Die Vokabel wurde erfolgreich gelöscht!")


def change_voc_edit_set_add() -> None:
    """
    Dialog to add a new Vocabulary to the selected set. Requires 'set_for_edit' in the data dict.
    :return: None
    """
    #  öffnen der Datei und auslesen der Daten
    with open(f"{path}/data/{data['user_id']}/voc/{data['set_for_edit']}", "r") as file:
        set_data = json.load(file)

    #  Nutzereingabe, für die neue Vokabel
    voc = input("Welche Vokabel möchtest du hinzufügen?\n")
    translation = input("Wie lautet die Übersetzung?\n")

    #  hinzufügen der neuen Vokabel in der Variable
    set_data["vocs"][voc] = translation

    #  überschreiben der Datei mit neuen Werten
    with open(f"{path}/data/{data['user_id']}/voc/{data['set_for_edit']}", "w") as file:
        json.dump(set_data, file, indent=4)

    set_site("change_voc_edit_set")


def change_voc_menu() -> None:
    """
    Shows the Menu for the 'Vokabeln bearbeiten' tab
    :return: None
    """
    converter = {1: "main", 2: "change_voc_new", 3: "change_voc_remove", 4: "change_voc_edit"}
    user_input = int(input("Was möchtest du machen?\n"
                           "1 -> Menü\n"
                           "2 -> Set hinzufügen\n"
                           "3 -> Set entfernen\n"
                           "4 -> Set bearbeiten\n"))

    set_site(converter[user_input])


def train_voc_menu() -> None:
    """
    Dialog, that manages the training of the vocabulary fully.
    :return: None
    """
    #  auslesen aller zur Verfügung stehenden Sets
    sets = [file for file in os.listdir(f"{path}/data/{data['user_id']}/voc/")]
    for i, set_name in enumerate(sets):
        print(f"{i + 1} -> {set_name.replace('.json', '')}")

    #  Nutzereigabe mit Überprüfung
    set_number = 0

    while set_number > len(sets) or set_number <= 0:
        set_number = int(input("Welches Set möchtest du trainieren?\n"))

    #  auslesen des gewollten Sets
    with open(f"{path}/data/{data['user_id']}/voc/{sets[set_number - 1]}", "r") as file:
        set_data = json.load(file)

    #  abspeichern des dicts, welches die Vokabeln beinhaltet
    #  {"apple": "apfel", "hello": "hallo"}
    vocs = set_data["vocs"]

    all_time_lerned = set_data['stats']['all_time_lerned']
    all_time_right = set_data['stats']['all_time_right']
    #  Training des Sets bis zur eingabe von '1'
    user_input = ""
    print("Um das Training zu beenden gebe 1 ein")
    while user_input != "1":

        keys = list(vocs.keys())
        voc = random.choice(keys)
        print("Übersetze " + voc)
        user_input = input("")
        if user_input == "1":
            break

        if user_input == vocs[voc]:
            print("Richtig")
            all_time_right += 1
        else:
            print("Falsch")

        all_time_lerned += 1

    set_data['stats']['all_time_lerned'] = all_time_lerned
    set_data['stats']['all_time_right'] = all_time_right

    #  überschreiben der Datei mit neuen Werten
    with open(f"{path}/data/{data['user_id']}/voc/{sets[set_number - 1]}", "w") as file:
        json.dump(set_data, file, indent=4)
    set_site("main")


def stats_menu() -> None:
    """
    Dialog, that shows the statistics of the set's
    :return: None
    """
    sets = [file for file in os.listdir(f"{path}/data/{data['user_id']}/voc/")]

    #  die erstellte Liste wird ausgegeben
    for i, set_name in enumerate(sets):
        print(f"{i + 1} -> {set_name.replace('.json', '')}")

    #  der Nutzer wird gefragt, welches Set er löschen möchte.
    #  Ebenfalls wird überprüft, ob diese Setnummer überhaubt möglich ist
    set_nummer = 0

    while set_nummer > len(sets) or set_nummer <= 0:
        set_nummer = int(input("Welche Setnummer soll gelöscht werden?\n"))

    #  auslesen des Dateinamens, anhand der eingegebenen Nummer
    file_name = f"{sets[set_nummer - 1]}"

    #  Überprüfung, ob das Set existirt(Ist nicht wirklich notwendig, habe es aber aus Sicherheitsgründen gemacht)
    if os.path.isfile(f"{path}/data/{data['user_id']}/voc/{file_name}"):
        with open(f"{path}/data/{data['user_id']}/voc/{file_name}", "r") as file:
            set_data = json.load(file)

        stats = set_data['stats']

        print("Du hast folgende Statistiken für das Set!")
        print("Gelernte Vokabeln: " + str(stats['all_time_lerned']))
        print("Davon richtig: " + str(stats['all_time_right']))

    set_site("main")


def menu() -> None:
    """
    The start page dialog
    :return: None
    """
    converter = {1: "change_voc_menu", 2: "train_voc_menu", 3: "statistic", 4: "logout"}
    user_input = int(input("Was möchtest du machen?\n"
                           "1 -> Vokabeln bearbeiten\n"
                           "2 -> Vokabeln trainieren\n"
                           "3 -> Statistiken anzeigen\n"
                           "4 -> Logout\n"))

    set_site(converter[user_input])


def login_login_func():
    user_name = input("Nutzername: ")
    password = getpass.getpass(prompt='Password: ', stream=None)

    with open(f"{path}/data/user.json", "r") as file:
        user_datas = json.load(file)

    if user_name in user_datas:
        hash_save = hashlib.new("whirlpool")
        hash_save.update(password.encode())

        if hash_save.hexdigest() == user_datas[user_name]["user_password_hashed"]:
            print("Login erfolgreich")


            data['user_id'] = user_datas[user_name]['user_id']
            data['user_set'] = user_datas[user_name]

            set_site("main")
            return

    print("Anmeldedaten ungültig")


def login_register_func():
    user_name = input("Nutzername: ")
    password = ""
    password_two = "_"
    while password != password_two:
        password = getpass.getpass(prompt='Password: ')
        password_two = getpass.getpass(prompt='Password bestätigen: ')
        if password != password_two:
            print("Leider sind die Passwörter nicht passend!")

    checked_uuid = False

    while not checked_uuid:
        uuid = ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(7))
        uuids = [file for file in os.listdir(f"{path}/data/") if os.path.isdir(f"{path}/data/{file}")]
        checked_uuid = not uuid in uuids

    with open(f"{path}/data/user.json", "r") as file:
        user_datas = json.load(file)

    if user_name in user_datas:
        print("Der Benutzername existrt bereits!")
        return

    name = input("Ganzer Name: ")

    hash_save = hashlib.new("whirlpool")
    hash_save.update(password.encode())

    user_data = {
        "name": name,
        "user_id": uuid,
        "user_password_hashed": hash_save.hexdigest()
    }

    user_datas[user_name] = user_data

    with open(f"{path}/data/user.json", "w") as file:
        json.dump(user_datas, file, indent=4)

    os.makedirs(f"{path}/data/{uuid}/voc/")

    print("Dein Nutzer wurde erstellt bitte melde dich an!")

def login():
    translater = {
        1: login_login_func,
        2: login_register_func
    }
    print("1 -> Login")
    print("2 -> Register")

    user_select = int(input("Welche Aktion soll asgeführt werden?"))

    translater[user_select]()


def logout():
    global data
    data = {}
    print("Sie wurden erfolgreich abgemeldet.")
    set_site("login")


site = "login"
sites = {"login": login,
         "logout": logout,
         "main": menu,
         "change_voc_menu": change_voc_menu,
         "train_voc_menu": train_voc_menu,
         "statistic": stats_menu,
         "change_voc_new": change_voc_new,
         "change_voc_remove": change_voc_remove,
         "change_voc_edit": change_voc_edit,
         "change_voc_edit_set": change_voc_edit_set,
         "change_voc_edit_set_add": change_voc_edit_set_add}


def set_site(site_name) -> None:
    """
    Funktion to set the site, that will be shown in the next call of 'call_site()'
    :param site_name: string of the site
    :return: None
    """
    global site
    site = site_name


def call_site() -> None:
    """
    Calls the site by the saved str 'site'. To do so the funktion uses the 'sites' dict.
    :return:
    """
    sites[site]()



while True:
    try:
        if "user_set" in data:
            print(f"---------------[Vokabeltrainer - {data['user_set']['name']}]---------------")
        else:
            print(f"---------------[Vokabeltrainer]---------------")
        call_site()
    except KeyboardInterrupt as key_error:
        exit(1)
    except:
        print("Es ist ein Fehler aufgetreten, bitte versuche es erneut!")

