## 确认界面 ########################################################################
##

screen confirm(message, yes_action=None, no_action=None, show_cancel_button=True):

    python:
        if yes_action == None:
            yes_action = [ Hide(transition=config.exit_yesno_transition) ]
        if no_action == None:
            no_action = [ Hide(transition=config.exit_yesno_transition) ]

    ## 显示此界面时，确保其他界面无法输入。
    modal True
    zorder 200

    # 背景黑色遮罩
    frame:
        at transform:
            alpha 0.0
            ease 0.15 alpha 0.6
        xalign 0.5
        yalign 0.5
        xsize 1.1
        ysize 1.1

        background Solid("#000000")

    frame:
        background Image("gui/confirm/bg.png")
        xysize (1295, 755)
        xalign 0.5
        yalign 0.5

        at transform:
            alpha 0.0
            ease 0.2 alpha 1.0

        frame:
            xalign 0.5
            yalign 0.43

            label _(message):
                style "confirm_prompt"
                xalign 0.5
                yalign 0.5
                xpadding 170
                if len(message) > 50:
                    text_size 46
                text_textalign 0.5
                text_color "#2a533b"
                text_line_spacing 20

        hbox:
            style_prefix "confirm"
            xalign 0.5
            yalign 1.0
            yoffset -120
            spacing 80

            if show_cancel_button:
                textbutton _("取消") action no_action:
                    hover_background Frame("gui/confirm/no_hovered_bg.png", 40, 40)
                    background Frame("gui/confirm/no_idle_bg.png", 40, 40)

            textbutton _("确定") action yes_action:
                hover_background Frame("gui/confirm/yes_hovered_bg.png", 40, 40)
                background Frame("gui/confirm/yes_idle_bg.png", 40, 40)

    if show_cancel_button:
        key "game_menu" action no_action
    else:
        key "game_menu" action yes_action


style confirm_button is button:
    padding (100, 15)
    ysize 107

style confirm_button_text is text:
    color "#FFFFFF"
    size 50
    yalign 0.5
