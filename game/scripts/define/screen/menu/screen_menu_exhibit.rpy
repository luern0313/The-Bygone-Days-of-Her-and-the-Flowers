screen menu_exhibit():

    tag menu

    default page_name_value = FilePageNameInputValue(pattern=_("第 {} 页"), auto=_("自动存档"), quick=_("快速存档"))

    use game_menu(_("证据袋")):
        frame:
            left_padding 36
            xsize 1.0
            ysize 1.0
            bottom_margin 126

            vbox:
                ## 此代码确保输入控件在任意按钮执行前可以获取 enter 事件。
                order_reverse True
                xsize 1.0
                ysize 1.0

                null height 60

                hbox:
                    text "证据袋":
                        size 74
                        xoffset 16
                        color "#346649"
                        outlines  [ (6, "#346649", 0, 0), (4.5, "#FFFFFF", 0, 0) ]

                    null width 50

                    text "共{space=5}" + str(len(game.exhibit_list)) + "{space=5}个证据":
                        size 47
                        yoffset -6
                        yalign 1.0
                        color "#346649"
                        outlines  [ (3, "#fcfcfa", 0, 0) ]

                null height 30

                if len(game.exhibit_list) > 0:
                    vpgrid:
                        child_size (1.0, 1.0)
                        cols 3
                        xoffset 10
                        yspacing 18
                        mousewheel True

                        scrollbars "vertical"
                        vscrollbar_unscrollable "hide"
                        vscrollbar_xsize 18
                        vscrollbar_base_bar Null(width=18, height=1400)
                        vscrollbar_thumb Frame("gui/menu/exhibit_vertical_bar.png", 9, 9, 9, 9, tile=False)

                        for i in range(len(game.exhibit_list)):
                            $ exhibit = game.exhibit_list[i]

                            button:
                                xysize (583, 229)
                                action Show("screen_get_exhibit", _layer="screens", name=exhibit.name, img=exhibit.image, desc=exhibit.details,
                                            is_update=False, is_full=exhibit.is_full, add_to_list=False, is_menu=True)

                                hover_background Image("gui/menu/exhibit_item_selected_bg.png")
                                background Image("gui/menu/exhibit_item_bg.png")

                                if not exhibit.is_full:
                                    add "images/exhibit/" + exhibit.image + ".png":
                                        at transform:
                                            alpha 0.7
                                            blur 6.0
                                            matrixcolor SaturationMatrix(0) * TintMatrix("#DDD")
                                        xoffset 36
                                        yoffset 8
                                        xysize (150, 150)
                                        yalign 0.5

                                add "images/exhibit/" + exhibit.image + ".png":
                                    yalign 0.5
                                    if exhibit.is_full:
                                        xoffset 8
                                        xysize (190, 190)
                                    else:
                                        xoffset 28
                                        xysize (150, 150)

                                add "gui/menu/exhibit_item_fg.png":
                                    xsize 230
                                    ysize 203
                                    yalign 0.5
                                    xoffset 4.5

                                null height 12

                                text exhibit.name:
                                    color "#346649"
                                    size 40
                                    xsize 300
                                    xoffset 230
                                    yoffset 52
                                    outlines  [ (3, "#fcfcfa", 0, 0) ]

                else:
                    fixed:
                        text "旅行者还没有收集到证据{p}旅途还在继续…":
                            xysize (1.0, 1.0)
                            xalign 0.5
                            yalign 0.42
                            size 48
                            color "#7d907f"
                            outlines  [ (3, "#fcfcfa", 0, 0) ]
                            textalign 0.5
                            line_leading 24
