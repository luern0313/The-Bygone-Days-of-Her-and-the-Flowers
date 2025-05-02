import renpy

from game.scripts.game_ren import game
from game.scripts.music_ren import pause_ambient_sound, resume_ambient_sound
from game.scripts.screen_ren import resume_time_indicator, hide_time_indicator
from game.scripts.statement_ren import recover_character, hide_character
from game.scripts.utils_ren import get_store, game_pause

"""renpy
init -2 python:
"""

from typing import Optional

from enum import Enum, unique


# 游戏状态
@unique
class Status(Enum):
    dialogue = 1 << 0  # 对话，默认状态
    narration = 1 << 1  # 黑屏旁白
    time_indicator_showing = 1 << 2  # 左上角时间、证据数UI是否正在显示
    time_indicator_extending = 1 << 3  # 左上角时间、证据数UI是否展开
    is_evening = 1 << 4  # 是否夜晚，左上角时间、证据数UI用

    hide_character = 1 << 5  # 是否临时隐藏立绘，突出背景
    enter_closure = 1 << 6  # 是否进入下一个闭包

    in_trial = 1 << 7  # 是否正在庭审中
    in_testimony = 1 << 8  # 庭审-证言中
    in_interrogate = 1 << 9  # 庭审-讯问中

    in_thinking = 1 << 10  # 思考中，背景变暗
    in_memory = 1 << 11  # 思考中，背景变暗


def has_status(target_status: Status) -> bool:
    return "game" in globals() and (game.status & target_status.value) > 0


# 退出状态
def handle_state_exit(t: Status, args: Optional[dict] = None):
    if args is None:
        args = {}
    if not has_status(t):
        return

    print("exit state: " + str(t) + ", current state: " + bin(game.status))
    if t == Status.narration:
        renpy.hide("black", layer="sticker")
        renpy.with_statement(get_store()[args.get("transition", "transition_fade")])
        # 恢复环境音
        resume_ambient_sound()
    elif t == Status.hide_character:
        recover_character()
    elif t == Status.in_trial:
        renpy.layer_at_list(get_store()["camera_special_default"], layer="master", camera=True, reset=True)
    elif t == Status.in_testimony:
        renpy.hide_screen("screen_trial_in_testimony", layer="sticker")
    elif t == Status.in_interrogate:
        renpy.hide_screen("screen_trial_in_testimony", layer="sticker")
        renpy.free_memory()
    elif t == Status.in_thinking:
        renpy.hide("black")
        # 恢复环境音
        resume_ambient_sound()
        game_pause(0.5)
    elif t == Status.in_memory:
        renpy.hide("memory", layer="sticker")
        renpy.layer_at_list([], layer="master", camera=False, reset=True)
        renpy.layer_at_list([], layer="cg", camera=False, reset=True)
        renpy.layer_at_list([], layer="screens", camera=False, reset=True)
        # 恢复环境音
        resume_ambient_sound()
        # 恢复时间证据ui
        resume_time_indicator()

    exit_state(t)

    if t == Status.is_evening:
        renpy.restart_interaction()


# 进入状态
def handle_state_into(t: Status, args: Optional[dict] = None):
    if args is None:
        args = {}
    if has_status(t):
        return

    print("into state: " + str(t) + ", current state: " + bin(game.status))
    if t == Status.narration:
        renpy.show("black", layer="sticker")
        renpy.with_statement(get_store()[args.get("transition", "transition_fade")])
        exit_state(Status.dialogue)
        # 暂停环境音
        pause_ambient_sound()
    elif t == Status.hide_character:
        hide_character()
    elif t == Status.in_trial:
        game.trial_position = None
        game.trial_image_liat.clear()
    elif t == Status.in_testimony:
        renpy.show_screen("screen_trial_in_testimony", _layer="sticker", name="in_testimony")
        game_pause(0.5)
    elif t == Status.in_interrogate:
        renpy.show_screen("screen_trial_in_testimony", _layer="sticker", name="in_interrogate")
    elif t == Status.in_thinking:
        game_pause(0.2)
        at = "bg_special_thinking_trial" if has_status(Status.in_trial) else "bg_special_thinking"
        renpy.show("black", at_list=[get_store()[at]], layer=None, zorder=25)
        # 暂停环境音
        pause_ambient_sound()
        game_pause(0.8)
    elif t == Status.in_memory:
        if args.get("transition", "transition_exposure") != "None":
            renpy.transition(get_store()[args.get("transition", "transition_exposure")])
            renpy.play("audio/闪白.ogg", channel="audio")
        renpy.show("memory", layer="sticker", zorder=100, at_list=[get_store()["bg_transform_appear"]])
        renpy.layer_at_list(get_store()["camera_special_memory"], layer="master", camera=False, reset=True)
        renpy.layer_at_list(get_store()["camera_special_memory"], layer="cg", camera=False, reset=True)
        if args.get("dialogue_effect") != "False":
            renpy.layer_at_list(get_store()["camera_special_memory"], layer="screens", camera=False, reset=True)
        # 暂停环境音
        pause_ambient_sound()
        # 临时隐藏时间证据ui
        hide_time_indicator()

    into_state(t)

    if t == Status.is_evening:
        renpy.restart_interaction()


def exit_state(t: Status):
    game.status &= ~t.value


def into_state(t: Status):
    game.status |= t.value
