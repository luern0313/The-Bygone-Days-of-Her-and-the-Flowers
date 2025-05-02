## 快捷菜单界面 ######################################################################
##
## 快捷菜单显示于游戏内，以便于访问游戏外的菜单。

screen quick_menu():

    ## 确保该菜单出现在其他界面之上，
    zorder 300

    if quick_menu:

        hbox:
            xalign 1.0
            yalign 1.0
            spacing -14
            yoffset -22
            xoffset -12

            # 自动
            imagebutton action Preference("auto-forward", "toggle"):
                selected_idle Image("gui/quick_menu/auto_selected.png")
                selected_hover Image("gui/quick_menu/auto_selected_hovered.png")
                hover Image("gui/quick_menu/auto_unselected_hovered.png")
                idle Image("gui/quick_menu/auto_unselected.png")

                hovered ShowTransient("quick_menu_tip", text="自动", xoff=-240)
                unhovered Hide("quick_menu_tip")

            # 快进
            imagebutton action Skip() alternate Skip(fast=True, confirm=True):
                selected_idle Image("gui/quick_menu/skip_selected.png")
                selected_hover Image("gui/quick_menu/skip_selected_hovered.png")
                hover Image("gui/quick_menu/skip_unselected_hovered.png")
                idle Image("gui/quick_menu/skip_unselected.png")

                hovered ShowTransient("quick_menu_tip", text="快进", xoff=-138)
                unhovered Hide("quick_menu_tip")

            # 设置
            imagebutton action ShowMenu():
                hover Image("gui/quick_menu/menu_hovered.png")
                idle Image("gui/quick_menu/menu.png")

                hovered ShowTransient("quick_menu_tip", text="设置", xoff=-36)
                unhovered Hide("quick_menu_tip")

default quick_menu = True


screen quick_menu_tip(text, xoff):
    zorder 300
    frame:
        align (1.0, 1.0)
        xoffset xoff

        at transform:
            on show:
                alpha 0.0
                yoffset -100
                easein 0.3 alpha 1.0 yoffset -150
            on hide:
                easeout 0.3 alpha 0.0 yoffset -100

        text _(text):
            size 40
            color "#375644"
            outlines  [ (3, "#e1eed9", 0, 0) ]
