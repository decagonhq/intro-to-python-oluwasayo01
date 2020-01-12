import random
import matplotlib.pyplot as plt
from functools import reduce
import math


def roll_dice(n):
    die_1, die_2 = [random.randrange(1, 7) for _ in range(n)], [random.randrange(1, 7) for _ in range(n)]
    result = [sum(value) for value in zip(die_1, die_2)]
    dist = die_1, die_2, result
    return dist


def show_dist():
    die_1, die_2, combined = a
    # print(die_1, die_2, combined)
    x, y = [], []
    for index, value in enumerate(combined):
        x.append(index + 1)
        y.append(value)
    plt.bar(x, y)
    plt.title("Die roll distribution")
    plt.xlabel("Try")
    plt.ylabel("Sum")
    plt.show()


def filter_greater_than(value):
    return list(filter(lambda x: x > value, a[2]))

def sigmoid():
    return list(map(lambda x: round((1/(1 + math.exp(-x))), 3), a[2]))

a = roll_dice(8)
print(a)
print(filter_greater_than(7))
print(sigmoid())
show_dist()