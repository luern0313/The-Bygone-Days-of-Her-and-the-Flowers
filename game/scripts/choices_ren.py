import renpy

from game.scripts.effect_ren import effect
from game.scripts.exception.RenPyException_ren import RenPyException
from game.scripts.game_ren import game
from game.scripts.screen_ren import call_screen
from game.scripts.statement_ren import handle_dialogue
from game.scripts.status_ren import Status, into_state, exit_state, handle_state_into, handle_state_exit
from game.scripts.text_ren import pretreatment_other
from game.scripts.utils_ren import game_pause

"""renpy
init -1 python:
"""

from typing import List, Tuple, Dict
from enum import Enum


def show_choices(mode: str, statement_index: int, tip_character: str, tip: str, options: List[str], args: Dict[str, str]):
    mode = next((m for m in ChoicesMode.__members__.values() if m.identifier == mode), None)
    scope = {}
    if mode == ChoicesMode.EXHIBIT or mode == ChoicesMode.OPTION:
        scope.update({"avatar": str(tip_character), "tip": "	" + pretreatment_other(tip, game.display_name_map, space=0)})
    elif mode == ChoicesMode.TOPIC:
        scope.update({"title": pretreatment_other(args.get("title"), game.name_map, space=0),
                      "small_style": args.get("small_style") == "True", "turtle_riddle": args.get("turtle_riddle")})

    if mode.need_interactive:
        options = ["\n".join(["·" + line for line in option.split("\n")]) for option in options]

    choices_index = statement_index + mode.statement_index_offset
    if mode == ChoicesMode.EXHIBIT:
        show_choices_exhibit(scope, handle_options(options), choices_index, args.get("is_shout") != "False")
    elif mode == ChoicesMode.OPTION:
        show_choices_option(scope, handle_options(options), choices_index)
    elif mode == ChoicesMode.GENERAL_INTERROGATE:
        handle_choices_general_interrogate(choices_index)
    elif mode == ChoicesMode.INTERROGATE:
        show_choices_interrogate(choices_index, args.get("previous") != "False", args.get("next"))
    elif mode == ChoicesMode.VARIABLE:
        handle_choices_variable(args.get("var").split("、"), choices_index)
    elif mode == ChoicesMode.SCENE:
        show_choices_scene(handle_options(options), choices_index)
    elif mode == ChoicesMode.TOPIC:
        show_choices_topic(scope, handle_options(options), choices_index)


class ChoicesMode(Enum):
    EXHIBIT = ("证据", True)
    OPTION = ("选项", True)
    GENERAL_INTERROGATE = ("讯问", False)
    INTERROGATE = ("单句讯问", False, -1)
    VARIABLE = ("变量", False)
    SCENE = ("场景", True)
    TOPIC = ("话题", True)

    def __init__(self, identifier: str, need_interactive: bool, statement_index_offset: int = 0):
        self.identifier = identifier
        self.need_interactive = need_interactive
        # 部分类型的选项语句位置有所不同，保存位置时需要加上offset
        self.statement_index_offset = statement_index_offset


# 选择证物
def show_choices_exhibit(scope: Dict[str, str], options: List[Tuple[str, renpy.ui.ChoiceReturn]], choices_index: int, is_shout: bool = True):
    append_selected_options(renpy.display_menu(options, scope=scope, screen="screen_choices_exhibit"), choices_index)
    if is_shout:
        effect("看这个", {"name": "旅行者"})
    game_pause(0.5)


# 选择文本选项
def show_choices_option(scope: Dict[str, str], options: List[Tuple[str, renpy.ui.ChoiceReturn]], choices_index: int):
    position = 0
    for option in options:
        option[1].kwargs["position"] = position
        position += 1
        if "alone_line" in option[1].kwargs and option[1].kwargs["alone_line"] == "True":
            position += 1
    append_selected_options(renpy.display_menu(options, scope=scope, screen="screen_choices_options"), choices_index)
    game_pause(0.5)


# 庭审中讯问
def handle_choices_general_interrogate(choices_index: int):
    # 进入讯问时设置默认出现第一句
    # 讯问时会跳转回讯问开头，这种情况下不设置
    # 避免上一次讯问的状态延续到下一个讯问，会判断行号，不匹配会重新设置
    if (game.indentation_level not in game.statement_choices or
            game.statement_choices[game.indentation_level][0] != choices_index):
        append_selected_options("第一句", choices_index)


