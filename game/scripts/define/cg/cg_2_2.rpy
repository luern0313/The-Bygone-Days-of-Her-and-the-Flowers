# 教令院外人群
label cg_教令院外人群_1:
    show cg_img_2_2_bg:
        zpos -500
        zzoom True
        align (0.5, 0.5)
        matrixcolor TintMatrix("#E8E8E8") * SaturationMatrix(0.85)

    show cg_img_2_2_1:
        zpos -500
        zzoom True
        matrixcolor TintMatrix("#E8E8E8") * SaturationMatrix(0.85)
        alpha 0.0
        ease 0.5 alpha 1.0

    show cg_img_2_2_2:
        zpos -500
        zzoom True
        align (0.5, 0.3)
        rotate 0
        alpha 0.0
        ease 0.5 alpha 1.0
        block:
            xoffset 0
            rotate 0
            pause 0.75
            xoffset 50
            rotate 3
            pause 0.75
            repeat

    show cg_img_2_2_3:
        zpos -500
        zzoom True
        align (0.5, 0.3)
        rotate 0
        alpha 0.0
        ease 0.5 alpha 1.0
        block:
            xoffset 0
            rotate 0
            pause 0.75
            xoffset -40
            rotate -3
            pause 0.75
            repeat
    return

label cg_教令院外人群_2:
    pause 1

    hide cg_img_2_2_1
    hide cg_img_2_2_2
    hide cg_img_2_2_3
    with dissolve

    show cg_img_2_2_bg:
        parallel:
            ease 0.5 align (0.5, 0.7)
        parallel:
            ease 0.5 zoom 1.5

    pause 1
