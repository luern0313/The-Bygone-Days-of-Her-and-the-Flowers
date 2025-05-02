init python:
    def cg_3_6_sound_1(trans, st, at):
        renpy.play("audio/lightbulb.ogg", channel="sound", relative_volume=0.5)

# 被绑架的J
label cg_被绑架的J_1:
    camera cg:
        perspective True
        gl_depth True
        zpos 0
        yoffset 160

    show cg_img_3_6_bg onlayer cg:
        zpos 0

    show cg_img_3_6_1 onlayer cg:
        zpos 0
        alpha 0.0
        ease 0.3 alpha 1.0

    show cg_img_3_6_2 onlayer cg:
        zpos 0
        on show:
            alpha 0.0
            ease 0.3 alpha 0.6
        on hide:
            ease 0.3 alpha 0.0

    pause 2

    show cg_img_3_6_4 onlayer cg:
        zpos 0
        anchor (0.7, 1.0)
        align (0.78, 0.4)
        parallel:
            alpha 0.0
            ease 0.6 alpha 1.0
        parallel:
            function cg_3_6_sound_1
            ease 0.2 xzoom 1.2 yzoom 1.5
            ease 0.5 xzoom 1.0 yzoom 1.0

    return

label cg_被绑架的J_2:
    hide cg_img_3_6_2 onlayer cg
    hide cg_img_3_6_4 onlayer cg

    show cg_img_3_6_3 onlayer cg:
        zpos 0
        alpha 0.0
        ease 0.3 alpha 1.0

    return
