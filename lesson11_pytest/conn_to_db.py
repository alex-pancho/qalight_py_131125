def flatten(lst: list):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))  # рекурсія
        else:
            result.append(item)
    return result

def check_age(age:int):
    if age < 0:
        raise ValueError("Too small age")
    elif age >= 150:
        raise ValueError("Too big age")
    return age

# list_of_lists = [1, [2, [3, 4]], 5, [[[["a"]], "b"]]]
# # expected = [1, 2, 3, 4,...]
# out_flat = flatten(list_of_lists)
# print(out_flat)