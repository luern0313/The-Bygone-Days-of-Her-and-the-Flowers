# 庭审相关
transform camera_position_trial_defense:
    perspective True
    gl_depth True
    xpos -3840
    zpos -150
    rotate 0.0
    ypos 0
    blur 0
    matrixtransform OffsetMatrix(0, 0, 0.0)

transform camera_position_trial_witness:
    perspective True
    gl_depth True
    xpos 0
    zpos -150
    rotate 0.0
    ypos 0
    blur 0
    matrixtransform OffsetMatrix(0, 0, 0.0)

transform camera_position_trial_prosecution:
    perspective True
    gl_depth True
    xpos 3840
    zpos -150
    rotate 0.0
    ypos 0
    blur 0
    matrixtransform OffsetMatrix(0, 0, 0.0)


transform camera_position_trial_defense_toggle:
    perspective True
    gl_depth True
    zpos -150
    rotate 0.0
    ypos 0
    parallel:
        ease 0.56 xpos -3840
    parallel:
        easeout 0.28 blur 20
        easein 0.28 blur 0

transform camera_position_trial_witness_toggle:
    perspective True
    gl_depth True
    zpos -150
    rotate 0.0
    ypos 0
    parallel:
        ease 0.56 xpos 0
    parallel:
        easeout 0.28 blur 20
        easein 0.28 blur 0

transform camera_position_trial_prosecution_toggle:
    perspective True
    gl_depth True
    zpos -150
    rotate 0.0
    ypos 0
    parallel:
        ease 0.56 xpos 3840
    parallel:
        easeout 0.28 blur 20
        easein 0.28 blur 0

# 效果 旅行者凌空一指
transform camera_special_pointed:
    perspective True
    gl_depth True
    ease 0.2 pos (-3980, -12) zpos -474 rotate 6.0

# 效果 镜头抖动
transform camera_special_shake:
    perspective True
    gl_depth True
    zpos -150
    ease 0.05 matrixtransform OffsetMatrix(13.896, 12.316, 0.0)
    ease 0.05 matrixtransform OffsetMatrix(-13.36, 7.038, 0.0)
    ease 0.05 matrixtransform OffsetMatrix(10.795, -8.85, 0.0)
    ease 0.05 matrixtransform OffsetMatrix(10.621, 8.700, 0.0)
    ease 0.05 matrixtransform OffsetMatrix(-9.42, -14.94, 0.0)
    ease 0.05 matrixtransform OffsetMatrix(7.579, -9.51, 0.0)
#     ease 0.05 matrixtransform OffsetMatrix(-12.22, -10.69, 0.0)
#     eaRRse 0.05 matrixtransform OffsetMatrix(-19.56, -11.73, 0.0)
#     ease 0.05 matrixtransform OffsetMatrix(16.508, -12.14, 0.0)
#     ease 0.05 matrixtransform OffsetMatrix(-12.58, -18.47, 0.0)
    ease 0.05 matrixtransform OffsetMatrix(0.0, 0.0, 0.0)

# 效果 镜头抖动
transform camera_special_shake_loop:
    perspective True
    gl_depth True
    zpos -150
    block:
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        ease 0.08 matrixtransform OffsetMatrix(random.uniform(-30, 30), random.uniform(-30, 30), 0.0)
        repeat

transform camera_special_shake_loop_stop:
    perspective True
    gl_depth True
    zpos -150
    matrixtransform OffsetMatrix(0, 0, 0.0)
