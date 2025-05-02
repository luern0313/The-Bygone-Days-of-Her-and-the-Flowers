# image cg_3_1:
#     anchor (0.5, 0.5)
#     pos (0.58, 0.70)
#     block:
#         "cg_img_3_1_1"
#         rotate 4.0
#         pause 0.5
#         "cg_img_3_1_2"
#         rotate -3.0
#         pause 0.5
#         repeat
#
# image cg_3_2:
#     anchor (0.5, 0.5)
#     pos (0.31, 0.62)
#     block:
#         "cg_img_3_2_1"
#         rotate 1.0
#         pause 0.5
#         "cg_img_3_2_2"
#         rotate -1.0
#         pause 0.5
#         repeat

image cg_1_3_3:
    "cg_img_3_3"
    anchor (0.5, 0.5)
    block:
        pos (0.524, 0.41)
        rotate 4.0
        pause 0.5
        pos (0.516, 0.414)
        rotate -4.0
        pause 0.5
        repeat

init python:
    def cg_1_3_sound(trans, st, at):
        renpy.play("audio/jump.ogg", channel="sound", relative_volume=0.7)

# H推销报纸
label cg_H推销报纸_1:
    camera cg:
        perspective True
        gl_depth True
        zpos -300
        yoffset 240
        xoffset -20

    show cg_img_1_3_bg onlayer cg:
        zpos -500
        zzoom True

    show cg_img_1_3_4 onlayer cg:
        zpos -200
        alpha 0.0
        ease 0.6 alpha 1.0

    show cg_img_1_3_1 onlayer cg:
        zpos -200
        alpha 0.0
        ease 0.6 alpha 1.0
        pause 2.0

        block:
            function cg_1_3_sound
            easein_quad 0.08 yoffset -80
            easeout 0.14 yoffset 0
            pause 0.05

            function cg_1_3_sound
            easein_quad 0.12 yoffset -80
            easeout 0.15 yoffset 0
            pause 2.0
            repeat 5

    show cg_img_1_3_2 onlayer cg:
        zpos -200
        alpha 0.0
        ease 0.6 alpha 1.0
        pause 2.8
        ease 0.2 xoffset -60 yoffset -6
        pause 2.34
        ease 0.2 xoffset -100 yoffset -10
        pause 2.34
        ease 0.2 xoffset -150 yoffset -15
        pause 2.34
        ease 0.2 xoffset -210 yoffset -21
        pause 2.34
        ease 0.2 xoffset -270 yoffset -27
        pause 2.34

    show cg_img_1_3_3 onlayer cg:
        zpos -200
        alpha 0.0
        ease 0.6 alpha 1.0

    pause 8.0
    return

label cg_H推销报纸_2:
    camera cg:
        perspective True
        gl_depth True
        zpos -300
        yoffset 240
        xoffset -20

    pause 0.6

    show cg_img_1_3_3 onlayer cg:
        ease 0.2 alpha 0.0

    show cg_img_1_3_1 onlayer cg:
        zpos -200
        easeout 0.2 yoffset 1000

    pause 0.6

    show cg_img_1_3_2 onlayer cg:
        ease 0.4 xoffset -1000 yoffset -100
        pause 2.34

    pause 0.2
