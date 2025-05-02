import renpy

from game.scripts.exception.RenPyException_ren import RenPyException
from game.scripts.image_ren import show_camera
from game.scripts.screen_ren import call_screen
from game.scripts.trial_ren import effect_traveler_pointed, effect_traveler_thumped
from game.scripts.utils_ren import game_pause, get_store

"""renpy
init -1 python:
"""

from typing import Dict


def effect(name: str, args: Dict = None):
    if args is None:
        args = {}

    if name == "开始证言":
        call_screen("screen_start_testimony", _layer="sticker", name="start_testifying")
    elif name == "开始讯问":
        call_screen("screen_start_testimony", _layer="sticker", name="start_interrogate")
    elif name == "黑屏转场":
        renpy.transition(get_store()["transition_fade"])
        game_pause(0.5)
    elif name == "旅行者拍桌":
        effect_traveler_thumped(float(args.get("delay", "0.05")))
    elif name == "旅行者凌空一指":
        effect_traveler_pointed()
    elif name == "镜头抖动":
        show_camera("camera_special_shake", reset=False)
    elif name in ["反对", "看这个", "等一下"]:
        if args.get("play_sound") != "False":
            renpy.play(f"audio/{name}_{args.get('name')}.wav", channel="audio")
        call_screen("screen_shout", _layer="sticker", mode=name, character="旅行者")
    elif name == "灵感":
        call_screen("screen_inspiration", _layer="sticker")
    else:
        raise RenPyException("未定义的效果：" + name)
