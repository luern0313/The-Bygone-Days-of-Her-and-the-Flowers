import renpy

from game.scripts.image_ren import show_camera
from game.scripts.statement_ren import handle_hide_character
from game.scripts.status_ren import exit_state, Status, has_status
from game.scripts.utils_ren import get_store, game_pause

"""renpy
init -1 python:
"""

from typing import Optional


def show_cg(name: str, part: str = "1", transition: str = None):
    # if name not in cg_list:
    #     renpy.notify(f"显示CG {name}")
    #     return
    if transition is None:
        transition = "transition_fade"

    # 退出对话状态，清除立绘
    exit_state(Status.dialogue)
    handle_hide_character("clear")

    if name not in get_store()["persistent"].gallery_unlock and name in map(lambda g: g.label, gallery_cg_list):
        get_store()["persistent"].gallery_unlock.append(name)

    # 调用CG块
    if transition != "None" and part == "1":
        renpy.transition(get_store()[transition])
    renpy.call(f"cg_{name}_{part}")


def hide_cg(transition: str = None, pause_time: Optional[int] = None):
    if transition is None:
        transition = "transition_fade"
    if pause_time is None:
        pause_time = 1.5

    renpy.scene("cg")
    if transition != "None":
        renpy.transition(get_store()[transition], layer="cg")

    if pause_time != 0 and not has_status(Status.narration):
        game_pause(pause_time)
    # 重置cg层摄像机
    show_camera("camera_special_default", layer="cg", reset=True)


def show_cg_gallery(index: int):
    gallery = gallery_cg_list[index]
    renpy.call_in_new_context("batch_call_label", target_list=[f"cg_{gallery.label}_{i}" for i in range(1, gallery.part_count + 1)])


class GalleryEntity:
    name: str
    label: str
    part_count: int

    def __init__(self, name: str, label: str, part_count: int = 1):
        self.name = name
        self.label = label
        self.part_count = part_count


gallery_cg_list = [
    GalleryEntity("智慧之神的沉思", "纳西妲拿着罐装知识"),
    GalleryEntity("「派蒙…」", "旅行者捂住派蒙的嘴"),
    GalleryEntity("小草神的温柔诊疗", "纳西妲在健康之家", 2),
    GalleryEntity("相框里的陌生故事", "相框"),
    GalleryEntity("真假艾尔海森", "真假艾尔海森"),
    GalleryEntity("闹别扭的情侣", "E挽留B"),
    GalleryEntity("「买一份报纸吧~」", "H推销报纸", 2),
    GalleryEntity("「嘿嘿，客人们~」", "H偷看"),
    GalleryEntity("枫丹代表团", "枫丹代表团", 2),
    GalleryEntity("梦的余影", "旅行者和派蒙在旅店醒来"),
    GalleryEntity("花之间的意外发现", "躲进花之间"),
    GalleryEntity("「那个女仆装是…」", "D坐在教令院外"),
    GalleryEntity("检察官的小秘密", "F脸红"),
    GalleryEntity("「哼哼，如果你没来…」", "迪希雅挥拳头"),
    GalleryEntity("心理辅导室变换的景色", "心理辅导室变换的景色"),
    GalleryEntity("「救命啊——」", "H跑来"),
    GalleryEntity("夜晚的花车", "广场上的花车"),
    GalleryEntity("谜团笼罩的地下房间", "被绑架的J", 2),
    GalleryEntity("黑暗中的脚步声", "纳西妲回头", 2),
    GalleryEntity("神明的生日庆典", "花神诞祭"),
    GalleryEntity("探头探脑", "探头探脑"),
    GalleryEntity("「啊！是谁——」", "派蒙撞到E"),
    GalleryEntity("预言中的末日", "装着未来的罐装知识"),
    GalleryEntity("跨越命运的重逢", "神明相拥", 3),
    GalleryEntity("第二枚火邪眼", "第二个火邪眼"),
    GalleryEntity("转瞬间的逆转", "刹那之间"),
    GalleryEntity("泪洒世界树下", "B与世界树", 3),
    GalleryEntity("微笑送别落幕", "花车", 2),
    GalleryEntity("定格在昨日的欢笑", "照片", 2),
]
