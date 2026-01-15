from lesson12_class.quest_room import QuestRoom


def test_constructor():
    room = QuestRoom("Quest", 2, 3)
    assert room.name == "Quest"
    assert room.difficulty == 2
    assert room.limit == 3
    assert room.players == []
    assert room.status == "waiting"
    assert room.events_log == []


def test_add_player_ok_and_log():
    room = QuestRoom("Quest", 2, 2)
    room.add_player("Oleg")
    assert room.players == ["Oleg"]
    assert room.events_log == ["Player Oleg joined"]


def test_add_player_no_free_slots():
    room = QuestRoom("Quest", 2, 2)
    room.add_player("Oleg")
    room.add_player("Dasha")
    msg = room.add_player("Ira")
    assert msg == "No free slots!"
    assert room.players == ["Oleg", "Dasha"]


def test_remove_player_ok_and_log():
    room = QuestRoom("Quest", 2, 3)
    room.add_player("Oleg")
    room.add_player("Dasha")
    room.remove_player("Oleg")
    assert room.players == ["Dasha"]
    assert room.events_log[-1] == "Player Oleg left"


def test_remove_player_not_found():
    room = QuestRoom("Quest", 2, 3)
    msg = room.remove_player("Oleg")
    assert msg == "Player not found!"
    assert room.players == []


def test_is_full_and_free_slots_scenario_2():
    room = QuestRoom("Quest", 2, 2)

    assert room.is_full() is False
    assert room.free_slots() == 2

    room.add_player("Oleg")
    assert room.is_full() is False
    assert room.free_slots() == 1

    room.add_player("Dasha")
    assert room.is_full() is True
    assert room.free_slots() == 0

    msg = room.add_player("Ira")
    assert msg == "No free slots!"

    room.remove_player("Dasha")
    assert room.is_full() is False
    assert room.free_slots() == 1

    room.add_player("Ira")
    assert room.players == ["Oleg", "Ira"]


def test_start_empty():
    room = QuestRoom("Quest", 2, 2)
    msg = room.start()
    assert msg == "Room is empty!"
    assert room.status == "waiting"
    assert room.events_log == []


def test_start_with_players_changes_status_and_log():
    room = QuestRoom("Quest", 2, 2)
    room.add_player("Oleg")
    msg = room.start()

    assert msg == "Quest 'Quest' started with 1 players!"
    assert room.status == "active"
    assert room.events_log[-1] == "Quest started"


def test_players_list_empty_and_non_empty():
    room = QuestRoom("Quest", 2, 2)
    assert room.players_list() == "No players in the room"

    room.add_player("Oleg")
    assert room.players_list() == ["Oleg"]


def test_reset_room_status_and_log():
    room = QuestRoom("Quest", 2, 2)
    room.add_player("Oleg")
    room.start()

    msg = room.reset_room()
    assert msg == "Room reset!"
    assert room.players == []
    assert room.status == "waiting"
    assert room.events_log[-1] == "Room reset"


def test_show_log_returns_all_events_in_order():
    room = QuestRoom("Quest", 2, 2)
    room.add_player("Oleg")
    room.add_player("Dasha")
    room.start()
    room.remove_player("Oleg")
    room.reset_room()

    assert room.show_log() == [
        "Player Oleg joined",
        "Player Dasha joined",
        "Quest started",
        "Player Oleg left",
        "Room reset",
    ]


def test_str_format():
    room = QuestRoom("Quest", 2, 3)
    assert str(room) == "QuestRoom: Quest | Difficulty: 2 | Players: 0/3"
