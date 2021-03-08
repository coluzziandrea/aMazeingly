class Room:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.north = -1
        self.south = -1
        self.east = -1
        self.west = -1
        self._objects = []

    def hasNorth(self):
        return self.north != -1

    def hasSouth(self):
        return self.south != -1

    def hasEast(self):
        return self.east != -1

    def hasWest(self):
        return self.west != -1

    def hasNorthToVisit(self, room_result):
        return self.hasNorth() and not room_result.isRoomVisited(self.north)

    def hasSouthToVisit(self, room_result):
        return self.hasSouth() and not room_result.isRoomVisited(self.south)

    def hasEastToVisit(self, room_result):
        return self.hasEast() and not room_result.isRoomVisited(self.east)

    def hasWestToVisit(self, room_result):
        return self.hasWest() and not room_result.isRoomVisited(self.west)

    def hasAnyObject(self):
        return len(self._objects) > 0

    def addObject(self, val):
        self._objects.append(val)

    def hasTargetObject(self, targets):
        return any(item in targets for item in self._objects)

    def collectTargetObject(self, targets):
        for item in targets:
            if item in self._objects:
                return item
        return None

    def hasConnectedRooms(self):
        return self.north != -1 or self.south != -1 or self.west != -1 or self.east != -1

    def visit(self, room_result):

        print("Room: Visiting room named '{}'".format(self.name))

        collected = self.collectTargetObject(room_result.getRemainingTargets())
        if collected:
            room_result.addCollectedObject(collected)
            room_result.addVisitedRoom(self.id, self.name, collected)
        else:
            room_result.addVisitedRoom(self.id, self.name)

    def hasRoomsToVisit(self, room_result):
        if not self.hasConnectedRooms():
            return False

        return self.hasNorthToVisit(room_result) or self.hasSouthToVisit(room_result) or self.hasWestToVisit(room_result) or self.hasEastToVisit(room_result)

    def __eq__(self, other):
        """Overrides the default implementation"""
        if not isinstance(other, Room):
            return False

        connected_rooms_are_eq = self.north == other.north and self.south == other.south and self.east == other.east and self.west == other.west
        have_same_objects = self._objects == other._objects

        return self.id == other.id and self.name == other.name and connected_rooms_are_eq and have_same_objects
