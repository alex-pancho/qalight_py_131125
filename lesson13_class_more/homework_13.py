'''🧩 Завдання: "Банківський сейф із магічними властивостями"

### Опис
Створи клас **`Safe`**, який імітує банківський сейф.
Сейф має власний пароль, може зберігати обмежену кількість предметів (наприклад, 5), і дозволяє взаємодіяти з ним через магічні методи.
### Вимоги
1. **Ініціалізація (`__init__`)**
   * Приймає пароль (`password`) і створює порожній список речей (`items`).
   * Максимальна кількість предметів у сейфі — 5.'''
class Safe:

    def __init__(self, password):
        self.password = password
        self.items = [None] * 5
        self.limit = 5
        self.is_open = False


'''2. **Представлення (`__str__` / `__repr__`)**
   * Повертає рядок типу:
     `"Safe with 3/5 items (locked)"` або `"Safe with 3/5 items (unlocked)"`.'''
def __str__(self):
    status = "unlocked" if self.is_open else "locked"
    return f'"Safe with {len(self.items)}/{self.limit} items ({status})"'


'''3. **Доступ за допомогою `__getitem__` та `__setitem__`**
   * `safe[i]` — повертає предмет із сейфу.'''
def __getitem__(self, index):
    if not self.is_open:
        return"Access Denied: Safe is locked!"
    if not(0 <= index < self.limit):
        return "Invalid slot index!"
    item = self.items[index]
    return item if item is not None else "Slot is empty!"

'''* `safe[i] = value` — додає або змінює предмет у сейфі, але тільки якщо сейф **розблоковано**.'''
def __setitem__(self, index, value):
    if not self.is_open:
        raise PermissionError("Safe is locked!")
    if not(0 <= index < self.limit):
        raise IndexError("Invalid slot index!")
    self.items[index] = value
    print(f'Item {value} placed in slot {index}!')


'''4. **Використання `__len__`**
   * `len(safe)` повертає кількість предметів у сейфі.'''
def __len__(self):
    return sum(1 for item in self.items if item is not None)


'''5. **Використання `__contains__`**
   * Перевірка, чи є предмет у сейфі:
     `"gold" in safe`'''
def __contains__(self, item):
    if not self.is_open:
        print("Access Denied: Safe is locked!")
        return False
    return item in self.items


'''6. **Відкриття сейфа**
   * Метод `unlock(password)`:
     * Якщо пароль правильний — сейф відкривається.
     * Якщо ні — підняти `ValueError("Wrong password")`.'''
def unlock(self, password):
    if self.is_open:
        return "Safe is already unlocked!"
    if password == self.password:
            self.is_open = True
            return "Safe is unlocked successfully!"
    else:
        raise ValueError("Wrong password!")
    

'''7. **Закриття сейфа**
   * Метод `lock()` блокує сейф.'''
def lock(self):
    if not self.is_open:
        return "Safe is already locked!"
    self.is_open = False
    return "Safe is locked successfully!"


'''8. **Використати `try-except`**
   * Приклад роботи коду має ловити помилки:
     * неправильний пароль'''
my_safe = Safe("12345")    
try:
    result = my_safe.unlock("54321")
    print(result)
except ValueError as e:
    print(f'Wrong password. An error has occurred: {e}')


'''* спробу додати елемент, коли сейф закрито
     '''   
my_safe = Safe("12345")
try:
    my_safe[0] = "$500"
except PermissionError as e:
    print(f'Cannot add an item if the safe is closed. An error has occurred: {e}')


'''* спробу додати більше ніж 5 предметів'''
my_safe = Safe("12345")
my_safe.unlock("12345")
try:
    my_safe[5] = "$500"
except IndexError as e:
    print(f'It is not possible to add more than 5 items to the safe. An error has occurred: {e}')
    

'''### 💡 Ідеї для розширення:
* Додати метод `__delitem__`, щоб видаляти предмети.'''
def __delitem__(self, index):
    if not self.is_open:
        raise PermissionError("Safe is locked!")
    if not(0 <= index < self.limit):
        raise IndexError("Invalid slot index!")
    removed_item = self.items[index]
    self.items[index] = None
    if removed_item:
        print(f'Item {removed_item} was removed from slot {index}!')
    else:
        print(f'Slot {index} was already empty.')


'''* Реалізувати автоматичне блокування після 3 невдалих спроб входу.'''
# додаємо в def __init__() нові змінні:
    def __init__(self, password):
        self.password = password
        self.items = [None] * 5
        self.limit = 5
        self.is_open = False
        self.count_wrong_password = 0
        self.is_blocked = False
# переписуємо def unlock () для реалізації автоматичного блокування:
    def unlock(self, password):
        if self.is_blocked:
            return "Safe is blocked. Too many attempts with wrong password. "
        if self.is_open:
            return "Safe is already unlocked!"
        if password == self.password:
            self.is_open = True
            self.count_wrong_password = 0
            return "Safe is unlocked successfully!"
        else:
            self.count_wrong_password += 1
            if self.count_wrong_password >= 3:
                self.is_blocked = True
                raise ValueError(f"Safe is blocked. Too many attempts with wrong password. Attempt {self.count_wrong_password}/3")
            raise ValueError("Wrong password!")
