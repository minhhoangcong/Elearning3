import os
import sys

import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from backend.server import GameServer


def test_all_same_choice_draw():
    server = GameServer()
    p1, p2 = object(), object()
    choices = {"rock": [p1, p2]}
    results = server.compare_choices(choices)
    assert results == {p1: 'draw', p2: 'draw'}


def test_rock_beats_scissors():
    server = GameServer()
    rock1, rock2, scissors1 = object(), object(), object()
    choices = {"rock": [rock1, rock2], "scissors": [scissors1]}
    results = server.compare_choices(choices)
    assert results[rock1] == 'win'
    assert results[rock2] == 'win'
    assert results[scissors1] == 'lose'


def test_all_three_choices_draw():
    server = GameServer()
    rock = object()
    paper = object()
    scissors = object()
    choices = {"rock": [rock], "paper": [paper], "scissors": [scissors]}
    results = server.compare_choices(choices)
    assert all(result == 'draw' for result in results.values())
    assert set(results.keys()) == {rock, paper, scissors}
