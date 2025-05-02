# 旅行者捂住派蒙的嘴
label cg_旅行者捂住派蒙的嘴_1:
    camera cg:
        perspective True
        gl_depth True
        yoffset 140

    show cg_img_1_5_bg onlayer cg:
        zpos 0

    show cg_img_1_5_1 onlayer cg:
        zpos 0
        alpha 0.0
        ease 0.6 alpha 1.0

    show cg_img_1_5_2 onlayer cg:
        zpos 0
        align (0.653, 0.688)
        alpha 0.0
        ease 0.6 alpha 1.0

        transform_anchor True
        block:
            ease 0.1 rotate 1
            ease 0.1 rotate -1
            repeat

    pause 2.0

    return
