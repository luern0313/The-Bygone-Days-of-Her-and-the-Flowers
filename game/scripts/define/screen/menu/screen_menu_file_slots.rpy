## 读取和保存界面 #####################################################################
##
## 这些界面负责让用户保存游戏并能够再次读取。由于它们几乎完全一样，因此这两个界
## 面都是以第三个界面 file_slots 来实现的。
##
## https://www.renpy.cn/doc/screen_special.html#save https://www.renpy.cn/doc/
## screen_special.html#load

screen save():

    tag menu

    use file_slots(_("保存游戏"))


screen load():

    tag menu

    use file_slots(_("读取游戏"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("第 {} 页"), auto=_("自动存档"), quick=_("快速存档"))

    use game_menu(title):
        frame:
            left_padding 36
            xsize 1.0
            ysize 1.0

            vbox:
                ## 此代码确保输入控件在任意按钮执行前可以获取 enter 事件。
                order_reverse True
                xsize 1.0
                ysize 1.0

                null height 60

                text title:
                    size 74
                    xoffset 16
                    color "#346649"
                    outlines  [ (6, "#346649", 0, 0), (4.5, "#FFFFFF", 0, 0) ]

                null height 58

                hbox:
                    style_prefix "page"
                    xoffset 22
                    spacing 34

                    textbutton _("自动保存") action FilePage("auto"):
                        selected_background Frame("gui/menu/archive_page_auto_bg.png", 40, 40)
                        hover_background Frame("gui/menu/archive_page_auto_bg.png", 40, 40)
                        background Frame("gui/menu/archive_page_auto_unhover_bg.png", 40, 40)

                    for i in range(1, 7):
                        textbutton _(f"第{i}页") action FilePage(i):
                            selected_background Frame("gui/menu/archive_page_manual_bg.png", 40, 40)
                            hover_background Frame("gui/menu/archive_page_manual_bg.png", 40, 40)
                            background Frame("gui/menu/archive_page_manual_unhover_bg.png", 40, 40)

                null height 25

                ## 存档位网格。
                grid 3 2:
                    style_prefix "slot"

                    spacing 18

                    for i in range(6):

                        $ slot = i + 1
                        $ isNewest = FileNewest(slot)

                        button:
                            action FileAction(slot)

                            has vbox

                            frame:
                                add AlphaMask(FileScreenshot(slot), Frame("gui/menu/archive_image_mask.svg")) xalign 0.5 yalign 0.5
                                xsize 563
                                ysize 329
                                padding (14, 14)
                                hover_background Frame("gui/menu/archive_image_selected.svg")
                                background Frame("gui/menu/archive_image_unselected.svg")

                            null height 12

                            text FileSaveName(slot, empty=_("空存档位")):
                                color "#346649"
                                size 40
                                xoffset 14

                            null height 4

                            text FileTime(slot, format=_("{#file_time}%Y-%m-%d %H:%M")) + ("{space=12}最新" if isNewest else ""):
                                if isNewest:
                                    color "#b07d0f"
                                else:
                                    color "#666666"
                                size 34
                                xoffset 14

                            key "save_delete" action FileDelete(slot)


style page_button is button:
    padding (53, 15)

style page_button_text is text:
    selected_color "#FFFFFF"
    hover_color "#FFFFFF"
    color "#fcfbf5"
    size 40

style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
