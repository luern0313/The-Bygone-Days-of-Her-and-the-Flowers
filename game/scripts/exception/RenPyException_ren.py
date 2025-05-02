from game.scripts.game_ren import game

"""renpy
init -1 python:
"""


class RenPyException(Exception):
    def __init__(self, cause):
        self.cause = cause

    def __str__(self):
        return f"{self.cause}\nindex: {game.index}"
