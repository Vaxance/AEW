def change_voc_new():
    category_input = input("In welche Kategorie soll das Set eingefügt werden?\n")
    name_input = input("Wie soll das Set heißen?\n")

    set_site("change_voc_menu")
    call_site()


def change_voc_remove():
    #  Sets anzeigen
    category_input = input("Aus welche Kategorie soll das Set entfernt werden?\n")
    name_input = input("Wie heißt das Set?\n")

    set_site("change_voc_menu")
    call_site()


def change_voc_edit():
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
         "change_voc_edit": change_voc_edit}


def call_site():
    sites[site]()


call_site()
