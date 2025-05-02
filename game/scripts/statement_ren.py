import renpy

from game.scripts.exception.RenPyException_ren import RenPyException
from game.scripts.game_ren import game
from game.scripts.image_ren import game_show, get_showing_images_name, show_camera, get_background_images_name, show_background
from game.scripts.status_ren import Status, has_status, exit_state, handle_state_into, handle_state_exit
from game.scripts.text_ren import pretreatment_text, pretreatment_other, get_adv_character, handle_voice, update_save_text
from game.scripts.trial_ren import handle_trial_dialogue
from game.scripts.utils_ren import get_store, move_element, game_pause

"""renpy
init -1 python:
"""

from renpy.character import ADVCharacter
from typing import Optional, Union, List

IMAGE_TAG_DEFAULT = "正常"


# 对话统一处理逻辑
def handle_dialogue(text: str, character: str = None, image_tag: str = None, show_image: str = None, show_name: str = None,
                    at_list: str = None, interact: bool = True, is_show_img: bool = True, **kwargs):
    character = character.lower() if character else None
    show_name = show_name.lower() if show_name else None
    if show_image is None:
        show_image = character
    if show_name is None:
        show_name = character
    at_list = at_list.split(",") if at_list is not None else []
    show_image = show_image if is_show_img else "narrate"

    if not has_status(Status.in_trial):
        handle_normal_dialogue(text, image_tag, show_image, show_name, character, at_list, interact, **kwargs)
    else:
        handle_trial_dialogue(text, character, image_tag, show_image, show_name, character, at_list, interact, **kwargs)


# 处理非庭审普通对话
def handle_normal_dialogue(text: str, image_tag: str, show_image: str, show_name: str, voice_character: str, at_list: List[str],
                           interact: bool, **kwargs):
    update_save_text(text)
    text = pretreatment_text(text)
    # 普通旁白
    if show_name is None or show_name == "*":
        handle_voice(voice_character, text, interact=interact)
        handle_image("narrate", "", **kwargs)
        renpy.say(None, text)
        return

    if image_tag is None:
        if show_image in game.history_character_list:
            image_tag = game.history_character_list[show_image]
        else:
            image_tag = IMAGE_TAG_DEFAULT

    # 角色对话
    handle_image(show_image, image_tag, at_list, **kwargs)

    if text != "*":
        handle_voice(voice_character, text, interact=interact)
        get_adv_character(show_name, **kwargs)(text, interact=interact)


# 立绘统一处理逻辑
def handle_image(character: str, image_tag: str, at_list: List[str] = None, **kwargs):
    if has_status(Status.hide_character):
        raise RenPyException("不允许在隐藏立绘时更新立绘，character: " + character + "，image_tag: " + image_tag)
    if at_list is None:
        at_list = []

    camera_at = None

    # 普通旁白
    if character == "narrate":
        for i in game.showing_image_list:
            game_show(i[0], i[1], at_list="char_active_inactive_toggle", **kwargs)
        renpy.transition(get_store()["transition_dissolve_15"], layer="master")

        game.history_character_list["narrate"] = ""
        move_element(game.history_character_list, "narrate", 0)
        return

    if character not in get_showing_images_name():
        # 显示新角色立绘
        if len(game.showing_image_list) == 0:
            # 当前无立绘，新立绘显示在屏幕中间
            at_list.extend(["char_position_center", "char_transform_appear_toggle"])
            at_list = game_show(character, image_tag, at_list=at_list, **kwargs)
            game.showing_image_list.append((character, image_tag, tuple(at_list)))
        elif len(game.showing_image_list) == 1:
            # 已存在一个立绘，之前立绘左移，新立绘显示在右边，左侧立绘变暗
            last_at_list = game_show(game.showing_image_list[0][0], game.showing_image_list[0][1],
                                     at_list=["char_position_smooth_to_left", "char_active_inactive_toggle"], **kwargs)
            at_list.extend(["char_position_right", "char_transform_appear_toggle_delay"])
            at_list = game_show(character, image_tag, at_list=at_list, **kwargs)
            camera_at = "camera_position_zoom_out_toggle"
            # 更新showing_image_list
            game.showing_image_list[0] = (game.showing_image_list[0][0], game.showing_image_list[0][1],
                                          tuple(last_at_list))
            game.showing_image_list.append((character, image_tag, tuple(at_list)))
        else:
            # 屏幕上存在两个立绘，移出较旧的立绘，显示当前立绘
            try:
                last_character_index = get_showing_images_name().index(get_last_active_characters())
            except Exception:
                raise RenPyException("当前显示立绘列表中不存在最近活跃的角色，showing_image_list: " +
                                     str(game.showing_image_list) + "; history_character_list: " +
                                     str(game.history_character_list))

            if last_character_index == 1:
                renpy.hide(game.showing_image_list[0][0])
                at_list.extend(["char_position_left", "char_transform_appear_toggle"])
                at_list = game_show(character, image_tag, at_list=at_list, **kwargs)
                last_at_list = game_show(game.showing_image_list[1][0], game.showing_image_list[1][1],
                                         at_list="char_active_inactive_toggle", **kwargs)
                # 更新showing_image_list
                game.showing_image_list[0] = (character, image_tag, tuple(at_list))
                game.showing_image_list[1] = (game.showing_image_list[1][0],
                                              game.showing_image_list[1][1], tuple(last_at_list))
            else:
                renpy.hide(game.showing_image_list[1][0])
                at_list.extend(["char_position_right", "char_transform_appear_toggle"])
                at_list = game_show(character, image_tag, at_list=at_list, **kwargs)
                last_at_list = game_show(game.showing_image_list[0][0], game.showing_image_list[0][1],
                                         at_list="char_active_inactive_toggle", **kwargs)
                # 更新showing_image_list
                game.showing_image_list[0] = (game.showing_image_list[0][0],
                                              game.showing_image_list[0][1], tuple(last_at_list))
                game.showing_image_list[1] = (character, image_tag, tuple(at_list))
    else:
        # 要显示的角色已出现在屏幕上，需要更新立绘
        index = get_showing_images_name().index(character)

        # 更新立绘优先级
        if (list(game.history_character_list.keys())[0] != character or
                game.showing_image_list[index][1] != image_tag):
            at_list.append("char_active_active_toggle")
            at_list = game_show(character, image_tag, at_list=at_list, **kwargs)
            # 另一个立绘非活跃立绘，将立绘变暗
            if len(game.showing_image_list) > 1:
                other_index = 1 - index
                last_at_list = game_show(game.showing_image_list[other_index][0],
                                         game.showing_image_list[other_index][1],
                                         at_list="char_active_inactive_toggle", **kwargs)
                game.showing_image_list[other_index] = (game.showing_image_list[other_index][0],
                                                        game.showing_image_list[other_index][1], tuple(last_at_list))
            renpy.transition(get_store()["transition_dissolve_15"], layer="master")
            game.showing_image_list[index] = (character, image_tag, tuple(at_list))

    # 更新活跃人物栈
    game.history_character_list[character] = image_tag
    move_element(game.history_character_list, character, 0)

    if camera_at:
        show_camera(camera_at)


