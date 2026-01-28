"""
w (write): will open file in write mode. Each time it is called a new file is created, deleting previous text present inside it.
a (append): appends data on last inputed charcter in file
r (read): allows user to read all context of mentioned file
"""


"""
file = open("store.txt", "w")
file.write(f"{name}\n") # adds new line after this name otherwise all names will just start from last charcter
"""
def appendToFile():
    name = input("Enter Name: ")
    file = open("store.txt", "a")
    file.write(f"{name}\n")

def readFromFile():
    with open("store.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        print(line, end="")



# appendToFile()
# readFromFile()