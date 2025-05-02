# 选择-选项
screen screen_choices_options(items, avatar, tip):
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

        add "gui/choices/options/bg.png":
            align (0.5, 0.5)
            yoffset 1
            at transform:
                alpha 0.0
                pause 5
                alpha 1.0

        add "choices_options_bg" align (0.5, 0.5)

    # 提示
    frame:
        add "gui/choices/avatar_" + avatar + ".png" align (0.86, 0.2):
            yoffset 100
            at transform:
                alpha 0.0
                pause 0.8
                ease 0.6 alpha 1.0

        add "gui/choices/bubble_3.png" align (0.76, 0.30):
            yoffset 100
            at transform:
                alpha 0.0
                pause 1.0
                ease 0.4 alpha 1.0

        add "gui/choices/bubble_2.png" align (0.737, 0.28):
            yoffset 100
            at transform:
                alpha 0.0
                pause 1.2
                ease 0.4 alpha 1.0

        frame:
            align (0.43, 0.21)
            xysize (1253, 221)
            yoffset 100
            padding (120, 60, 120, 60)

            at transform:
                alpha 0.0
                pause 1.6
                function sound_choices_exhibit_tip
                ease 0.4 alpha 1.0

            text tip:
                align (0.5, 0.5)
                size 48
                color "#4f5345"
                line_spacing 12

            background Frame("gui/choices/bubble_1.png")

    # 选项
    for i, item in enumerate(items):
        button:
            at transform:
                alpha 0.0
                xoffset 100
                pause i * 0.3 + 2.8
                function sound_choices_options_choices
                parallel:
                    easein 0.4 alpha 1.0
                parallel:
                    easein 0.4 xoffset 0

            anchor (0.0, 0.5)
            ysize 195

            if item.kwargs["position"] == 0:
                pos (0.12, 0.51)
            elif item.kwargs["position"] == 1:
                pos (0.48, 0.51)
            elif item.kwargs["position"] == 2:
                pos (0.12, 0.67)
            elif item.kwargs["position"] == 3:
                pos (0.48, 0.67)

            frame:
                ysize 195
                left_padding 190
                right_padding 80
                bottom_padding 15

                at transform:
                    alpha (0 if is_rec_mode else 1)

                text item.kwargs.get("shown_name"):
                    align (0.5, 0.5)
                    color "#000000"
                    size 58

                background Frame("gui/choices/bilibili_button_reversal.png", 251, 0, 120, 0)
            action [item.action, Hide(transition=transition_dissolve_15)]
