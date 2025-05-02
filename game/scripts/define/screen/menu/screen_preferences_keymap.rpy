screen preferences_keymap():
    button:
        at transform:
            alpha 0.0
            ease 0.3 alpha 1.0

        xysize(1.01, 1.01)
        align (0.5, 0.5)
        add Frame("images/other/keymap.png")
        action [ Hide(transition=Dissolve(0.3, time_warp=_warper.easeout)), Return() ]

    timer 8 action [ Hide(transition=Dissolve(0.3, time_warp=_warper.easeout)), Return() ]


screen preferences_keymap_white():
    button:
        at transform:
            alpha 0.0
            ease 0.3 alpha 1.0

        xysize(1.02, 1.02)
        align (0.5, 0.5)
        add Frame("images/other/keymap_white.png")
        action Hide(transition=Dissolve(0.3, time_warp=_warper.easeout))

    key "game_menu" action Hide(transition=Dissolve(0.3, time_warp=_warper.easeout))


screen preferences_staff():
    button:
        at transform:
            alpha 0.0
            ease 0.3 alpha 1.0

        xysize(1.02, 1.02)
        align (0.5, 0.5)
        add Frame("images/other/staff.png")
        action Hide(transition=Dissolve(0.3, time_warp=_warper.easeout))

    key "game_menu" action Hide(transition=Dissolve(0.3, time_warp=_warper.easeout))

