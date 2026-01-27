"""

# Loops
for i in range(5):
    print("Ha", end="")

print()

for i in range(5,10):
    print(i, end="")

print()

"""

# printing multiple similar output using only print statement
# print("Hello\t"*3, end="! ")

"""

# While loop
while True:
    num = int(input("Enter Positive Number: "))
    if num >= 0:
        break

"""

"""

# dictionary
students = {"A":"a", "B":"b", "C":"c", "D":"d"}
for i in students:
    print(i, students[i], sep=" : ")

"""

# Printing a width * height brick
i = int(input(""))
j = int(input(""))

for _ in range(i):
    for _ in range(j):
        print("#", end=" ")
    print()