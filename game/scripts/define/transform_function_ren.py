import renpy

from game.scripts.game_ren import game, is_rec_mode
from game.scripts.screen_ren import show_time_indicator
from game.scripts.status_ren import Status, into_state, has_status

"""renpy
init -2 python:
"""


def typewriter_sound(event, interact=True, **kwargs):
    if not interact:
        return

    if event == "show":
        renpy.play("audio/typewriter.ogg", channel="sound")
        renpy.sound.queue("audio/typewriter.ogg")
        renpy.sound.queue("audio/typewriter.ogg")
        renpy.sound.queue("audio/typewriter.ogg")
        renpy.sound.queue("audio/typewriter.ogg")
        renpy.sound.queue("audio/typewriter.ogg")
        renpy.sound.queue("audio/typewriter.ogg")
        renpy.sound.queue("audio/typewriter.ogg")
        renpy.sound.queue("audio/typewriter.ogg")
        renpy.sound.queue("audio/typewriter.ogg")
        renpy.sound.queue("audio/typewriter.ogg")
        renpy.sound.queue("audio/typewriter.ogg")
        renpy.sound.queue("audio/typewriter.ogg")
        renpy.sound.queue("audio/typewriter.ogg")
        renpy.sound.queue("audio/typewriter.ogg")
        renpy.sound.queue("audio/typewriter.ogg")
        renpy.sound.queue("audio/typewriter.ogg")
        renpy.sound.queue("audio/typewriter.ogg")
        renpy.sound.queue("audio/typewriter.ogg")
        renpy.sound.queue("audio/typewriter.ogg")
        renpy.sound.queue("audio/typewriter.ogg")

    elif event == "slow_done" or event == "end":
        renpy.sound.stop(fadeout=0.3)


def voice_male_sound(event, interact=True, **kwargs):
    if not interact:
        return

    if event == "show":
        renpy.play("audio/blipmale.ogg", channel="sound")
        renpy.sound.queue("audio/blipmale.ogg")
        renpy.sound.queue("audio/blipmale.ogg")
        renpy.sound.queue("audio/blipmale.ogg")
        renpy.sound.queue("audio/blipmale.ogg")
        renpy.sound.queue("audio/blipmale.ogg")
        renpy.sound.queue("audio/blipmale.ogg")
        renpy.sound.queue("audio/blipmale.ogg")
        renpy.sound.queue("audio/blipmale.ogg")
        renpy.sound.queue("audio/blipmale.ogg")
        renpy.sound.queue("audio/blipmale.ogg")
        renpy.sound.queue("audio/blipmale.ogg")
        renpy.sound.queue("audio/blipmale.ogg")
        renpy.sound.queue("audio/blipmale.ogg")
        renpy.sound.queue("audio/blipmale.ogg")
        renpy.sound.queue("audio/blipmale.ogg")
        renpy.sound.queue("audio/blipmale.ogg")
        renpy.sound.queue("audio/blipmale.ogg")
        renpy.sound.queue("audio/blipmale.ogg")
        renpy.sound.queue("audio/blipmale.ogg")
        renpy.sound.queue("audio/blipmale.ogg")

    elif event == "slow_done" or event == "end":
        renpy.sound.stop(fadeout=0.3)


def voice_female_sound(event, interact=True, **kwargs):
    if not interact:
        return

    if event == "show":
        renpy.play("audio/blipfemale.ogg", channel="sound")
        renpy.sound.queue("audio/blipfemale.ogg")
        renpy.sound.queue("audio/blipfemale.ogg")
        renpy.sound.queue("audio/blipfemale.ogg")
        renpy.sound.queue("audio/blipfemale.ogg")
        renpy.sound.queue("audio/blipfemale.ogg")
        renpy.sound.queue("audio/blipfemale.ogg")
        renpy.sound.queue("audio/blipfemale.ogg")
        renpy.sound.queue("audio/blipfemale.ogg")
        renpy.sound.queue("audio/blipfemale.ogg")
        renpy.sound.queue("audio/blipfemale.ogg")
        renpy.sound.queue("audio/blipfemale.ogg")
        renpy.sound.queue("audio/blipfemale.ogg")
        renpy.sound.queue("audio/blipfemale.ogg")
        renpy.sound.queue("audio/blipfemale.ogg")
        renpy.sound.queue("audio/blipfemale.ogg")
        renpy.sound.queue("audio/blipfemale.ogg")
        renpy.sound.queue("audio/blipfemale.ogg")
        renpy.sound.queue("audio/blipfemale.ogg")
        renpy.sound.queue("audio/blipfemale.ogg")
        renpy.sound.queue("audio/blipfemale.ogg")

    elif event == "slow_done" or event == "end":
        renpy.sound.stop(fadeout=0.3)


def click_sound(event, interact=True, **kwargs):
    if not interact:
        return
    # if event == "show":
        # renpy.play("audio/click.ogg", channel="sound")


def sound_jump(trans, st, at):
    renpy.play("audio/jump.ogg", channel="sound")


def sound_get_exhibit(trans, st, at):
    renpy.play("audio/get_exhibit.ogg", channel="sound")


def sound_choices_exhibit(trans, st, at):
    renpy.play("audio/choices_exhibit.ogg", channel="sound")


def sound_choices_exhibit_choices(trans, st, at):
    renpy.play("audio/choices_exhibit_choices.ogg", channel="audio")


def sound_choices_options_choices(trans, st, at):
    if not is_rec_mode:
        renpy.play("audio/choices_exhibit_choices.ogg", channel="audio")


def sound_choices_exhibit_tip(trans, st, at):
    renpy.play("audio/choices_exhibit_tip.ogg", channel="audio")


def is_dialogue_state() -> bool:
    return has_status(Status.dialogue)


def into_dialogue_state(trans, st, at):
    into_state(Status.dialogue)


def expand_time_indicator_if_collapse(trans, st, at):
    if has_status(Status.time_indicator_showing):
        show_time_indicator("expand")


# 收起证据时间条
def collapse_time_indicator_if_expand(trans, st, at):
    if has_status(Status.time_indicator_showing):
        show_time_indicator("collapse")


def sound_show_exhibit(trans, st, at):
    renpy.play("audio/click.ogg", channel="sound")


def sound_lightbulb(trans, st, at):
    renpy.play("audio/lightbulb.ogg", channel="audio")
