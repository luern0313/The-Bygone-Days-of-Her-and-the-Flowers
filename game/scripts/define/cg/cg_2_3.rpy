# 看守所
label cg_看守所_1:
    show cg_img_2_3_bg zorder 0:
        zpos 0
        yoffset -20
        matrixcolor TintMatrix("#E8E8E8") * SaturationMatrix(0.85)

    show cg_img_2_3_1 zorder 100:
        zpos 0
        yoffset -20
        matrixcolor TintMatrix("#E8E8E8") * SaturationMatrix(0.85)
        alpha 0.0
        ease 0.5 alpha 1.0

    return
