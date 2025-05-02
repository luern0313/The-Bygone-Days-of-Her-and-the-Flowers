# 纳西妲在健康之家
label cg_纳西妲在健康之家_1:
    camera cg:
        perspective True
        gl_depth True
        zpos -1500
        xoffset -20
        pause 1.5
        easein 4 zpos -900

    show cg_img_1_2_bg onlayer cg:
        zpos -500
        zzoom True

    show cg_img_1_2_1 onlayer cg:
        zpos -500
        alpha 0.0
        ease 0.6 alpha 1.0

    pause 0.2

    show cg_img_1_2_2 onlayer cg:
        zpos 0
        alpha 0.0
        ease 0.6 alpha 1.0

    pause 0.5

    show cg_img_1_2_3 onlayer cg:
        zpos 0
        alpha 0.0
        ease 0.6 alpha 1.0

    pause 0.5

    show cg_img_1_2_4 onlayer cg:
        zpos 0
        alpha 0.0
        ease 0.6 alpha 1.0

    return

label cg_纳西妲在健康之家_2:
    camera cg:
        perspective True
        gl_depth True
        parallel:
            ease 1.2 zpos -200
        parallel:
            ease 1.2 xoffset 0

    pause 2.0
    return
