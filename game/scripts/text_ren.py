import re
from typing import Dict, Optional

import renpy
import voice
import base_character

from game.scripts.define.transform_function_ren import voice_male_sound
from game.scripts.game_ren import game
from game.scripts.music_ren import play_music
from game.scripts.status_ren import Status, has_status
from game.scripts.utils_ren import get_store

"""renpy
init -1 python:
"""

from renpy.character import ADVCharacter

from Lmd05.lmd0_5 import Lmd05

lmd0_5 = Lmd05(48)


# 替换对话文本
def pretreatment_text(text: str) -> str:
    if text == "*":
        return "*"

    # 对话框渐变出现时，延后文字的出现
    if not has_status(Status.dialogue):
        text = "{cps=3}\u200B{/cps}" + text

    text = text.replace("树之间", "{image=树之间}")
    text = text.replace("花之间", "{image=花之间}")
    text = text.replace("灵殒香", "{image=灵殒香}")
    for name, formatted_name in game.display_name_map.items():
        text = replace_text(text, name, formatted_name)
    return text


# 替换对话名字
def pretreatment_name(text: str, mapping=None) -> str:
    if mapping is None:
        mapping = game.display_name_map
    if text in map(lambda n: n.lower(), mapping.keys()):
        return mapping[text.upper()]
    return text


# 替换其他
def pretreatment_other(text: str, mapping: Dict[str, str], space: int = 4) -> str:
    for name, formatted_name in mapping.items():
        text = replace_text(text, name, formatted_name, space)
    return text


# 查找并指定配音文件，在下一次交互时播放
def handle_voice(character: str, text: str, interact: bool = True):
    if character is None or not interact or character == "scene_info" or character == "泰坦":
        return

    if get_voice_text(text) == "":
        return

    if ((character == "a" or character.upper() not in name_code)
            and character not in ["旅行者", "派蒙", "纳西妲", "艾尔海森", "迪希雅"]):
        voice_folder_prefix = "all"  # npc
    else:
        location = game.voice_location.split("_")
        if location[0] == "1" or (location[0] == "2" and location[1] in ["1", "2"]):
            voice_folder_prefix = "1"  # 一期
        else:
            voice_folder_prefix = "2"  # 二期

    voice_name = f"{game.voice_location}_{pretreatment_name(character, name_code)}_{get_text_identifier(text)}"
    voice_path = f"voices/{voice_folder_prefix}_{pretreatment_name(character, name_code)}/{voice_name}.wav"
    if renpy.loadable(voice_path):
        print(f"播放配音：{voice_path}，index：{game.index}")
        voice(voice_path)
    else:
        print(f"配音文件缺失：{voice_path}，index：{game.index}")
        # renpy.notify(f"配音文件缺失：{voice_path}，index：{game.index}")


SPACE_TEXT = "{space=%d}"

# 黑名单内词语不替换
BLACK_LIST = ["FA"]


def replace_text(original_text, old_str, new_str, space: int = 4):
    result = ""
    prev_chinese = False
    i = 0  # 初始化索引

    while i < len(original_text):
        char = original_text[i]

        # 黑名单内词语不替换
        is_hit = False
        for black_word in BLACK_LIST:
            if original_text[i:i + len(black_word)] == black_word:
                i += len(black_word)
                result += black_word
                is_hit = True
                break
        if is_hit:
            continue

        if i > 0 and is_chinese_char(char):
            prev_chinese = True
        elif is_chinese_char(old_str[0]):
            prev_chinese = False

        if original_text[i:i + len(old_str)] == old_str:
            if prev_chinese:
                result += SPACE_TEXT % space
            result += new_str
            if i + len(old_str) < len(original_text) and is_chinese_char(original_text[i + len(old_str)]):
                result += SPACE_TEXT % space
            prev_chinese = False
            i += len(old_str)  # 移动索引以跳过替换的部分
        else:
            result += char
            i += 1  # 移动索引以继续遍历原始文本的字符
    return result


def is_chinese_char(char) -> bool:
    return '\u4e00' <= char <= '\u9fa5'


def count_non_bracket_chars(text):
    count = 0
    in_brackets = False

    for char in text:
        if char == '{':
            in_brackets = True
        elif char == '}':
            in_brackets = False
        elif not in_brackets:
            count += 1

    return count


# 动态创建ADVCharacter实例
def get_adv_character(name: str, **kwargs) -> ADVCharacter:
    if name == "scene_info":
        return get_store()["scene_info"]
    elif name == "sumeru_introduce":
        return get_store()["sumeru_introduce"]
    elif name == "泰坦":
        return ADVCharacter(pretreatment_name(name), kind=base_character, callback=voice_male_sound)
    return ADVCharacter(pretreatment_name(name), kind=base_character, callback=get_store().get(kwargs.get("callback")))


# 获取文本对应配音id
def get_text_identifier(text):
    voice_text = get_voice_text(text)
    lmd0_5.set_byte_array(voice_text.encode("utf-8"))
    return lmd0_5.solve()


def get_voice_text(text: str) -> str:
    return "".join(filter(lambda c: '\u4e00' <= c <= '\u9fff', text))


BRACKET_PATTERN = re.compile(r"\{[^{}]*?}")


def update_save_text(text: str):
    if text == "" or text == "*":
        return None

    for name, formatted_name in game.name_map.items():
        text = replace_text(text, name, formatted_name)

    get_store()["save_name"] = BRACKET_PATTERN.sub("", text)[0:13]


# 角色code，不外显，不随游戏进程改变
name_code = {
    "A": "阿斯法德",
    "B": "拉尼娅",
    "C": "芙纳蕾娜",
    "D": "艾莉",
    "E": "卡莱尔",
    "F": "妮莉亚",
    "G": "十斗",
    "H": "多莉斯",
    "J": "珐蒂玛",
    "M": "柯莱蒂",
    "K": "艾芙琳"
}
