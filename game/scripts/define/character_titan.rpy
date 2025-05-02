image 泰坦_表情_正常:
    "cg_泰坦_正常"
    block:
        ease 2.2 yoffset 20
        ease 2.2 yoffset -20
        repeat

image 泰坦_表情_疑惑:
    "cg_泰坦_疑惑_2"
    anchor (0.5, 0.5)
    block:
        parallel:
            ease 1.2 xoffset 30
            pause 1.2
            ease 1.2 xoffset -30
            pause 1.2
        parallel:
            ease 1.2 matrixtransform RotateMatrix(0, 0, 10)
            pause 1.2
            ease 1.2 matrixtransform RotateMatrix(0, 0, -10)
            pause 1.2
        repeat

image 泰坦 正常 = Composite(
    (1558, 1394),
    (0, 0), "cg_泰坦",
    (0, 0), "泰坦_表情_正常"
)

image 泰坦 疑惑 = Composite(
    (1558, 1394),
    (0, 0), "cg_泰坦",
    (0, 0), "泰坦_表情_疑惑",
    (0, 0), "cg_泰坦_疑惑_1"
)
