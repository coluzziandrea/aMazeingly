import pytest


from amaze.room import Room


def test_init():
    room = Room(1, "Foo Room")
    assert room is not None
    assert room.id == 1
    assert room.name == "Foo Room"


def test_connected_rooms():
    room = Room(1, "Foo Room")
    assert not room.hasNorth()
    assert not room.hasSouth()
    assert not room.hasEast()
    assert not room.hasWest()

    assert not room.hasConnectedRooms()

    room.north = 10
    room.south = 20
    room.east = 30
    room.west = 40

    assert room.hasNorth()
    assert room.hasSouth()
    assert room.hasEast()
    assert room.hasWest()

    assert room.north == 10
    assert room.south == 20
    assert room.east == 30
    assert room.west == 40

    assert room.hasConnectedRooms()


def test_objects():
    room = Room(1, "Foo Room")

    assert not room.hasAnyObject()

    room.addObject("Foo Object")

    assert room.hasAnyObject()

    assert room.hasTargetObject(["Foo Object", "Test Object"])

    assert "Foo Object" == room.collectTargetObject(
        ["Foo Object", "Test Object"])


def test_visit():
    room = Room(1, "Foo Room")
    room.addObject("Foo Object")

    already_visited = set(2, 3, 4)
