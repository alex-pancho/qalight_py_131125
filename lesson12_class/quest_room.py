class QuestRoom:
    def __init__(self, name, difficulty, limit):
        self.name = name
        self.difficulty = difficulty
        self.limit = limit

        self.players = []
        self.status = "waiting"
        self.events_log = []

    def add_player(self, name):
        if len(self.players) >= self.limit:
            return "No free slots!"
        self.players.append(name)
        self.events_log.append(f"Player {name} joined")

    def remove_player(self, name):
        if name not in self.players:
            return "Player not found!"
        self.players.remove(name)
        self.events_log.append(f"Player {name} left")

    def is_full(self):
        return len(self.players) == self.limit

    def free_slots(self):
        return self.limit - len(self.players)

    def players_list(self):
        if not self.players:
            return "No players in the room"
        return list(self.players)

    def start(self):
        if not self.players:
            return "Room is empty!"
        self.status = "active"
        self.events_log.append("Quest started")
        return f"Quest '{self.name}' started with {len(self.players)} players!"

    def reset_room(self):
        self.status = "finished"
        self.players = []
        self.events_log.append("Room reset")
        self.status = "waiting"
        return "Room reset!"

    def show_log(self):
        return list(self.events_log)

    def __str__(self):
        return (
            f"QuestRoom: {self.name} | Difficulty: {self.difficulty} | "
            f"Players: {len(self.players)}/{self.limit}"
        )
