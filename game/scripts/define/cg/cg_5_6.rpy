# B与世界树
label cg_B与世界树_1:
    camera cg:
        perspective True
        gl_depth True
        zpos -600
        pos (-300, 70)
        easein 5.0 pos (-300, 30)

    show cg_img_5_6_bg onlayer cg:
        zpos 0
        align (0.5, 0.5)
        yoffset -200

    show cg_img_5_6_1 onlayer cg:
        zpos 100
        align (0.5, 0.5)
        yoffset -200

    return

label cg_B与世界树_2:
    hide cg_img_5_6_1 onlayer cg

    camera cg:
        perspective True
        gl_depth True
        zpos -500
        pos (-230, 10)

    show cg_img_5_6_bg onlayer cg:
        zpos 0
        align (0.5, 0.5)
        yoffset -200

    show cg_img_5_6_2 onlayer cg:
        zpos 100
        align (0.5, 0.5)
        yoffset -200

    return

label cg_B与世界树_3:
    camera cg:
        perspective True
        gl_depth True
        zpos -500
        pos (-230, 10)
        easein 3.5 pos (20, -100) zpos -100

    show cg_img_5_6_3 onlayer cg:
        zpos 100
        align (0.5, 0.5)
        yoffset -200

    pause 2.0

    return
