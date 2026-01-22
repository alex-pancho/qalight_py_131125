import pytest
from homework_12 import QuestRoom

'''1. Тести конструктора**
* Чи правильно зберігаються:
  * назва
  * складність
  * ліміт гравців
  * початковий список гравців пустий
  * статус `"waiting"`
  * лог пустий'''
def test_constructor():
    room = "Піратський острів"
    level = 4
    limit = 5
    room = QuestRoom(room, level, limit)
    assert room.room == "Піратський острів"
    assert room.level == 4
    assert room.limit == 5
    assert room.current_players == []
    assert len(room.current_players) == 0
    assert room.status == "waiting"
    assert room.events_log == []
    assert len(room.events_log) == 0
    print(f'Кімната {room.room} з складністю {room.level} з лімітом гравців {room.limit} ініціалізована. \n'
          f'Початковий список гравців {len(room.current_players)} осіб, статус {room.status}, кількість записів в логу {len(room.events_log)}')

''' **2. Додавання гравців (`add_player`)**
Додавання одного гравця — має опинитися у списку.'''
def test_add_one_player():
     room = QuestRoom("Піратський острів", 3, 4)
     player_name = "Іван"
     result = room.add_player(player_name)
     assert player_name in room.current_players
     assert len(room.current_players) == 1
     assert result == f"Player {player_name} was added to Піратський острів!"

'''Додавання одного гравця — має опинитися у списку. '''
# Після виконання тесту гравець видаляється зі списку 
@pytest.fixture
def room_with_cleanup():
     room = QuestRoom("Піратський острів", 3, 4)
     player_name = "Іван"
     yield room, player_name
     room.remove_player(player_name)
     print(f'Post-conditions: Player {player_name} was removed, player list: {room.current_players}')

def test_add_one_player(room_with_cleanup):
     room, player_name = room_with_cleanup
     result = room.add_player(player_name)
     assert player_name in room.current_players
     assert len(room.current_players) == 1
     assert result == f"Player {player_name} was added to Піратський острів!"

'''Додавання кількох гравців — у правильному порядку.''' 
def test_add_several_players():
     room = QuestRoom("Піратський острів", 3, 4)
     players = ["Борис", "Марія", "Петро"]
     
     print("\n--- Початок додавання гравців ---")
     result = None
     for name in players:
          result = room.add_player(name)
          assert result == f"Player {name} was added to Піратський острів!"
          print(f"Черга: додаємо {name}...")
     
     assert room.current_players == ["Борис", "Марія", "Петро"]
     assert room.current_players[0] == "Борис"
     assert room.current_players[1] == "Марія"
     assert room.current_players[2] == "Петро"
     assert len(room.current_players) == 3
     print("--- Усі гравці додані успішно ---")
     
'''Додавання гравця, коли досягнуто ліміт — отримуємо `"No free slots!"`.'''
def test_limit_players():
    limit = 4
    room = QuestRoom("Піратський острів", 3, limit)
    players = ["Борис", "Марія", "Петро", "Іван"]
    
    for name in players:
        result = room.add_player(name)
    print('Player List completed!')

    result = room.add_player("Анна")
    assert result == 'No free slots!'
    assert "Анна" not in room.current_players
    assert len(room.current_players) == limit

'''Додавання гравця з тим самим ім’ям (якщо заборонено — перевірити поведінку).
В даному завданні - не заборонено'''
def test_add_the_same_player():
    room = QuestRoom("Піратський острів", 3, 4)
    player_name_1 = "Іван"
    result = room.add_player(player_name_1)
    assert player_name_1 in room.current_players
    assert result == f"Player {player_name_1} was added to Піратський острів!"
    player_name_2 = "Іван"
    result = room.add_player(player_name_2)
    assert player_name_2 in room.current_players
    assert len(room.current_players) == 2
    assert result == f"Player {player_name_2} was added to Піратський острів!"

'''Лог повинен містити `"Player X joined"`.'''
def test_log_player_joined():
    room = QuestRoom("Піратський острів", 3, 4)
    player_name = "Іван"
    result = room.add_player(player_name)
    assert player_name in room.current_players
    assert len(room.current_players) == 1
    assert f'Player {player_name} joined.' in room.events_log 
    assert result == f"Player {player_name} was added to Піратський острів!"

''' **3. Видалення гравців (`remove_player`)**
Видалення існуючого гравця → має зникнути зі списку.'''
def test_remove_current_player():
     room = QuestRoom("Піратський острів", 3, 4)
     player_name = "Іван"
     room.add_player(player_name)
     result = room.remove_player(player_name)
     assert player_name not in room.current_players
     assert result == f'Player {player_name} removed.'

'''Видалення неіснуючого → `"Player not found!"`.'''
def test_remove_non_existent_player():
     room = QuestRoom("Піратський острів", 3, 4)
     result = room.remove_player("Капітан Шторм")
     assert result == f'Player not found!'

