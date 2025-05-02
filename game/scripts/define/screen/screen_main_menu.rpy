## 标题菜单界面 ######################################################################
##
## 用于在 Ren'Py 启动时显示标题菜单。
##
## https://www.renpy.cn/doc/screen_special.html#main-menu

screen main_menu():
    ## 此语句可确保替换掉任何其他菜单界面。
    tag menu

    style_prefix "main_menu"

    add "gui/main_menu/layer1.png"

    if not persistent.is_finish_mainline:
        add Movie(play="gui/main_menu/main_menu_heiyi.webm", side_mask=True, loop=True):
            align (0.0, 1.0)
            offset (-250, -150)
            xysize (0.92, 0.92)
            at transform:
                on show:
                    alpha 0.0
                    ease 0.3 alpha 1.0
    else:
        add Movie(play="gui/main_menu/main_menu_shuwang.webm", side_mask=True, loop=True):
            align (0.0, 1.0)
            offset (-250, -150)
            xysize (0.92, 0.92)
            at transform:
                on show:
                    alpha 0.0
                    ease 0.3 alpha 1.0

    add "gui/main_menu/layer2.png"

    vbox:
        xalign 1.0
        yalign 0.5

        spacing 44

        textbutton _("开始游戏"):
            at main_menu_button_anim
            action [ Play("sound", "audio/click.ogg"),
                     Show("confirm", message="在开始新的旅程前，需要回顾须弥篇的故事吗？如果你没有玩过须弥章节或略有遗忘，推荐观看回顾后开始~",
                          yes_action=Start("start_with_introduce"), no_action=Start("start_without_introduce")) ]

        textbutton _("继续游戏") action ShowMenu("load"):
            at main_menu_button_anim

        textbutton _("勘验官的考验"):
            if persistent.turtle_soup_1 == False and persistent.turtle_soup_2 == False:
                action Show("confirm", message="推进剧情以解锁此小游戏！", show_cancel_button=False)
                at transform:
                    alpha 0.5
            else:
                action Start("turtle_soup")
                at main_menu_button_anim

        textbutton _("画廊") action ShowMenu("menu_gallery"):
            at main_menu_button_anim

        textbutton _("设置") action ShowMenu("preferences"):
            at main_menu_button_anim

        if renpy.variant("pc"):
            textbutton _("退出游戏") action Quit(confirm=not main_menu):
                at main_menu_button_anim


transform main_menu_button_anim:
    on hover:
        easein 0.2 xoffset -40
    on idle:
        easeout 0.2 xoffset 0


style main_menu_button is button:
    xsize 600
    hover_sound "audio/click.ogg"
    xanchor 1.0
    xpos 0.8

style main_menu_button_text is text:
    color "#FFFFFF"
    size 68
    xalign 1.0
    outlines [ (6, "#4d6d4c", 0, 0) ]

style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_vbox:
    xalign 1.0
    xoffset -40
    xmaximum 1600
    yalign 1.0
    yoffset -40

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")