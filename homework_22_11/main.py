def mathematischeFunktion(formula, min_value, max_value, steps):
    """
    Returns all points of the given function that are in the given range.
    --------------
    :param formula: the function on which the points are
    :type str
    :param min_value: the lower limit of the value range (as x coordinate)
    :type int
    :param max_value: the upper limit of the value range (as x coordinate)
    :type int
    :param steps: describes the distance between the steps
    :type float
    :raises ValueError, MemoryError
    """
    x = min_value
    while x != (max_value + 1):
        print("P(", x, "|", eval(formula), ")")
        x += steps

def get_int_input(message):
    """
    gets an input and trays to cast it in an int.
    if it's not cast able it will ask another time
    :param message: that will be shown in the console
    :type str
    :return: the input value
    :rtype int
    """
    try:
        return int(input(message + " (Als Ganzzahl)\n"))
    except ValueError:
        return get_int_input(message)


def get_float_input(message):
    """
    gets an input and trays to cast it in a float.
    if it's not cast able it will ask another time
    :param message: that will be shown in the console
    :type str
    :return: the input value
    :rtype float
    """
    try:
        return float(input(message + " (Als Kommazahl)\n"))
    except ValueError:
        return get_int_input(message)


if __name__ == '__main__':

    formula = input(
        "Bitte gebe die Formel an. Nutze bitte alle Malzeichen, sowie für Hochzahlen mit ** an.Bitte nutze nur die 'x' Variable\n")
    # formula = "(-1/24) * x ** 4 + (2/9) * x ** 3 + (7/12) * x ** 2 - (5/3) * x + 5"
    min_value = get_int_input("Bitte gebe den niedrigsten Wert der Wertetabelle ein.")
    max_value = get_int_input("Bitte gebe den höchten Wert der Wertetabelle ein.")
    steps = get_float_input("Bitte gebe die Schritte an.")

    mathematischeFunktion(formula, min_value, max_value, steps)
