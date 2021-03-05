class RoomResult:

    def __init__(self):
        self.visited = []

    def getResultLines(self):
        result = []
        result.append("ID\tRoom\t\tObject collected")
        result.append("----------------------------------")

        for visited_el in self.visited:
            result.append("{}\t{}\t\t{}".format(
                visited_el[0], visited_el[1], visited_el[2]))

        return result

    def addVisitedRoom(self, id, name, obj="None"):
        self.visited.append((id, name, obj))

    def __eq__(self, other):

        if not isinstance(other, RoomResult):
            return False

        return self.visited == other.visited
