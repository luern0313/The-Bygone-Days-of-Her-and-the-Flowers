# 选择-话题
screen screen_choices_topic(items, title, small_style, turtle_riddle=None):
    # 黑色遮罩
    frame:
        at transform:
            alpha 0.0
            ease 0.3 alpha 0.8
        xalign 0.5
        yalign 0.5
        xsize 1.1
        ysize 1.1

        background Solid("#000000")

    frame align (0.5, 0.2):
        at transform:
            alpha 0.0
            pause 0.5
            parallel:
                easein 0.4 alpha 1.0

        hbox:
            add "gui/choices/topic/title_decoration_left.png" yalign 0.5
            null width 20

            text title:
                color "#dfe9c5"
                size 54

            null width 20
            add "gui/choices/topic/title_decoration_right.png" yalign 0.5

        background Image("gui/choices/topic/title_bg.png", xalign=0.5, yalign=0.2)

    # 选项
    vbox anchor (0.5, 0.0) pos (0.5, 0.3):
        for i, item in enumerate(items):
            button:
                at transform:
                    alpha 0.0
                    pause 1.0
                    parallel:
                        easein 0.6 alpha 1.0

                if small_style:
                    ysize 117
                else:
                    ysize 195

                frame:
                    if small_style:
                        ysize 117
                        bottom_padding 9
                        left_padding 48
                        right_padding 114
                    else:
                        ysize 195
                        bottom_padding 15
                        left_padding 80
                        right_padding 190

                    at transform:
                        alpha (0 if is_rec_mode else 1)

                    text item.kwargs.get("shown_name"):
                        align (0.5, 0.5)
                        color "#000000"
                        if small_style:
                            size 39
                        else:
                            size 58

                    if small_style:
                        background Frame("gui/choices/bilibili_button_small.png", 72, 0, 151, 0)
                    else:
                        background Frame("gui/choices/bilibili_button.png", 120, 0, 251, 0)
                action [item.action, Hide(transition=transition_dissolve_15)]

            null height 20

    # 海龟汤在此处显示谜面
    if turtle_riddle != None:
        frame:
            at transform:
                alpha 0.0
                ease 0.5 alpha 1.0

            xsize 737
            offset (65, 268)
            padding (74, 40, 74, 60)

            vbox:
                text _("谜面"):
                    color "#FFFFFF"
                    size 54

                null height 60

                text turtle_riddle:
                    color "#305F44"
                    size 42

            background Frame("gui/choices/topic/turtle_riddle.png", 200, 150, 100, 100)
