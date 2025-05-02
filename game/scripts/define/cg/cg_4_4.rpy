init python:
    def cg_4_4_sound_1(trans, st, at):
        renpy.play("audio/jump.ogg", channel="sound", relative_volume=0.7)

# 探头探脑
label cg_探头探脑_1:
    camera cg:
        perspective True
        gl_depth True
        zpos -800
        offset (-600, -200)
        pause 1
        function cg_4_4_sound_1
        pause 2

        parallel:
            pause 0.05
            function cg_4_4_sound_1
        parallel:
            ease 0.4 offset (200, -100)

        pause 1.5
        function cg_4_4_sound_1
        ease 0.2 offset (0, 80) zpos 0

    show cg_img_4_4_bg onlayer cg:
        zpos 0

    show cg_img_4_4_1 onlayer cg:
        zpos 200
        yoffset 200
        xoffset 240
        zoom 0.8
        block:
            ease 1.8 yoffset 180
            ease 1.8 yoffset 220
            repeat

    show cg_img_4_4_2 onlayer cg:
        zpos 200
        yoffset 200
        xoffset 200
        zoom 0.8

    return
