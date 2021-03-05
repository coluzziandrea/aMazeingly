class Room:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.north = -1
        self.south = -1
        self.east = -1
        self.west = -1
        self.objects = []

    def hasAnyObject(self):
        return len(self.objects) > 0

    def addObject(self, val):
        self.objects.append(val)

    def collectTargetObjects(self, targets):
        return list(filter(lambda x:  x in targets, self.objects))

    def getConnectedRoomsToVisit(self, visitedRooms):
        connectedRoomIDs = []

        if self.hasConnectedRooms():
            if self.north not in visitedRooms:
                connectedRoomIDs.append(self.north)
            if self.south not in visitedRooms:
                connectedRoomIDs.append(self.south)
            if self.east not in visitedRooms:
                connectedRoomIDs.append(self.east)
            if self.west not in visitedRooms:
                connectedRoomIDs.append(self.west)

        return connectedRoomIDs

    def hasConnectedRooms(self):
        return self.north != -1 or self.south != -1 or self.west != -1 or self.east != -1

    def __eq__(self, other):
        """Overrides the default implementation"""
        if not isinstance(other, Room):
            return False

        connected_rooms_are_eq = self.north == other.north and self.south == other.south and self.east == other.east and self.west == other.west
        have_same_objects = self.objects == other.objects

        return self.id == other.id and self.name == other.name and connected_rooms_are_eq and have_same_objects
