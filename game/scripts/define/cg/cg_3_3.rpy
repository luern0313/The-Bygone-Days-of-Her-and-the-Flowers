image cg_3_3_1:
    ytile 2
    anchor (0, 0.5)
    blur 10.0
    parallel:
        block:
            yoffset 0
            linear 0.3 yoffset 1600
            repeat
    parallel:
        block:
            "cg_img_3_3_3"
            pause 0.3
            "cg_img_3_3_4"
            pause 0.3
            "cg_img_3_3_5"
            pause 0.3
            "cg_img_3_3_6"
            pause 0.3
            "cg_img_3_3_7"
            pause 0.3
            "cg_img_3_3_8"
            pause 0.3
            repeat

# 心理辅导室变换的景色
label cg_心理辅导室变换的景色_1:
    camera cg:
        perspective True
        gl_depth True
        zpos 0

    show cg_3_3_1 onlayer cg:
        zpos 0

    show cg_img_3_3_1 onlayer cg:
        zpos 0

    show cg_img_3_3_2 onlayer cg:
        zpos 0

    return
