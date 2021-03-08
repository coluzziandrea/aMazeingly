

class RoomResult:

    def __init__(self, targets):
        self.visited = []
        self.collected = []
        self.targets = targets
        self.precedent_branches = {}

    def getResultLines(self):
        result = []
        result.append("ID \t Room \t\t Object collected")
        result.append("----------------------------------")

        for visited_el in self.visited:
            result.append("{} \t {} \t\t {}".format(
                visited_el[0], visited_el[1], visited_el[2]))

        return result

    def addCollectedObject(self, target):
        self.collected.append(target)

    def getRemainingTargets(self):
        return [ele for ele in self.targets if ele not in self.collected]

    def addVisitedRoom(self, room_id, name, obj="None"):
        self.visited.append((room_id, name, obj))

    def isRoomVisited(self, room_id):
        return any(vis[0] == room_id for vis in self.visited)

    def hasPrecedentBranchToFollow(self, room_id):
        return room_id in self.precedent_branches

    def takePrecedentBranchToFollow(self, room_id):
        precedent = self.precedent_branches[room_id]
        del self.precedent_branches[room_id]
        return precedent

    def addPrecedentBranchToFollow(self, room_id, child_id):
        self.precedent_branches[child_id] = room_id

    def __eq__(self, other):

        if not isinstance(other, RoomResult):
            return False

        return self.visited == other.visited
