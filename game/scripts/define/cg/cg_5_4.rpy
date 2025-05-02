init python:
    def cg_5_4_sound_1(trans, st, at):
        renpy.play("audio/guilty.ogg", channel="sound")

# 无罪
label cg_无罪_1:
    show cg_img_5_4_1 onlayer cg:
        zpos 0
        pos (0.25, 0.3)
        anchor (0.5, 0.5)
        zoom 2.0
        alpha 0.0
        function cg_5_4_sound_1
        easein 0.2 zoom 1.0 alpha 1.0
        on hide:
            easeout 0.8 zoom 2.0 alpha 0.0

    pause 1.5

    show cg_img_5_4_2 onlayer cg:
        zpos 0
        pos (0.75, 0.3)
        anchor (0.5, 0.5)
        zoom 2.0
        alpha 0.0
        function cg_5_4_sound_1
        easein 0.2 zoom 1.0 alpha 1.0
        on hide:
            easeout 0.8 zoom 2.0 alpha 0.0

    pause 1.5

    hide cg_img_5_4_1 onlayer cg
    hide cg_img_5_4_2 onlayer cg

    pause 0.8

    return
