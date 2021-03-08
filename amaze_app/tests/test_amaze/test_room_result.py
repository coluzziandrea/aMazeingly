import pytest


from amaze.room_result import RoomResult


def test_result():
    room_result = RoomResult(["Foo", "Test"])
    assert room_result is not None

    room_result.addVisitedRoom(1, "Foo Room")
    room_result.addVisitedRoom(2, "Test Room", "Test Object")

    result_lines = [
        "ID \t Room \t\t Object collected",
        "----------------------------------",
        "1 \t Foo Room \t\t None",
        "2 \t Test Room \t\t Test Object"

    ]

    room_result_cpy = RoomResult(["Foo", "Test"])
    room_result_cpy.addVisitedRoom(1, "Foo Room")
    room_result_cpy.addVisitedRoom(2, "Test Room", "Test Object")

    assert result_lines == room_result.getResultLines()
    assert room_result_cpy == room_result
    assert room_result != "notValid"

    room_result.addCollectedObject("Foo")

    assert room_result.getRemainingTargets() == ["Test"]

    room_result.addPrecedentBranchToFollow(5, 1)

    assert room_result.hasPrecedentBranchToFollow(1)

    assert not room_result.hasPrecedentBranchToFollow(10)

    assert room_result.takePrecedentBranchToFollow(1) == 5

    assert not room_result.hasPrecedentBranchToFollow(1)
