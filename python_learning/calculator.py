n, a, b = 0, 0, 0

def inputN():
    n = int(input("Enter N: "))

def inputAB():
    a, b = int(input("Enter A and B: "))

def main():
    square(inputN())
    add(inputAB())
    sub(inputAB())
    mul(inputAB())
    div(inputAB())

def square(n):
    return n * n

def add(a, b):
    return a + b

def sub(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

if __name__ == "__main__":
    main()