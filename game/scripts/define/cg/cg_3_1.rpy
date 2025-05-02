# 虚掩的房门
label cg_虚掩的房门_1:
    camera cg:
        perspective True
        gl_depth True
        zpos -400
        yoffset 150
        xoffset -50

    show cg_img_3_1_bg onlayer cg:
        zpos 0

    return

label cg_虚掩的房门_2:
    show cg_img_3_1_1 onlayer cg:
        zpos 0
        alpha 0.0
        ease 3 alpha 0.8
        block:
            ease 3 alpha 0.4
            ease 3 alpha 0.8
            repeat
