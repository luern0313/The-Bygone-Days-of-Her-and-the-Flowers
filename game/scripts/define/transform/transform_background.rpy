transform bg_position_blur:
    zpos -500
    zzoom True
    parallel:
        ease 0.3 blur 0.0
    parallel:
        ease 0.3 matrixcolor TintMatrix("#E8E8E8") * SaturationMatrix(0.85)
    # matrixcolor TintMatrix("#ffeec2") * SaturationMatrix(0.5, (0.2126, 0.7152, 0.0722))

transform bg_position_normal:
    zpos -500
    zzoom True
    parallel:
        ease 0.3 blur 0.0
    parallel:
        ease 0.3 matrixcolor TintMatrix("#FFF") * SaturationMatrix(1.0)

# 思考效果
transform bg_special_thinking:
    zpos -100
    matrixtransform ScaleMatrix(2.0, 2.0, 1.0)
    on show:
        alpha 0.0
        ease 1.0 alpha 0.6
    on hide:
        ease 0.7 alpha 0.0

transform bg_special_thinking_trial:
    zpos -100
    matrixanchor (0.5, 0.5)
    matrixtransform ScaleMatrix(4.0, 1.0, 1.0)
    on show:
        alpha 0.0
        ease 0.7 alpha 0.6
    on hide:
        ease 0.7 alpha 0.0

# 庭审
transform bg_position_trial:
    align (0.5, 0.5)
    zpos -150

transform bg_position_trial_foreground:
    align (0.5, 0.5)
    zpos 0

transform bg_position_trial_judge_foreground:
    align (0.5, 0.5)
    zpos 0

transform bg_transform_appear:
    on show:
        alpha 0.0
        ease 0.3 alpha 1.0
    on hide:
        ease 0.3 alpha 0.0

transform bg_transform_appear_06:
    on show:
        alpha 0.0
        ease 0.6 alpha 1.0
    on hide:
        ease 0.6 alpha 0.0

transform bg_transform_appear_10:
    on show:
        alpha 0.0
        ease 1.0 alpha 1.0
    on hide:
        ease 1.0 alpha 0.0
