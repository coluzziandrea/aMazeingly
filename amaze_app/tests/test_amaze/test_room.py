import pathlib
import pytest


from amaze.room import Room


def test_init():
    room = Room()
    assert room is not None
