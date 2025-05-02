# 枫丹代表团
label cg_枫丹代表团_1:
    camera cg:
        perspective True
        gl_depth True
        yoffset 166

    show cg_img_1_8_bg onlayer cg:
        zpos 0

    return

label cg_枫丹代表团_2:
    show cg_img_1_8_1 onlayer cg:
        zpos 0
        alpha 0.0
        ease 0.6 alpha 1.0

    return
