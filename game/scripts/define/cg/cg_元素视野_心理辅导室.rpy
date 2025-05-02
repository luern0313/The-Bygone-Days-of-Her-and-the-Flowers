label cg_元素视野_心理辅导室_1:
    show 4_5_第三天心理辅导室 onlayer cg:
        xalign 0.5 yalign 0.5

    return

label cg_元素视野_心理辅导室_2:
    show 4_8_心理辅导室元素视野 onlayer cg:
        xalign 0.5 yalign 0.5
        crop (0.5, 0.5, 0.0, 0.0)
        blur 0.0
        parallel:
            easein 0.3 crop (0.0, 0.0, 1.0, 1.0)
        parallel:
            easein 0.3 blur 0.0

    return
