import os
import json

data = {}

if "user_id" not in data:
    data['user_id'] = "jsdjaf"

path = os.getcwd()

print(data['user_id'])

def change_voc_new():
    category_input = "_"
    name_input = "_"

    while "_" in category_input or "_" in name_input:
        category_input = input("In welche Kategorie soll das Set eingefügt werden?\n")
        name_input = input("Wie soll das Set heißen?\n")

    file_name = f"{category_input}_{name_input}.json"

    if os.path.isfile(f"{path}/data/{data['user_id']}/voc/{file_name}"):
        print("Leider existirt dieses Set schon!")
    else:
        data_set = {
                  "vocs": {

                  },
                  "stats": {
                    "all_time_lerned": 0,
                    "all_time_right": 0
                  }
                }

        with open(f"{path}/data/{data['user_id']}/voc/{file_name}", "w") as file:
            json.dump(data_set, file)
        print("Das Set wurde angelegt!")


    set_site("change_voc_menu")
    call_site()


def change_voc_remove():
    sets = [file for file in os.listdir(f"{path}/data/{data['user_id']}/voc/")]
    for i, set_name in enumerate(sets):
        print(f"{i + 1} -> {set_name.replace('.json', '')}")

    set_nummer = 0

    while set_nummer > len(sets) or set_nummer <= 0:
        set_nummer = int(input("Welche Setnummer soll gelöscht werden?\n"))

    file_name = f"{sets[set_nummer - 1]}"

    if os.path.isfile(f"{path}/data/{data['user_id']}/voc/{file_name}"):
        os.remove(f"{path}/data/{data['user_id']}/voc/{file_name}")
        print("Das Set wurde gelöscht!")
    else:
        print("Das Set ist nicht zu finden")


    set_site("change_voc_menu")
    call_site()


def change_voc_edit():
    sets = [file for file in os.listdir(f"{path}/data/{data['user_id']}/voc/")]
    for i, set_name in enumerate(sets):
        print(f"{i + 1} -> {set_name.replace('.json', '')}")

    set_nummer = 0

    while set_nummer > len(sets) or set_nummer <= 0:
        set_nummer = int(input("Welche Setnummer soll bearbeitet werden?\n"))

    data["set_for_edit"] = f"{sets[set_nummer - 1]}"

    print("Das Set wurde erfolgreich ausgewählt!")

    set_site("change_voc_edit_set")
    call_site()

def change_voc_edit_set():
    with open(f"{path}/data/{data['user_id']}/voc/{data['set_for_edit']}", "r") as file:
        set_data = json.load(file)

    print("0 -> Vokabel hinzufügen\n"
          "Vokabelnummer -> Vokabel - Übersetzung")

    vocs = [voc for voc in set_data["vocs"]]

    for i, voc_key in enumerate(vocs):
        print(f"{i + 1} -> {voc_key} - {set_data['vocs'][voc_key]}")

    print(f"{len(set_data['vocs']) + 1} -> Zurück\n")

    voc_numer = -1

    while voc_numer > len(set_data["vocs"]) + 1 or voc_numer < 0:
        voc_numer = int(input("Welche Vokabel soll gelöscht werden oder welche Aktion soll ausgeführt werden?\n"))

    if voc_numer == 0:
        set_site("change_voc_edit_set_add")
        call_site()
    if voc_numer == len(set_data["vocs"]) + 1:
        set_site("change_voc_menu")
        call_site()
    else:
        print(set_data["vocs"])
        print(vocs[voc_numer - 1])
        del set_data["vocs"][vocs[voc_numer - 1]]
        print(set_data["vocs"])
        with open(f"{path}/data/{data['user_id']}/voc/{data['set_for_edit']}", "w") as file:
            json.dump(set_data, file)
        print("Die Vokabel wurde erfolgreich gelöscht!")
        call_site()

def change_voc_edit_set_add():
    pass

def change_voc_menu():
    converter = {1: "main", 2: "change_voc_new", 3: "change_voc_remove", 4: "change_voc_edit"}
    user_input = int(input("Was möchtest du machen?\n"
                           "1 -> Menü\n"
                           "2 -> Set hinzufügen\n"
                           "3 -> Set entfernen\n"
                           "4 -> Set bearbeiten\n"))

    set_site(converter[user_input])
    call_site()


def train_voc_menu():
    user_input = int(input("Was möchtest du lernen?"))

    call_site()


def stats_menu():
    set_site("main")
    call_site()


def set_site(site_name):
    global site
    site = site_name


def menu():
    converter = {1: "change_voc_menu", 2: "train_voc_menu", 3: "statistic"}
    user_input = int(input("Was möchtest du machen?\n"
                  "1 -> Vokabeln bearbeiten\n"
                  "2 -> Vokabeln trainieren\n"
                  "3 -> Statistiken anzeigen\n"))
    
    set_site(converter[user_input])
    call_site()


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


def call_site():
    sites[site]()


call_site()