'''Видалення з порожньої кімнати → `"Player not found!"`.'''
def test_remove_player_from_empty_room():
    room = QuestRoom("Піратський острів", 3, 4)
    name_to_remove = "Богдан"
    result = room.remove_player(name_to_remove)
    assert result == f'Player not found!'
    assert len(room.current_players) == 0

'''Лог має записати `"Player X left"`.'''
def test_log_remove_current_player():
    room = QuestRoom("Піратський острів", 3, 4)
    player_name = "Іван"
    room.add_player(player_name)
    result = room.remove_player(player_name)
    assert player_name not in room.current_players
    assert f'Player {player_name} left.' in room.events_log
    assert result == f'Player {player_name} removed.'

''' **4. Перевірка заповненості (`is_full`, `free_slots`)**
Якщо гравців менше ліміту → не повна.'''
def test_players_under_limit():
    limit = 4
    room = QuestRoom("Піратський острів", 3, limit)
    player_name = "Іван"
    room.add_player(player_name)
    assert len(room.current_players) < limit
    assert room.is_full() is False
    assert room.free_slots() == 3

'''Якщо рівно ліміт → повна.'''
def test_players_equal_limit():
    limit = 1
    room = QuestRoom("Піратський острів", 3, limit)
    player_name = "Іван"
    room.add_player(player_name)
    assert len(room.current_players) == limit
    assert room.is_full() is True
    assert room.free_slots() == 0

'''Кількість вільних місць обчислюється правильно при різних значеннях.'''
def test_free_slots():
  room = QuestRoom("Піратський острів", 2, 3) 
  assert room.is_full() is False
  assert room.free_slots() == 3

  room.add_player("Ігор")
  assert room.is_full() is False
  assert room.free_slots() == 2

  room.add_player("Даша")
  assert room.is_full() is False
  assert room.free_slots() == 1

  room.add_player("Михайло")
  assert room.is_full() is True
  assert room.free_slots() == 0

  room.remove_player("Даша")
  assert room.is_full() is False
  assert room.free_slots() == 1

'''**5. Запуск квесту (`start`)**
Якщо список порожній → `"Room is empty!"`.'''
def test_start_with_no_players():
    room = QuestRoom("Піратський острів", 2, 3)
    result = room.start()
    assert result == f'Room is empty!'
    assert len(room.current_players) == 0

'''Якщо є гравці:
  * статус змінюється на `"active"`
  * повертається `"Quest 'X' started with Y players!"`
  * лог містить `"Quest started"`'''
def test_start_with_players():
    room = QuestRoom("Піратський острів", 2, 3)
    room.add_player("Ігор")
    room.add_player("Даша")
    result = room.start()
    assert room.status == "active"
    assert f'Quest started.' in room.events_log
    assert result == f"Quest '{room.room}' started with {len(room.current_players)} players!"

'''**6. Скидання кімнати (`reset_room`)** 
Перевірити:
* після скиду список гравців порожній
* статус змінюється `"finished"` → `"waiting"`
* лог містить `"Room reset!"`'''
def test_reset_room():
    room = QuestRoom("Піратський острів", 2, 3)
    room.add_player("Ігор")   
    room.add_player("Даша")    
    room.start()               
    result = room.reset_room()    
    assert f'Status - finished' in room. events_log 
    print(f'Статус кімнати одразу після скидання finished')
    assert room.current_players == []
    assert len(room.current_players) == 0
    assert f'Room reset.' in room. events_log
    assert room.status == "waiting"
    print(f'Статус кімнати після видалення гравців {room.status}')
    assert result == f"Room reset!"

'''**7. Список гравців (`players_list`)**
Повертає правильний список.'''
def test_current_players_list():
    room = QuestRoom("Піратський острів", 3, 5)
    players = ["Ігор", "Григорій", "Роман", "Оксана", "Константин"]
    for player in players:
        room.add_player(player)
    result = room.players_list()
    assert result == "Ігор, Григорій, Роман, Оксана, Константин"
    assert room.current_players == players

'''Якщо пусто → `"No players in the room"`.'''
def test_empty_players_list():
    room = QuestRoom("Піратський острів", 3, 5)
    result = room.players_list()
    assert result == 'No players in the room.'
    

