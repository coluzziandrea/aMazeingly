
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

    def collect_rec(self, room_result, rooms, current_room):

        current_room.visit(room_result)

        children_to_visit = []

        if current_room.hasNorthToVisit(room_result):
            children_to_visit.append(("north", current_room.north))

        if current_room.hasSouthToVisit(room_result):
            children_to_visit.append(("south", current_room.south))

        if current_room.hasWestToVisit(room_result):
            children_to_visit.append(("west", current_room.west))

        if current_room.hasEastToVisit(room_result):
            children_to_visit.append(("east", current_room.east))

        print("RoomMap: room with ID {} named '{}' has these rooms remaining to visit: {}".format(current_room.id, current_room.name,
                                                                                                  children_to_visit))

        has_children = len(children_to_visit) > 0

        # if precedent room has other children to visit, come back to that room
        if room_result.hasPrecedentBranchToFollow(current_room.id):

            precedent_room_id = room_result.takePrecedentBranchToFollow(
                current_room.id)

            print("RoomMap: coming back to precedent room with ID: {}".format(
                precedent_room_id))
            self.collect_rec(room_result, rooms,
                             rooms[precedent_room_id])
        elif has_children:

            first_available_child = children_to_visit.pop(0)

            needs_revisit = len(children_to_visit) > 0

            print("RoomMap: visiting children room: {}, current room needs to be revisited: {}".format(
                first_available_child, needs_revisit))

            child_id = first_available_child[1]

            if needs_revisit:
                room_result.addPrecedentBranchToFollow(
                    current_room.id, child_id)

            self.collect_rec(room_result, rooms,
                             rooms[child_id])

    def collectAllObjects(self):
        room_result = RoomResult(self.target_objects)
        current_room_obj = self.rooms[self.start_room]

        self.collect_rec(room_result, self.rooms,
                         current_room_obj)
        return room_result
