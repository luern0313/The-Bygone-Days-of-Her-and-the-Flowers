# 照片
label cg_照片_1:
    camera cg:
        perspective True
        gl_depth True
        yoffset 0

    show cg_img_5_7_1 onlayer cg:
        zpos 0
        align (0.5, 0.5)

    return

label cg_照片_2:
    camera cg:
        perspective True
        gl_depth True
        yoffset 0

    show cg_img_5_7_2 onlayer cg:
        zpos 0
        align (0.5, 0.5)
    with transition_exposure_03

    return
