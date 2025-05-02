import renpy

from game.scripts.achievement_ren import grant_achievement
from game.scripts.cg_ren import hide_cg, show_cg
from game.scripts.choices_ren import show_choices, handle_choices_option, handle_return
from game.scripts.effect_ren import effect
from game.scripts.exhibit_ren import remove_exhibit
from game.scripts.game_ren import TYPE_COMMENT, TYPE_COMMEND, TYPE_NARRATION, TYPE_SCENE, TYPE_STATUS_CANCEL, TYPE_STATUS, \
    TYPE_PAUSE, TYPE_SHOW, TYPE_CHOICES, TYPE_CHOICES_OPTION, TYPE_GET_EXHIBIT, TYPE_SHOW_EXHIBIT, TYPE_SHOW_INDICATOR, \
    TYPE_HIDE_CHARACTER, TYPE_EFFECT, TYPE_DIALOGUE, TYPE_RETURN, TYPE_MUSIC, TYPE_SHOW_CHARACTER, TYPE_HIDE, TYPE_MUSIC_STOP, \
    TYPE_HIDE_EXHIBIT, TYPE_TODO, TYPE_SHOW_CG, TYPE_HIDE_CG, TYPE_LOCATION, game, TYPE_REMOVE_EXHIBIT, TYPE_ACHIEVEMENT
from game.scripts.image_ren import game_show
from game.scripts.music_ren import play_music, stop_music
from game.scripts.screen_ren import show_get_exhibit, show_show_exhibit, hide_show_exhibit, show_time_indicator, disable_menu, \
    enable_menu, call_screen
from game.scripts.statement_ren import handle_narrate, handle_scene, handle_hide_character, handle_dialogue
from game.scripts.status_ren import Status, has_status, exit_state, handle_state_into, handle_state_exit
from game.scripts.exception.RenPyException_ren import RenPyException
from game.scripts.utils_ren import to_int, game_pause, get_store

"""renpy
init -1 python:
"""

import re
from typing import List


# 语句匹配正则、语句类型、语句状态（可选）
PATTERN_LIST = [(re.compile(p[0]),) + p[1:] for p in [
    ("^//.*$", TYPE_COMMENT),  # 注释
    ("^\\$ ?(?P<commend>.+)$", TYPE_COMMEND),  # 命令
    ("^——(?P<text>.+)$", TYPE_NARRATION, Status.narration),  # 黑屏旁白
    ("^status cancel (?P<status>\\S+)(?P<options>.+?)?$", TYPE_STATUS_CANCEL),  # 取消状态
    ("^status (?P<status>\\S+)(?P<options>.+?)?$", TYPE_STATUS),  # 进入状态
    ("^pause (?P<time>.+)$", TYPE_PAUSE),  # 暂停
    ("^show_character (?P<image>.+?)(?:(?: zorder=(?P<zorder>\\d+))|(?: at=(?P<at>\\S+))|(?: layer=(?P<layer>\\S+)))*?$",
     TYPE_SHOW_CHARACTER),  # 显示立绘
    ("^show (?P<image>.+?)(?:(?: zorder=(?P<zorder>\\d+))|(?: at=(?P<at>\\S+))|(?: layer=(?P<layer>\\S+)))*?$", TYPE_SHOW),
    # 显示图片
    ("^hide (?P<image>.+?)(?:(?: layer=(?P<layer>\\S+)))*?$", TYPE_HIDE),  # 隐藏图片

    ("^（选项-(?P<type>.+?)）(?P<options>.+?)?$", TYPE_CHOICES),  # 选项
    ("^-> (?P<option>.+)$", TYPE_CHOICES_OPTION),  # 判断选项
    ("^return ?(?P<options>.+?)?$", TYPE_RETURN),  # 回到上一个选项处

    ("^（成就 (?P<achievement>\\S+)）$", TYPE_ACHIEVEMENT),  # 获得成就
    ("^（位置 (?P<location>\\S+)）$", TYPE_LOCATION),  # 剧本位置，播放配音用
    ("^（场景 (?P<scene>\\S+)(?P<options>.+?)?）$", TYPE_SCENE),  # 切换场景
    ("^（CG (?P<name>\\S+)(?P<options>.+?)?）$", TYPE_SHOW_CG),  # 显示CG
    ("^（隐藏CG(?P<options>.+?)?）$", TYPE_HIDE_CG),  # 隐藏CG
    ("^（(?:音乐|音效) \"(?P<name>.+?)\"(?P<options>.+?)?）$", TYPE_MUSIC),  # 播放音乐
    ("^（停止播放(?: (?P<options>.+?))?）$", TYPE_MUSIC_STOP),  # 停止播放
    ("^（获得证据 (?P<exhibit>\\S+)(?P<options>.+?)?）$", TYPE_GET_EXHIBIT),  # 获得证据
    ("^（移除证据 (?P<exhibit>\\S+)(?P<options>.+?)?）$", TYPE_REMOVE_EXHIBIT),  # 移除证据
    ("^（证据框 (?P<exhibit>\\S+)(?P<options>.+?)?）$", TYPE_SHOW_EXHIBIT),  # 展示证据框
    ("^（隐藏证据框）$", TYPE_HIDE_EXHIBIT),  # 隐藏证据框
    ("^（状态栏 (?P<state>.+)）$", TYPE_SHOW_INDICATOR),  # 显示时间
    ("^（立绘 (?P<mode>hide|recover|clear)）$", TYPE_HIDE_CHARACTER),  # 隐藏/显示/清除立绘
    ("^（效果 (?P<effect>\\S+) ?(?P<options>.+?)?）$", TYPE_EFFECT),  # 显示特效
    ("^（TODO (?P<todo>.+)）$", TYPE_TODO),  # 显示TODO
    ("^(?:(?P<character>.+?)(?P<show_img>\\*)?(?:（(?P<tag>.+?)）)?(?:<(?P<options>.+?)>)?：)?(?P<text>.+)$", TYPE_DIALOGUE),  # 对话
]]


