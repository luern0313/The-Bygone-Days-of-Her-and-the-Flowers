image snow1 = Fixed(Snow("images/particle/snow1.png"))
image snow2 = Fixed(Snow("images/particle/snow2.png"))

label cg_第二天世界树_1:
    camera cg:
        perspective True
        gl_depth True
        pos (370, -230) zpos -500.0

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

    show 世界树_2 onlayer cg:
        zpos -500
        zzoom True
        matrixanchor (0.5, 0.5)
        align (0.5, 0.5)
        block:
            ease 1.6 matrixcolor TintMatrix("#E8E8E8") * SaturationMatrix(0.85)
            ease 1.6 matrixcolor TintMatrix("#FFFFFF") * SaturationMatrix(1.0)
            repeat

    show leaf onlayer cg:
        zpos -500
        align (0.5, 0.5)
        zoom 1.33

    pause 6.0
    hide openeyes onlayer sticker
    return

label cg_第二天世界树_2:
    $ import random
    show 世界树_2 onlayer cg:
        zpos -500
        zoom 1.4
        matrixanchor (0.5, 0.5)
        align (0.5, 0.5)

        block:
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            ease 0.1 matrixtransform OffsetMatrix(random.uniform(-12, 12), random.uniform(-12, 12), 0.0)
            repeat

    show leaf onlayer cg:
        zpos -500
        align (0.5, 0.5)
        zoom 1.32
