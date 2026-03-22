from room import Room

class Cinema:

    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)