# 庭审中单句讯问
def show_choices_interrogate(choices_index: int, previous: bool = True, following: str = None):
    if not following:
        following = "下一句"
    choice = call_screen("screen_trial_interrogate", _layer="screens", _zorder=100, previous=previous, following=following)
    append_selected_options(choice, choices_index)
    if choice == "追问":
        effect("等一下", {"name": "旅行者"})


# 根据变量判断分支
def handle_choices_variable(variables: List[str], choices_index: int):
    result = "True"
    for variable in variables:
        if game.variable_list[int(variable)] == 0:
            result = "False"
    append_selected_options(result, choices_index)


# 选择场景元素
def show_choices_scene(options: List[Tuple[str, renpy.ui.ChoiceReturn]], choices_index: int):
    append_selected_options(renpy.display_menu(options, screen="screen_choices_scene"), choices_index)
    game_pause(0.5)


# 选择话题
def show_choices_topic(scope: Dict[str, str], options: List[Tuple[str, renpy.ui.ChoiceReturn]], choices_index: int):
    append_selected_options(renpy.display_menu(options, scope=scope, screen="screen_choices_topic"), choices_index)
    game_pause(0.5)


# 拼装选项数据
def handle_options(options: List[str]) -> List[Tuple[str, renpy.ui.ChoiceReturn]]:
    choices = []
    for option in options:
        name = option.split(" ")[1]
        kwargs = {"shown_name": pretreatment_other(name, game.colored_map, space=0)}
        if len(option.split(" ")) > 2:
            kwargs.update({o.split("=")[0]: o.split("=")[1] for o in option.split(" ")[2:]})
            if "rule" in kwargs and not calculate_variable(kwargs["rule"]):
                continue
            if "desc" in kwargs:
                kwargs["desc"] = "\n".join(["·" + pretreatment_other(line, game.colored_map, space=0)
                                            for line in kwargs["desc"].split("\\n")])
        choices.append((name, renpy.ui.ChoiceReturn(name, name, kwargs=kwargs)),)
        print(str(kwargs))
    return choices


# 处理选项语句
def handle_choices_option(option):
    if len(game.statement_choices) == 0:
        raise RenPyException("无历史选项，无法判断选择正确性")

    if game.statement_choices[game.indentation_level][1] in option.split("、"):
        # 选择成功匹配，进入下一个闭包
        into_state(Status.enter_closure)


# 处理return语句
def handle_return(stack: int, offset: int, fade_to_witness: str = None):
    if len(game.statement_choices) == 0:
        raise RenPyException("无历史选项位置，无法跳转")

    # 丢弃大于等于当前语句缩进的选项
    for indentation_level in filter(lambda m: m >= game.indentation_level, list(game.statement_choices.keys())):
        game.statement_choices.pop(indentation_level)

    # 要跳转语句的缩进数
    target_index_indentation_level = list(game.statement_choices.keys())[-stack]
    game.index = game.statement_choices[target_index_indentation_level][0] - offset

    # 回到证人席视角
    if fade_to_witness:
        exit_state(Status.dialogue)
        handle_state_into(Status.narration)
        handle_dialogue("*", fade_to_witness.split("_")[0], fade_to_witness.split("_")[1])
        handle_state_exit(Status.narration)

    # 丢弃大于目标语句缩进的选项
    for indentation_level in filter(lambda m: m > target_index_indentation_level, list(game.statement_choices.keys())):
        game.statement_choices.pop(indentation_level)


# 按照当前语句缩进数，保存当前选择项
def append_selected_options(option: str, choices_index: int):
    game.statement_choices[game.indentation_level] = (choices_index, option)


# 讯问使用，修改当前讯问选择项
def update_interrogate_choice(text: str, indentation_level: int):
    choices_index = game.statement_choices[indentation_level][0]
    game.statement_choices[indentation_level] = (choices_index, text)


def set_variable(index: int, value: int):
    if index < 0 or index >= 12 or value < 0 or value > 100:
        raise RenPyException("变量超过限制值，index=" + str(index) + "，value=" + str(value))
    game.variable_list[index] = value


def calculate_variable(expression: str) -> bool:
    for exp in expression.split("、"):
        target_value = []
        if ":" not in exp:
            # 不指定目标值时，默认为1
            target_value.append(1)
        else:
            target_value += [int(v) for v in exp.split(":")[1].split("|")]

        value = game.variable_list[int(exp.split(":")[0])]
        if value not in target_value:
            return False
    return True


def reset_variable():
    game.variable_list.clear()
    for _ in range(12):
        game.variable_list.append(0)
