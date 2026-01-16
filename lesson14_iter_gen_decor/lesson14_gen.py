
def simple_generator():
    # setup
    yield 1
    # teardown
    yield 2
    yield 3

gen = simple_generator()
print(next(gen))

def my_generator(n):
    # Ініціалізуємо лічильник
    value = 1
    # Цикл виконується доти, доки лічильник не стане менше n
    while value <= n:
        # Повертаємо поточне значення лічильника
        yield value
        # Збільшуємо лічильник
        value += 1

for value in my_generator(7):
    # Виводимо кожне значення, отримане від генератора
    print(value)

generator = my_generator(3)
print(next(generator))  # 1
print(next(generator))  # 2
print(next(generator))  # 3
print(*generator)

numbers = [1, 2, 3, 4, 5]
iterator = map(lambda x: x * 2, numbers)
print(iterator)
print(next(iterator))

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
iterator = zip(names, ages)

print(next(iterator))