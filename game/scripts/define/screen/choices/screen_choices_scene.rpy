# 选择-选项
screen screen_choices_scene(items):
    # 选项
    for i, item in enumerate(items):
        button:
            at transform:
                alpha 0.0
                parallel:
                    easein 0.4 alpha 1.0

            if not item.kwargs.get("is_reversal") == "True":
                anchor (0.0, 0.5)
            else:
                anchor (1.0, 0.5)
            ysize 195

            pos (float(item.kwargs["position"].split("_")[0]), float(item.kwargs["position"].split("_")[1]))

            frame:
                ysize 195
                bottom_padding 15
                if not item.kwargs.get("is_reversal") == "True":
                    left_padding 190
                    right_padding 80
                else:
                    left_padding 80
                    right_padding 190

                at transform:
                    alpha (0 if is_rec_mode else 1)

                text item.caption:
                    align (0.5, 0.5)
                    color "#000000"
                    size 58

                if not item.kwargs.get("is_reversal") == "True":
                    background Frame("gui/choices/bilibili_button_reversal.png", 251, 0, 120, 0)
                else:
                    background Frame("gui/choices/bilibili_button.png", 120, 0, 251, 0)
            action [item.action, Hide(transition=transition_dissolve_15)]
