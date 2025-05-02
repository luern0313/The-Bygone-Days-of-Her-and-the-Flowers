# 证言中
transform screen_in_testimony:
    alpha 1
    block:
        pause 3
        ease 0.3 alpha 0
        pause 0.3
        ease 0.3 alpha 1
        repeat

# 获得证物
transform get_exhibit_bg_1:
    xalign 0.5
    yalign 0.5
    xsize 1722

transform get_exhibit_bg_2:
    xalign 0.5
    yalign 0.5
    xsize 1746
    rotate 0
    pause 0.8
    easein 0.5 rotate -2

transform get_exhibit_bg_flower_1:
    xalign 0.0
    yalign 0.0
    yoffset 600
    rotate_pad False
    xanchor 0.5
    yanchor 0.5
    rotate -40
    easein 0.5 rotate 0

transform get_exhibit_bg_flower_2:
    xalign 1.0
    yalign 1.0
    yoffset -100

# 时间、证物条相关
transform time_indicator_bg_collapse_toggle:
    on start:
        crop (104, 0, 878, 160)
        ease_cubic 0.8 crop (486, 0, 496, 160)

transform time_indicator_exhibit_collapse_toggle:
    on start:
        alpha 1.0
        crop(0, 0, 1.0, 1.0)
        parallel:
            ease_cubic 0.8 crop(0, 0, 0.0, 1.0)
        parallel:
            easein 0.8 alpha 0.0

transform time_indicator_bg_expand_toggle:
    on start:
        crop (486, 0, 496, 160)
        ease_cubic 0.8 crop (104, 0, 878, 160)

transform time_indicator_exhibit_expand_toggle:
    on start:
        alpha 0.0
        crop(0, 0, 0.0, 1.0)
        parallel:
            ease_cubic 0.7 crop(0, 0, 1.0, 1.0)
        parallel:
            easeout 0.8 alpha 1.0

transform time_indicator_bg_collapse:
    crop (486, 0, 496, 160)

transform time_indicator_exhibit_collapse:
    alpha 0.0
    crop(0, 0, 0.0, 1.0)

transform time_indicator_bg_expand:
    crop (104, 0, 878, 160)

transform time_indicator_exhibit_expand:
    alpha 1.0
    crop(0, 0, 1.0, 1.0)

transform time_indicator_exhibit_tip:
    alpha 0.0
    xoffset 950
    xsize 400
    pause 7.0
    parallel:
        pause 1.65
        ease 0.4 xsize 550
    parallel:
        ease 0.5 alpha 1.0
        pause 5.0
        ease 0.5 alpha 0.0
    parallel:
        easein 0.4 xoffset 920
        easeout 0.4 xoffset 950
        repeat 10

transform time_indicator_exhibit_tip_exhibit:
    alpha 1.0
    yalign 0.5
    pause 9.0
    parallel:
        ease 0.4 yalign 0.0
    parallel:
        ease 0.4 alpha 0.0

transform time_indicator_exhibit_tip_reply:
    alpha 0.0
    yalign 1.0
    pause 9.0
    parallel:
        ease 0.4 yalign 0.5
    parallel:
        ease 0.4 alpha 1.0


# 展示证据
transform show_exhibit_center:
    on show:
        function sound_show_exhibit
        xalign 0.5
        yalign 0.2
        alpha 0.0
        ease 0.3 alpha 1.0
    on hide:
        ease 0.3 alpha 0.0

transform show_exhibit_left:
    on show:
        function sound_show_exhibit
        xalign 0.18
        yalign 0.2
        alpha 0.0
        ease 0.3 alpha 1.0
    on hide:
        ease 0.3 alpha 0.0

transform show_exhibit_trial_left:
    on show:
        function sound_show_exhibit
        xalign 0.25
        yalign 0.2
        alpha 0.0
        ease 0.3 alpha 1.0
    on hide:
        ease 0.3 alpha 0.0

transform show_exhibit_trial_right:
    on show:
        function sound_show_exhibit
        xalign 0.75
        yalign 0.2
        alpha 0.0
        ease 0.3 alpha 1.0
    on hide:
        ease 0.3 alpha 0.0
