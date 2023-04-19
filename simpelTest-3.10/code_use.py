"""
Setzt die Stringlänge auf 10
# ist das um was ergänzt wird
< setzt das ganze nach den strin
> setzt das ganze vor den String
^ teilt die länge auf
"""
tmp_string = "test"
tmp_string_two = "test"
print(f"{tmp_string:#^10}")

"""
macht große zahlen lesbar
setzt alle drei zahlen ein komma
nut int, float wird gerunded
"""
tmp_digit = 1374867578932543.908834
print(f"{tmp_digit:,}")

"""
gibt alles das gleiche aus
"""
print(tmp_string, tmp_string_two)
print(f"{tmp_string} {tmp_string_two}")
print("%s %s" % (tmp_string, tmp_string_two))
print("{} {}".format(tmp_string, tmp_string_two))

"""
open a file simple
"""
with open("test.json") as file:
    print(file.read())

"""
shot if statments
== False ist wichtig hier!!!
"""
x = "yes" if bool("False") == False else "no"
print(x)

"""
einfache wege für zahlen und zeichen inhalte
.isdigit nur für int nicht für float
"""
print("1.6".isnumeric())