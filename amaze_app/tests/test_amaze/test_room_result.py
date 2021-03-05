import pytest


from amaze.room_result import RoomResult


def test_result():
    room_result = RoomResult()
    assert room_result is not None

    room_result.addVisitedRoom(1, "Foo Room")
    room_result.addVisitedRoom(2, "Test Room", "Test Object")

    result_lines = [
        "ID\tRoom\t\tObject collected",
        "----------------------------------",
        "1\tFoo Room\t\tNone",
        "2\tTest Room\t\tTest Object"

    ]

    room_result_cpy = RoomResult()
    room_result_cpy.addVisitedRoom(1, "Foo Room")
    room_result_cpy.addVisitedRoom(2, "Test Room", "Test Object")

    assert result_lines == room_result.getResultLines()
    assert room_result_cpy == room_result
    assert room_result != "notValid"
