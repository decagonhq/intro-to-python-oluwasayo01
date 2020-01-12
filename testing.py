data = [2, 2, 3, 3, 4, 5, 11, 13, 15]
result = {}
for key in data:
    result[key] = result.get(key) + 1 if result.get(key) != None else 1
mode_value = max(result.values())
modes = tuple(value for value in result if result.get(value) == mode_value)
print(modes)