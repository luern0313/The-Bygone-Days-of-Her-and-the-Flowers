label start_with_introduce:
    call start(True) from _call_start

label start_without_introduce:
    call start(False) from _call_start_1

label start(is_introduce_sumeru):
    define _dismiss_pause = False
    default save_name = "开场"
    default persistent.gallery_unlock = []
    default persistent.turtle_soup_1 = False
    default persistent.turtle_soup_2 = False
    default persistent.is_finish_mainline = False
    default persistent.grant_achievement = []

    python:
        renpy.layer_at_list([camera_position_zoom_in], camera=True)
        renpy.music.set_volume(1.2, 0, channel="voice")
        if config.developer:
            renpy.show_screen("screen_developer", _layer="screens")

        is_sec = False
        is_rec_mode = False

    if is_introduce_sumeru:
        $ game = Game()
        call start_story_process("story/sumeru_introduce.txt") from _call_start_story_process

    $ game = Game()
    call start_story_process("story/story.txt") from _call_start_story_process_1

    return
