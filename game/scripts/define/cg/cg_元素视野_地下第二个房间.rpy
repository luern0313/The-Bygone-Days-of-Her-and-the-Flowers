label cg_元素视野_地下第二个房间_1:
    show 3_10_地下第二个房间 onlayer cg:
        xalign 0.5 yalign 0.5

    return

label cg_元素视野_地下第二个房间_2:
    show 4_9_地下第二个房间元素视野 onlayer cg:
        xalign 0.5 yalign 0.5
        crop (0.5, 0.5, 0.0, 0.0)
        blur 0.0
        parallel:
            easein 0.3 crop (0.0, 0.0, 1.0, 1.0)
        parallel:
            easein 0.3 blur 0.0

    return