'''**8. Лог подій (`show_log`)**
* Лог повинен містити всі події у правильному порядку.
* Після серії дій перевірити, що лог містить точно те, що очікується.'''
# В метод reset_room() для перевірки статусу в тесті 6. Скидання кімнати (`reset_room`) було додано
# self.events_log.append(f'Status - finished')     
def test_show_log():
    room = QuestRoom("Піратський острів", 3, 5)
    player_name_1 = "Ігор"
    player_name_2 = "Даша"
    player_name_3 = "Роман"
    assert len(room.events_log) == 0
    room.add_player(player_name_1)
    assert f'Player {player_name_1} joined.' in room.events_log
    room.add_player(player_name_2)
    room.add_player(player_name_3)
    room.start()
    assert 'Quest started.' in room.events_log
    room.remove_player(player_name_2) 
    assert f'Player {player_name_2} left.' in room.events_log
    room.add_player(player_name_2)
    room.reset_room()
    assert 'Room reset.' in room.events_log
    expected_logs_sequence = [f'Player {player_name_1} joined.',
                               f'Player {player_name_2} joined.',
                               f'Player {player_name_3} joined.',
                               'Quest started.',
                               f'Player {player_name_2} left.',
                               f'Player {player_name_2} joined.',
                               'Status - finished',
                               'Room reset.']
    assert room.events_log == expected_logs_sequence

'''**9. Комбіновані сценарії**
**Сценарій 1:**
1. Додати 2 гравців
2. Запустити гру
3. Скинути кімнату
Перевірити:
* статуси у правильному порядку
* лог у правильному порядку
* після скиду немає гравців'''
def test_scenario_1():
    room = QuestRoom("Піратський острів", 3, 5)
    assert room.status == "waiting"
    assert len(room.events_log) == 0
    
    player_name_1 = "Максим"
    player_name_2 = "Вероніка"
    room.add_player(player_name_1)
    room.add_player(player_name_2)
    assert len(room.current_players) == 2
    
    room.start()
    assert room.status == "active"
    
    room.reset_room()
    assert len(room.current_players) == 0
    assert room.status == "waiting"

    expected_logs_sequence = [f'Player {player_name_1} joined.',
                               f'Player {player_name_2} joined.',                                
                               'Quest started.',
                               'Status - finished',
                               'Room reset.']
    assert room.events_log == expected_logs_sequence

'''**Сценарій 2:**
1. Додати гравців до ліміту
2. Викликати `is_full`
3. Спробувати додати ще одного
4. Видалити когось
5. Додати нового'''
def test_scenario_2():
    limit = 3
    room = QuestRoom("Піратський острів", 3, limit)
    assert len(room.events_log) == 0
    
    player_name_1 = "Максим"
    player_name_2 = "Вероніка"
    player_name_3 = "Роман"
    player_name_4 = "Ігор"

    assert room.add_player(player_name_1) == f'Player {player_name_1} was added to {room.room}!'
    assert room.add_player(player_name_2) == f'Player {player_name_2} was added to {room.room}!'
    assert room.add_player(player_name_3) == f'Player {player_name_3} was added to {room.room}!'
    assert len(room.current_players) == limit
    assert room.current_players == [player_name_1, player_name_2, player_name_3]

    assert room.is_full() is True

    result = room.add_player(player_name_4)
    assert result == 'No free slots!'
    assert {player_name_4} not in room.current_players
    assert len(room.current_players) == limit

    result = room.remove_player(player_name_3)
    assert result == f'Player {player_name_3} removed.'
    assert {player_name_3} not in room.current_players
    assert len(room.current_players) == limit - 1
    assert room.current_players == [player_name_1, player_name_2]

    result = room.add_player(player_name_4)
    assert result == f'Player {player_name_4} was added to {room.room}!'
    assert len(room.current_players) == limit
    assert room.current_players == [player_name_1, player_name_2, player_name_4]
  

    expected_logs_sequence = [f'Player {player_name_1} joined.',
                               f'Player {player_name_2} joined.',
                               f'Player {player_name_3} joined.',
                               f'Player {player_name_3} left.',
                               f'Player {player_name_4} joined.']
    assert room.events_log == expected_logs_sequence

