"""
# Using modulo % operator to check if there is any remainder after dividing

a = 10
b = 3
c = a / b
d = a % b
# print("Resultant:", round(c, 2), "Remainder", d)

if d != 0:
    print("Not Divisible!")
else:
    print("Divisible!")

"""

# Pythonic Expressions (Makes multiline code into a single compressed manner expression like this)
def isOdd(n):
    return n % 2 != 0

# match (just like switch case in c++)
name = input("Nav taka: ")
match name:
    case "Harry":
        print("Harri Pootarrrr!")
    case "Hermione":
        print("Harmonium Ginger")
    case "Ron":
        print("Ronya Patil")
    case _:
        print("Kon hay hya chracter!!!!")
