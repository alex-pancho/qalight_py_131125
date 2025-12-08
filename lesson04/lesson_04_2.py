first_example = "Любіть Україну всім серцем своїм"

first_char = first_example[0]
six_char = first_example[5]

last_char = first_example[-1]
print("Це вивід для результатів зрізів:", first_char, six_char, last_char)

substring = first_example[4:12]
print("Its sub:", substring)

substring_2 = first_example[4:22:2]
print("Its sub 2:", substring_2)

substring_3_before = first_example[:7]
print("Its BEFORE 7:", substring_3_before)

substring_4_after = first_example[7:]
print("Its AFTER 7:", substring_4_after)

substring_3_before_min = first_example[:-7]
print("Its BEFORE -7:", substring_3_before_min)

substring_4_after_min = first_example[-7:]
print("Its AFTER -7:", substring_4_after_min)

my_len = len(first_example)
print("first_example len", my_len) 

for char in first_example:
    print(char)

string_sum = "Tolya" + "Olya"
print(string_sum)

string_mul = "*" * 88
print(string_mul)

j_string = ' і ще раз '.join(("гол", "гол", "НЕПОВЕЗЛО", "гол", "гол"))
print(j_string)

splitted_str = first_example.split()
print(splitted_str)

text = "роздільник,мобільнік,купальник"
splitted_text = text.split(",")
print(splitted_text)

new_url = "https://www.youtube.com"
print("http", new_url.startswith("http"))
print("ftp", new_url.startswith("ftp"))

print("end http", new_url.endswith("http"))
print("end com", new_url.endswith("com"))

print("all text >", new_url.startswith("https://www.youtube.com"))
print("all text <", new_url.endswith("https://www.youtube.com"))

all_up = "HELP ME !"
print(all_up.isupper())
no_all_up = "HELP Me if !"
print(no_all_up.isupper())
im_small = "it is first day of the"
print("small", im_small.islower())
title_me = "Mr. John Smith"
print("title", title_me.istitle())

now_you_big = im_small.upper()
print("big", now_you_big)

now_you_big = now_you_big.lower()
print("lower", now_you_big)

capital = now_you_big.capitalize()
print("capital", capital)

titled = now_you_big.title()
print("titled", titled)

for_search = "Це приклад для пошуку у рядку"
index = for_search.find("пошук")
print("пошук", "index", index)

index_2 = for_search.find("Євген")
print("Євген", "index", index_2)

long_text = "Якщо слово не знайдено, виведеться повідомлення про те, що підстрічку не знайдено"

index_3 = long_text.find("знайдено")
print(index_3)
start = index_3 + 1
index_4 = long_text.find("знайдено", start)
print(index_4)

index_5 = long_text[start:].find("знайдено")
print(index_5)

print("знайдено", long_text.count("знайдено"))
print("з", long_text.count("з"))

chars_repl = "Це приклад для заміни у рядку"
new_chars = chars_repl.replace("заміни", "підміни")
print(new_chars)

new_chars_1 = chars_repl.replace("д", "d")
print(new_chars_1)

new_chars_2 = chars_repl.replace("д", "d", 2)
print(new_chars_2)

some_str = "    Привіт, світ!    "
cleaned_str = some_str.strip()
print(f"Оригінальний рядок:|{some_str}|")
print(f"Очищений рядок:|{cleaned_str}|")

cleaned_str_1 = some_str.lstrip()
print(f"Очищений L рядок:|{cleaned_str_1}|")

cleaned_str_2 = some_str.rstrip()
print(f"Очищений R рядок:|{cleaned_str_2}|")

some_str = ",zzzz    Привіт, світ!    zzzz!!"
print(f"Оригінальний рядок:|{some_str}|")
cleaned_str_4 = some_str.strip("!,z ")#.strip()
print(f"Очищений рядок:|{cleaned_str_4}|")

str_list = ["apple", "orange", "banana"]
joined_strs = ', '.join(str_list)

print("Об'єднані рядки:", joined_strs)

# value = input("Данні:")
num_1 = "12345"
let_num = int(num_1)
print(let_num, type(let_num))

num_2 = "123.99"
let_num_2 = float(num_2)
print(let_num_2, type(let_num_2))
let_num_3 = int(let_num_2)
print(let_num_3, type(let_num_3))

num_chars = "1,2,3,4,5"
num_list = num_chars.split(",")
print(num_list)

# False
"", '', """""",

string = "False"
bool_var = bool(string)
print(bool_var)

pi = 3.14159265359
print("Pi:", f"Значення числа: {pi:.2f}")
