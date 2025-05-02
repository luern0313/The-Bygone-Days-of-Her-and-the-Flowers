# 选择-证物
screen screen_choices_exhibit(items, avatar, tip):
    # 黑色遮罩
    frame:
        at transform:
            alpha 0.0
            ease 0.2 alpha 0.4
        xalign 0.5
        yalign 0.5
        xsize 1.1
        ysize 1.1

        background Solid("#000000")

    # 背景
    frame:
        at transform:
            function sound_choices_exhibit
            alpha 0.0
            ease 0.3 alpha 1.0

        add "gui/choices/exhibit/bg.png":
            align (0.5, 0.5)
            yoffset 1
            at transform:
                alpha 0.0
                pause 5
                alpha 1.0

        add "choices_exhibit_bg" align (0.5, 0.5)

    # 提示
    frame:
        add "gui/choices/avatar_" + avatar + ".png" align (0.86, 0.2):
            at transform:
                alpha 0.0
                pause 0.8
                ease 0.6 alpha 1.0

        add "gui/choices/bubble_3.png" align (0.76, 0.30):
            at transform:
                alpha 0.0
                pause 1.0
                ease 0.4 alpha 1.0

        add "gui/choices/bubble_2.png" align (0.737, 0.28):
            at transform:
                alpha 0.0
                pause 1.2
                ease 0.4 alpha 1.0

        frame:
            align (0.43, 0.21)
            xysize (1253, 221)
            padding (120, 60, 120, 60)

            at transform:
                alpha 0.0
                pause 1.6
                function sound_choices_exhibit_tip
                ease 0.4 alpha 1.0

            text tip:
                align (0.5, 0.5)
                size 49
                color "#4f5345"
                line_spacing 12

            background Frame("gui/choices/bubble_1.png")

    # 选项
    hbox align (0.5, 0.7):
        for i, item in enumerate(items):
            null width 6

            button:
                if len(items) == 4:
                    xysize (473, 741)
                elif len(items) == 3:
                    xysize (633, 741)

                frame:
                    if len(items) == 4:
                        xysize (473, 741)
                    elif len(items) == 3:
                        xysize (633, 741)

                    at transform:
                        alpha 0.0
                        xoffset 100
                        pause i * 0.3 + 2.8
                        function sound_choices_exhibit_choices
                        parallel:
                            easein 0.4 alpha 1.0
                        parallel:
                            easein 0.4 xoffset 0

                    text item.kwargs.get("shown_name"):
                        anchor (0.5, 0.5)
                        pos (0.5, 0)
                        yoffset 67
                        line_spacing 6
                        if len(items) == 4:
                            xsize 324
                            if count_non_bracket_chars(item.kwargs.get("shown_name")) <= 6:
                                size 46
                            elif count_non_bracket_chars(item.kwargs.get("shown_name")) <= 7:
                                size 43
                            elif count_non_bracket_chars(item.kwargs.get("shown_name")) <= 8:
                                size 40
                            elif count_non_bracket_chars(item.kwargs.get("shown_name")) <= 9:
                                size 36
                            else:
                                size 38
                                line_spacing 0
                        else:
                            xsize 484
                            if count_non_bracket_chars(item.kwargs.get("shown_name")) <= 9:
                                size 46
                            elif count_non_bracket_chars(item.kwargs.get("shown_name")) <= 10:
                                size 43
                            elif count_non_bracket_chars(item.kwargs.get("shown_name")) <= 11:
                                size 40
                            elif count_non_bracket_chars(item.kwargs.get("shown_name")) <= 12:
                                size 36
                            else:
                                size 38
                                line_spacing 0
                        color "#4f5345"
                        textalign 0.5


                    if not item.kwargs.get("is_full") == "True":
                        add "images/exhibit/" + item.kwargs["img"] + ".png":
                            at transform:
                                alpha 0.7
                                blur 4.0
                                matrixcolor SaturationMatrix(0)
                            xoffset 6
                            yoffset 122
                            xalign 0.5
                            yalign 20
                            xysize (132, 132)

                    add "images/exhibit/" + item.kwargs["img"] + ".png":
                        xysize (132, 132)
                        xalign 0.5
                        if not item.kwargs.get("is_full") == "True":
                            yoffset 116
                        else:
                            yoffset 120

                    frame:
                        xysize (1.0, 1.0)
                        align (0.0, 0.0)
                        if len(items) == 4:
                            xpadding 26
                        else:
                            xpadding 31
                        yoffset 274

                        text item.kwargs["desc"]:
                            xysize (1.0, 1.0)
                            size 39
                            color "#5b6050"
                            line_spacing 14
                            kerning -1

                    background Frame("gui/choices/exhibit/choice_bg.png", 0, 0, 0, 0)
                action [item.action, Hide(transition=transition_dissolve_15)]

            null width 6
