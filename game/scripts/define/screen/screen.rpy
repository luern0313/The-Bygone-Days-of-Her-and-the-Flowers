# 黑屏旁白
screen screen_narrate(who, what):
    text what id "what":
        color "#EEEEEE"
        xalign 0.5
        yalign 0.5
        size 60
        text_align 0.5
        at char_transform_narration

# 须弥介绍
screen screen_sumeru_introduce(who, what):
    frame:
        at transform:
            on show:
                alpha 0.0
                ease 0.3 alpha 1.0
            on hide:
                ease 0.3 alpha 0.0

        xsize 1.0
        ysize 193
        xalign 0.5
        yalign 1.0

        background Image("gui/bottom.png", xalign=0.5, yalign=1.0)

    text what id "what":
        color "#FFFFFF"
        xalign 0.5
        ypos 0.93
        yanchor 1.0
        size 47
        text_align 0.5
        outlines [ (3, "#000000", 0, 0) ]
        at char_transform_narration

# 时间、证据数量
screen screen_time_indicator(expend, anim):
    frame:
        at transform:
            on show:
                alpha 0.0
                ease 0.3 alpha 1.0

        left_margin 80
        top_margin 30

        frame:
            left_margin 60
            top_margin 30

            frame:
                if expend:
                    at (time_indicator_bg_expand_toggle if anim else time_indicator_bg_expand)
                else:
                    at (time_indicator_bg_collapse_toggle if anim else time_indicator_bg_collapse)

                xsize 982
                ysize 160

                background Image("gui/time_indicator/bg.png", xalign=1.0, yalign=0.5)

        frame:
            top_margin 72
            left_margin 210

            hbox:
                # 时间
                frame:
                    top_padding 8
                    bottom_padding 4

                    hbox:
                        text "假期第":
                            size 49
                            color "#ecf0d8"
                            kerning 2
                            outlines  [ (4.5, "#315a38", 0, 0) ]

                        null width 4

                        text "[game.current_day_num]":
                            size 49
                            color "#e6e094"
                            outlines  [ (4.5, "#315a38", 0, 0) ]

                        null width 4

                        text "日":
                            size 49
                            color "#ecf0d8"
                            outlines  [ (4.5, "#315a38", 0, 0) ]


                # 证物数
                frame:
                    if expend:
                        at (time_indicator_exhibit_expand_toggle if anim else time_indicator_exhibit_expand)
                    else:
                        at (time_indicator_exhibit_collapse_toggle if anim else time_indicator_exhibit_collapse)

                    left_padding 24
                    right_padding 24
                    left_margin 12
                    top_padding 4
                    yalign 0.5
                    background Frame("gui/time_indicator/time_bg.png", 50, 0, 50, 0)

                    hbox:
                        text "获得证据数":
                            size 49
                            color "#ecf0d8"
                            kerning 2
                            outlines  [ (3, "#497150", 0, 0) ]

                        null width 4

                        $ exhibit_num = len(game.exhibit_list)
                        text ("[exhibit_num]" if len(str(exhibit_num)) > 1 else " [exhibit_num] "):
                            size 49
                            color "#e6e094"
                            outlines  [ (3, "#497150", 0, 0) ]


        frame:
            xsize 221
            ysize 221

            if not has_status(Status.is_evening):
                background Frame("gui/time_indicator/clock.png")
            else:
                background Frame("gui/time_indicator/clock_black.png")

screen screen_shout(mode, character):
    add "gui/shout/" + mode + ".png" align (0.5, 0.4):
        at transform:
            alpha 0.0
            pause 0.1
            alpha 1.0
            pause 0.05
            parallel:
                pause 0.05 xoffset 18.896
                pause 0.05 xoffset -18.36
                pause 0.05 xoffset 15.621
                pause 0.05 xoffset 15.795
                pause 0.05 xoffset -14.42
            parallel:
                pause 0.05 yoffset 17.316
                pause 0.05 yoffset 12.038
                pause 0.05 yoffset -13.85
                pause 0.05 yoffset 13.700
                pause 0.05 yoffset -19.94

    add "white" xysize (1.0, 1.0):
        at transform:
            alpha 0.0
            ease 0.1 alpha 0.5
            ease 0.1 alpha 0.0

    timer 1.4 action [ Hide(transition=dissolve), Return() ]

screen screen_inspiration():
    add "white" xysize (1.0, 1.0):
        at transform:
            alpha 0.0
            pause 0.8
            function sound_lightbulb
            ease 0.1 alpha 0.5
            ease 0.1 alpha 0.0

    timer 2.5 action [ Return() ]
