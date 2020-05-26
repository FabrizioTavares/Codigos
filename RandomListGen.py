import random


def generate(size, intmin, intmax):
    randomlist = []
    for i in range(size):
        randomlist.append(random.randint(intmin, intmax))

    return randomlist
