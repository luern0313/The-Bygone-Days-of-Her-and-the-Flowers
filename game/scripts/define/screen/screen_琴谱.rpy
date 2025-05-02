screen screen_琴谱():
    frame:
        at transform:
            on show:
                alpha 0.0
                ease 0.3 alpha 1.0
            on hide:
                ease 0.3 alpha 0.0

        align (0.5, 0.0)

        add "琴谱"

        hbox:
            anchor (0.0, 0.5)
            pos (0.155, 0.22)

            text "2" size 100 color ("#000000" if game.variable_list[11] == 1 else "#999999")
            null width 150

            text "1" size 100 color ("#000000" if game.variable_list[11] == 2 else "#999999")
            null width 30

            text "3" size 100 color ("#000000" if game.variable_list[11] == 3 else "#999999")
            null width 30

            text "2" size 100 color ("#000000" if game.variable_list[11] == 4 else "#999999")
            null width 100

            text "?" size 100 color ("#000000" if game.variable_list[11] == 5 else "#999999")
            null width 70

            text "1" size 100 color ("#000000" if game.variable_list[11] == 6 else "#999999")
            null width 70

            text "2" size 100 color ("#000000" if game.variable_list[11] == 7 else "#999999")
            null width 180

            text "1" size 100 color ("#000000" if game.variable_list[11] == 8 else "#999999")
            null width 30

            text "5" size 100 color ("#000000" if game.variable_list[11] == 9 else "#999999")
            null width 40

            text "?" size 100 color ("#000000" if game.variable_list[11] == 10 else "#999999")
            null width 70

            text "5" size 100 color ("#000000" if game.variable_list[11] == 11 else "#999999")
            null width 65

            text "1" size 100 color ("#000000" if game.variable_list[11] == 12 else "#999999")
