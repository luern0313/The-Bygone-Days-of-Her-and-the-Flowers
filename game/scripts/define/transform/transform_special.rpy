# 效果 蹦跳
transform char_special_ypos_jump:
    yoffset -20
    ease 0.1 zoom 1.03
    pause 0.04

    function sound_jump
    easein_quad 0.08 yoffset -80
    easeout 0.14 yoffset -20
    pause 0.05

    function sound_jump
    easein_quad 0.12 yoffset -80
    easeout 0.15 yoffset -20
    pause 0.04

    ease 0.16 zoom 1

# 效果 派蒙漂浮
transform char_special_ypos_paimon_float:
    ease 0.8 yoffset 0
    block:
        ease 1.6 yoffset -40
        ease 1.6 yoffset 0
        repeat

# 效果 缓慢出现、用于第一次出场等
transform char_special_appear_slowly:
    alpha 0
    ease 1.5 alpha 1.0

# 效果 从上到下出现
transform char_special_appear_down:
    alpha 0
    anchor (0.5, 0.0)
    ypos 0.092
    crop (0, 0, 1.0, 0.0)
    ease 1.5 alpha 1.0 crop (0, 0, 1.0, 1.0)

# 效果 缓慢消失
transform char_special_disappear_slowly:
    alpha 1.0
    ease 1 alpha 0.0

# 效果 抖动
transform char_special_shake:
    matrixanchor (0.5, 0.5)
    ease 0.08 matrixtransform OffsetMatrix(13.896, 12.316, 0.0)
    ease 0.08 matrixtransform OffsetMatrix(-13.36, 7.038, 0.0)
    ease 0.08 matrixtransform OffsetMatrix(10.795, -8.85, 0.0)
    ease 0.08 matrixtransform OffsetMatrix(10.621, 8.700, 0.0)
    ease 0.08 matrixtransform OffsetMatrix(-9.42, -14.94, 0.0)
    ease 0.08 matrixtransform OffsetMatrix(7.579, -9.51, 0.0)
    ease 0.08 matrixtransform OffsetMatrix(-12.22, -10.69, 0.0)
    ease 0.08 matrixtransform OffsetMatrix(2.56, 1.73, 0.0)
#     ease 0.08 matrixtransform OffsetMatrix(16.508, -12.14, 0.0)
#     ease 0.08 matrixtransform OffsetMatrix(-12.58, -18.47, 0.0)
    ease 0.08 matrixtransform OffsetMatrix(0.0, 0.0, 0.0)

# 效果 从下方出现
transform char_special_up:
    yoffset 1100
    function sound_jump
    ease 0.25 yoffset 0

# 效果 从下方消失
transform char_special_down:
    function sound_jump
    ease 0.25 yoffset 1100

# 看守所 牢大 代替char_special_default
transform char_special_prison:
    fit "scale-down"
    xysize(0.788, 0.788)
    xanchor 0.5
    yanchor 1.0
    ypos 0.919
    zpos 0

transform bg_special_thinking_trial_fast:
    zpos -100
    matrixanchor (0.5, 0.5)
    matrixtransform ScaleMatrix(4.0, 1.0, 1.0)
    on show:
        alpha 0.0
        ease 0.3 alpha 0.8
    on hide:
        ease 0.5 alpha 0.0
