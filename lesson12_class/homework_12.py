class QuestRoom:
    '''
    Завдання 1.
    1.1. Створюємо конструктор, який приймає: назву, рівень складності, ліміт гравців
    2.6. Додатковий стан кімнати, "waiting" — до старту
    2.7. Лог подій (історія). Додати поле **events_log** (список рядків)
    '''
    def __init__(self, room, level, limit):
        self.room = room
        self.level = level
        self.limit = limit
        self.current_players = []
        self.status = "waiting"    
        self.events_log = []
    
    '''
    1.2. Створюємо метод add_player(name), який додає гравця до кімнати. 
    Якщо місць немає — повертає повідомлення `"No free slots!"`
    2.7. При додаванні гравця записувати `"Player <name> joined"`
    '''
    def add_player(self, player_name):
        if len(self.current_players) < self.limit:
            self.current_players.append(player_name)
            self.events_log.append(f'Player {player_name} joined.')
            return f'Player {player_name} was added to {self.room}!'
        else:
            return f'No free slots!'

    '''
    1.3. Створюємо метод start(), який якщо кімната пуста повертає `"Room is empty!"` 
    Інакше повертає `"Quest '<назва>' started with <кількість гравців> players!"`
    2.6. Додатковий стан кімнати, стан переводиться у "active".
    2.7. При старті лог подій — `"Quest started"`
    '''
    def start(self):
        if len(self.current_players) == 0:
            return f'Room is empty!'
        else:
            self.status = "active"
            self.events_log.append(f'Quest started.')
            return f"Quest '{self.room}' started with {len(self.current_players)} players!"
                    
    '''
    1.4. Створюємо Метод **__str__**()** для красивого виводу:
    QuestRoom: <name> | Difficulty: <level> | Players: <players_count>/<limit>   
    '''    
    def __str__(self):
        return f"QuestRoom: {self.room} | Difficulty: {self.level} з 5 | Players: {len(self.current_players)}/{self.limit}"

    '''
    Завдання 2.
    2.1. Створюємо метод `remove_player(name)`, який видаляє гравця зі списку.
    Якщо такого гравця немає — повертає повідомлення `"Player not found!"`.
    2.7. При видаленні гравця лог подій — `"Player <name> left"`
    '''
    def remove_player(self, player_name):
        if player_name in self.current_players:
            self.current_players.remove(player_name)
            self.events_log.append(f'Player {player_name} left.')
            return f'Player {player_name} removed.'
        else:
            return f'Player not found!'
        
    '''
    2.2. Метод `is_full(), який повертає True, якщо кімната заповнена.
    Інакше — False.
    '''
    def is_full(self):
        return len(self.current_players) >= self.limit
        
    '''
    2.3. Метод `free_slots()`, який повертає кількість вільних місць у кімнаті.
    '''
    def free_slots(self):
        return (self.limit - len(self.current_players))
    
    '''
    2.4. Метод `reset_room()`, який очищає список гравців, ніби почали нову гру.
    Повертає повідомлення `"Room reset!"`.
    2.6. Метод reset_room(): змінює стан на "finished" → очищає гравців → ставить `"waiting"`.
    2.7. При рестарті лог подій — `"Room reset"`
    '''
    def reset_room(self):
        self.status = "finished"
        self.events_log.append(f'Status - finished')    # додано цей лог для перевірки статусу в тесті 6. Скидання кімнати (`reset_room`)
        self.current_players.clear()
        self.events_log.append(f'Room reset.')
        self.status = "waiting"
        return f"Room reset!"
    
    '''
    2.5. Метод `players_list()`, який повертає список імен гравців.
    Якщо список порожній — `"No players in the room"`.
    '''
    def players_list(self):
        if not self.current_players:
            return f'No players in the room.'
        else:
            return ", ".join(self.current_players)
        
    '''2.6. Додатковий стан кімнати.
    Додати поле status: "waiting" — до старту, "active" — під час гри, "finished" — після скиду.
    Метод start() тепер: перевіряє, чи кімната не пуста; переводить стан у `"active"`.
    Метод reset_room(): змінює стан на "finished" → очищає гравців → ставить `"waiting"`.'''

    '''2.7. Лог подій (історія). Додати поле **events_log** (список рядків):
    * При додаванні гравця записувати `"Player <name> joined"`
    * При видаленні — `"Player <name> left"`
    * При старті — `"Quest started"`
    * При рестарті — `"Room reset"`
    Метод **show_log()**: повертає історію всіх подій.'''
    def show_log(self):
        if not self.events_log:
            return f'Log is empty.'
        return "\n".join(self.events_log)


if __name__ == "__main__":
    room = QuestRoom("Піратський острів", 3, 4)
    print(room)    #QuestRoom: 'Піратський острів' | Difficulty: 3 з 5 | Players: 0 / 4 
    print(room.start())    # "Room is empty!"
    room.add_player("Олег")
    room.add_player("Даша")
    print(room)    # QuestRoom: Піратський острів | Difficulty: 3 з 5 | Players: 2 / 4
    room.add_player("Марина")
    room.add_player("Роман")    # QuestRoom: Піратський острів | Difficulty: 3 з 5 | Players: 4 / 4
    print(room)
    print(room.add_player("Анатолій"))    # "No free slots!"
    
    print(room.start())
    print(room)

    print(room.remove_player("Марина"))    # "Player Марина removed."
    print(room.remove_player("Анатолій"))    # "Player not found!"
    print(room.is_full())
    print(room.free_slots())
    print(room.reset_room())
    print(room.players_list())
    print(room)
    
    print(room.show_log())