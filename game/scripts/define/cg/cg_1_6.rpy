# 真假艾尔海森
label cg_真假艾尔海森_1:
    camera cg:
        perspective True
        gl_depth True
        yoffset 166

    show cg_img_1_6_bg onlayer cg:
        zpos 0

    show cg_img_1_6_1 onlayer cg:
        zpos 0
        alpha 0.0
        ease 0.6 alpha 1.0

    show cg_img_1_6_2 onlayer cg:
        zpos 0

        parallel:
            alpha 0.0
            ease 0.6 alpha 1.0
        parallel:
            block:
                ease 0.07 matrixtransform OffsetMatrix(3.896, 2.316, 0.0)
                ease 0.07 matrixtransform OffsetMatrix(-2.36, 2.038, 0.0)
                ease 0.07 matrixtransform OffsetMatrix(3.795, -3.85, 0.0)
                ease 0.07 matrixtransform OffsetMatrix(0.621, 3.70, 0.0)
                ease 0.07 matrixtransform OffsetMatrix(-2.42, -3.94, 0.0)
                ease 0.07 matrixtransform OffsetMatrix(2.579, -2.51, 0.0)
                ease 0.07 matrixtransform OffsetMatrix(-2.22, -3.69, 0.0)
                ease 0.07 matrixtransform OffsetMatrix(0.56, 0.73, 0.0)
                ease 0.07 matrixtransform OffsetMatrix(2.508, -2.14, 0.0)
                ease 0.07 matrixtransform OffsetMatrix(-1.58, -5.47, 0.0)
                ease 0.07 matrixtransform OffsetMatrix(3.795, -3.85, 0.0)
                ease 0.07 matrixtransform OffsetMatrix(0.621, 3.70, 0.0)
                ease 0.07 matrixtransform OffsetMatrix(-2.42, -3.94, 0.0)
                ease 0.07 matrixtransform OffsetMatrix(0.56, 0.73, 0.0)
                ease 0.07 matrixtransform OffsetMatrix(2.508, -2.14, 0.0)
                ease 0.07 matrixtransform OffsetMatrix(-1.58, -5.47, 0.0)
                ease 0.07 matrixtransform OffsetMatrix(3.795, -3.85, 0.0)
                ease 0.07 matrixtransform OffsetMatrix(-2.36, 2.038, 0.0)
                ease 0.07 matrixtransform OffsetMatrix(3.795, -3.85, 0.0)
                ease 0.07 matrixtransform OffsetMatrix(0.621, 3.70, 0.0)
                repeat

    show cg_img_1_6_3 onlayer cg:
        zpos 0
        alpha 0.0
        ease 0.6 alpha 1.0

    pause 2.0

    return
