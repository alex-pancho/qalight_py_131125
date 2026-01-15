class QuestRoom:
    def __init__(self, name, difficulty, limit):
        self.name = name
        self.difficulty = difficulty
        self.limit = limit
        self.players = []
        self.status = "waiting"
        self.events_log = []

    # 1. Додати гравця
    def add_player(self, name):
        if self.is_full():
            return "No free slots!"
        self.players.append(name)
        self.events_log.append(f"Player {name} joined")

    # 2. Видалити гравця
    def remove_player(self, name):
        if name not in self.players:
            return "Player not found!"
        self.players.remove(name)
        self.events_log.append(f"Player {name} left")

    # 3. Чи заповнена кімната
    def is_full(self):
        return len(self.players) >= self.limit

    # 4. Кількість вільних місць
    def free_slots(self):
        return self.limit - len(self.players)

    # 5. Скидання кімнати
    def reset_room(self):
        self.status = "finished"
        status_1 = self.status
        self.players.clear()
        self.events_log.append("Room reset")
        self.status = "waiting"
        status_2 = self.status
        return status_1, status_2

    # 6. Список гравців
    def players_list(self):
        if not self.players:
            return "No players in the room"
        return self.players

    # 7. Старт гри
    def start(self):
        if not self.players:
            return "Room is empty!"
        self.status = "active"
        self.events_log.append("Quest started")
        return f"Квест '{self.name}' починається з {len(self.players)} гравцями!"

    # 8. Показати лог
    def show_log(self):
        return self.events_log

    # 9. Вивід інформації
    def __str__(self):
        return (
            f"Квест-кімната: {self.name} | "
            f"Рівень складності: {self.difficulty} | "
            f"Статус: {self.status} | "
            f"Гравці: {len(self.players)}/{self.limit} "
            f"({', '.join(self.players) or 'немає гравців'})"
        )
room = QuestRoom("Піратський острів", 3, 5)

if __name__ == "__main__":
    room.add_player("Олег")
    room.add_player("Даша")
    room.add_player("Назар")
    print(f"Початок. {room.start()}")
    print(room)
    print(f"Вільних місць в кімнаті - {room.free_slots()}")
    print(f"Лог подій: {room.show_log()}")
    old_status, new_status = room.reset_room()
    print("Був статус:", old_status)
    print("Став статус:", new_status)
    room.reset_room()
    print(room)
