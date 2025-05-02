# 刹那之间
label cg_刹那之间_1:
    camera cg:
        perspective True
        gl_depth True
        zpos -50
        parallel:
            block:
                ease 0.5 matrixtransform OffsetMatrix(8.896, 7.316, 0.0)
                ease 0.5 matrixtransform OffsetMatrix(-8.36, 2.038, 0.0)
                ease 0.5 matrixtransform OffsetMatrix(3.795, -3.85, 0.0)
                ease 0.5 matrixtransform OffsetMatrix(3.621, 3.700, 0.0)
                ease 0.5 matrixtransform OffsetMatrix(-2.42, -8.94, 0.0)
                ease 0.5 matrixtransform OffsetMatrix(2.579, -4.51, 0.0)
                ease 0.5 matrixtransform OffsetMatrix(-7.22, -5.69, 0.0)
                ease 0.5 matrixtransform OffsetMatrix(-12.56, -6.73, 0.0)
                ease 0.5 matrixtransform OffsetMatrix(11.508, -7.14, 0.0)
                ease 0.5 matrixtransform OffsetMatrix(-7.58, -12.47, 0.0)
                repeat
        parallel:
            pause 1.6
            block:
                ease 1.4 blur 5.0
                ease 1.4 blur 1.0
                pause 1.0
                repeat

    show cg_img_5_3_bg onlayer cg:
        zpos 0

    show cg_img_5_3_1 onlayer cg:
        zpos 0

    return
