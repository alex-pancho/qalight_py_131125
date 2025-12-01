
# single_element_tuple =  42,
single_element_tuple =  (42,)
mixed_tuple = (1, 'hello', 3.14, True )# (1, "def", False)

first = mixed_tuple[0]
last = mixed_tuple[-1]
print(first, last)
last_last = mixed_tuple[-3][1]
print("last_last", last_last)

my_tuple = (1, 2, 3, 2, 4, 2, 5)
count_of_2 = my_tuple.count(2)
print("count_of_2", count_of_2)
index_of_2 = my_tuple.index(2)
print("index_of_2", index_of_2)
index_of_2_2 = my_tuple.index(2, index_of_2 + 1)
print("index_of_2_2", index_of_2_2)
subset = my_tuple[2:5]
print(subset)
subset_2 = my_tuple[2:8:2]
print(subset_2)

one, two, thre, four = mixed_tuple
print("four vals", one, two, thre, four)

*one, two, thre = mixed_tuple
print("unpack to one", one)
print("to two", two)
print("to thre", thre)
print("=="*8)
one, *two, thre = mixed_tuple
print("to one", one)
print("unpack to two", two)
print("to thre", thre)
print("=="*8)
one, two, *thre = mixed_tuple
print("to one", one)
print("to two", two)
print("unpack to thre", thre)
print("=="*8)
one, *two = mixed_tuple
print(one, two)

my_string = "Привіт, світ!"
tuple_from_string = tuple(my_string)
print(tuple_from_string)

my_list = [1, 2, 3, 'Python', True, "привіт!"]
tuple_from_list = tuple(my_list)
print(tuple_from_list)

# list

my_list_2 = [1, 2, 3, 'a', 'b', 'c']
print(my_list_2[0])
print(my_list_2[-1])

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
subset = my_list[2:7]
print(subset)
subset_2 = my_list[2:9:2]
print(subset_2)
print(my_list[-2:])

my_list.append(4)
print(my_list)
jolm = [4, 5, 6]
my_list.append(jolm)
print(my_list)
print(len(my_list))
print("get 5:", my_list[-1][1])
my_list.append((12, 33, 445))
print(my_list[-1][1])
print(my_list)

my_list.extend(jolm)
print("extend", my_list)
my_list.extend((12, 33, 445, ("foo", "bar")))
print("extend 2", my_list)

my_list.insert(7, "fun-fun-fun")
print("insert", my_list)

my_list.remove(4)
print("remove", my_list)

popped_element = my_list.pop(10)

print("popped_element", popped_element)  
print("my_list", my_list)

index_of_4 = my_list.index(4) 
print(index_of_4)

count_of_2 = my_list.count(4)
print(count_of_2)

small =  [0, 1, 2, 3, 4]
*one, two, thre = small
print("3 vals small", one, two, thre)
one, *two, thre = small
print("3 vals small", one, two, thre)
one, two, *thre = small
print("3 vals small", one, two, thre)

numbers = [1, 2, 3, 4, 5, 7, 2, 4, 2, 0]

sorted_list = sorted(numbers)
print("sorted_list", sorted_list)
print("numbers after sorted", numbers)
print(numbers.sort())
print("numbers after sort", numbers)

fruits = ["яблуко", "апельсин", "бана", "груша", "слива"]
sorted_words = sorted(fruits, key=lambda x: len(x))
print(sorted_words)

my_string = "Привіт, світ!"
list_from_string = list(my_string)
print(list_from_string)
split_by_coma = my_string.split(", ")
print(split_by_coma)

my_tuple = (10, 20, 30, 40, 50)
list_from_tuple = list(my_tuple)
print(list_from_tuple)

# Генерацiя спискiв (List Comprehension)

squares = [x**2 for x in range(10)]
print(squares)

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

lengths_fruits = [len(word) for word in fruits]
print(lengths_fruits)

# set
my_set = set()

fruits = {"яблуко", "банан", "апельсин", "apple", "apple", "яблуко", "windows"}
print(fruits)

print("apple" in fruits)
print(1 in numbers)
print("apple" in fruits)
print(1 in numbers)

popped_element = fruits.pop()
print(f"Видалений елемент: {popped_element}, Залишок: {fruits}")
fruits.update({"apple"})
fruits.remove("apple") # може бути помилка
print(f"Множина після видалення: {fruits}")

my_set = {1, 2, 3, 4}
add_set = {3, 4, 5, 6, 7}

uni_set = my_set.union(add_set)
# або
# uni_set = my_set | add_set
print(uni_set)

# logical_intersection = my_set.intersection(add_set)
# або
logical_intersection = my_set & add_set
print(logical_intersection)

logical_difference_1 = my_set - add_set
print(logical_difference_1)
logical_difference_2 = add_set - my_set
print(logical_difference_2)

# logical_symmetric_difference = set1.symmetric_difference(set2)
# або
logical_symmetric_difference = add_set ^ my_set
print(logical_symmetric_difference)

my_text_set = set("Приклади створення множини в Python з інших типів даних за допомогою")
print(my_text_set)

f_list = ["яблуко", "банан", "апельсин", "apple", "apple"]
set_from_list = set(f_list)
print(set_from_list, len(set_from_list) == len(f_list))

# dict
en_ua = {"hello": "привіт", "good": "добре", "day": "день", "nice": "приємно", "you": "ти",}

means_1 = en_ua["good"]
print(means_1)
# str, tuple, None, frozenset, 
# int, float, bool, bytes
with_tuple_dict =  {(1, 2, 3):'значення1', 10:'значення2', "none": None, False:"my value" }
print(with_tuple_dict[(1, 2, 3)])
print(with_tuple_dict[False])

used_params = {'name': 'Василь', 'age': 25, 'city': 'Київ',} # "job":"IT spec"
user_age = used_params["age"]
print("user age", user_age)
# print(used_params["job"])
print("has 'job' key", "job" in used_params)
print("has 'age' key", "age" in used_params)
print("use get")
print("get age key", used_params.get("age"))
print("get 'job' key", used_params.get('job', "Programmer"))

for i in used_params:
    print(i)

all_keys = used_params.keys()
print(all_keys)
all_vals = used_params.values()
print(all_vals)
all_pairs = used_params.items()
print(all_pairs)

for i in used_params:
    print(i, used_params[i])

for v in used_params.values():
    print(v)

for k, v in used_params.items():
    print(k, v)

sec_dict = {"k1":"v1", "k2":"v2"}
new_dict = sec_dict.copy()
sec_dict.update({"k3": 123, "k3":37463})
print(new_dict)

sec_dict["asd"] = 123
print(sec_dict)

vals_2 = new_dict.pop('k2', 'значення за замовчуванням')
print(vals_2)
print(new_dict)

del sec_dict["k1"]
print("del k1", sec_dict)

# my_dict = {'ключ1':1, 'ключ2':2, 'ключ3':3}
# for key, value in my_dict.items():
#     print(key, value)
#     del my_dict[key]

list_tuple = [('ключ1', 'значення1'), ('ключ2', 'значення2'), ('ключ3', 'значення3')]
dict_from_tuple = dict(list_tuple)
print(dict_from_tuple)

list_lists = [['ключ1', 'значення1'], ['ключ2', 'значення2']]
dict_from_lists = dict(list_lists)
print(dict_from_lists)

some_keys = ('ключA', 'ключB', 'ключC', "a")
some_vals = ("valA", "valB", "valC", "ssd")
dict_from_pairs = dict(zip(some_keys, some_vals))
print(dict_from_pairs)

gen_dict = {x: x**2 for x in range(11) }#if x % 2 == 0
print(gen_dict)
