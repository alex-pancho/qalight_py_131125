import pytest
from quest_room import QuestRoom
@pytest.fixture
def room():
    return QuestRoom("Піратський острів", 3, 3)

# 1. Тести загальні
def test_general(room):
    assert room.name == "Піратський острів"
    assert room.difficulty == 3
    assert room.limit == 3
    assert room.players == []
    assert room.status == "waiting"
    assert room.events_log == []

# 2. Додавання гравців
def test_add_one_player(room):
    room.add_player("Олег")
    assert "Олег" in room.players

def test_add_two_players(room):
    room.add_player("Олег")
    room.add_player("Даша")
    assert room.players == ["Олег", "Даша"]

def test_add_player_room_is_full(room):
    room.add_player("Олег")
    room.add_player("Даша")
    room.add_player("Назар")
    result = room.add_player("Іра")
    assert result == "No free slots!"
    assert len(room.players) == 3

def test_add_player_log(room):
    room.add_player("Олег")
    assert room.events_log[-1] == "Player Олег joined"

# 3. Видалення гравців
def test_del_exist_player(room):
    room.add_player("Олег")
    room.remove_player("Олег")
    assert "Олег" not in room.players

def test_del_non_exist_player(room):
    result = room.remove_player("Назар")
    assert result == "Player not found!"

def test_del_player_empty_room(room):
    result = room.remove_player("Олег")
    assert result == "Player not found!"

def test_del_player_log(room):
    room.add_player("Олег")
    room.remove_player("Олег")
    assert room.events_log[-1] == "Player Олег left"

# 4. Перевірка заповненості
def test_is_not_full(room):
    room.add_player("Олег")
    assert room.is_full() is False

def test_is_full(room):
    room.add_player("Олег")
    room.add_player("Даша")
    room.add_player("Назар")
    assert room.is_full() is True

def test_free_slot(room):
    room.add_player("Олег")
    assert room.free_slots() == 2

# 5. Запуск квесту
def test_start_empty_room(room):
    result = room.start()
    assert result == "Room is empty!"
    assert room.status == "waiting"

def test_start_with_players(room):
    room.add_player("Олег")
    room.add_player("Даша")
    result = room.start()
    assert room.status == "active"
    assert "Квест" in result
    assert "Quest started" in room.events_log

# 6. Скидання кімнати
def test_reset_room(room):
    room.add_player("Олег")
    old_status, new_status = room.reset_room()
    assert old_status == "finished"
    assert new_status == "waiting"
    assert room.players == []
    assert "Room reset" in room.events_log

# 7. Список гравців
def test_players_list_not_empty(room):
    room.add_player("Олег")
    assert room.players_list() == ["Олег"]

def test_players_list_empty(room):
    assert room.players_list() == "No players in the room"

# 8. Лог подій
def test_events_log_order(room):
    room.add_player("Олег")
    room.add_player("Даша")
    room.start()
    room.remove_player("Олег")
    assert room.show_log() == ["Player Олег joined", "Player Даша joined","Quest started", "Player Олег left"]

# 9. Комбіновані сценарії
def test_scen_1(room):
    room.add_player("Олег")
    room.add_player("Даша")
    room.start()
    room.reset_room()
    assert room.status == "waiting"
    assert room.players == []

def test_scen_2(room):
    room.add_player("Олег")
    room.add_player("Даша")
    room.add_player("Назар")
    assert room.is_full() is True
    assert room.add_player("Іра") == "No free slots!"
    room.remove_player("Даша")
    room.add_player("Іра")
    assert "Іра" in room.players
    assert len(room.players) == 3

