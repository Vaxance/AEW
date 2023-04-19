#  declaration that this script is runnable
if __name__ == '__main__':
    for i in range(3):
        user_input = int(input("Gebe eine Zahl zur Überprüfung ein?"))

        #  check if the value is in the right format
        if (user_input < 1) or (user_input > 50):
            print("Die geprüfte Zahl ist kleiner als 1 oder größer als 50!")
        else:
            print("Die Zahl wurde mit erfolg geprüft")
