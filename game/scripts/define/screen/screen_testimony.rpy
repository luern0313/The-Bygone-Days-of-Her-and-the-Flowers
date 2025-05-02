# 证言中、讯问中标志
screen screen_trial_in_testimony(name):
    frame:
        at screen_in_testimony
        left_margin 250
        top_margin 155
        xsize 423
        ysize 139

        background Image("gui/trial/" + name + ".png", xalign=0.5, yalign=0.5)

# 开始证言、讯问
screen screen_start_testimony(name):
    button:
        at transform:
            alpha 0.0
            ease 0.3 alpha 1.0
        align (0.5, 0.5)

        add name
        action [ Hide(transition=Dissolve(0.3, time_warp=_warper.easeout)), Return() ]

    timer 4.9 action [ Hide(transition=Dissolve(0.3, time_warp=_warper.easeout)), Return() ]
