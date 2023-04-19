import secrets
import string
from tkinter import *

alphabet = string.ascii_letters + string.digits + string.punctuation


def generate_pw(laenge):
    return ''.join(secrets.choice(alphabet) for i in range(laenge))
    if not (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)):
        return generate_pw()


def get_entry():
    try:
        if int(textLine.get()) < 8:
            set_output("Das Passwort ist zu kurz")
        elif int(textLine.get()) > 90:
            set_output("Das Passwort ist zu lang")
        else:
            return int(textLine.get())
    except ValueError:
        set_output("Die Eingabe muss eine Ganzezahl sein")


def set_output(text):
    output.config(state="normal")
    output.delete(0, END)
    output.insert(END, text)
    output.config(state="readonly")


def push_gen_button():
    entry = get_entry()
    if isinstance(entry, int):
        set_output(generate_pw(entry))


if __name__ == '__main__':

    window = Tk()
    window.geometry("750x150")
    window.title("Passwortgenerator")

    Label(window, text="Passwortgenerator", font=("arial", 25)).place(x=0, y=0)

    for i in range(0, 3):
        Label(window, text="").grid(row=i, column=0)

    Label(window, text="Länge: ").grid(row=7, column=0)
    Label(window, text="Passwort: ").grid(row=8, column=0)

    textLine = Entry(window, width=100)
    textLine.grid(row=7, column=1)

    output = Entry(window, width=100)
    output.config(state="readonly")
    output.grid(row=8, column=1)

    button = Button(window, text="Generate", command=push_gen_button)
    button.grid(row=9, column=0)

    window.mainloop()
