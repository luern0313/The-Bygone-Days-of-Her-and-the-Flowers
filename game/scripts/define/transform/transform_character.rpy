# 立绘默认状态
transform char_special_default:
    fit "scale-down"
    xysize (0.848, 0.848)
    anchor (0.5, 1.0)
    ypos 0.939
    zpos 200

# 立绘位置 左中右
transform char_position_left:
    xpos 0.31

transform char_position_center:
    xpos 0.5

transform char_position_right:
    xpos 0.69


# 立绘从中间过渡到左侧
transform char_position_smooth_to_left:
    alpha 0
    xpos 0.35
    time 0.1
    parallel:
        easein 0.4 alpha 1.0
    parallel:
        easein 0.4 xpos 0.31


# 立绘渐变出现消失
transform char_transform_appear_toggle:
    alpha 0
    ease 0.4 alpha 1.0

transform char_transform_appear_toggle_delay:
    alpha 0
    time 0.2
    ease 0.3 alpha 1.0

transform char_transform_disappear_toggle:
    ease 0.3 alpha 0.0

transform char_transform_appear:
    alpha 1.0

transform char_transform_disappear:
    alpha 0.0

transform char_transform_narration:
    on show:
        alpha 0.0
        ease 0.5 alpha 1.0
    on hide:
        ease 0.5 alpha 0.0


# 立绘活跃-非活跃状态渐变切换
transform char_active_inactive_toggle:
    ease 0.15 matrixcolor TintMatrix("#AAA")
    alpha 1.0

transform char_active_active_toggle:
    ease 0.15 matrixcolor TintMatrix("#FFF")
    alpha 1.0

transform char_active_inactive:
    matrixcolor TintMatrix("#AAA")
    alpha 1.0

transform char_active_active:
    matrixcolor TintMatrix("#FFF")
    alpha 1.0
