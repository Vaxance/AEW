import random

# sys.setrecursionlimit(4000)

players = []


def get_str_input(out_put: str) -> str:
    """
    gets an Input and cast it to a String
    :param out_put: the Text, that the User see
    :type out_put: String
    :return: the Input of the User
    :rtype String
    """
    try:
        return str(input(f"{out_put}\n"))
    except ValueError:
        print("Your Input was not a Text")
        return get_str_input(out_put)


def get_int_input(out_put: str) -> int:
    """
    gets an Input and cast it to an Integer
    :param out_put: the Text, that the User see
    :type out_put: String
    :return: the Input of the User
    :rtype Integer
    """
    try:
        return int(input(f"{out_put}\n"))
    except ValueError:
        print("Your Input was not a Integer")
        return get_int_input(out_put)


def get_bool_input(out_put: str, true_condition: list[str]) -> bool:
    """
    gets an Input and compares it to a List
    :param out_put: the Text, that the User see
    :type out_put: String
    :param true_condition: the List to compare with
    :type true_condition: list[str]
    :return: the Input of the User, compared to the List
    :rtype Boolean
    """
    try:
        return True if str(input(f"{out_put}\n")) in true_condition else False
    except ValueError:
        return get_bool_input(out_put, true_condition)


def print_spacer() -> None:
    print("-----------------------[Böse 6]-----------------------")


def roll_the_dice() -> tuple[bool, int]:
    """
    Simulates the rolling of a die
    :return: whether the player is allowed to continue playing and the number on the dice
    :rtype: tuple[bool, int]
    """
    roll = random.randint(1, 6)
    return True if roll != 6 else False, roll


def play_players_round(player_dict: dict) -> dict:
    """
    the counts the number of the dice and checks if a player is allowed or wants to player further
    :param player_dict: the information about the player
    :type player_dict: dict
    :return: the updated information about the player
    :rtype: dict
    """
    playing = True
    while playing:
        playing, roll = roll_the_dice()
        print(player_dict["name"] + " hat eine " + str(roll) + " gewürfelt")
        if playing:
            player_dict["round_points"] = player_dict["round_points"] + roll
            print("Punkte insgesamt: " + str(player_dict["game_points"]) + " | Punkte diese Runde: " + str(
                player_dict["round_points"]))
            playing = get_bool_input("Willst du weiter Spielen? (j/N)", ["j", "J", "Ja", "ja"])
            if not playing:
                player_dict["game_points"] = player_dict["game_points"] + player_dict["round_points"]
        else:
            print("Die Runde ist vorbei, der Spieler hat eine 6 gewürfelt")

    player_dict["round_points"] = 0
    return player_dict


def play_game_round() -> None:
    """
    Loops trow every player and calls the method to play their rounds.
    It also ends the game
    :return: None
    """
    for index, player in enumerate(players):
        player = play_players_round(player)
        players[index] = player
        if player["game_points"] >= 50:
            print(player["name"] + " hat das Spiel gewonnen")
            quit(0)
    play_game_round()


def setup_game() -> None:
    """
    Asks for the Player count and sets the Dictionary's  up
    :return: None
    """
    print_spacer()
    player_cout = get_int_input("Wie viele Spieler sollen mit Spielen?")
    for player_number in range(1, player_cout + 1):
        players.append({"name": f"Player {player_number}", "game_points": 0, "round_points": 0})
    play_game_round()


setup_game()
