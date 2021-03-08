import pytest
from unittest import TestCase

from amaze.room_map import RoomMap
from amaze.room import Room
from amaze.room_result import RoomResult


def input_rooms_1():
    rooms = {}

    room = Room(1, "Foo Room")
    room.south = 2
    room.addObject("Foo Obj")
    rooms[1] = room

    room = Room(2, "Test Room")
    room.north = 1
    room.addObject("Test Obj")
    rooms[2] = room

    return rooms


def testdata_1():
    exp_result = RoomResult(["Test Obj"])
    exp_result.addVisitedRoom(1, "Foo Room")
    exp_result.addVisitedRoom(2, "Test Room", "Test Obj")
    return (input_rooms_1(), 1, ["Test Obj"], exp_result)


def input_rooms_2():
    result = {}

    room = Room(1, "Hallway")
    room.north = 2
    result[1] = room

    room = Room(2, "Dining Room")
    room.south = 1
    room.west = 3
    room.east = 4
    result[2] = room

    room = Room(3, "Kitchen")
    room.east = 2
    room.addObject("Knife")
    result[3] = room

    room = Room(4, "Sun Room")
    room.west = 2
    room.addObject("Potted Plant")
    result[4] = room

    return result


def testdata_2():
    exp_result = RoomResult(["Knife", "Potted Plant"])
    exp_result.addVisitedRoom(2, "Dining Room")
    exp_result.addVisitedRoom(1, "Hallway")
    exp_result.addVisitedRoom(2, "Dining Room")
    exp_result.addVisitedRoom(3, "Kitchen", "Knife")
    exp_result.addVisitedRoom(2, "Dining Room")
    exp_result.addVisitedRoom(4, "Sun Room", "Potted Plant")
    return (input_rooms_2(), 2, ["Knife", "Potted Plant"], exp_result)


def test_init():

    input_rooms = input_rooms_1()

    target_objects = ["Foo Room"]
    with pytest.raises(Exception):
        RoomMap("notValid", 1, target_objects)
    with pytest.raises(Exception):
        RoomMap(input_rooms, 1, "notValid")

    room_map = RoomMap(input_rooms, 1, target_objects)
    assert room_map is not None
    assert room_map.target_objects == target_objects
    assert room_map.start_room == 1

    TestCase().assertDictEqual(input_rooms, room_map.rooms)


testdata = [
    testdata_1(),
    testdata_2()
]


@pytest.mark.parametrize("room_dict,start_room,target_objects,exp_result", testdata)
def test_collect_all_objects(room_dict, start_room, target_objects, exp_result):
    room_map = RoomMap(room_dict, start_room, target_objects)

    room_result = room_map.collectAllObjects()

    assert room_result == exp_result
