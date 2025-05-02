image speed_line:
    Movie(play="video/speed_line.webm", side_mask=True)
    xzoom 1.5
    yzoom 1.5

image speed_line_white:
    Movie(play="video/speed_line_white.webm", side_mask=True)
    xzoom 1.5
    yzoom 1.5

image get_exhibit_bg:
    Movie(play="video/get_exhibit_bg.webm", side_mask=True, loop=False)

image get_exhibit_light:
    Movie(play="video/exhibit_light.webm", side_mask=True, loop=False)
    xzoom 1.333
    yzoom 1.333
    xoffset 180
    yoffset 64

image start_testifying:
    Movie(play="video/start_testifying.webm", loop=False)

image start_interrogate:
    Movie(play="video/start_interrogate.webm", loop=False)

image choices_exhibit_bg:
    Movie(play="video/choices_exhibit_bg.webm", side_mask=True, loop=False)
    xzoom 1.2658
    yzoom 1.2658

image choices_options_bg:
    Movie(play="video/choices_options_bg.webm", side_mask=True, loop=False)
    xzoom 1.2658
    yzoom 1.2658

image openeyes:
    Movie(play="video/openeyes.webm", side_mask=True, loop=False)
    xzoom 1.333
    yzoom 1.333

image memory:
    Movie(play="video/memory.webm", side_mask=True, loop=True)
    xzoom 1.333
    yzoom 1.333

image hallucination:
    Movie(play="video/hallucination.webm", loop=True)
    xzoom 1.333
    yzoom 1.333
    on hide:
        alpha 1.0
        ease 0.6 alpha 0.0

image link_start:
    Movie(play="video/link_start.webm", loop=False)
    xzoom 1.333
    yzoom 1.333
    on show:
        alpha 0.0
        ease 0.6 alpha 1.0
    on hide:
        alpha 1.0
        ease 0.6 alpha 0.0

image 闪回:
    Movie(play="video/闪回.webm", loop=False)
    xzoom 1.333
    yzoom 1.333
    on show:
        alpha 0.0
        ease 1.0 alpha 1.0
    on hide:
        alpha 1.0
        ease 1.0 alpha 0.0

image fireworks:
    Movie(play="video/fireworks.webm", side_mask=True, loop=False)
    xzoom 1.333
    yzoom 1.333
    on hide:
        alpha 1.0
        ease 0.3 alpha 0.0

image leaf:
    Movie(play="video/leaf.webm", side_mask=True, loop=True)
    xzoom 1.333
    yzoom 1.333
    on hide:
        alpha 1.0
        ease 0.3 alpha 0.0

image logo:
    Movie(play="video/logo.webm", side_mask=False, loop=False)
    xzoom 1.02
    yzoom 1.02
    on hide:
        alpha 1.0
        ease 1.0 alpha 0.0

image staff1:
    Movie(play="video/staff1.webm", side_mask=False, loop=False)
    xzoom 1.02
    yzoom 1.02
    on hide:
        alpha 1.0
        ease 1.0 alpha 0.0

image staff2:
    Movie(play="video/staff2.webm", side_mask=False, loop=False)
    xzoom 1.02
    yzoom 1.02
    on hide:
        alpha 1.0
        ease 1.0 alpha 0.0

image staff3:
    Movie(play="video/staff3.webm", side_mask=False, loop=False)
    xzoom 1.02
    yzoom 1.02
    on hide:
        alpha 1.0
        ease 1.0 alpha 0.0

image staff4:
    Movie(play="video/staff4.webm", side_mask=False, loop=False)
    xzoom 1.02
    yzoom 1.02
    on hide:
        alpha 1.0
        ease 1.0 alpha 0.0
