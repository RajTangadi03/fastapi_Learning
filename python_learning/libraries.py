def main():
    print("Helloooooooooooo!")

# modules

# random library : gives random output
cards = [1, 2, 3]

"""

from random import choice, randint, shuffle

print(choice(['Head', 'Tail']))
print(randint(1, 10))


shuffle(cards)
for i in cards:
    print(i)

"""

"""

import statistics

print(statistics.mean(cards))

"""

####################################################################
############################ IMPORTANT #############################
####################################################################

import sys

# sys.argv means after entering in terminal:
# python3 ......
# all those ..... are argv

"""
Example:
python3 libraries.py hello_world "kay bolti public!"
Output--> 
libraries.py
hello_world
kay bolti public!
"""

# for i in sys.argv:
#     print(i)

# print(sys.argv[1])


# if len(sys.argv) > 4:
#     print(sys.argv[2:4])
#     print(sys.argv[2:])
#     print(sys.argv[::2])


###################################################################
############################ PACKAGES #############################
###################################################################

# cowsay

import cowsay

# cowsay.cow('Pankajjjjjjjjjjjjjjjjjjj!!!!!!!!!!!!!!')
# cowsay.trex('Pankajjjjjjjjjjjjjjjjjjj!!!!!!!!!!!!!!')

def cow(ip):
    names = ['beavis', 'cheese', 'cow', 'daemon', 'dragon', 'fox', 'ghostbusters', 'kitty', 'meow', 'miki', 'milk', 'octopus', 'pig', 'stegosaurus', 'stimpy', 'trex', 'turkey', 'turtle', 'tux']
    for name in names:
        # getattr is used to merge custom request of name used in loop with api to call all functions provided by API
        cowsay_func = getattr(cowsay, name)
        cowsay_func(ip)



"""
Why this is used? --> When we export this file, the content from this file
gets read by calling file line by line. Then if from terminal it checks, which 
file called main function, if it is this files then and only then it is get called
otherwise not.
"""

if __name__ == "__main__":
    main()