def get_next_statement(index, story_texts, lines) -> (int, int):
    statement_index = -1  # 该语句index（多行语句以首行为准）
    while True:
        line = story_texts[index].strip("\n")

        # 跳过空行
        if line.lstrip() == "":
            index += 1
            continue

        (indentation_level, line) = strip_space(line)
        if len(lines) == 0:
            # 首行时处理
            if indentation_level > game.indentation_level:
                if has_status(Status.enter_closure):
                    game.indentation_level = indentation_level
                    exit_state(Status.enter_closure)
                else:
                    index += 1
                    continue
            elif indentation_level < game.indentation_level:
                game.indentation_level = indentation_level

            statement_index = index

        index += 1
        if line.endswith(" \\"):
            lines.append(line.strip(" \\"))
        else:
            lines.append(line)
            break
    return statement_index, index


def parse_single(statement_index: int, statements: List[str]):
    statements_type, target_status, args = match_statements_type(statements[0])
    # 处理固定格式options
    # 正在使用这一字段：TYPE_CHOICES、TYPE_DIALOGUE、TYPE_RETURN、TYPE_MUSIC、TYPE_MUSIC_STOP、TYPE_GET_EXHIBIT、TYPE_REMOVE_EXHIBIT、
    # TYPE_SHOW_EXHIBIT、TYPE_SHOW_CG、TYPE_HIDE_CG、TYPE_SCENE
    if args.get("options") is not None:
        options = [arg.split("=") for arg in args.get("options").strip().split(" ")]
        args.update({o[0]: o[1] for o in options})

    # 多行语句处理
    if len(statements) > 1:
        if statements_type == TYPE_DIALOGUE or statements_type == TYPE_NARRATION:
            # 对话类型，多行文本用{p}拼接
            args["text"] += ("{p=1.5}" + "{p=1.5}".join(statements[1:]))

    # 游戏状态切换
    if target_status is not None and target_status != game.status:
        handle_state_into(target_status, args)

    # 语句处理
    if statements_type == TYPE_COMMEND:
        command = args.get("commend")
        regex = re.compile(r'[\w_]+_ren\.(.+)')
        match = regex.search(command)
        if match:
            replacement = match.group(1)
            command = regex.sub(replacement, command)
        exec(command)
    elif statements_type == TYPE_NARRATION:
        handle_narrate(args.get("text"))
    elif statements_type == TYPE_STATUS_CANCEL:
        handle_state_exit(Status[args.get("status")], args)
    elif statements_type == TYPE_PAUSE:
        game_pause(float(args.get("time")))
    elif statements_type == TYPE_SHOW_CHARACTER:
        game_show(args.get("image"), zorder=to_int(args.get("zorder")),
                  at_list=args.get("at").split(",") if args.get("at") else [], layer=args.get("layer"))
    elif statements_type == TYPE_SHOW:
        renpy.show(args.get("image"), zorder=to_int(args.get("zorder")), layer=args.get("layer"),
                   at_list=[get_store()[at] for at in args.get("at").split(",")] if args.get("at") else [])
    elif statements_type == TYPE_HIDE:
        renpy.hide(args.get("image"), layer=args.get("layer"))

    elif statements_type == TYPE_CHOICES:
        show_choices(args.get("type"), statement_index, args.get("avatar"), args.get("tip"), statements[1:], args)
    elif statements_type == TYPE_CHOICES_OPTION:
        handle_choices_option(args.get("option"))
    elif statements_type == TYPE_RETURN:
        handle_return(int(args.get("stack")) if args.get("stack") else 1,
                      int(args.get("offset")) if args.get("offset") else 0, args.get("fade_to_witness"))

    elif statements_type == TYPE_ACHIEVEMENT:
        grant_achievement(args.get("achievement"))
    elif statements_type == TYPE_LOCATION:
        game.voice_location = args.get("location")
    elif statements_type == TYPE_SCENE:
        handle_scene(args.get("scene"), args.get("transition"), int(args.get("pause")) if args.get("pause") else None)
    elif statements_type == TYPE_SHOW_CG:
        show_cg(args.get("name"), args.get("part", "1"), args.get("transition"))
    elif statements_type == TYPE_HIDE_CG:
        hide_cg(args.get("transition"), int(args.get("pause")) if args.get("pause") else None)
    elif statements_type == TYPE_MUSIC:
        play_music(args.get("name"), args.get("channel"), float(args.get("fade")) if args.get("fade") else None,
                   args.get("loop") != "False", float(args.get("volume")) if args.get("volume") else None)
    elif statements_type == TYPE_MUSIC_STOP:
        stop_music(args.get("channel"), float(args.get("fade")) if args.get("fade") else None)
    elif statements_type == TYPE_GET_EXHIBIT:
        show_get_exhibit(args)
    elif statements_type == TYPE_REMOVE_EXHIBIT:
        remove_exhibit(args)
    elif statements_type == TYPE_SHOW_EXHIBIT:
        show_show_exhibit(args.get("exhibit"), args.get("is_full") == "True")
    elif statements_type == TYPE_HIDE_EXHIBIT:
        hide_show_exhibit()
    elif statements_type == TYPE_SHOW_INDICATOR:
        show_time_indicator(args.get("state"))
    elif statements_type == TYPE_HIDE_CHARACTER:
        handle_hide_character(args.get("mode"))
    elif statements_type == TYPE_EFFECT:
        effect(args.get("effect"), args)
    elif statements_type == TYPE_TODO:
        renpy.notify(args.get("todo"))
    elif statements_type == TYPE_DIALOGUE:
        text = args.get("text")
        if text.rfind("*") != -1 and text.rfind("*") != len(text) - 1:
            text = text[:text.rfind("*")]

        extra_args = {}
        if "zorder" in args:
            extra_args["zorder"] = int(args.get("zorder"))
        if "default_at" in args:
            extra_args["default_at"] = args.get("default_at")
        if "transition" in args:
            extra_args["transition"] = args.get("transition")
        if "pause" in args:
            extra_args["pause"] = args.get("pause")
        if "reset_scene" in args:
            extra_args["reset_scene"] = args.get("reset_scene")
        if "smooth" in args:
            extra_args["smooth"] = args.get("smooth")
        if "callback" in args:
            extra_args["callback"] = args.get("callback")

        handle_dialogue(text, args.get("character"), args.get("tag"), args.get("img"), args.get("name"), args.get("at"),
                        args.get("interact") != "False", args.get("show_img") != "*", **extra_args)


# 匹配语句类型
def match_statements_type(text) -> (str, str, dict):
    for pattern in PATTERN_LIST:
        match = pattern[0].match(text)
        if match is None:
            continue

        # 切换状态语句，动态返回状态
        if pattern[1] == TYPE_STATUS:
            return pattern[1], Status[match.groupdict()["status"]], match.groupdict()
        return pattern[1], pattern[2] if len(pattern) > 2 else None, match.groupdict()
    raise RenPyException("未匹配到语句规则：" + text)


# 删去语句的缩进，并返回缩进数
def strip_space(text: str) -> (int, str):
    indentation_level = 0
    for c in text:
        if c == " ":
            indentation_level += 1
        else:
            break
    return indentation_level, text.lstrip()


def not_usage():
    # 避免以下import被优化
    disable_menu
    enable_menu
    call_screen
