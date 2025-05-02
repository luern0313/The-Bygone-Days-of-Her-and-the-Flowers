import renpy

from game.scripts.game_ren import game, Exhibit
from game.scripts.text_ren import pretreatment_other

"""renpy
init -1 python:
"""


def add_exhibit(name: str, image: str, desc: str, is_full: bool, is_update: bool):
    ex_list = list(filter(lambda e: e.name == name, game.exhibit_list))
    if not is_update and len(ex_list) == 0:
        game.exhibit_list.append(Exhibit(name, image, desc, is_full))
    else:
        if ex_list is not None and len(ex_list) > 0:
            ex_list[0].update(name, image, desc, is_full)


def remove_exhibit(args: dict):
    name = pretreatment_other(args.get("exhibit"), game.colored_map, space=0)
    for i in range(len(game.exhibit_list) - 1, -1, -1):
        if game.exhibit_list[i].name == name:
            del game.exhibit_list[i]
