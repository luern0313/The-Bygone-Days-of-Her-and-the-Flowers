define transition_fade_02 = Fade(0.2, 0, 0.2)  # 黑色转场
define transition_fade = Fade(0.5, 0, 0.5)  # 黑色转场
define transition_fade_10 = Fade(1.0, 0, 1.0)  # 黑色转场
define transition_fade_15 = Fade(1.5, 0, 1.5)  # 黑色转场
define transition_fade_25 = Fade(2.5, 0, 2.5)  # 黑色转场

define transition_white_fade = Fade(0.5, 0, 0.5, color="#FFFFFF")  # 白色转场

define transition_dissolve_10 = Dissolve(0.10)  # 溶解效果转场
define transition_dissolve_15 = Dissolve(0.15)  # 溶解效果转场
define transition_dissolve = Dissolve(0.25)  # 溶解效果转场
define transition_dissolve_70 = Dissolve(0.70)  # 溶解效果转场

transform transition_exposure(new_widget=None, old_widget=None):
    delay 0.7
    xalign 0.5 yalign 0.5

    old_widget
    matrixcolor BrightnessMatrix(0.0)
    easein 0.2 matrixcolor BrightnessMatrix(1.0)
    alpha 0.0

    new_widget
    matrixcolor BrightnessMatrix(1.0)
    alpha 1.0
    easein 0.5 matrixcolor BrightnessMatrix(0.0)

transform transition_exposure_03(new_widget=None, old_widget=None):
    delay 0.3
    xalign 0.5 yalign 0.5

    old_widget
    matrixcolor BrightnessMatrix(0.0)
    easein 0.1 matrixcolor BrightnessMatrix(1.0)
    alpha 0.0

    new_widget
    matrixcolor BrightnessMatrix(1.0)
    alpha 1.0
    easein 0.2 matrixcolor BrightnessMatrix(0.0)
