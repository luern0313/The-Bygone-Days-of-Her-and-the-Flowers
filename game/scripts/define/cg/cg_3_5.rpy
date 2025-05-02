# 广场上的花车
label cg_广场上的花车_1:
    camera cg:
        perspective True
        gl_depth True
        zpos 0
        yoffset 20

    show cg_img_3_5_bg onlayer cg:
        zpos 0

    show cg_img_3_5_1 onlayer cg:
        zpos 0
        alpha 0.0
        block:
            ease 3 alpha 1.0
            ease 3 alpha 0.5
            repeat

    return
