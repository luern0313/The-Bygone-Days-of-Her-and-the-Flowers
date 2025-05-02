## 设置界面 ########################################################################
##
## 设置界面允许用户配置游戏，使其更适合自己。
##
## https://www.renpy.cn/doc/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("设置")):
        $ slider_bg = Frame(Image("gui/slider/horizontal_slider_bg.svg"), 100, 0, 100, 0)

        frame:
            left_padding 36
            xsize 1.0
            bottom_margin 126

            vbox:
                xsize 1.0
                ysize 1.0

                null height 60

                text "设置":
                    size 74
                    xoffset 16
                    color "#346649"
                    outlines  [ (6, "#346649", 0, 0), (4.5, "#FFFFFF", 0, 0) ]

                null height 50

                hbox:
                    box_wrap True

                    vbox:
                        xsize 450
                        xoffset 24

                        hbox:
                            null width 1
                            add "gui/menu/label_mark.png" yalign 0.5
                            null width 20
                            text _("画面设置"):
                                color "#346649"
                                size 42
                                yalign 0.5

                        null height 40

                        frame:
                            xysize (644, 97)

                            textbutton _("窗口") action Preference("display", "any window"):
                                xysize (326, 97)
                                xalign 0.0

                                selected_background Image("gui/menu/preference_display_window_selected.png")
                                hover_background Image("gui/menu/preference_display_window_selected.png")
                                background Image("gui/menu/preference_display_window_unselected.png")

                                text_align (0.5, 0.6)
                                text_color "#fffffe"
                                text_size 42
                                text_selected_outlines [ (6, "#608f56", 0, 0) ]
                                text_hover_outlines [ (6, "#608f56", 0, 0) ]

                            textbutton _("全屏") action Preference("display", "fullscreen"):
                                xysize (326, 97)
                                xalign 1.0

                                selected_background Image("gui/menu/preference_display_full_selected.png")
                                hover_background Image("gui/menu/preference_display_full_selected.png")
                                background Image("gui/menu/preference_display_full_unselected.png")

                                text_align (0.5, 0.6)
                                text_color "#fffffe"
                                text_size 42
                                text_selected_outlines [ (6, "#c18926", 0, 0) ]
                                text_hover_outlines [ (6, "#c18926", 0, 0) ]

                        null height 20

                        textbutton _("重置窗口大小") action Preference("display", 1.0):
                            xysize (299, 76)

                            sensitive not _preferences.fullscreen
                            hover_background Image("gui/menu/preference_display_reset_enable_hover.png")
                            background Image("gui/menu/preference_display_reset_enable.png")
                            insensitive_background Image("gui/menu/preference_display_reset_disable.png")

                            text_align (0.5, 0.5)
                            text_color "#fffffe"
                            text_size 36

                        null height 60

                        hbox:
                            null width 1
                            add "gui/menu/label_mark.png" yalign 0.5
                            null width 20
                            text _("文字速度"):
                                color "#346649"
                                size 42
                                yalign 0.5

                        null height 20

                        frame:
                            xysize(636, 34)
                            add slider_bg
                            bar value Preference("text speed", range = 34) xysize(636, 34)

                        null height 89

                        hbox:
                            imagebutton:
                                idle "gui/menu/preference_attention_me.png"
                                hover "gui/menu/preference_attention_me_hover.png"
                                action OpenURL("https://space.bilibili.com/8014831")

                            null width 12

                            imagebutton:
                                idle "gui/menu/preference_github.png"
                                hover "gui/menu/preference_github_hover.png"
                                action OpenURL("https://github.com/luern0313/The-Bygone-Days-of-Her-and-the-Flowers")

                        null height 35

                        textbutton _("重置选项"):
                            action [ Preference("display", 1),
                                     Preference("text speed", 18),
                                     Preference("all mute", "disable"),
                                     Preference("mixer main volume", 1.0),
                                     Preference("music volume", 0.63),
                                     Preference("sound volume", 0.63),
                                     Preference("mixer ambient volume", 1.0),
                                     Preference("voice volume", 1.0)
                            ]

                            ysize 80
                            left_padding 60
                            right_padding 60

                            hover_background Frame("gui/menu/preference_more_hover.png", 40, 0, 40, 0)
                            background Frame("gui/menu/preference_more.png", 40, 0, 40, 0)
                            insensitive_background Image("")

                            text_align (0.5, 0.5)
                            text_color "#fffffe"
                            text_size 36

                        null height 20

                        textbutton _("键位帮助") action [ Show("preferences_keymap_white") ]:
                            ysize 80
                            left_padding 60
                            right_padding 60

                            hover_background Frame("gui/menu/preference_more_hover.png", 40, 0, 40, 0)
                            background Frame("gui/menu/preference_more.png", 40, 0, 40, 0)
                            insensitive_background Image("")

                            text_align (0.5, 0.5)
                            text_color "#fffffe"
                            text_size 36

                        null height 20

                        textbutton _("制作人员表") action [ Show("preferences_staff") ]:
                            ysize 80
                            left_padding 60
                            right_padding 60

                            hover_background Frame("gui/menu/preference_more_hover.png", 40, 0, 40, 0)
                            background Frame("gui/menu/preference_more.png", 40, 0, 40, 0)
                            insensitive_background Image("")

                            text_align (0.5, 0.5)
                            text_color "#fffffe"
                            text_size 36

                    null width 270

                    vbox:
                        hbox:
                            null width 1
                            add "gui/menu/label_mark.png" yalign 0.5
                            null width 20
                            text _("总音量"):
                                color "#346649"
                                size 42
                                yalign 0.5

                        null height 20

                        frame:
                            xysize(636, 34)
                            add slider_bg
                            bar value Preference("mixer main volume") xysize(636, 34)

                        null height 60

                        hbox:
                            null width 1
                            add "gui/menu/label_mark.png" yalign 0.5
                            null width 20
                            text _("音乐音量"):
                                color "#346649"
                                size 42
                                yalign 0.5

                        null height 20

                        frame:
                            xysize(636, 34)
                            add slider_bg
                            bar value Preference("music volume") xysize(636, 34)

                        null height 60

                        hbox:
                            add "gui/menu/label_mark.png" yalign 0.5
                            null width 20
                            text _("音效音量"):
                                color "#346649"
                                size 42
                                yalign 0.5

                        null height 20

                        frame:
                            xysize(636, 34)
                            add slider_bg
                            bar value Preference("sound volume") xysize(636, 34)

                        null height 60

                        hbox:
                            add "gui/menu/label_mark.png" yalign 0.5
                            null width 20
                            text _("环境音量"):
                                color "#346649"
                                size 42
                                yalign 0.5

                        null height 20

                        frame:
                            xysize(636, 34)
                            add slider_bg
                            bar value Preference("mixer ambient volume") xysize(636, 34)

                        null height 60

                        hbox:
                            add "gui/menu/label_mark.png" yalign 0.5
                            null width 20
                            text _("语音音量"):
                                color "#346649"
                                size 42
                                yalign 0.5

                        null height 20

                        frame:
                            xysize(636, 34)
                            add slider_bg
                            bar value Preference("voice volume") xysize(636, 34)

                        null height 80

                        textbutton _("全部静音") action Preference("all mute", "toggle"):
                            ysize 80

                            selected_idle_background Frame("gui/menu/preference_volume_reset.png", 40, 40)
                            selected_hover_background Frame("gui/menu/preference_volume_reset_hover.png", 40, 40)
                            hover_background Frame("gui/menu/preference_volume_reset_unselected_hover.png", 40, 40)
                            background Frame("gui/menu/preference_volume_reset_unselected.png", 40, 40)

                            text_align (0.5, 0.5)
                            text_color "#fffffe"
                            text_size 38
                            xpadding 40


        showif _preferences.get_mute("main"):
            frame:
                xysize (780, 920)
                yoffset 120
                xoffset 900

                imagebutton action NullAction():
                    idle Frame("gui/menu/preference_volume_mask.png")

                    at transform:
                        alpha 0.8
