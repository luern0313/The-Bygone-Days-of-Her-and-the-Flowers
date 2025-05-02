# 派蒙撞到E
label cg_派蒙撞到E_1:
    camera cg:
        perspective True
        gl_depth True
        zpos -300
        xoffset -200
        yoffset 250

    show cg_img_4_2_bg onlayer cg:
        zpos 0

    show cg_img_4_2_1 onlayer cg:
        zpos 0
        block:
            ease 1.8 yoffset 25
            ease 1.8 yoffset -25
            repeat

    show cg_img_4_2_2 onlayer cg:
        zpos 0
        on show:
            alpha 0.0
            ease 0.2 alpha 1.0

    return
