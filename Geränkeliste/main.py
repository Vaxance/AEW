drink_list = {}


def add_drink_to_dict() -> None:
    # global drink_list
    drink = input("Welches Getränk möchtest du hinzufügen?\n")
    if drink in drink_list:
        print("Das Getränk ist bereits erstellt.")
        return

    drink_list[drink] = {}
    print("Das Getränk wurde gespeichert!")


def add_person() -> None:
    drink = input("Für welches Geränk soll eine Person hinzugefügt werden?\n")

    if not drink in drink_list:
        print("Das Getränk ist nicht gespeichert!")
        return

    person = input("Wie soll die Person gespeichert werden?\n")

    drink_list[drink][person] = 0
    print("Die Person wurde hinzugefügt!")


def add_drink_menu():
    drinks = [drink_d for drink_d in drink_list]

    for i, drink in enumerate(drinks):
        print(f"{i + 1} -> {drink}")

    drink_input = -1
    while drink_input <= 0 or drink_input < len(drinks):
        drink_input = int(input("Welches Getränk möchtest du buchen?\n"))

    add_drink_person(drinks[drink_input - 1])


def add_drink_person(drink: str):
    try:
        while True:
            person = input(f"Welche Person hat ein {drink} gebucht?\n")

            if not person in drink_list[drink]:
                if input("Diese Person ist nicht hinterlegt. Soll sie erstellt werden? [y/n] - ") == "y":
                    drink_list[drink][person] = 1
                else:
                    print("Verstanden, Sie werden zurückgeleitet!")
            else:
                drink_list[drink][person] += 1
                print("Das Getränk wurde gebucht.")
    except KeyboardInterrupt:
        print("Verstanden!")


def get_list():
    for drink in drink_list:
        print(f"--------------[{drink}]--------------")
        for person in drink_list[drink]:
            print(f"{person} - {drink_list[drink][person]}")


def menu():
    translator = {1: add_drink_to_dict, 2: add_person, 3: add_drink_menu, 4: get_list}
    num = int(input("Was möchten Sie machen?\n"
                    "1 -> Getränk hinzugügen\n"
                    "2 -> Person hinzufügen\n"
                    "3 -> Getränke eintragen\n"
                    "4 -> Liste ausgeben\n"))

    if num in translator:
        translator[num]()
    else:
        print("Leide gibt es die Funktion nicht.")


while True:
    print("---------------------------------")
    menu()
    print("---------------------------------")
