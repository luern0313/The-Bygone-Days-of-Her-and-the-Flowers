init python:
    # 点击右键事件
    def turtle_soup_right_button():
        layout.yesno_screen(_("您确定要返回到标题界面吗？"), MainMenu(confirm=False, save=False))


# 监听右键点击
screen turtle_soup_right_button():
    key "game_menu" action Function(turtle_soup_right_button)


# 海龟汤
label turtle_soup():
    $ _autosave = False
    $ disable_menu()
    show screen turtle_soup_right_button()

    $ game = Game()
    call start_story_process("story/turtle_soup.txt") from _call_start_story_process_2