'''**Бонусні тестові ідеї (якщо хочеш підвищити складність)**'''
'''* Тест на продуктивність: додати 1000 гравців у кімнату з великим лімітом.'''
def test_load_with_1000_players():
    room = QuestRoom("Піратський острів", 3, 1001)
    players = [
    "Іван_1", "Марія_1", "Олександр_1", "Олена_1", "Дмитро_1", "Наталія_1", "Сергій_1", "Тетяна_1", "Андрій_1", "Ольга_1",
    "Микола_1", "Світлана_1", "Віктор_1", "Юлія_1", "Анатолій_1", "Людмила_1", "Володимир_1", "Ірина_1", "Василь_1", "Галина_1",
    "Іван_2", "Марія_2", "Олександр_2", "Олена_2", "Дмитро_2", "Наталія_2", "Сергій_2", "Тетяна_2", "Андрій_2", "Ольга_2",
    "Микола_2", "Світлана_2", "Віктор_2", "Юлія_2", "Анатолій_2", "Людмила_2", "Володимир_2", "Ірина_2", "Василь_2", "Галина_2",
    "Іван_3", "Марія_3", "Олександр_3", "Олена_3", "Дмитро_3", "Наталія_3", "Сергій_3", "Тетяна_3", "Андрій_3", "Ольга_3",
    "Микола_3", "Світлана_3", "Віктор_3", "Юлія_3", "Анатолій_3", "Людмила_3", "Володимир_3", "Ірина_3", "Василь_3", "Галина_3",
    "Іван_4", "Марія_4", "Олександр_4", "Олена_4", "Дмитро_4", "Наталія_4", "Сергій_4", "Тетяна_4", "Андрій_4", "Ольга_4",
    "Микола_4", "Світлана_4", "Віктор_4", "Юлія_4", "Анатолій_4", "Людмила_4", "Володимир_4", "Ірина_4", "Василь_4", "Галина_4",
    "Іван_5", "Марія_5", "Олександр_5", "Олена_5", "Дмитро_5", "Наталія_5", "Сергій_5", "Тетяна_5", "Андрій_5", "Ольга_5",
    "Микола_5", "Світлана_5", "Віктор_5", "Юлія_5", "Анатолій_5", "Людмила_5", "Володимир_5", "Ірина_5", "Василь_5", "Галина_5",
    "Іван_6", "Марія_6", "Олександр_6", "Олена_6", "Дмитро_6", "Наталія_6", "Сергій_6", "Тетяна_6", "Андрій_6", "Ольга_6",
    "Микола_6", "Світлана_6", "Віктор_6", "Юлія_6", "Анатолій_6", "Людмила_6", "Володимир_6", "Ірина_6", "Василь_6", "Галина_6",
    "Іван_7", "Марія_7", "Олександр_7", "Олена_7", "Дмитро_7", "Наталія_7", "Сергій_7", "Тетяна_7", "Андрій_7", "Ольга_7",
    "Микола_7", "Світлана_7", "Віктор_7", "Юлія_7", "Анатолій_7", "Людмила_7", "Володимир_7", "Ірина_7", "Василь_7", "Галина_7",
    "Іван_8", "Марія_8", "Олександр_8", "Олена_8", "Дмитро_8", "Наталія_8", "Сергій_8", "Тетяна_8", "Андрій_8", "Ольга_8",
    "Микола_8", "Світлана_8", "Віктор_8", "Юлія_8", "Анатолій_8", "Людмила_8", "Володимир_8", "Ірина_8", "Василь_8", "Галина_8",
    "Іван_9", "Марія_9", "Олександр_9", "Олена_9", "Дмитро_9", "Наталія_9", "Сергій_9", "Тетяна_9", "Андрій_9", "Ольга_9",
    "Микола_9", "Світлана_9", "Віктор_9", "Юлія_9", "Анатолій_9", "Людмила_9", "Володимир_9", "Ірина_9", "Василь_9", "Галина_9",
    "Іван_10", "Марія_10", "Олександр_10", "Олена_10", "Дмитро_10", "Наталія_10", "Сергій_10", "Тетяна_10", "Андрій_10", "Ольга_10",
    "Микола_10", "Світлана_10", "Віктор_10", "Юлія_10", "Анатолій_10", "Людмила_10", "Володимир_10", "Ірина_10", "Василь_10", "Галина_10",
    "Іван_11", "Марія_11", "Олександр_11", "Олена_11", "Дмитро_11", "Наталія_11", "Сергій_11", "Тетяна_11", "Андрій_11", "Ольга_11",
    "Микола_11", "Світлана_11", "Віктор_11", "Юлія_11", "Анатолій_11", "Людмила_11", "Володимир_11", "Ірина_11", "Василь_11", "Галина_11",
    "Іван_12", "Марія_12", "Олександр_12", "Олена_12", "Дмитро_12", "Наталія_12", "Сергій_12", "Тетяна_12", "Андрій_12", "Ольга_12",
    "Микола_12", "Світлана_12", "Віктор_12", "Юлія_12", "Анатолій_12", "Людмила_12", "Володимир_12", "Ірина_12", "Василь_12", "Галина_12",
    "Іван_13", "Марія_13", "Олександр_13", "Олена_13", "Дмитро_13", "Наталія_13", "Сергій_13", "Тетяна_13", "Андрій_13", "Ольга_13",
    "Микола_13", "Світлана_13", "Віктор_13", "Юлія_13", "Анатолій_13", "Людмила_13", "Володимир_13", "Ірина_13", "Василь_13", "Галина_13",
    "Іван_14", "Марія_14", "Олександр_14", "Олена_14", "Дмитро_14", "Наталія_14", "Сергій_14", "Тетяна_14", "Андрій_14", "Ольга_14",
    "Микола_14", "Світлана_14", "Віктор_14", "Юлія_14", "Анатолій_14", "Людмила_14", "Володимир_14", "Ірина_14", "Василь_14", "Галина_14",
    "Іван_15", "Марія_15", "Олександр_15", "Олена_15", "Дмитро_15", "Наталія_15", "Сергій_15", "Тетяна_15", "Андрій_15", "Ольга_15",
    "Микола_15", "Світлана_15", "Віктор_15", "Юлія_15", "Анатолій_15", "Людмила_15", "Володимир_15", "Ірина_15", "Василь_15", "Галина_15",
    "Іван_16", "Марія_16", "Олександр_16", "Олена_16", "Дмитро_16", "Наталія_16", "Сергій_16", "Тетяна_16", "Андрій_16", "Ольга_16",
    "Микола_16", "Світлана_16", "Віктор_16", "Юлія_16", "Анатолій_16", "Людмила_16", "Володимир_16", "Ірина_16", "Василь_16", "Галина_16",
    "Іван_17", "Марія_17", "Олександр_17", "Олена_17", "Дмитро_17", "Наталія_17", "Сергій_17", "Тетяна_17", "Андрій_17", "Ольга_17",
    "Микола_17", "Світлана_17", "Віктор_17", "Юлія_17", "Анатолій_17", "Людмила_17", "Володимир_17", "Ірина_17", "Василь_17", "Галина_17",
    "Іван_18", "Марія_18", "Олександр_18", "Олена_18", "Дмитро_18", "Наталія_18", "Сергій_18", "Тетяна_18", "Андрій_18", "Ольга_18",
    "Микола_18", "Світлана_18", "Віктор_18", "Юлія_18", "Анатолій_18", "Людмила_18", "Володимир_18", "Ірина_18", "Василь_18", "Галина_18",
    "Іван_19", "Марія_19", "Олександр_19", "Олена_19", "Дмитро_19", "Наталія_19", "Сергій_19", "Тетяна_19", "Андрій_19", "Ольга_19",
    "Микола_19", "Світлана_19", "Віктор_19", "Юлія_19", "Анатолій_19", "Людмила_19", "Володимир_19", "Ірина_19", "Василь_19", "Галина_19",
    "Іван_20", "Марія_20", "Олександр_20", "Олена_20", "Дмитро_20", "Наталія_20", "Сергій_20", "Тетяна_20", "Андрій_20", "Ольга_20",
    "Микола_20", "Світлана_20", "Віктор_20", "Юлія_20", "Анатолій_20", "Людмила_20", "Володимир_20", "Ірина_20", "Василь_20", "Галина_20",
    "Іван_21", "Марія_21", "Олександр_21", "Олена_21", "Дмитро_21", "Наталія_21", "Сергій_21", "Тетяна_21", "Андрій_21", "Ольга_21",
    "Микола_21", "Світлана_21", "Віктор_21", "Юлія_21", "Анатолій_21", "Людмила_21", "Володимир_21", "Ірина_21", "Василь_21", "Галина_21",
    "Іван_22", "Марія_22", "Олександр_22", "Олена_22", "Дмитро_22", "Наталія_22", "Сергій_22", "Тетяна_22", "Андрій_22", "Ольга_22",
    "Микола_22", "Світлана_22", "Віктор_22", "Юлія_22", "Анатолій_22", "Людмила_22", "Володимир_22", "Ірина_22", "Василь_22", "Галина_22",
    "Іван_23", "Марія_23", "Олександр_23", "Олена_23", "Дмитро_23", "Наталія_23", "Сергій_23", "Тетяна_23", "Андрій_23", "Ольга_23",
    "Микола_23", "Світлана_23", "Віктор_23", "Юлія_23", "Анатолій_23", "Людмила_23", "Володимир_23", "Ірина_23", "Василь_23", "Галина_23",
    "Іван_24", "Марія_24", "Олександр_24", "Олена_24", "Дмитро_24", "Наталія_24", "Сергій_24", "Тетяна_24", "Андрій_24", "Ольга_24",
    "Микола_24", "Світлана_24", "Віктор_24", "Юлія_24", "Анатолій_24", "Людмила_24", "Володимир_24", "Ірина_24", "Василь_24", "Галина_24",
    "Іван_25", "Марія_25", "Олександр_25", "Олена_25", "Дмитро_25", "Наталія_25", "Сергій_25", "Тетяна_25", "Андрій_25", "Ольга_25",
    "Микола_25", "Світлана_25", "Віктор_25", "Юлія_25", "Анатолій_25", "Людмила_25", "Володимир_25", "Ірина_25", "Василь_25", "Галина_25",
    "Іван_26", "Марія_26", "Олександр_26", "Олена_26", "Дмитро_26", "Наталія_26", "Сергій_26", "Тетяна_26", "Андрій_26", "Ольга_26",
    "Микола_26", "Світлана_26", "Віктор_26", "Юлія_26", "Анатолій_26", "Людмила_26", "Володимир_26", "Ірина_26", "Василь_26", "Галина_26",
    "Іван_27", "Марія_27", "Олександр_27", "Олена_27", "Дмитро_27", "Наталія_27", "Сергій_27", "Тетяна_27", "Андрій_27", "Ольга_27",
    "Микола_27", "Світлана_27", "Віктор_27", "Юлія_27", "Анатолій_27", "Людмила_27", "Володимир_27", "Ірина_27", "Василь_27", "Галина_27",
    "Іван_28", "Марія_28", "Олександр_28", "Олена_28", "Дмитро_28", "Наталія_28", "Сергій_28", "Тетяна_28", "Андрій_28", "Ольга_28",
    "Микола_28", "Світлана_28", "Віктор_28", "Юлія_28", "Анатолій_28", "Людмила_28", "Володимир_28", "Ірина_28", "Василь_28", "Галина_28",
    "Іван_29", "Марія_29", "Олександр_29", "Олена_29", "Дмитро_29", "Наталія_29", "Сергій_29", "Тетяна_29", "Андрій_29", "Ольга_29",
    "Микола_29", "Світлана_29", "Віктор_29", "Юлія_29", "Анатолій_29", "Людмила_29", "Володимир_29", "Ірина_29", "Василь_29", "Галина_29",
    "Іван_30", "Марія_30", "Олександр_30", "Олена_30", "Дмитро_30", "Наталія_30", "Сергій_30", "Тетяна_30", "Андрій_30", "Ольга_30",
    "Микола_30", "Світлана_30", "Віктор_30", "Юлія_30", "Анатолій_30", "Людмила_30", "Володимир_30", "Ірина_30", "Василь_30", "Галина_30",
    "Іван_31", "Марія_31", "Олександр_31", "Олена_31", "Дмитро_31", "Наталія_31", "Сергій_31", "Тетяна_31", "Андрій_31", "Ольга_31",
    "Микола_31", "Світлана_31", "Віктор_31", "Юлія_31", "Анатолій_31", "Людмила_31", "Володимир_31", "Ірина_31", "Василь_31", "Галина_31",
    "Іван_32", "Марія_32", "Олександр_32", "Олена_32", "Дмитро_32", "Наталія_32", "Сергій_32", "Тетяна_32", "Андрій_32", "Ольга_32",
    "Микола_32", "Світлана_32", "Віктор_32", "Юлія_32", "Анатолій_32", "Людмила_32", "Володимир_32", "Ірина_32", "Василь_32", "Галина_32",
    "Іван_33", "Марія_33", "Олександр_33", "Олена_33", "Дмитро_33", "Наталія_33", "Сергій_33", "Тетяна_33", "Андрій_33", "Ольга_33",
    "Микола_33", "Світлана_33", "Віктор_33", "Юлія_33", "Анатолій_33", "Людмила_33", "Володимир_33", "Ірина_33", "Василь_33", "Галина_33",
    "Іван_34", "Марія_34", "Олександр_34", "Олена_34", "Дмитро_34", "Наталія_34", "Сергій_34", "Тетяна_34", "Андрій_34", "Ольга_34",
    "Микола_34", "Світлана_34", "Віктор_34", "Юлія_34", "Анатолій_34", "Людмила_34", "Володимир_34", "Ірина_34", "Василь_34", "Галина_34",
    "Іван_35", "Марія_35", "Олександр_35", "Олена_35", "Дмитро_35", "Наталія_35", "Сергій_35", "Тетяна_35", "Андрій_35", "Ольга_35",
    "Микола_35", "Світлана_35", "Віктор_35", "Юлія_35", "Анатолій_35", "Людмила_35", "Володимир_35", "Ірина_35", "Василь_35", "Галина_35",
    "Іван_36", "Марія_36", "Олександр_36", "Олена_36", "Дмитро_36", "Наталія_36", "Сергій_36", "Тетяна_36", "Андрій_36", "Ольга_36",
    "Микола_36", "Світлана_36", "Віктор_36", "Юлія_36", "Анатолій_36", "Людмила_36", "Володимир_36", "Ірина_36", "Василь_36", "Галина_36",
    "Іван_37", "Марія_37", "Олександр_37", "Олена_37", "Дмитро_37", "Наталія_37", "Сергій_37", "Тетяна_37", "Андрій_37", "Ольга_37",
    "Микола_37", "Світлана_37", "Віктор_37", "Юлія_37", "Анатолій_37", "Людмила_37", "Володимир_37", "Ірина_37", "Василь_37", "Галина_37",
    "Іван_38", "Марія_38", "Олександр_38", "Олена_38", "Дмитро_38", "Наталія_38", "Сергій_38", "Тетяна_38", "Андрій_38", "Ольга_38",
    "Микола_38", "Світлана_38", "Віктор_38", "Юлія_38", "Анатолій_38", "Людмила_38", "Володимир_38", "Ірина_38", "Василь_38", "Галина_38",
    "Іван_39", "Марія_39", "Олександр_39", "Олена_39", "Дмитро_39", "Наталія_39", "Сергій_39", "Тетяна_39", "Андрій_39", "Ольга_39",
    "Микола_39", "Світлана_39", "Віктор_39", "Юлія_39", "Анатолій_39", "Людмила_39", "Володимир_39", "Ірина_39", "Василь_39", "Галина_39",
    "Іван_40", "Марія_40", "Олександр_40", "Олена_40", "Дмитро_40", "Наталія_40", "Сергій_40", "Тетяна_40", "Андрій_40", "Ольга_40",
    "Микола_40", "Світлана_40", "Віктор_40", "Юлія_40", "Анатолій_40", "Людмила_40", "Володимир_40", "Ірина_40", "Василь_40", "Галина_40",
    "Іван_41", "Марія_41", "Олександр_41", "Олена_41", "Дмитро_41", "Наталія_41", "Сергій_41", "Тетяна_41", "Андрій_41", "Ольга_41",
    "Микола_41", "Світлана_41", "Віктор_41", "Юлія_41", "Анатолій_41", "Людмила_41", "Володимир_41", "Ірина_41", "Василь_41", "Галина_41",
    "Іван_42", "Марія_42", "Олександр_42", "Олена_42", "Дмитро_42", "Наталія_42", "Сергій_42", "Тетяна_42", "Андрій_42", "Ольга_42",
    "Микола_42", "Світлана_42", "Віктор_42", "Юлія_42", "Анатолій_42", "Людмила_42", "Володимир_42", "Ірина_42", "Василь_42", "Галина_42",
    "Іван_43", "Марія_43", "Олександр_43", "Олена_43", "Дмитро_43", "Наталія_43", "Сергій_43", "Тетяна_43", "Андрій_43", "Ольга_43",
    "Микола_43", "Світлана_43", "Віктор_43", "Юлія_43", "Анатолій_43", "Людмила_43", "Володимир_43", "Ірина_43", "Василь_43", "Галина_43",
    "Іван_44", "Марія_44", "Олександр_44", "Олена_44", "Дмитро_44", "Наталія_44", "Сергій_44", "Тетяна_44", "Андрій_44", "Ольга_44",
    "Микола_44", "Світлана_44", "Віктор_44", "Юлія_44", "Анатолій_44", "Людмила_44", "Володимир_44", "Ірина_44", "Василь_44", "Галина_44",
    "Іван_45", "Марія_45", "Олександр_45", "Олена_45", "Дмитро_45", "Наталія_45", "Сергій_45", "Тетяна_45", "Андрій_45", "Ольга_45",
    "Микола_45", "Світлана_45", "Віктор_45", "Юлія_45", "Анатолій_45", "Людмила_45", "Володимир_45", "Ірина_45", "Василь_45", "Галина_45",
    "Іван_46", "Марія_46", "Олександр_46", "Олена_46", "Дмитро_46", "Наталія_46", "Сергій_46", "Тетяна_46", "Андрій_46", "Ольга_46",
    "Микола_46", "Світлана_46", "Віктор_46", "Юлія_46", "Анатолій_46", "Людмила_46", "Володимир_46", "Ірина_46", "Василь_46", "Галина_46",
    "Іван_47", "Марія_47", "Олександр_47", "Олена_47", "Дмитро_47", "Наталія_47", "Сергій_47", "Тетяна_47", "Андрій_47", "Ольга_47",
    "Микола_47", "Світлана_47", "Віктор_47", "Юлія_47", "Анатолій_47", "Людмила_47", "Володимир_47", "Ірина_47", "Василь_47", "Галина_47",
    "Іван_48", "Марія_48", "Олександр_48", "Олена_48", "Дмитро_48", "Наталія_48", "Сергій_48", "Тетяна_48", "Андрій_48", "Ольга_48",
    "Микола_48", "Світлана_48", "Віктор_48", "Юлія_48", "Анатолій_48", "Людмила_48", "Володимир_48", "Ірина_48", "Василь_48", "Галина_48",
    "Іван_49", "Марія_49", "Олександр_49", "Олена_49", "Дмитро_49", "Наталія_49", "Сергій_49", "Тетяна_49", "Андрій_49", "Ольга_49",
    "Микола_49", "Світлана_49", "Віктор_49", "Юлія_49", "Анатолій_49", "Людмила_49", "Володимир_49", "Ірина_49", "Василь_49", "Галина_49",
    "Іван_50", "Марія_50", "Олександр_50", "Олена_50", "Дмитро_50", "Наталія_50", "Сергій_50", "Тетяна_50", "Андрій_50", "Ольга_50",
    "Микола_50", "Світлана_50", "Віктор_50", "Юлія_50", "Анатолій_50", "Людмила_50", "Володимир_50", "Ірина_50", "Василь_50", "Галина_50"
]
    for player in players:
      room.add_player(player)
    
    result = room.players_list()
    assert room.current_players == players
    assert len(room.current_players) == 1000
    result = room.start()
    assert result == f"Quest '{room.room}' started with {len(room.current_players)} players!"

