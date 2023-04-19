text = input("Ihr Text: ")
key = int(input("Ihr Schlüssel (1-25)"))

result = ""

text = text.lower()

for i in range(len(text)):
    char = text[i]
    char_id = ord(char)
    new_char_id = char_id + key
    if new_char_id > 122:
        new_char_id = 97 + (new_char_id - 122) % 26
    new_char = chr(new_char_id)
    result += new_char

print(f"Der verschlüsselte Text lautet: {result}")