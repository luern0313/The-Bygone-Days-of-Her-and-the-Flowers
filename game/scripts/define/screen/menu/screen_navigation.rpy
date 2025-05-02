
## 导航界面 ########################################################################
##
## 该界面包含在标题菜单和游戏菜单中，并提供导航到其他菜单，以及启动游戏。

screen navigation():
    vbox:
        style_prefix "navigation"
        yalign 0.46
        spacing 34

        if main_menu:
            textbutton _("开始游戏"):
                action [ Play("sound", "audio/click.ogg"),
                         Show("confirm", message="在开始新的旅程前，需要回顾须弥篇的故事吗？如果你没有玩过须弥章节或略有遗忘，推荐观看回顾后开始~",
                              yes_action=Start("start_with_introduce"), no_action=Start("start_without_introduce")) ]

            textbutton _("继续游戏") action [Play("sound", "audio/click.ogg"), ShowMenu("load")]

            textbutton _("勘验官的考验"):
                if persistent.turtle_soup_1 == False and persistent.turtle_soup_2 == False:
                    action [ Play("sound", "audio/click.ogg"), Show("confirm", message="推进剧情以解锁此小游戏！", show_cancel_button=False) ]
                    text_selected_color "#ccdbca"
                    text_hover_color "#ccdbca"
                    text_color "#ccdbca"
                    text_selected_outlines [ (6, "#759c70", 0, 0) ]
                    text_hover_outlines [ (6, "#759c70", 0, 0) ]
                    text_outlines [ (6, "#759c70", 0, 0) ]
                else:
                    action [ Play("sound", "audio/click.ogg"), Start("turtle_soup") ]

            textbutton _("画廊") action [Play("sound", "audio/click.ogg"), ShowMenu("menu_gallery")]

        else:
            textbutton _("证据袋") action [Play("sound", "audio/click.ogg"), ShowMenu("menu_exhibit")]

            textbutton _("保存游戏") action [Play("sound", "audio/click.ogg"), ShowMenu("save")]

            textbutton _("读取游戏") action [Play("sound", "audio/click.ogg"), ShowMenu("load")]

            textbutton _("返回标题菜单") action [Play("sound", "audio/click.ogg"), MainMenu()]

        textbutton _("设置") action [Play("sound", "audio/click.ogg"), ShowMenu("preferences")]

        if renpy.variant("pc"):
            ## 退出按钮在 iOS 上是被禁止使用的，在安卓和网页上也不是必要的。
            textbutton _("退出游戏") action [Play("sound", "audio/click.ogg"), Quit(confirm=not main_menu)]


transform navigation_button:
    pass

style navigation_button is button:
    xsize 600
#     hover_sound "audio/click.ogg"

    xanchor 1.0
    xpos 0.8

style navigation_button_text is text:
    selected_color "#FFFFFF"
    hover_color "#FFFFFF"
    color "#ccdbca"
    size 58
    xalign 1.0
    selected_outlines [ (6, "#4d6d4c", 0, 0) ]
    hover_outlines [ (6, "#4d6d4c", 0, 0) ]
    outlines [ (6, "#759c70", 0, 0) ]
