transform camera_special_default:
    perspective True
    gl_depth True
    zpos 0
    xpos 0
    blur 0
    yoffset 0
    xoffset 0
    rotate 0.0
    ypos 0
    matrixtransform OffsetMatrix(0.0, 0.0, 0.0)

transform camera_position_zoom_in_toggle:
    perspective True
    gl_depth True
    ease 0.3 zpos -100

transform camera_position_zoom_in:
    perspective True
    gl_depth True
    zpos -100

transform camera_position_zoom_out_toggle:
    perspective True
    gl_depth True
    time 0.25
    ease 0.25 zpos 0

transform camera_position_zoom_out:
    perspective True
    gl_depth True
    zpos 0

transform camera_special_memory:
    matrixcolor TintMatrix("#EEEED2") * SaturationMatrix(0.4)

transform camera_special_memory_cancel:
    matrixcolor TintMatrix("#FFFFFF") * SaturationMatrix(1.0)
