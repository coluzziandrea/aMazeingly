import sys
import json

from .room import Room
from .room_map import RoomMap
from .room_maker import *


def get_target_objects(args):
    result = []
    for index in range(3, len(args)):
        result.append(args[index])
    return result


def load_input_json(file_name):
    with open(input_file, 'rt') as f:
        return json.load(f)


print("app: Init...")

input_file = sys.argv[1]
start_room = int(sys.argv[2])

print("app: Starting aMazeAPP, Input file: '{}', start room ID: {}".format(
    input_file, start_room))

target_objects = get_target_objects(sys.argv)

print("app: target objects: {}".format(target_objects))

input_map = load_input_json(input_file)

print("app: Indexing rooms by ID...")

rooms_dict = create_rooms_from_json(input_map)


print("app: Creating map object...")
room_map = RoomMap(rooms_dict, start_room, target_objects)


print("app: Calling collectAllObjects method on map...")
result_map = room_map.collectAllObjects()


print("app: printing result...")
for line in result_map.getResultLines():
    print(line)


print("app: Finish.")
