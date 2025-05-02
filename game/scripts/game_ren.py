import renpy

from game.scripts.trial_ren import TrialPosition

"""renpy
init -1 python:
"""

from typing import Optional, Dict, List, Tuple

# 语句类型
TYPE_COMMENT = "comment"  # 注释
TYPE_COMMEND = "commend"  # 命令
TYPE_NARRATION = "narration"  # 黑屏旁白
TYPE_STATUS_CANCEL = "status_cancel"  # 取消状态
TYPE_STATUS = "status"  # 进入状态
TYPE_PAUSE = "pause"  # 暂停
TYPE_SHOW_CHARACTER = "show_character"  # 显示立绘
TYPE_SHOW = "show"  # 显示displayable
TYPE_HIDE = "hide"  # 隐藏displayable

TYPE_CHOICES = "choices"  # 显示选项
TYPE_CHOICES_OPTION = "choices_option"  # 选项分支
TYPE_RETURN = "return"  # 回到上一个选项

TYPE_ACHIEVEMENT = "achievement"  # 获得成就
TYPE_LOCATION = "location"  # 剧本位置，播放配音用
TYPE_SCENE = "scene"  # 切换场景
TYPE_SHOW_CG = "show_CG"  # 显示CG
TYPE_HIDE_CG = "hide_CG"  # 隐藏CG
TYPE_MUSIC = "music"  # 播放音乐
TYPE_MUSIC_STOP = "music_stop"  # 音乐停止
TYPE_GET_EXHIBIT = "get_exhibit"  # 获得证据
TYPE_REMOVE_EXHIBIT = "remove_exhibit"  # 移除证据
TYPE_SHOW_EXHIBIT = "show_exhibit"  # 显示证据框
TYPE_HIDE_EXHIBIT = "hide_exhibit"  # 隐藏证据框
TYPE_SHOW_INDICATOR = "show_indicator"  # 显示时间
TYPE_HIDE_CHARACTER = "hide_character"  # 隐藏立绘
TYPE_EFFECT = "effect"  # 隐藏立绘
TYPE_TODO = "TODO"  # 显示TODO
TYPE_DIALOGUE = "dialogue"  # 对话

is_rec_mode: bool = False


class Exhibit(renpy.store.object):
    name: str
    image: str
    details: str
    is_full: bool = False

    def __init__(self, name, image, details, is_full=False):
        self.update(name, image, details, is_full)

    def update(self, name, image, details, is_full=False):
        self.name = name
        self.image = image
        self.details = details
        self.is_full = is_full


class Game(renpy.store.object):
    index: int = 0  # 剧本进度
    indentation_level: int = 0  # 当前语句缩进数
    status: int = 0  # 状态
    voice_location: str  # 当前配音位置

    showing_image_list: List[Tuple[str, str, Tuple[str]]]  # 正在显示的立绘列表，按照屏幕位置排序 [立绘名, 立绘tag, 立绘变换列表]
    history_character_list: Dict[str, str]  # 历史活跃角色 [立绘名, 立绘tag]
    camera_transform_list: List[str]  # 摄像机当前变换列表
    background_image_list: List[Tuple[str, Tuple[str]]]  # 背景列表

    ambient_sound_name: Optional[str]  # 当前播放的环境音

    current_day_num: int = 1  # 当前天，UI显示用

    statement_choices: Dict[int, Tuple[int, str]]  # 按照缩进数保存 [选项位置, 当前选择内容]

    trial_position: Optional[TrialPosition]  # 当前庭审视角
    trial_image_liat: Dict[str, Tuple[str, str, Tuple[str]]]  # 庭审立绘列表 [立绘名, 立绘tag, 立绘变换列表]

    variable_list: List[int]  # 变量列表

    exhibit_list: List[Exhibit]  # 当前拥有的证据列表

    name_map: Dict[str, str]
    colored_map: Dict[str, str]
    display_name_map: Dict[str, str]

    def __init__(self):
        self.index = 0
        self.indentation_level = 0
        self.status = 0
        self.voice_location = ""
        self.showing_image_list = []
        self.history_character_list = {}
        self.camera_transform_list = ["camera_position_zoom_in"]
        self.background_image_list = []
        self.ambient_sound_name = None
        self.statement_choices = {}
        self.trial_position = None
        self.trial_image_liat = {}
        self.variable_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.exhibit_list = []
        self.name_map = {
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
        self.colored_map = {
            "A": "{color=#081202}" + self.name_map["A"] + "{/color}",
            "B": "{color=#214807}" + self.name_map["B"] + "{/color}",
            "C": "{color=#304180}" + self.name_map["C"] + "{/color}",
            "D": "{color=#47384c}" + self.name_map["D"] + "{/color}",
            "E": "{color=#27422d}" + self.name_map["E"] + "{/color}",
            "F": "{color=#6e0e42}" + self.name_map["F"] + "{/color}",
            "G": "{color=#563805}" + self.name_map["G"] + "{/color}",
            "H": "{color=#8f1165}" + self.name_map["H"] + "{/color}",
            "J": "{color=#064a5e}" + self.name_map["J"] + "{/color}",
            "M": "{color=#86366d}" + self.name_map["M"] + "{/color}",
            "K": "{color=#000000}" + self.name_map["K"] + "{/color}",
        }
        self.display_name_map = {
            "A": self.colored_map['A'] + "{image=text_a_1}",
            "B": self.colored_map['B'] + "{image=text_b_1}",
            "C": self.colored_map['C'] + "{space=4}{image=text_c_1}",
            "D": self.colored_map['D'] + "{space=4}{image=text_d_1}",
            "E": self.colored_map['E'] + "{space=2}{image=text_e_1}",
            "F": self.colored_map['F'] + "{space=2}{image=text_f_1}",
            "G": "{image=text_g_1}{space=2}" + self.colored_map['G'] + "{space=2}{image=text_g_2}",
            "H": self.colored_map['H'] + "{space=2}{image=text_h_1}",
            "J": self.colored_map['J'] + "{space=2}{image=text_j_1}",
            "M": self.colored_map['M'] + "{space=2}{image=text_m_1}",
            "K": self.colored_map['K']
        }

    def __str__(self):
        return (
            f"Game Object:\n"
            f"  index: {self.index}\n"
            f"  indentation_level: {self.indentation_level}\n"
            f"  status: {self.status}\n"
            f"  voice_location: {self.voice_location}\n"
            f"  showing_image_list: {self.showing_image_list}\n"
            f"  history_character_list: {self.history_character_list}\n"
            f"  camera_transform_list: {self.camera_transform_list}\n"
            f"  background_image_list: {self.background_image_list}\n"
            f"  ambient_sound_name: {self.ambient_sound_name}\n"
            f"  current_day_num: {self.current_day_num}\n"
            f"  statement_choices: {self.statement_choices}\n"
            f"  trial_position: {self.trial_position}\n"
            f"  trial_image_liat: {self.trial_image_liat}\n"
            f"  variable_list: {self.variable_list}\n"
            f"  exhibit_list: {self.exhibit_list}\n"
            f"  name_map: {self.name_map}\n"
            f"  colored_map: {self.colored_map}\n"
            f"  display_name_map: {self.display_name_map}\n"
        )


game: Game
