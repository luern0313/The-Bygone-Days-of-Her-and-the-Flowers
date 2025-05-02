## 游戏菜单界面 ######################################################################
##
## 此界面列出了游戏菜单的基本共同结构。可使用界面标题调用，并显示背景、标题和导
## 航菜单。
##
## scroll 参数可以是 None，也可以是 viewport 或 vpgrid。当此界面与一个或多个子界
## 面同时使用时，这些子界面将被嵌入（放置）在其中。

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    add "gui/menu/bg.png"

    imagebutton:
        idle "gui/menu/back_unhover.png"
        hover "gui/menu/back_hover.png"
        style "return_button"
        action Return()

    frame:
        style "game_menu_outer_frame"

        hbox:
            ## 导航部分的预留空间。
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_outer_frame:
    bottom_padding 60

style game_menu_navigation_frame:
    xsize 560
    yfill True

style game_menu_content_frame:
    left_margin 80
    right_margin 40
    top_margin 20

style game_menu_viewport:
    xsize 1840

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 20

style return_button is button:
    yalign 0.0
    yoffset 40
