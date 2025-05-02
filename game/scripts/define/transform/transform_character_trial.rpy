# 立绘位置 左中右
transform char_position_trial_ypos_left:
    matrixanchor (0.5, 0.5)
    matrixtransform ScaleMatrix(1.15, 1.15, 1.15) * OffsetMatrix(-3030, 190, -50)

transform char_position_trial_ypos_center:
    matrixanchor (0.5, 1.0)
    matrixtransform ScaleMatrix(0.95, 0.95, 0.95)
    xalign 0.5
    xoffset -20
    yoffset 20
    zpos -50

transform char_position_trial_ypos_right:
    matrixanchor (0.5, 0.5)
    matrixtransform ScaleMatrix(1.28, 1.28, 1.28) * OffsetMatrix(3542, 190, -50)

transform char_position_trial_ypos_assistant:
    matrixanchor (0.5, 0.0)
    matrixtransform ScaleMatrix(0.98, 0.98, 0.98) * OffsetMatrix(0, 0, -50)
    xalign 0.5
    yalign 0.5
