# 启动游戏流程
# - 主线
# - 两个海龟汤
label start_story_process(story_path):
    $ story_texts = renpy.open_file(story_path, encoding="utf-8").readlines()

    while game.index < len(story_texts):
        python:
            lines = []
            (statement_index, game.index) = get_next_statement(game.index, story_texts, lines)
            parse_single(statement_index, lines)
            renpy.restart_interaction()
    return


# 批量call label
# - 主菜单画廊
# - 键位帮助
label batch_call_label(target_list):
    $ _dismiss_pause = True
    $ stop_music()
    $ i = 0
    while i < len(target_list):
        call expression target_list[i] from _call_expression
        with Dissolve(0.2)
        pause
        $ i += 1
    $ _dismiss_pause = False
    return
