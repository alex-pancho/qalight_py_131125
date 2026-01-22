class Safe:
    max_items = 5

    def __init__(self, password):
        self._password = password
        self._items = []
        self._locked = True

    def __str__(self):
        status = "locked" if self._locked else "unlocked"
        return f"Safe with {len(self._items)}/{self.max_items} items ({status})"

    __repr__ = __str__

    def unlock(self, password):
        if password != self._password:
            raise ValueError("Wrong password")
        self._locked = False

    def lock(self):
        self._locked = True

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        if self._locked:
            raise PermissionError("Safe is locked")

        if index >= self.max_items:
            raise IndexError("Safe capacity exceeded")

        if index < len(self._items):
            self._items[index] = value
        else:
            if len(self._items) >= self.max_items:
                raise OverflowError("Safe is full")

            while len(self._items) < index:
                self._items.append(None)
            self._items.append(value)

    def __len__(self):
        return len(self._items)

    def __contains__(self, item):
        return item in self._items

# Приклад використання
# python
safe = Safe("1234")

try:
    safe.unlock("1111")  # невірний пароль
except ValueError as e:
    print(e)

safe.unlock("1234")
safe[0] = "gold"
safe[1] = "documents"

print(safe)
print("gold" in safe)
print(len(safe))

try:
    for i in range(5):
        safe[i] = f"item_{i}"
except Exception as e:
    print("Error:", e)

safe.lock()
try:
    safe[0] = "diamonds"
except Exception as e:
    print("Error:", e)