'''* Перевірка, що порядок запису в лог зберігається точно при великій кількості подій.'''
def test_with_bulk_actions():
   room = QuestRoom("Піратський острів", 3, 5)
   player_name_1 = "Максим"
   player_name_2 = "Вероніка"
   player_name_3 = "Роман"
   room.add_player(player_name_1)
   room.remove_player(player_name_1)
   room.add_player(player_name_1)
   room.add_player(player_name_2)
   room.remove_player(player_name_2)
   result = room.start()
   result = room.reset_room()
   room.add_player(player_name_1)
   room.remove_player(player_name_1)
   room.add_player(player_name_1)
   room.add_player(player_name_2)
   room.remove_player(player_name_2)
   room.add_player(player_name_3)
   result = room.start()
   result = room.reset_room()
   result = room.start()
   room.add_player(player_name_1)
   room.remove_player(player_name_1)
   room.add_player(player_name_1)
   room.add_player(player_name_2)
   room.remove_player(player_name_2)
   room.add_player(player_name_3)
   room.add_player(player_name_2)
   result = room.start()
   result = room.reset_room()

   expected_logs_sequence = [f'Player {player_name_1} joined.',
                             f'Player {player_name_1} left.',
                             f'Player {player_name_1} joined.',
                             f'Player {player_name_2} joined.',
                             f'Player {player_name_2} left.',
                             f'Quest started.',
                             f'Status - finished',
                             f'Room reset.',

                             f'Player {player_name_1} joined.',
                             f'Player {player_name_1} left.',
                             f'Player {player_name_1} joined.',
                             f'Player {player_name_2} joined.',
                             f'Player {player_name_2} left.',
                             f'Player {player_name_3} joined.',
                             f'Quest started.',
                             f'Status - finished',
                             f'Room reset.',

                             f'Player {player_name_1} joined.',
                             f'Player {player_name_1} left.',
                             f'Player {player_name_1} joined.',
                             f'Player {player_name_2} joined.',
                             f'Player {player_name_2} left.',
                             f'Player {player_name_3} joined.',
                             f'Player {player_name_2} joined.',
                             f'Quest started.',
                             f'Status - finished',
                             f'Room reset.']
   assert room.events_log == expected_logs_sequence

