# 花神诞祭
label cg_花神诞祭_1:
    camera cg:
        perspective True
        gl_depth True
        zpos 0
        yoffset 160

    show black onlayer cg:
        zpos 0
        zoom 2.0

    pause 2.0

    show cg_img_4_1_1 onlayer cg:
        zpos 0
        on show:
            alpha 0.0
            ease 0.2 alpha 1.0

    pause 1.8

    show cg_img_4_1_2 onlayer cg:
        zpos 0
        on show:
            alpha 0.0
            ease 0.2 alpha 1.0

    pause 1.5

    show cg_img_4_1_3 onlayer cg:
        zpos 0
        on show:
            alpha 0.0
            ease 0.2 alpha 1.0

    pause 1.5

    show cg_img_4_1_4 onlayer cg:
        zpos 0
        on show:
            alpha 0.0
            ease 0.2 alpha 1.0

    return
