# unpacking

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

name = "Monkey D. Luffy (King of The Pirates)!"

first, *_ = name.split(" ") # anything with * infront of it will store the rest of the output
# print(first, _)

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


# print(total(100, 50, 25), "Knuts")


################################################################################
################################# args VS kwargs ###############################
################################################################################

"""
args are positional arguments, such as those we provide to print like print("Hello", "World")
kwargs are named arguments, or “keyword arguments”, such as those we provide to print like print(end="")
"""


def f(*args, **kwargs):
    print("Positional:", args)


# f(100, 50, 25)

def f(*args, **kwargs):
    print("Named:", args)


# f(galleons=100, sickles=50, knuts=25)

################################################################################

"""
def main():
    yell("This is CS50")


def yell(word):
    print(word.upper())


if __name__ == "__main__":
    main()
"""
"""
def main():
    yell(["This", "is", "CS50"])


def yell(words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)


if __name__ == "__main__":
    main()
"""


"""
emails = ["a@gmail.com", "b@yahoo.com", "c@gmail.com"]

gmail_users = list(filter(lambda e: "gmail" in e, emails))
print(gmail_users)

# map: transform each element
print(list(map(lambda x: x * 2, nums)))

# reduce: combine elements (needs functools)
from functools import reduce
print(reduce(lambda a, b: a + b, nums))
"""

def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    flock = []
    for i in range(n):
        flock.append("🐑" * i)
    return flock


if __name__ == "__main__":
    main()
