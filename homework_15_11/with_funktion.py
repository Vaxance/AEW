#  ask the user for one input and cast the input to an int
#  if it's not an int, the funktion ask agan
#  ------------
#  returns int -> input of the user
def __get_userinput():
    try:
        return int(input("Gebe eine Zahl zur Überprüfung ein?"))
    except ValueError:
        print("Bitte gebe eine Zahl ein!")
        return __get_userinput()


#  check if the value is bigger 1
#  or smaller 50
#  ------------
#  params:
#   - input(int) -> the int to check
#  returns bool -> the state of the format
def __check_userinput(input=int):
    return (input < 1) or (input > 50)


#  send the results from the check state
#  ------------
#  params:
#   - check_state(bool) -> the bool to send the error
#  returns None
def __send_userresult(check_state=bool):
    print("Die geprüfte Zahl ist kleiner als 1 oder größer als 50!") if check_state else print(
        "Die Zahl wurde mit erfolg geprüft")


#  declaration that this script is runnable
if __name__ == '__main__':
    for i in range(3):
        __send_userresult(__check_userinput(__get_userinput()))
