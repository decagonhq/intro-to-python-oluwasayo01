import random
import matplotlib.pyplot as plt
from functools import reduce


def roll_die(n):
    die_1, die_2 = [random.randrange(1, 7) for _ in range(n)], [random.randrange(1, 7) for _ in range(n)]
    result = [sum(value) for value in zip(die_1, die_2)]
    dist = die_1, die_2, result
    return dist


# ans = reduce(lambda x, y: x + y, [1, 2, 6, 7, 4, 7, 9, 0, 6, 1, 4])
# die = roll_die()


def show_dist(val, n):
    die_1, die_2, combined = val(n)
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


def filter_greater_than(number):
    return list(filter(lambda x: x > number, ))


print(roll_die(4))
show_dist(roll_die, 4)
