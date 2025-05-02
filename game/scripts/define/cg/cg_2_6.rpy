# 迪希雅挥拳头
label cg_迪希雅挥拳头_1:
    camera cg:
        perspective True
        gl_depth True
        zpos -200
        yoffset 150

    show cg_img_2_6_bg onlayer cg:
        zpos 0

    show cg_img_2_6_1 onlayer cg:
        zpos 0
        alpha 0.0
        ease 0.5 alpha 1.0

    show cg_img_2_6_2 onlayer cg:
        zpos 0
        alpha 0.0
        parallel:
            ease 0.5 alpha 1.0
        parallel:
            easein 5 xoffset -100 yoffset 50

    return
