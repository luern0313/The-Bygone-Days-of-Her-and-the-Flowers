init python:
    def cg_1_4_sound_1(trans, st, at):
        renpy.play("audio/jump.ogg", channel="sound", relative_volume=0.7)

    def cg_1_4_sound_2(trans, st, at):
        renpy.play("audio/lightbulb.ogg", channel="sound", relative_volume=0.5)

# H偷看
label cg_H偷看_1:
    camera cg:
        perspective True
        gl_depth True
        zpos -1200
        offset (-650, -500)
        pause 2.0
        parallel:
            pause 0.05
            function cg_1_4_sound_1
        parallel:
            ease 0.4 offset (-800, 550)

        pause 1.0
        parallel:
            pause 0.05
            function cg_1_4_sound_1
        parallel:
            ease 0.4 offset (300, -100)
        pause 0.4

        function cg_1_4_sound_1
        ease 0.2 offset (0, 200) zpos -800


    show cg_img_1_4_bg onlayer cg:
        zpos -500
        zzoom True

    show cg_img_1_4_1 onlayer cg:
        zpos -475
        align (0.465, 0.68)
        alpha 0.0
        ease 0.6 alpha 1.0

    show cg_img_1_4_2 onlayer cg:
        zpos -450
        align (0.543, 0.732)
        alpha 0.0
        ease 0.6 alpha 1.0

    pause 5.0

    show cg_img_1_4_3 onlayer cg:
        zpos -450
        anchor (0.7, 1.0)
        align (0.412, 0.45)
        parallel:
            alpha 0.0
            ease 0.6 alpha 1.0
        parallel:
            function cg_1_4_sound_2
            ease 0.2 xzoom 1.2 yzoom 1.5
            ease 0.5 xzoom 1.0 yzoom 1.0

    pause 1.5

    return

label cg_H偷看_2:
    camera cg:
        perspective True
        gl_depth True
        zpos -300
        yoffset 240
        xoffset -20

    pause 0.6

    show cg_3_3 onlayer cg:
        ease 0.2 alpha 0.0

    show cg_img_3_1 onlayer cg:
        zpos -200
        easeout 0.2 yoffset 1000

    pause 0.6

    show cg_img_3_2 onlayer cg:
        ease 0.4 xoffset -1000 yoffset -100
        pause 2.34

    pause 0.2

    return
