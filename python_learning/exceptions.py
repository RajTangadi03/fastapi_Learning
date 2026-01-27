# Exceptions

"""

try:
    print("Hello")
    c = int(input())
except ValueError:
    print("How you can input anything in int data type :)")

"""

# pass keyword

while True:
    try:
        print("Hello")
        c = int(input())
    except ValueError:
        pass
    else:
        break
