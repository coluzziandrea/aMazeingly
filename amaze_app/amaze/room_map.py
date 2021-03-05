
from .room_result import RoomResult


class RoomMap:

    def __init__(self, room_dict, start_room, target_objects):
        self.rooms = room_dict
        self.target_objects = target_objects
        self.start_room = start_room

    @property
    def rooms(self):
        return self._rooms

    @rooms.setter
    def rooms(self, val):
        if (not val) or (not isinstance(val, dict)):
            raise Exception("Rooms cannot be empty")
        self._rooms = val

    @property
    def target_objects(self):
        return self._target_objects

    @target_objects.setter
    def target_objects(self, val):
        if (not val) or (not isinstance(val, list)):
            raise Exception("Target Objects cannot be empty")
        self._target_objects = val

    def collect_rec(self, room_result, rooms, current_room, current_targets):
        return False

    def collectAllObjects(self):
        room_result = RoomResult()
        current_room_obj = self.rooms[self.start_room]
        current_targets = self.target_objects.copy()
        self.collect_rec(room_result, self.rooms,
                         current_room_obj, current_targets)
        return room_result
