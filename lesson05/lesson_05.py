
if True:
    print("Я відбуваюся")

age = 33

if age >= 18:
    print("Ти повнолітній!")
else:
    print("В інших випадках")


if age < 18:
    print("Ти дитина.")
elif age >= 18 and age < 25:
    print("Ти молодь.")
else:
    print("Ти дорослий.")

age = 17
is_student = True
has_experience = False

if age >= 18 and is_student:
    print("Ти студент і тобі більше 18 років.")
elif (age >= 25 and has_experience) or (is_student and not has_experience):
    print("дві умови")    
elif has_experience or is_student:
    print("Ти студент АБО з досвідом роботи")
else:
    print("Ти не можеш бути студентом або тобі менше 18 років.")


count = 0
while count < 5:
    print(count)
    count += 1

word = "Python"
index = 0
while index < len(word):
    print(word[index])
    index += 1

# while True:
#     print(index)
#     index += 1

for num in word:
    print(num)

message = "Hello"
for char in message:
    print(char)

age = 25
is_student = True

if age >= 18:
    print("You are an adult.")

    if is_student:
        print("And you are a student.")

        # Вкладений цикл
        for semester in range(1, 4):
            print("Semester:", semester)
    else:
        print("But you are not a student.")
else:
    print("You are not an adult.")

for i in range(6):
    print("Outer loop, iteration:", i)

    # Вкладена умова
    if i % 2:
        print(f"{i} не ділиться на 2")
    else:
        print(f"{i} парне")

my_line = "aaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaa"
i = 0
for char in my_line:
    if char == "b":
        print("Break викликаний на i =", i)
        break
    i += 1
    print(char)

my_line_1 = "aabaaabaaaaaacaaaabaaaaaaabaaaaaaaaaaaaad"

counter_a = 0
for char in my_line_1:
    if char != "a":
        continue
    counter_a += 1

print(f"Total a: {counter_a} ==", my_line_1.count("a"))

customer = 0
target_value = 7
for i in range(10):
    if i == target_value:
        print("Знайдено шукане значення:", i)
        break
    else:
        customer = customer + i
    print(customer)

print("Це кінець")
