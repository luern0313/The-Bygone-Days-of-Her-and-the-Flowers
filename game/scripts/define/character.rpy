define narrate = Character(None, screen="screen_narrate", what_suffix="{fast}{cps=2}\u200B\u200B\u200B{/cps}")
define scene_info = Character(None, callback=typewriter_sound, what_prefix="{color=#004a89}{cps=10}", what_suffix="{/cps}{/color}")
define sumeru_introduce = Character(None, screen="screen_sumeru_introduce", what_suffix="{fast}{cps=2}\u200B\u200B\u200B{/cps}")

image ctc:
    "gui/ctc.png"
    align (0.815, 0.94)
    alpha 0.0
    ease 0.3 alpha 1.0

# define base_character = Character("base_character", ctc="ctc", ctc_position="fixed")
define base_character = Character("base_character")