def handle_background(image: str = None, at_list: Optional[Union[str, List[str]]] = None, zorder: int = 0):
    if image is None:
        image = game.background_image_list[0][0]

    if at_list is None:
        at_list = []
    elif isinstance(at_list, str):
        at_list = [at_list]

    if image not in get_background_images_name():
        at_list = show_background(image, at_list, zorder)
        game.background_image_list.append((image, at_list),)
    else:
        at_list = show_background(image, at_list, zorder)
        game.background_image_list[get_background_images_name().index(image)] = (image, at_list)


# 隐藏立绘，突出背景
def hide_character():
    for image in game.showing_image_list:
        renpy.hide(image[0])
    renpy.transition(get_store()["transition_dissolve"], layer="master")
    handle_background(at_list="bg_position_normal")
    show_camera("camera_position_zoom_in_toggle")


# 恢复隐藏的立绘
def recover_character():
    handle_background(at_list="bg_position_blur")
    show_camera("camera_position_zoom_out_toggle")


# 处理全屏旁白显示
def handle_narrate(text: str):
    text = pretreatment_other(text, game.name_map)
    renpy.say(get_store()["narrate"], text)
    game_pause(1)


# 场景切换处理
def handle_scene(image: str, transition: str = None, pause_time: Optional[int] = None):
    if not transition:
        transition = "transition_fade"
    if pause_time is None:
        pause_time = 0.5

    if has_status(Status.hide_character):
        raise RenPyException("不允许在隐藏立绘时切换场景")

    game.showing_image_list.clear()
    game.history_character_list.clear()
    game.background_image_list.clear()
    exit_state(Status.dialogue)

    # 某些transition不能从黑色过渡
    if "dissolve" in transition:
        handle_scene_without_blank(image, transition)
        return

    # 黑屏
    if not has_status(Status.narration) and transition != "None":
        renpy.show("black", layer="sticker")
        renpy.with_statement(get_store()[transition])

    renpy.scene("master")
    if image != "*":
        handle_background(image, "bg_position_blur")
    show_camera("camera_special_default")

    # 释放缓存
    if image != "*":
        renpy.free_memory()

    # 退出黑屏
    if not has_status(Status.narration) and transition != "None":
        renpy.hide("black", layer="sticker")
        renpy.with_statement(get_store()[transition])
        exit_state(Status.narration)

    if image != "*" and pause_time != 0 and not has_status(Status.narration):
        game_pause(pause_time)


def handle_scene_without_blank(image: str, transition: str = None):
    renpy.scene("master")
    if image != "*":
        handle_background(image, "bg_position_blur")
    show_camera("camera_special_default")
    if transition is not None:
        renpy.with_statement(get_store()[transition])

    # 释放缓存
    if image != "*":
        renpy.free_memory()


def handle_hide_character(state: str):
    if state == "hide":
        handle_state_into(Status.hide_character)
    elif state == "recover":
        handle_state_exit(Status.hide_character)
    elif state == "clear":
        for image in game.showing_image_list:
            renpy.hide(image[0])
        renpy.transition(get_store()["transition_dissolve"], layer="master")
        game.showing_image_list.clear()
        game.history_character_list.clear()


# 返回最近活跃的角色
def get_last_active_characters() -> str:
    name_list = list(game.history_character_list.keys())
    for name in name_list:
        if name != "narrate":
        #temp_name = name.upper()
        #if temp_name in get_store():
            #character = get_store()[temp_name]
            #if isinstance(character, ADVCharacter) and character.name is not None:
            return name
    raise RenPyException("获取不到最近活跃的角色，history_character_list: " + str(game.history_character_list))
