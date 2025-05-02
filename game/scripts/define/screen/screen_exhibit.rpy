# 获得证据
screen screen_get_exhibit(name, img, desc, is_update, is_full, add_to_list, is_menu=False):

    $ action_list = []
    if not has_status(Status.in_trial) and not is_update and add_to_list:
        $ action_list.append(Show("screen_get_exhibit_light", _layer="sticker"))
    $ action_list.append(Hide(transition=transition_dissolve))
    if not is_menu:
        $ action_list.append(Return())

    button:
        if not is_menu:
            at transform:
                function sound_get_exhibit
                alpha 0
                ease 0.5 alpha 1
        else:
            at transform:
                alpha 0
                ease 0.3 alpha 1

        # 背景黑色遮罩
        frame:
            at transform:
                alpha 0.6
            xalign 0.5
            yalign 0.5
            xsize 1.1
            ysize 1.1

            background Solid("#000000")

        frame:
            xalign 0.5
            yalign 0.4

            if not is_menu:
                add "get_exhibit_bg"
            else:
                add "gui/exhibit/get_exhibit_bg.png":
                    xalign 0.5
                    yalign 0.4

        frame:
            xalign 0.5
            yalign 0.0
            xsize 1580
            yoffset 250

            xpadding 110
            top_padding 40
            bottom_padding 120

            frame:
                xalign 0.5

                hbox xalign 0.5 yoffset 20:
                    if is_update:
                        add "gui/exhibit/get_exhibit_update.png" yalign 0.5

                        null width 20

                    text name:
                        yalign 0.5
                        size 78
                        color "#515648"

                frame:
                    xsize 220
                    ysize 220
                    xalign 0.5
                    yoffset 146

                    if not is_full:
                        add "images/exhibit/" + img + ".png":
                            at transform:
                                alpha 0.7
                                blur 6.0
                                matrixcolor SaturationMatrix(0)
                            xoffset 12
                            yoffset 12
                            xsize 0.9
                            ysize 0.9

                    add "images/exhibit/" + img + ".png":
                        xalign 0.5
                        if not is_full:
                            xsize 0.9
                            ysize 0.9
                        else:
                            xsize 0.9
                            ysize 0.9

                text desc:
                    align (0.0, 0.0)
                    xsize 1.0
                    yoffset 398
                    size 56
                    color "#515648"
                    line_spacing 22

        action action_list

    if not is_menu:
        timer 5 action action_list

# 获得证据后光效
screen screen_get_exhibit_light():
    frame:
        at transform:
            function expand_time_indicator_if_collapse
            pause 3.0
            function collapse_time_indicator_if_expand

        add "get_exhibit_light"

        timer 6 action [ Hide(transition=dissolve) ]

# 证据展示框
screen screen_show_exhibit(position_at, exhibit, is_full):
    frame:
        at position_at
        xsize 370
        ysize 370

        add "gui/show_exhibit/bg.png"

        if not is_full:
            add "images/exhibit/" + exhibit + ".png":
                at transform:
                    alpha 0.7
                    blur 6.0
                    matrixcolor SaturationMatrix(0) * TintMatrix("#DDD")
                xoffset 12
                yoffset 12
                xysize (258, 258)
                align (0.5, 0.5)

        add "images/exhibit/" + exhibit + ".png":
            align (0.5, 0.5)
            if is_full:
                xysize (288, 288)
            else:
                xysize (258, 258)

        add "gui/show_exhibit/fg.png":
            xalign 0.5
            yalign 0.5
