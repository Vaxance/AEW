import random

# setting defaults
player_values = []


# //----API----

def get_int_input(out: str) -> int:
    try:
        return int(input(f"{out}\n"))
    except ValueError:
        return get_int_input(out=out)


# //------Game------
def calculate_from_list() -> list:
    results = []

    for player_index in range(player_count):
        sum = 0
        for play_set in range(play_rounds):
            sum += (player_values[play_set + player_index * play_rounds]) * play_set + 1
        results.append(sum)
    return results


def roll_the_dice() -> int:
    return random.randint(1, dice_size)


def play_round(player: int) -> None:
    roll = roll_the_dice()
    print("------------[Offene Werte]------------")
    print(player_values)
    for i in range(play_rounds):
        if player_values[(player * play_rounds) + i] == 0:
            print(f"{i + 1} ist frei")

    print(f"Du hast eine {roll} gewürfelt")

    tmp = get_int_input("Welchen Multiplikator möchtest du wählen?") - 1
    while player_values[(player * play_rounds) + tmp] != 0:
        print("Der Wert ist belegt bitte nutze einen anderen Wert!")
        tmp = get_int_input("Welchen Multiplikator möchtest du wählen?") - 1

    player_values[player * play_rounds + tmp] = roll


def game_manage() -> None:
    for round_index in range(play_rounds):
        for player_index in range(player_count):
            print(f"Runde {round_index + 1} - Player {player_index + 1}")
            play_round(player_index)
    results = calculate_from_list()
    print("------------[Ergebnisse]------------")
    for i in range(player_count):
        print(f"Player {i + 1} hat {results[i]} Punkte")

    print(f"Gewonnen hat Player {results.index(max(results)) + 1}")

    exit(0)


def setup_game() -> tuple[int, int, int]:
    dice = get_int_input("Wie groß soll der Würfel sein? (Standart = 6)")
    rounds = get_int_input("Wie viele Runden sollen gespielt werden?")
    count = get_int_input("Wie viele Spieler sollen mit spielen?")

    """
    setting up a list with deafults for all players in one list
    playervalues stays behind the other players
    calculeted by: playerindex * play_rounds + ??
    """
    for i in range(count * rounds):
        player_values.append(0)
    return dice, rounds, count


dice_size, play_rounds, player_count = setup_game()

game_manage()
