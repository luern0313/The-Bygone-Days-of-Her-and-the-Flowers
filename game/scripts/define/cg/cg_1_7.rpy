# E挽留B
label cg_E挽留B_1:
    camera cg:
        perspective True
        gl_depth True
        yoffset 166

    show cg_img_1_7_bg onlayer cg:
        zpos 0

    show cg_img_1_7_1 onlayer cg:
        zpos 0
        alpha 0.0
        ease 0.6 alpha 1.0

    show cg_img_1_7_2 onlayer cg:
        zpos 0
        offset (-100, -100)
        alpha 0.0
        parallel:
            ease 0.6 alpha 1.0
        parallel:
            easein 5 offset (60, 60)

    pause 1.5

    return
