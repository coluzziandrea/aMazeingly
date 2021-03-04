class Room:

    north = -1
    south = -1
    east = -1
    west = -1

    objects = []

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def hasAnyObject(self):
        return len(self.objects) > 0

    def addObject(self, val):
        self.objects.append(val)

    def collectTargetObjects(self, targets):
        return list(filter(lambda x:  x in targets, self.objects))
