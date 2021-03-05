from unittest import TestCase
import pathlib
import pytest
import os
import json


from amaze.room import Room
from amaze.room_maker import create_rooms_from_json


def expected_rooms_1():
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


def expected_rooms_2():
    result = {}

    room = Room(1, "Hallway")
    room.north = 2
    room.east = 7
    result[1] = room

    room = Room(2, "Dining Room")
    room.south = 1
    room.west = 3
    room.east = 4
    room.north = 5
    result[2] = room

    room = Room(3, "Kitchen")
    room.east = 2
    room.addObject("Knife")
    result[3] = room

    room = Room(4, "Sun Room")
    room.west = 2
    room.north = 6
    room.south = 7
    result[4] = room

    room = Room(5, "Bedroom")
    room.east = 6
    room.south = 2
    room.addObject("Pillow")
    result[5] = room

    room = Room(6, "Bathroom")
    room.west = 5
    room.south = 4
    result[6] = room

    room = Room(7, "Living room")
    room.west = 1
    room.north = 4
    room.addObject("Potted Plant")
    result[7] = room

    return result


def open_test_json(file_name):
    parent_dir = os.sep.join(__file__.split(os.sep)[:-1])
    data_dir = os.path.join(parent_dir, "data")
    with open(os.path.join(data_dir, file_name), 'rt') as f:
        return json.load(f)


testdata = [
    (open_test_json("input_map_example_1.json"),
     expected_rooms_1()),
    (open_test_json("input_map_example_2.json"),
     expected_rooms_2())
]


@pytest.mark.parametrize("example_json,expected_rooms", testdata)
def test_create_rooms_from_json(example_json, expected_rooms):
    result_rooms = create_rooms_from_json(example_json)

    TestCase().assertDictEqual(expected_rooms, result_rooms)


def test_create_rooms_from_empty():
    assert len(create_rooms_from_json({})) == 0
