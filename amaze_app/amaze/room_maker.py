from .room import Room


def get_connected_room_id_or_none(room_obj, attr_key):
    if attr_key in room_obj:
        return room_obj[attr_key]
    else:
        return -1


def create_rooms_from_json(jsonMap):
    """
        Creates a dictionary from the JSON input.

        Elaborates the 'rooms' object of the JSON.

        The dictionary will have the ID of the rooms as key 
        and the room object itself as value.

        Returns empty dictionary if the input is not valid
    """

    if "rooms" not in jsonMap:
        return {}

    rooms = jsonMap["rooms"]

    result = {}

    for room in rooms:
        room_id = room["id"]
        room_name = room["name"]

        room_objects = room["objects"]

        result_room = Room(room_id, room_name)

        for room_object in room_objects:
            result_room.addObject(room_object["name"])

        result_room.south = get_connected_room_id_or_none(room, "south")
        result_room.north = get_connected_room_id_or_none(room, "north")
        result_room.west = get_connected_room_id_or_none(room, "west")
        result_room.east = get_connected_room_id_or_none(room, "east")

        result[room_id] = result_room

    return result
