import sys
import json

from .room import Room
from .room_maker import *


def load_input_json(file_name):
    with open(input_file, 'rt') as f:
        return json.load(f)


print("Number of arguments: {}".format(len(sys.argv)))
print("Argument List: {}".format(str(sys.argv)))


input_file = sys.argv[1]
start_room = sys.argv[2]

print("Starting aMazeAPP, Input file: '{}', start room ID: {}".format(
    input_file, start_room))


input_map = load_input_json(input_file)

print("Indexing rooms by ID...")

rooms_dict = create_rooms_from_json(input_map)
