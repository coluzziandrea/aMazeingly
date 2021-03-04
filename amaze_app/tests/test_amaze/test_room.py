import pathlib
import pytest


from amaze.room import Room


def test_init():
    room = Room(1, "Foo Room")
    assert room is not None
    assert room.id == 1
    assert room.name == "Foo Room"


def test_getters_setters():
    room = Room(1, "Foo Room")
    assert room.north == -1
    assert room.south == -1
    assert room.east == -1
    assert room.west == -1

    room.north = 10
    room.south = 20
    room.east = 30
    room.west = 40

    assert room.north == 10
    assert room.south == 20
    assert room.east == 30
    assert room.west == 40


def test_objects():
    room = Room(1, "Foo Room")

    assert not room.hasAnyObject()

    room.addObject("Foo Object")

    assert room.hasAnyObject()

    assert "Foo Object" in room.collectTargetObjects(
        ["Foo Object", "Test Object"])
