# 躲进花之间
label cg_躲进花之间_1:
    camera cg:
        perspective True
        gl_depth True
        yoffset 120

    show cg_img_2_4_bg onlayer cg:
        zpos 0

    show cg_img_2_4_1 onlayer cg:
        zpos 0
        alpha 0.0
        ease 0.5 alpha 1.0

    show cg_img_2_4_2 onlayer cg:
        zpos 0
        alpha 0.0
        align (0.528, 0.518)
        ease 0.5 alpha 1.0
        pause 0.8

        block:
            ease 1.6 yoffset -40
            ease 1.6 yoffset 0
            repeat

    return
