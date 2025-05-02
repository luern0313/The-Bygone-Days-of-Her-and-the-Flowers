# 花车
label cg_花车_1:
    camera cg:
        perspective True
        gl_depth True
        zpos -1200
        pos (150, 329)
        easein 1.6 ypos 217

        pause 0.4

        pos (400, -380) zpos -1500
        easein 1.3 xpos 300

        pause 0.4

        pos (30, 0) zpos -300
        easein 2.0 zpos -150

    show cg_img_5_5_1 onlayer cg:
        zpos -400
        align (0.5, 0.5)
        yoffset -200

    pause 6.0

    return

label cg_花车_2:
    camera cg:
        perspective True
        gl_depth True
        pos (30, 0)
        zpos -150
        ease 5.0 zpos -500 pos (-20, -50)

    show cg_img_5_5_2 onlayer cg:
        zpos -400
        align (0.5, 0.5)
        yoffset -200
        alpha 0.0
        pause 1.0
        easein 5.0 alpha 0.8

    return
