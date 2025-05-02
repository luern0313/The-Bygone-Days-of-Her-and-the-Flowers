# F脸红
label cg_F脸红_1:
    camera cg:
        perspective True
        gl_depth True
        zpos -800
        yoffset -150

    show cg_img_2_5_bg onlayer cg:
        zpos 0

    show cg_img_2_5_1 onlayer cg:
        zpos 0
        alpha 0.0
        ease 0.5 alpha 1.0

    return
