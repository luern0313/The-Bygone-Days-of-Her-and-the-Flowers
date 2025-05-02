import renpy

from game.scripts.game_ren import game
from game.scripts.utils_ren import array_contain, get_store

"""renpy
init -1 python:
"""

from typing import List, Optional, Union, Tuple


def game_show(name: str, tag: str = None, at_list: Optional[Union[str, List[str]]] = None, layer: Optional[str] = None,
              zorder: int = 100, **kwargs) -> List[str]:
    # 初始化at_list等
    if at_list is None:
        at_list = []
    elif isinstance(at_list, str):
        at_list = [at_list]

    # image未加tag时，从当前显示立绘中匹配tag
    img_list = get_showing_images_name()
    if tag is None and name in img_list:
        tag = game.showing_image_list[img_list.index(name)][1]

    print(str(name) + " " + str(tag))

    # 派蒙需要加漂浮
    if ("派蒙" == name and not array_contain(("char_special_ypos_jump",), at_list) and
            not array_contain(("char_special_ypos_jump",), at_list)):
        at_list.append("char_special_ypos_paimon_float")

    print("new: " + str(at_list))

    if name in img_list:
        last_character_index = get_showing_images_name().index(name)
        last_at_list = game.showing_image_list[last_character_index][2]
        print("origin: " + str(last_at_list))
        # 查表替换列表中的旧变换，避免一些动画重复出现。不替换新变换。
        last_at_list = list(filter(lambda a: a, map(outdated_transform_mapping, last_at_list)))
        at_list = merge_transform_list(last_at_list, at_list)

    # 保证存在 默认变换 并在首位
    default_at = kwargs.get("default_at", "char_special_default")
    if default_at:
        if default_at in at_list:
            at_list.remove(default_at)
        at_list.insert(0, default_at)

    at_list.sort(key=lambda item: 0 if (get_transform_identifier(item) == "special") else 1)

    print("result: " + str(at_list), end="\n\n")

    # 全部接手transform的继承合并后，理论上需要先hide后show，但怕有性能缓存等问题。
    # renpy.hide(name + " " + tag if tag else name, layer=layer)
    renpy.show(name + " " + tag if tag else name, at_list=[get_store()[t] for t in at_list], layer=layer, zorder=zorder)
    return list(at_list)


def show_camera(at: str, layer: str = "master", reset: bool = True):
    print("camera transform: " + str(at) + " layer: " + str(layer) + " reset: " + str(reset))

    renpy.layer_at_list(get_store()[at], layer=layer, camera=True, reset=reset)

    if layer == "master":
        if reset:
            game.camera_transform_list.clear()
        game.camera_transform_list.append(at)


def show_background(image: str = None, at_list: List[str] = None, zorder: int = 0) -> Tuple[str]:
    print("background new: " + image + ", at: " + str(at_list))

    if image in get_background_images_name():
        last_background_index = get_background_images_name().index(image)
        last_at_list = game.background_image_list[last_background_index][1]
        print("background origin: " + str(last_at_list))
        last_at_list = list(map(outdated_transform_mapping, last_at_list))
        at_list = merge_transform_list(last_at_list, at_list)

    print("background result: " + str(at_list), end="\n\n")
    renpy.show(image, at_list=[get_store()[at] for at in at_list], zorder=zorder)

    return tuple(at_list)


def merge_transform_list(origin_at_list: List[str], at_list: List[str]):
    for at in at_list:
        temp_origin_at_list = []
        for last_at_index in range(len(origin_at_list)):
            last_at = origin_at_list[last_at_index]
            # 如果last_at等于当前的at、或为"special_default"，则跳过继续下一轮循环。
            if last_at == at or (get_transform_identifier(last_at) == "special" and
                                 is_transform_contains_tag("default", last_at)):
                continue
            # 如果last_at的标识与当前的at的标识相同，也跳过继续下一轮循环。
            if get_transform_identifier(last_at) == get_transform_identifier(at):
                continue
            temp_origin_at_list.append(origin_at_list[last_at_index])
        origin_at_list = temp_origin_at_list
    at_list[:0] = origin_at_list
    return at_list


# 旧变换可能需要进行替换，避免一些带动画的变换重复出现
def outdated_transform_mapping(at: str) -> Optional[str]:
    # 角色相关变换
    if at == "char_position_smooth_to_left":
        return "char_position_left"

    elif at == "char_active_inactive_toggle":
        return "char_active_inactive"
    elif at == "char_active_active_toggle":
        return "char_active_active"

    elif at == "char_transform_appear_toggle":
        return None
    elif at == "char_transform_appear_toggle_delay":
        return None
    elif at == "char_transform_disappear_toggle":
        return None
    elif at in ("char_special_shake", "char_special_up", "char_special_appear_slowly", "char_special_appear_down"):
        return None
    # 相机相关变换
    elif at == "camera_position_zoom_out_toggle":
        return "camera_position_zoom_out"
    # 背景相关变换
    return at


# 获取transform的标识
# transform命名：type_identifier_tag_tag_...
def get_transform_identifier(transform: str):
    return transform.split("_")[1]


# 判断transform中是否指定的tag
def is_transform_contains_tag(target_tag: str, transform: str):
    return target_tag in transform.split("_")[2:]


# 返回当前显示的立绘角色名列表
def get_showing_images_name() -> List[str]:
    return [img[0] for img in game.showing_image_list]


# 返回当前显示的背景image列表
def get_background_images_name() -> List[str]:
    return [img[0] for img in game.background_image_list]
