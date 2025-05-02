label cg_世界树_1:
    camera cg:
        perspective True
        gl_depth True
        pos (383, -235) zpos -500.0

        parallel:
            pause 3.6
            ease 3.0 pos (0, 0) zpos -20.0
        parallel:
            block:
                ease 2 matrixtransform OffsetMatrix(13.896, 12.316, 0.0)
                ease 2 matrixtransform OffsetMatrix(-13.36, 7.038, 0.0)
                ease 2 matrixtransform OffsetMatrix(10.795, -8.85, 0.0)
                ease 2 matrixtransform OffsetMatrix(10.621, 8.700, 0.0)
                ease 2 matrixtransform OffsetMatrix(-9.42, -14.94, 0.0)
                ease 2 matrixtransform OffsetMatrix(7.579, -9.51, 0.0)
                ease 2 matrixtransform OffsetMatrix(-12.22, -10.69, 0.0)
                ease 2 matrixtransform OffsetMatrix(-19.56, -11.73, 0.0)
                ease 2 matrixtransform OffsetMatrix(16.508, -12.14, 0.0)
                ease 2 matrixtransform OffsetMatrix(-12.58, -18.47, 0.0)
                repeat
        parallel:
            pause 1.6
            block:
                ease 1.4 blur 5.0
                ease 1.4 blur 1.0
                pause 1.0
                repeat


    show openeyes onlayer sticker zorder 100

    show 世界树_1 onlayer cg:
        zpos -500
        zzoom True
        block:
            ease 1.6 matrixcolor TintMatrix("#E8E8E8") * SaturationMatrix(0.85)
            ease 1.6 matrixcolor TintMatrix("#FFFFFF") * SaturationMatrix(1.0)
            repeat

    show leaf onlayer cg:
        zpos -500
        align (0.5, 0.5)
        zoom 1.32

    pause 6.0
    hide openeyes onlayer sticker
    return
