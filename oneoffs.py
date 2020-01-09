def divide(num_1, num_2, floor=True):
    try:
        if floor:
            result = num_1//num_2
        else:
            result = num_1/num_2
        return result
    except TypeError:
        raise TypeError

print(divide(2, 5, False))
