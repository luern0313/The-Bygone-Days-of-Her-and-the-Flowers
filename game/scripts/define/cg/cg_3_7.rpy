init python:
    def cg_3_6_sound_1(trans, st, at):
        renpy.play("audio/lightbulb.ogg", channel="sound", relative_volume=0.5)

# 纳西妲回头
label cg_纳西妲回头_1:
    camera cg:
        perspective True
        gl_depth True
        zpos 0
        yoffset 160

    show cg_img_3_7_bg onlayer cg:
        zpos 0

    show cg_img_3_7_1 onlayer cg:
        zpos 0
        on show:
            alpha 0.0
            ease 0.3 alpha 1.0

    return

label cg_纳西妲回头_2:
    hide cg_img_3_7_1 onlayer cg
    hide cg_img_3_7_bg onlayer cg
    pause 0.1

    camera cg:
        perspective True
        gl_depth True
        zpos 0
        yoffset 160

    show cg_img_3_7_bg onlayer cg:
        zpos 0
        yoffset 240
        easein_cubic 0.2 yoffset 0

    show cg_img_3_7_2 onlayer cg:
        zpos 0
        yoffset 240
        easein_cubic 0.2 yoffset 0

    return
