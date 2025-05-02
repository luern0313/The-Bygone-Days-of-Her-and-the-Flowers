# 讯问ui
screen screen_trial_interrogate(previous, following):
    window:
        at transform:
            alpha 0.0
            pause 1.5
            easein 0.3 alpha 1.0

        if previous:
            button:
                anchor (1.0, 0.5)
                pos (0.0, 1.0)
                ysize 195
                xoffset 534
                yoffset -186

                frame:
                    ysize 195
                    left_padding 80
                    right_padding 190
                    bottom_padding 15

                    at transform:
                        alpha (0 if is_rec_mode else 1)

                    text "A 上一句":
                        align (0.5, 0.5)
                        color "#000000"
                        size 58

                    background Frame("gui/choices/bilibili_button.png", 120, 0, 230, 0)
                action [Hide(transition=transition_dissolve_15), Return("上一句")]

        button:
            anchor (0.0, 0.5)
            pos (1.0, 1.0)
            ysize 195
            xoffset -534
            yoffset -186

            frame:
                ysize 195
                left_padding 190
                right_padding 80
                bottom_padding 15

                at transform:
                    alpha (0 if is_rec_mode else 1)

                text "B " + following:
                    align (0.5, 0.5)
                    color "#000000"
                    size 58

                background Frame("gui/choices/bilibili_button_reversal.png", 251, 0, 120, 0)
            action [Hide(transition=transition_dissolve_15), Return(following)]

        button:
            anchor (1.0, 0.5)
            pos (0.0, 1.0)
            ysize 195
            xoffset 534
            yoffset -460

            frame:
                ysize 195
                left_padding 80
                right_padding 190
                bottom_padding 15

                at transform:
                    alpha (0 if is_rec_mode else 1)

                text "C 追问":
                    align (0.5, 0.5)
                    color "#000000"
                    size 58

                background Frame("gui/choices/bilibili_button.png", 120, 0, 251, 0)
            action [Hide(transition=transition_dissolve_15), Return("追问")]

        button:
            anchor (0.0, 0.5)
            pos (1.0, 1.0)
            ysize 195
            xoffset -534
            yoffset -460

            frame:
                ysize 195
                left_padding 190
                right_padding 80
                bottom_padding 15

                at transform:
                    alpha (0 if is_rec_mode else 1)

                text "D 指证":
                    align (0.5, 0.5)
                    color "#000000"
                    size 58

                background Frame("gui/choices/bilibili_button_reversal.png", 251, 0, 120, 0)
            action [Hide(transition=transition_dissolve_15), Return("指证")]
