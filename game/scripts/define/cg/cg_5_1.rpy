init python:
    def cg_5_1_sound_1(trans, st, at):
        renpy.play("audio/闪白.ogg", channel="sound", relative_volume=0.7)

# 第二个火邪眼
label cg_第二个火邪眼_1:
    camera cg:
        perspective True
        gl_depth True
        zpos 0

    show cg_img_5_1_bg onlayer cg:
        zpos 0

    show cg_img_5_1_1 onlayer cg:
        zpos 0
        yoffset 400
        align (1.0, 1.0)
        alpha 0
        pause 1.5
        function cg_5_1_sound_1
        easein 0.3 yoffset 0 alpha 1

    return
