import renpy
import achievement

from game.scripts.utils_ren import get_store

"""renpy
init -1 python:
"""


# 解锁成就
def grant_achievement(label: str):
    if label not in map(lambda g: g.label, achievement_list):
        return

    # api返回成就未达成
    if not achievement.has(label):
        achievement.grant(label)
        # 持久化数据中无达成记录
        if label not in get_store()["persistent"].grant_achievement:
            get_store()["persistent"].grant_achievement.append(label)

        # 达成所有成就后，触发最后一个成就，不计入持久化数据中
        if len(get_store()["persistent"].grant_achievement) >= len(achievement_list) - 1:
            achievement.grant("ACHIEVEMENT_44")

    achievement.sync()


class AchievementEntity:
    label: str
    name: str
    desc: str

    def __init__(self, label: str, name: str, desc: str):
        self.label = label
        self.name = name
        self.desc = desc


achievement_list = [
    AchievementEntity("ACHIEVEMENT_1", "穿越时空的脚步", "跟随纳西妲的指引，探索未知的「过去」。"),
    AchievementEntity("ACHIEVEMENT_2", "是「轻气球」！", "购买了花神诞祭火爆全城的「轻气球」。"),
    AchievementEntity("ACHIEVEMENT_3", "新朋友", "在过去的须弥城，结识了新朋友拉尼娅。"),
    AchievementEntity("ACHIEVEMENT_4", "初识「命定论」", "偶然翻阅，初次接触神秘的「命定论」。"),
    AchievementEntity("ACHIEVEMENT_5", "密室逃脱", "找到了钥匙，离开了这个房子。"),
    AchievementEntity("ACHIEVEMENT_6", "真假蒸汽鸟报", "揭穿了假报纸的真相。"),
    AchievementEntity("ACHIEVEMENT_7", "这里是…世界树？", "梦境中，世界树的真容悄然显现。"),
    AchievementEntity("ACHIEVEMENT_8", "命案惊闻", "早晨醒来，获知教令院昨夜命案的消息。"),
    AchievementEntity("ACHIEVEMENT_9", "代理人之名", "通过试炼，正式成为案件的「代理人」。"),
    AchievementEntity("ACHIEVEMENT_10", "开始调查吧！", "深入案发现场，追寻真相的足迹。"),
    AchievementEntity("ACHIEVEMENT_11", "神秘花束", "神秘人与神秘的红色花束，仿佛隐藏着什么秘密。"),
    AchievementEntity("ACHIEVEMENT_12", "代理人入门", "从第一位证人口中挖掘出线索。"),
    AchievementEntity("ACHIEVEMENT_13", "代理人进阶", "敏锐洞察，揭露了证言中的矛盾点。"),
    AchievementEntity("ACHIEVEMENT_14", "关键一刻", "在危机关头，为正义赢得喘息之机。"),
    AchievementEntity("ACHIEVEMENT_15", "拉尼娅的自白", "聆听了拉尼娅的自白。"),
    AchievementEntity("ACHIEVEMENT_16", "临时休庭", "暂时休庭，为拉尼娅争取了一天时间。"),
    AchievementEntity("ACHIEVEMENT_17", "往日的记忆", "了解到了卡莱尔和拉尼娅的过往。"),
    AchievementEntity("ACHIEVEMENT_18", "「异界之门」", "打开了通向异世界的门？"),
    AchievementEntity("ACHIEVEMENT_19", "暗夜尖叫", "多莉斯的尖叫打破了夜晚的寂静。"),
    AchievementEntity("ACHIEVEMENT_20", "地脉的震颤", "亲历了一次「过去的」地震。"),
    AchievementEntity("ACHIEVEMENT_21", "「那个房间」", "破解谜题，进入了教令院地下「那个房间」。"),
    AchievementEntity("ACHIEVEMENT_22", "…谁在后面！", "黑暗之中，未知的存在让人屏息。"),
    AchievementEntity("ACHIEVEMENT_23", "真正的花神诞祭", "体验了旧日须弥城的花神诞祭。"),
    AchievementEntity("ACHIEVEMENT_24", "众目睽睽下的命案", "目睹了花神诞祭巡游花车内的尸体。"),
    AchievementEntity("ACHIEVEMENT_25", "发光的花", "神秘的花束亮起了光…"),
    AchievementEntity("ACHIEVEMENT_26", "梦醒时分", "梦终究会醒来…"),
    AchievementEntity("ACHIEVEMENT_27", "破绽再现", "在庭审上，发现了勘验官证言与尸体报告间的矛盾。"),
    AchievementEntity("ACHIEVEMENT_28", "「灵殒香」的真相", "揭开阿斯法德研制「灵殒香」背后的真相。"),
    AchievementEntity("ACHIEVEMENT_29", "机械生命的证词", "在讯问环节，讯问了一位「机械生命」"),
    AchievementEntity("ACHIEVEMENT_30", "元素之眼", "使用元素视野，发现了被隐藏起来的蛛丝马迹。"),
    AchievementEntity("ACHIEVEMENT_31", "地下寻踪", "深入调查，在地下室找到失踪的纳西妲和珐蒂玛。"),
    AchievementEntity("ACHIEVEMENT_32", "上一个「轮回」", "不是五百年前，而是…"),
    AchievementEntity("ACHIEVEMENT_33", "邪眼疑云", "发现了邪眼，难道真的是愚人众…？"),
    AchievementEntity("ACHIEVEMENT_34", "草元素的审判", "使用元素视野确认了真正的凶手。"),
    AchievementEntity("ACHIEVEMENT_35", "你…就是「仆人」？", "听到凶手自称「仆人」。"),
    AchievementEntity("ACHIEVEMENT_36", "「最后的花神诞祭」", "再次见证纳西妲与大慈树王的故事。"),
    AchievementEntity("ACHIEVEMENT_37", "关键一刻", "在关键时刻，卡莱尔奋力扑倒「仆人」，粉碎了凶手的阴谋。"),
    AchievementEntity("ACHIEVEMENT_38", "无罪证明", "通过庭审，证明了珐蒂玛的清白。"),
    AchievementEntity("ACHIEVEMENT_39", "未寄出的告白", "你选择交出拉尼娅的信，帮助她将深埋心底的情感传达给卡莱尔。"),
    AchievementEntity("ACHIEVEMENT_40", "遗憾的守护者", "你选择让拉尼娅的信随着时间消逝，为她留下片刻的宁静。"),
    AchievementEntity("ACHIEVEMENT_41", "再见，大慈树王", "完成主线剧情，探寻了世界的真相，见证了又一段故事。"),

    AchievementEntity("ACHIEVEMENT_42", "「玩具商人」", "解开十斗的第一个故事谜题。"),
    AchievementEntity("ACHIEVEMENT_43", "「液体」", "解开十斗的第二个故事谜题。"),

    AchievementEntity("ACHIEVEMENT_44", "只属于「她与花」的往日", "完成了所有成就，书写了只属于「她与花」的完整回忆。"),
]


for ach in achievement_list:
    achievement.register(ach.label)
achievement.sync()
