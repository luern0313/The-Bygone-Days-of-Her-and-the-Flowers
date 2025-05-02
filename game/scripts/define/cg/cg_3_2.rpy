# 黑暗的房间
label cg_黑暗的房间_1:
    camera cg:
        perspective True
        gl_depth True
        zpos 0

    show cg_img_3_2_bg onlayer cg:
        zpos 0

    show cg_img_3_2_1 onlayer cg:
        zpos 0
        alpha 0.0
        ease 3 alpha 0.8
        block:
            ease 3 alpha 0.4
            ease 3 alpha 0.8
            repeat

    return

label cg_黑暗的房间_2:
    show cg_img_3_2_2 onlayer cg:
        zpos 0
        alpha 0.0
        ease 3 alpha 1.0
