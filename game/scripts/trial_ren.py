import renpy
import base_character

from game.scripts.game_ren import game
from game.scripts.image_ren import show_camera, game_show
from game.scripts.music_ren import play_music
from game.scripts.statement_ren import handle_background, IMAGE_TAG_DEFAULT
from game.scripts.status_ren import Status, exit_state
from game.scripts.text_ren import pretreatment_text, get_adv_character, handle_voice, get_save_text, update_save_text
from game.scripts.utils_ren import get_store, game_pause

"""renpy
init -1 python:
"""

from renpy.character import ADVCharacter
from typing import List

from enum import Enum


def handle_trial_dialogue(text: str, character: str, image_tag: str, show_image: str, show_name: str, voice_character: str,
                          at_list: List[str], interact: bool, transition: str = "transition_dissolve_15", **kwargs):
    if show_name is None or show_name == "*":
        handle_voice(voice_character, text, interact=interact)
        update_save_text(text)
        text = pretreatment_text(text)
        renpy.say(None, text)
        return

    current_position = game.trial_position
    target_position = get_target_trial_position(character) if show_image != "narrate" else current_position
    is_toggle = False  # 是否有镜头切换效果

    if show_image != "narrate":
        # 切换庭审区域
        if current_position is None or current_position.area != target_position.area:
            if kwargs.get("reset_scene") != "False":
                renpy.scene("master")

            if target_position.area == "below":
                handle_background("庭审_背景", "bg_position_trial", zorder=0)
                handle_background("庭审_前景", "bg_position_trial_foreground", zorder=100)
            elif target_position.area == "above":
                handle_background("审判席_背景", "bg_position_trial", zorder=0)
                handle_background("审判席_前景", "bg_position_trial_judge_foreground", zorder=100)
            elif target_position.area == "side":
                handle_background("助手席_背景", "bg_position_trial", zorder=0)

            if transition != "None":
                renpy.transition(get_store()[transition])

        # 切换视角
        if current_position != target_position:
            if current_position is not None:
                if (current_position.area == target_position.area == "below" and current_position != target_position
                        and kwargs.get("smooth") != "False"):
                    # if abs(current_position.position - target_position.position) == 1:
                    # 证人席到两侧或两侧到证人席才显示过渡动画
                    is_toggle = True

            if target_position == TrialPosition.DEFENSE:
                show_camera("camera_position_trial_defense" + ("_toggle" if is_toggle else ""))
            elif target_position == TrialPosition.WITNESS:
                show_camera("camera_position_trial_witness" + ("_toggle" if is_toggle else ""))
            elif target_position == TrialPosition.PROSECUTION:
                show_camera("camera_position_trial_prosecution" + ("_toggle" if is_toggle else ""))
            else:
                show_camera("camera_position_trial_witness")

            if transition != "None":
                renpy.transition(get_store()[transition])

        if image_tag is None:
            if (target_position.identifier in game.trial_image_liat and
                    game.trial_image_liat[target_position.identifier][0] == show_image):
                image_tag = game.trial_image_liat[target_position.identifier][1]
            else:
                image_tag = IMAGE_TAG_DEFAULT

        if (current_position != target_position or game.trial_image_liat[target_position.identifier][0] !=
                show_image or image_tag != game.trial_image_liat[target_position.identifier][1]):
            # 处理角色立绘、对话
            handle_trial_image(show_image, image_tag, target_position, at_list, transition)

        if current_position != target_position:
            exit_state(Status.dialogue)
            if kwargs.get("pause") != "False":
                game_pause(0.8 if is_toggle else 0.1)

    update_save_text(text)
    text = pretreatment_text(text)
    if text != "*":
        handle_voice(voice_character, text, interact)
        get_adv_character(show_name, **kwargs)(text, interact=interact)

    game.trial_position = target_position


# 庭审位置枚举
class TrialPosition(Enum):
    DEFENSE = ("defense", "below", 1)  # 辩护方
    WITNESS = ("witness", "below", 2)  # 证人席
    PROSECUTION = ("prosecution", "below", 3)  # 指控方

    ASSISTANT = ("assistant", "side",)  # 助手视角
    JUDGE = ("judge", "above",)  # 审判长

    def __init__(self, identifier, area, position=1):
        self.identifier = identifier
        self.area = area
        self.position = position


def handle_trial_image(character: str, image_tag: str, target_position: TrialPosition, at_list: List[str], transition: str):
    if target_position == TrialPosition.DEFENSE:
        character = character + " 庭审"
        at_list.append("char_position_trial_ypos_left")
    elif target_position == TrialPosition.PROSECUTION:
        character = character + " 庭审"
        at_list.append("char_position_trial_ypos_right")
    elif target_position == TrialPosition.ASSISTANT:
        at_list.append("char_position_trial_ypos_assistant")
    else:
        at_list.append("char_position_trial_ypos_center")

    at_list = game_show(character, image_tag, at_list, default_at=None, zorder=50)

    if target_position == TrialPosition.WITNESS:
        if (game.trial_image_liat and "witness" in game.trial_image_liat and
                game.trial_image_liat["witness"][0] != character):
            renpy.hide(game.trial_image_liat["witness"][0])

    if transition != "None":
        renpy.transition(get_store()[transition], layer="master")

    game.trial_image_liat[target_position.identifier] = (character.split(" ")[0], image_tag, tuple(at_list))


# 返回不同的人对应的位置
def get_target_trial_position(character: str) -> TrialPosition:
    if character == "旅行者":
        return TrialPosition.DEFENSE
    elif character == "f":
        return TrialPosition.PROSECUTION
    elif character == "派蒙":
        return TrialPosition.ASSISTANT
    elif character == "c":
        return TrialPosition.JUDGE
    else:
        return TrialPosition.WITNESS


# 旅行者拍桌效果
def effect_traveler_thumped(delay: float = 0.05):
    handle_trial_dialogue("*", "旅行者", "拍桌2", "旅行者", "旅行者", "旅行者",
                          [], True, "transition_dissolve_10")
    game_pause(delay)
    renpy.sound.queue("audio/thumped_desk.ogg")
    handle_trial_dialogue("*", "旅行者", "拍桌", "旅行者", "旅行者", "旅行者",
                          [], True, "transition_dissolve_10")
    show_camera("camera_special_shake", reset=False)
    game_pause(1)


# 旅行者凌空一指效果
def effect_traveler_pointed():
    # 拍桌子
    handle_trial_dialogue("*", "旅行者", "拍桌2", "旅行者", "旅行者", "旅行者",
                          [], True, "transition_dissolve_10")
    game_pause(0.2)
    renpy.sound.queue("audio/thumped_desk.ogg")
    handle_trial_dialogue("*", "旅行者", "拍桌", "旅行者", "旅行者", "旅行者",
                          [], True, "transition_dissolve_10")
    show_camera("camera_special_shake", reset=False)
    game_pause(0.8)

    # 凌空一指
    handle_trial_dialogue("*", "旅行者", "指2", "旅行者", "旅行者", "旅行者",
                          [], True, "transition_dissolve_10")
    game_pause(0.2)
    renpy.sound.queue("audio/objection.ogg")
    play_music("成歩堂 龍一 ～異議あり！ 2013", fade=0)
    show_camera("camera_special_pointed", reset=False)

    handle_trial_dialogue("*", "旅行者", "指", "旅行者", "旅行者", "旅行者",
                          [], True, "transition_dissolve_10")
    renpy.show("speed_line_white", layer="cg", zorder=100)
    game_pause(1)
