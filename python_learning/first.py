"""
This is introduction block, where i learned how to take input
and output it; Also used functions and passed variables.
"""
def sayHello(name):
    print(f"Hello {name}!")

# name = int(input("Enter Name: "))
# sayHello(name)

###################################################################

"""
# Table printer
for j in range(10):
    for i in range(10,20):
        print((i+1)*(j+1),"|", end="\t")
    print("\n")
"""

###################################################################

# int and float

a = 9999
b = 1
c = a + b
# print(c, "VS", f"{c:,}")
# f"{c:,}" This here is used for putting any character in between numbers. Like here used ","

d = 19.8
e = 12.2
f = d / e
# print(f, "VS", round(f, 2), "VS", f"{f:.2f}")
# round(f, 2) used to round output till mentioned spaces. Here till 2 digits.
# f"{f:.2f}" used to round output till mentioned spaces. Here till 2 digits.

###################################################################

# String functions
# person = input("Person: ")
# person = person.strip().title()
# print(person)
# lst = person.split()

# for i in range(len(lst)):
    # print(lst[i], end=" | ")

###################################################################