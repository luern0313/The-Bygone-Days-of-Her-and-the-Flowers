init python:
    def cg_2_1_sound_1(trans, st, at):
        renpy.play("audio/jump.ogg", channel="sound", relative_volume=0.5)

# 旅行者和派蒙在旅店醒来
label cg_旅行者和派蒙在旅店醒来_1:
    camera cg:
        perspective True
        gl_depth True

    show cg_img_2_1_bg onlayer cg:
        zpos 0

    show cg_img_2_1_1 onlayer cg:
        zpos 0
        alpha 0.0
        ease 0.5 alpha 1.0

    show cg_img_2_1_2 onlayer cg:
        zpos 0
        alpha 0.0
        align (0.528, 0.518)
        ease 0.5 alpha 1.0
        pause 0.8

        parallel:
            ease_cubic 1.0 align (0.569, 0.166)
        parallel:
            pause 0.3
            function cg_2_1_sound_1
            ease_cubic 0.7 rotate 3
        pause 0.4

        parallel:
            ease_cubic 1.0 align (0.528, 0.518)
        parallel:
            pause 0.3
            function cg_2_1_sound_1
            ease_cubic 0.7 rotate -3
        pause 0.4

        parallel:
            ease_cubic 1.0 align (0.569, 0.166)
        parallel:
            pause 0.3
            function cg_2_1_sound_1
            ease_cubic 0.7 rotate 3
        pause 0.4

    pause 2

    return
