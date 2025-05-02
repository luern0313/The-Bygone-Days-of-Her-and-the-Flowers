screen menu_gallery():
    tag menu

    use game_menu(_("画廊")):
        frame:
            left_padding 36
            xsize 1.0
            ysize 1.0
            bottom_margin 126

            vbox:
                order_reverse True
                xsize 1.0
                ysize 1.0

                null height 60

                hbox:
                    text "画廊":
                        size 74
                        xoffset 16
                        color "#346649"
                        outlines  [ (6, "#346649", 0, 0), (4.5, "#FFFFFF", 0, 0) ]

                    null width 50

                    text "已解锁{space=5}" + str(len(persistent.gallery_unlock)) + "{space=5}/{space=5}" + str(len(gallery_cg_list)) + "{space=5}":
                        size 47
                        yoffset -6
                        yalign 1.0
                        color "#346649"
                        outlines  [ (3, "#fcfcfa", 0, 0) ]

                null height 30

                vpgrid:
                    cols 3
                    xoffset 2
                    yspacing 22
                    mousewheel True

                    scrollbars "vertical"
                    vscrollbar_unscrollable "hide"
                    vscrollbar_xsize 18
                    vscrollbar_base_bar Null(width=18, height=1400)
                    vscrollbar_thumb Frame("gui/menu/exhibit_vertical_bar.png", 9, 9, 9, 9, tile=False)

                    for i in range(len(gallery_cg_list)):

                        $ gallery = gallery_cg_list[i]
                        $ is_unlocked = gallery.label in persistent.gallery_unlock

                        button:
                            if is_unlocked:
                                action [ Function(show_cg_gallery, i) ]

                            has vbox

                            frame:
                                if is_unlocked:
                                    add AlphaMask(Frame(f"gui/gallery/{gallery.label}.png"), Frame("gui/menu/archive_image_mask.svg")) xalign 0.5 yalign 0.5
                                    hover_background Frame("gui/menu/archive_image_selected.svg")
                                    background Frame("gui/menu/archive_image_unselected.svg")
                                else:
                                    add Frame(f"gui/gallery/unlocked.png") xalign 0.5 yalign 0.5
                                xsize 563
                                ysize 329
                                padding (14, 14)

                            null height 14

                            text _(gallery.name if is_unlocked else "未解锁"):
                                if is_unlocked:
                                    color "#346649"
                                else:
                                    color "#666666"
                                size 40
                                xoffset 14
