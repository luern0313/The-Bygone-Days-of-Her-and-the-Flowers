# 神明相拥
label cg_神明相拥_1:
    camera cg:
        perspective True
        gl_depth True
        zpos -800
        yoffset -100
        easein_quad 180 zpos 0 yoffset 160

    show cg_img_5_2_bg onlayer cg zorder 99:
        zpos 0

    show cg_img_5_2_1 onlayer cg zorder 99:
        zpos 300
        zoom 0.8
        align (0.5, 0.5)
        yoffset 80
        on show:
            alpha 0.0
            ease 0.3 alpha 1.0
        on hide:
            ease 1.7 alpha 0.0

    return

label cg_神明相拥_2:
    hide cg_img_5_2_1 onlayer cg

    show cg_img_5_2_2 onlayer cg zorder 99:
        zpos 300
        zoom 0.8
        align (0.5, 0.5)
        yoffset 80
        on show:
            alpha 0.0
            ease 2.0 alpha 1.0
        on hide:
            ease 2.0 alpha 0.0

    pause 2.0
    return

label cg_神明相拥_3:
    hide cg_img_5_2_2 onlayer cg

    show cg_img_5_2_3 onlayer cg zorder 99:
        zpos 300
        zoom 0.8
        align (0.5, 0.5)
        yoffset 80
        on show:
            alpha 0.0
            ease 2.0 alpha 1.0
        on hide:
            ease 0.3 alpha 0.0

    pause 2.0
    return
