import renpy

from game.scripts.game_ren import game

"""renpy
init -1 python:
"""

from typing import Optional


renpy.music.register_channel("ambient", mixer="ambient", loop=True, stop_on_mute=True, tight=True, file_prefix='', file_suffix='',
                             buffer_queue=True, movie=False, framedrop=False)


def play_music(name: str, channel: str = None, fade: Optional[int] = None, loop: bool = None, volume: float = None):
    if channel is None:
        channel = "music"
    if loop is None:
        loop = True
    if volume is None:
        volume = 0.8

    path = None
    if channel == "music":
        path = "music/" + name + ".mp3"
    elif channel == "sound":
        path = "audio/" + name + ".ogg"
    elif channel == "ambient":
        path = "audio/" + name + ".ogg"

    if not renpy.loadable(path):
        if renpy.config.developer:
            print(f"音频文件不存在：{path}")
        return

    if channel == "music":
        if fade is None:
            fade = 0.5
        renpy.music.play(path, loop=loop, fadeout=fade, fadein=fade, relative_volume=volume)
    elif channel == "sound":
        if fade is None:
            fade = 0
        renpy.music.play(path, channel="sound", loop=loop, fadeout=fade, fadein=fade, relative_volume=volume)
    elif channel == "ambient":
        game.ambient_sound_name = name
        renpy.music.play(path, channel="ambient", loop=loop)


def stop_music(channel: str = "music", fade: Optional[int] = None):
    if channel is None:
        channel = "music"
    if fade is None:
        fade = 2

    if channel == "ambient":
        game.ambient_sound_name = None
    renpy.music.stop(channel=channel, fadeout=fade)


def pause_ambient_sound():
    if game.ambient_sound_name is not None:
        renpy.music.stop(channel="ambient", fadeout=1.5)


def resume_ambient_sound():
    if game.ambient_sound_name is not None:
        renpy.music.play("audio/" + game.ambient_sound_name + ".ogg", channel="ambient", loop=True)
