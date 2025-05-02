import renpy

from game.scripts.status_ren import exit_state, Status

"""renpy
init -1 python:
"""

from typing import Optional, Dict, TypeVar, Any


def game_pause(time):
    exit_state(Status.dialogue)
    renpy.pause(time, hard=True)


def get_store():
    return renpy.python.store_dicts["store"]


def to_int(string: str) -> Optional[int]:
    try:
        return int(string)
    except TypeError:
        return None


def array_contain(array, target_array) -> bool:
    for element in target_array:
        if element in array:
            return True
    return False


T = TypeVar('T')


def move_element(original_dict: Dict[T, Any], key: T, new_pos: int) -> Dict[T, Any]:
    if key not in original_dict:
        raise KeyError(f"Key '{key}' not found in the original dictionary.")

    value = original_dict[key]

    del original_dict[key]

    items = list(original_dict.items())
    items.insert(new_pos, (key, value))

    original_dict.clear()
    original_dict.update(items)

    return original_dict
