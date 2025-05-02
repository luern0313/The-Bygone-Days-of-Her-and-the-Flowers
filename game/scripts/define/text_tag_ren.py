import renpy
import config

"""renpy
init -2 python:
"""


def tag_color_highlight(tag, argument, contents):
    return [
        (renpy.TEXT_TAG, "color=#855818"),
    ] + contents + [
        (renpy.TEXT_TAG, "/color"),
    ]


def tag_color_highlight_red(tag, argument, contents):
    return [
        (renpy.TEXT_TAG, "color=#B43512"),
    ] + contents + [
        (renpy.TEXT_TAG, "/color"),
    ]


config.custom_text_tags["color_highlight"] = tag_color_highlight
config.custom_text_tags["color_highlight_red"] = tag_color_highlight_red
