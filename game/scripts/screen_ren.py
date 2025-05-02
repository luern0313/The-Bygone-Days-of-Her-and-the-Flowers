from typing import Any

import renpy

from game.scripts.exhibit_ren import add_exhibit
from game.scripts.game_ren import game
from game.scripts.status_ren import Status, has_status, handle_state_into, handle_state_exit, exit_state
from game.scripts.text_ren import pretreatment_other
from game.scripts.trial_ren import TrialPosition
from game.scripts.utils_ren import game_pause, get_store

"""renpy
init -1 python:
"""


def show_time_indicator(state: str, is_temp: bool = False):
    if state == "hide":
        if not is_temp:
            exit_state(Status.time_indicator_showing)
        renpy.hide_screen("screen_time_indicator", layer="sticker")
        return

    expend = (state == "expand")
    anim = False
    if has_status(Status.time_indicator_showing):
        if expend and not has_status(Status.time_indicator_extending):
            anim = True
        elif not expend and has_status(Status.time_indicator_extending):
            anim = True
    renpy.show_screen("screen_time_indicator", _layer="sticker", expend=expend, anim=anim)

    if not is_temp:
        handle_state_into(Status.time_indicator_showing)
        if expend:
            handle_state_into(Status.time_indicator_extending)
        else:
            handle_state_exit(Status.time_indicator_extending)


def show_get_exhibit(args: dict):
    show_dialog = args.get("show_dialog") != "False"
    add_to_list = args.get("show_light") != "False"
    is_update = args.get("is_update") == "True"

    exhibit = pretreatment_other(args.get("exhibit"), game.colored_map)
    exhibit_screen = pretreatment_other(args.get("exhibit"), game.colored_map, space=0)
    image = args.get("img")
    desc = pretreatment_other(args.get("desc"), game.display_name_map)
    is_full = args.get("is_full") == "True"

    # 更新保存的证物列表
    if add_to_list:
        add_exhibit(exhibit_screen, image, desc, is_full, is_update)

    if show_dialog:
        call_screen("screen_get_exhibit", _layer="sticker", name=exhibit, img=image, desc=desc,
                    is_update=is_update, is_full=is_full, add_to_list=add_to_list)
        game_pause(0.5)


def show_show_exhibit(exhibit: str, is_full: bool):
    if not has_status(Status.in_trial):
        # 非庭审，根据当前显示的立绘数量确定位置
        position = "show_exhibit_left" if len(game.showing_image_list) == 1 else "show_exhibit_center"
    else:
        # 庭审时根据镜头位置确定位置
        position = "show_exhibit_trial_right" if game.trial_position == TrialPosition.DEFENSE \
            else "show_exhibit_trial_left"

    renpy.show_screen("screen_show_exhibit", position_at=get_store()[position], exhibit=exhibit, is_full=is_full)


def hide_show_exhibit():
    renpy.hide_screen("screen_show_exhibit")


# 调用renpy.call_screen
def call_screen(*args, **kwargs) -> Any:
    disable_menu(args[0])
    result = renpy.call_screen(*args, **kwargs)
    enable_menu()
    return result


# 恢复时间证据ui
def resume_time_indicator():
    if has_status(Status.time_indicator_showing):
        show_time_indicator("collapse", True)


# 临时隐藏时间证据ui
def hide_time_indicator():
    if has_status(Status.time_indicator_showing):
        show_time_indicator("hide", True)


# 临时禁止打开菜单和快捷菜单 游戏开始时和call_screen会调用
# call_screen时，根据screen_name判断是否在白名单中设置右键操作
def disable_menu(screen_name: str = None):
    # 右键打开菜单
    if screen_name not in ["screen_trial_interrogate"]:
        get_store()["_game_menu_screen"] = None

    # 右下角快捷按钮
    if screen_name not in []:
        get_store()["quick_menu"] = False


# 恢复打开菜单和快捷菜单
def enable_menu():
    get_store()["_game_menu_screen"] = "save"
    get_store()["quick_menu"] = True
