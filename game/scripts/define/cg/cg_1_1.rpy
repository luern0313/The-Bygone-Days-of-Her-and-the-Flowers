image cg1_snow1 = Fixed(SnowBlossom("images/particle/snow_cg_1_1_1.png", 30, xspeed=(-50, 50), yspeed=(-40, -80), start=0, fast=True))
image cg1_snow2 = Fixed(SnowBlossom("images/particle/snow_cg_1_1_2.png", 30, xspeed=(-50, 50), yspeed=(-40, -80), start=0, fast=True))

# 纳西妲拿着罐装知识
label cg_纳西妲拿着罐装知识_1:
    camera cg:
        perspective True
        gl_depth True
        zpos -900
        yoffset 75
        pause 0.8
        ease 1.2 zpos -700
        ease 40 zpos -200

    show cg1_snow1 onlayer cg zorder 100
    show cg1_snow2 onlayer cg zorder 100

    show cg_img_1_1_bg onlayer cg:
        zpos -500
        zzoom True

    show cg_img_1_1_1 onlayer cg:
        matrixcolor BrightnessMatrix(-0.2)

    show cg_img_1_1_2 onlayer cg:
        alpha 1.0
        matrixcolor BrightnessMatrix(-0.2)
        block:
            ease 1.8 alpha 1.0
            ease 1.8 alpha 0.0
            repeat

    show cg_img_1_1_3 onlayer cg:
        matrixcolor BrightnessMatrix(-0.2)
        block:
            ease 1.8 yoffset -30
            ease 1.8 yoffset 0
            repeat

    show cg_img_1_1_4 onlayer cg:
        alpha 1.0
        matrixcolor BrightnessMatrix(-0.2)
        parallel:
            block:
                ease 1.8 alpha 0.0
                ease 1.8 alpha 1.0
                repeat
        parallel:
            block:
                ease 1.8 yoffset -30
                ease 1.8 yoffset 0
                repeat

    play sound "audio/闪闪发光.ogg" fadeout 3.0 fadein 3.0 volume 0.2 loop

    return
