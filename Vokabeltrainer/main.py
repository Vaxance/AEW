import os
import json
import random

#  erstellen eines Speicherortes für Variablen, ohne diese fest zu definiren
data = {}

if "user_id" not in data:
    data['user_id'] = "jsdjaf"

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
            json.dump(set_data, file)
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
        json.dump(set_data, file)

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

    #  Training des Sets bis zur eingabe von '1'
    user_input = ""
    print("Um das Training zu beenden gebe 1 ein")
    while user_input != "1":

        keys = list(vocs.keys())
        voc = random.choice(keys)
        print("Übersetze " + voc)
        user_input = input("")
        if user_input == vocs[voc]:
            print("Richtig")
        else:
            print("Falsch")

    set_site("main")


def stats_menu() -> None:
    """
    Dialog, that shows the statistics of the set's
    :return: None
    """
    print("Funktion leider nicht verfügbar")
    set_site("main")


def menu() -> None:
    """
    The start page dialog
    :return: None
    """
    converter = {1: "change_voc_menu", 2: "train_voc_menu", 3: "statistic"}
    user_input = int(input("Was möchtest du machen?\n"
                           "1 -> Vokabeln bearbeiten\n"
                           "2 -> Vokabeln trainieren\n"
                           "3 -> Statistiken anzeigen\n"))

    set_site(converter[user_input])


site = "main"
sites = {"main": menu,
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
    call_site()
