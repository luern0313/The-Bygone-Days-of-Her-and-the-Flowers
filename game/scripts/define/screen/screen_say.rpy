## 对话界面 ########################################################################
##
## 对话界面用于向用户显示对话。它需要两个参数，who 和 what，分别是叙述角色的名字
## 和所叙述的文本。（如果没有名字，参数 who 可以是 None。）
##
## 此界面必须创建一个 id 为 what 的文本可视控件，因为 Ren'Py 使用它来管理文本显
## 示。它还可以创建 id 为 who 和 id 为 window 的可视控件来应用样式属性。
##
## https://www.renpy.cn/doc/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window id "window":
        if is_dialogue_state():
            at transform:
                on hide:
                    ease 0.3 alpha 0.0
        else:
            at transform:
                on show:
                    function into_dialogue_state
                    alpha 0.0
                    ease 0.3 alpha 1.0
                on hide:
                    ease 0.3 alpha 0.0

        frame:
            xsize 1.0
            ysize 193
            xalign 0.5
            yalign 1.0

            background Image("gui/bottom.png", xalign=0.5, yalign=1.0)

        frame:
            yoffset -40

            frame:
                xsize 1.0
                ysize 400
                xalign 0.5
                yalign 0.8
                xoffset 24

                text what id "what":
                    xanchor 0.0
                    yanchor 0.0
                    xpos 0.207
                    xsize 0.62
                    ysize 350
                    line_spacing 20

                    if who is not None:
                        ypos 0.412
                    else:
                        ypos 0.372

                background Image("gui/textbox.png", xalign=0.5, yalign=0.8)

            if who is not None:
                frame:
                    id "namebox"
                    style "namebox"
                    text who id "who":
                        xanchor 0.0
                        yanchor 0.5
                        ypos 0.45
                        xpos 0.05
                        color gui.name_color

            frame:
                xsize 1.0
                ysize 400
                xalign 0.5
                yalign 0.8
                left_margin 70
                bottom_margin 70

                background Image("gui/textbox_ornament.png", xalign=0.5, yalign=0.8)

        use quick_menu()

## 通过 Character 对象使名称框可用于样式化。
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height
    left_padding gui.namebox_padding_left

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False
