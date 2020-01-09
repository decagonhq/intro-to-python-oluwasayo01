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

def asterisk(*args, **kwargs):
    return "Positional arguments: {}\nKeyword arguments: {}".format(args, kwargs)

print(asterisk(2, 3, 4, 6, size=(2, 5), name="Oluwasayo", stack="Python"))