'''* Імітація кількох стартів або подвійного скиду (чи не ламається логіка).'''
def test_with_several_starts_and_resets():
    room = QuestRoom("Піратський острів", 3, 5)
    player_name_1 = "Максим"
    player_name_2 = "Вероніка"
    room.add_player(player_name_1) 
    room.add_player(player_name_2) 
    assert room.current_players == [player_name_1, player_name_2]
    assert len(room.current_players) == 2

    result = room.start()
    assert room.status == "active"
    assert f'Quest started.' in room.events_log
    assert result == f"Quest '{room.room}' started with {len(room.current_players)} players!"
    assert len(room.current_players) == 2

    result = room.start()
    assert room.status == "active"
    assert f'Quest started.' in room.events_log
    assert result == f"Quest '{room.room}' started with {len(room.current_players)} players!"
    assert len(room.current_players) == 2

    result = room.reset_room()
    assert len(room.current_players) == 0
    assert room.status == "waiting"

    result = room.reset_room()
    assert len(room.current_players) == 0
    assert room.status == "waiting"

    result = room.start()
    assert room.status == "waiting"
    assert len(room.current_players) == 0
    assert result == f'Room is empty!'
    
    expected_logs_sequence = [f'Player {player_name_1} joined.',
                               f'Player {player_name_2} joined.',                                
                               'Quest started.',
                               'Quest started.',
                               'Status - finished',
                               'Room reset.',
                               'Status - finished',
                               'Room reset.']
    assert room.events_log == expected_logs_sequence

'''* Перевірка поведінки при дивних іменах: `""`, `"   "`, `None` (якщо ти хочеш додати валідацію).'''
def test_strange_player_names():
    room = QuestRoom("Піратський острів", 3, 5)
    player_name_1 = '""'
    player_name_2 = '" "'
    player_name_3 = 'None'
    assert room.add_player(player_name_1) == f'Player {player_name_1} was added to {room.room}!'
    assert room.add_player(player_name_2) == f'Player {player_name_2} was added to {room.room}!'
    assert room.add_player(player_name_3) == f'Player {player_name_3} was added to {room.room}!'
    assert room.current_players == [player_name_1, player_name_2, player_name_3]