from enum import Enum

class Gender(Enum):
    MANN = ["mann", "m"]
    FRAU = ["frau", "f"]

if __name__ == '__main__':
    gen = input("gender")

    print(gen in Gender.MANN.value)
