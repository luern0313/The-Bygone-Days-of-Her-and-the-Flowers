## 此文件包含有可自定义您游戏的设置。
##
## 以“##”开头的语句是注释，您不应该对其取消注释。以“#”开头的语句是注释掉的代码，
## 在适用的时候您可能需要对其取消注释。


## 基础 ##########################################################################

## 用户可读的游戏名称。此命令用来设置默认窗口标题，并且会在界面和错误报告中出
## 现。
##
## 带有 _() 的字符串表示其可被翻译。

define config.name = _("只属于「她与花」的往日")


## 游戏版本号。

define config.version = "1.0"


## 放置在游戏内“关于”屏幕上的文本。将文本放在三个引号之间，并在段落之间留出空
## 行。

define gui.about = _p("""
""")


## 在构建的发布版中，可执行文件和目录所使用的短名称。此处仅限使用 ASCII 字符，并
## 且不能包含空格、冒号或分号。

define build.name = "HerAndTheFlowers"


init python:
    import os
    def get_subdirectories(root_folder):
        subdirectories = []
        for dirpath, dirnames, filenames in os.walk(root_folder):
            for dirname in dirnames:
                subdirectories.append(os.path.relpath(os.path.join(dirpath, dirname), "./"))
        return subdirectories

define config.search_prefixes = config.search_prefixes + get_subdirectories("images/")

## 图层 ##########################################################################

define config.layers = [ "master", "cg", "sticker", "transient", "screens", "overlay" ]

define config.tag_layer = { "speed_line": "sticker" }


## 音效和音乐 #######################################################################

define config.tts_voice = None

define config.voice_filename_format = "{filename}"

## 将以下语句取消注释就可以设置标题界面播放的背景音乐文件。此文件将在整个游戏中
## 持续播放，直至音乐停止或其他文件开始播放。

define config.main_menu_music = "music/成歩堂 龍一 ～異議あり！ 2013.mp3"

default preferences.wait_voice = True

define config.default_music_volume = 0.9
define config.default_sfx_volume = 0.9


## 转场 ##########################################################################
##
## 这些变量用来控制某些事件发生时的转场。每一个变量都应设置成一个转场，或者是
## None 来表示无转场。

## 进入或退出游戏菜单。

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## 各个游戏菜单之间的转场。

define config.intra_transition = Dissolve(0.1)


## 载入游戏后使用的转场。

define config.after_load_transition = None


## 在游戏结束之后进入主菜单时使用的转场。

define config.end_game_transition = None


## 用于控制在游戏开始标签不存在时转场的变量。作为替代，在显示初始化场景后使用
## with 语句。


## 窗口管理 ########################################################################
##
## 此命令控制对话框窗口何时显示。若为 show，对话框将总是显示。若为 hide，对话框
## 仅在对话出现时显示。若为 auto，对话框会在 scene 语句前隐藏，并在有新对话时重
## 新显示。
##
## 在游戏开始后，可以用 window show、window hide 和 window auto 语句来改变其状
## 态。

define config.window = "auto"


## 用于显示和隐藏对话框窗口的转场

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## 默认设置 ########################################################################

## 控制默认的文字显示速度。默认的 0 为瞬间，而其他数字则是每秒显示出的字符数。

default preferences.text_cps = 18


## 默认的自动前进延迟。数字越大，等待时间越长，有效范围为 0 - 30。

default preferences.afm_time = 10

default preferences.gl_framerate = 60


## 存档目录 ########################################################################
##
## 控制 Ren'Py 放置游戏存档的特定操作系统目录。存档文件将放置在：
##
## Windows：%APPDATA\RenPy\<config.save_directory>
##
## Macintosh：$HOME/Library/RenPy/<config.save_directory>
##
## Linux：$HOME/.renpy/<config.save_directory>
##
## 该语句通常不应变更，若要变更，应为有效字符串而不是表达式。

define config.save_directory = "The-Bygone-Days-of-Her-and-the-Flowers"


## 图标 ##########################################################################
##
## 在任务栏或 Dock 上显示的图标。

define config.window_icon = "gui/window_icon.png"


## 构建配置 ########################################################################
##
## 此部分控制 Ren'Py 如何将您的项目转变为发行版文件。

init python:

    ## 以下函数接受文件模式。文件模式不区分大小写，并与基础目录的相对路径相匹
    ## 配，包括或不包括 /。如果多个模式匹配，则使用第一个模式。
    ##
    ## 在一个模式中：
    ##
    ## / 是目录分隔符。
    ##
    ## * 匹配所有字符，目录分隔符除外。
    ##
    ## ** 匹配所有字符，包括目录分隔符。
    ##
    ## 例如，“*.txt”匹配基础目录中的 txt 文件，“game/**.ogg”匹配游戏目录或任何子
    ## 目录中的 ogg 文件，“**.psd”匹配项目中任何位置的 psd 文件。

    ## 将文件列为 None 来使其从构建的发行版中排除。

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    # 排除py源文件
    build.classify('game/*.py', None)
    build.classify('game/scripts/**.py', None)

    # 排除rpy源文件
    build.classify('game/**.rpy', None)

    build.classify('tools/**', None)
    build.classify('game/action_editor/**', None)
    build.classify('docs/**', None)
    build.classify('README.md', None)
    build.classify('README_en.md', None)
    build.classify('README_jp.md', None)
    build.classify('LICENSE', None)
    build.classify('NOTICE', None)

    # 排除存档文件
    build.classify('game/saves/**.save', None)
    build.classify('game/cache/**', None)


    ## 若要封装文件，需将其列为“archive”。

    build.classify('game/images/**.png', 'archive')
    build.classify('game/images/**.jpg', 'archive')
    build.classify('game/images/**.svg', 'archive')
    build.classify('game/images/**.webp', 'archive')

    build.classify('game/gui/choices/**.png', 'archive')
    build.classify('game/gui/confirm/bg.png', 'archive')
    build.classify('game/gui/exhibit/**.png', 'archive')
    build.classify('game/gui/gallery/**.png', 'archive')
    build.classify('game/gui/main_menu/**.png', 'archive')
    build.classify('game/gui/shout/**.png', 'archive')
    build.classify('game/gui/show_exhibit/**.png', 'archive')
    build.classify('game/gui/time_indicator/**.png', 'archive')
    build.classify('game/gui/trial/**.png', 'archive')
    build.classify('game/gui/ctc.png', 'archive')
    build.classify('game/gui/namebox.png', 'archive')
    build.classify('game/gui/textbox.png', 'archive')
    build.classify('game/gui/textbox_ornament.png', 'archive')

    build.classify('game/**.webm', 'archive')
    build.classify('game/**.mp3', 'archive')
    build.classify('game/**.ogg', 'archive')
    build.classify('game/**.wav', 'archive')
    build.classify('game/**.otf', 'archive')
    build.classify('game/**.ttf', 'archive')


    ## 匹配为文档模式的文件会在 Mac 应用程序构建中被复制，因此它们同时出现在 APP
    ## 和 ZIP 文件中。

    build.documentation('*.html')

    ## 快捷键 ##########################################################################

    config.keymap = dict(

        # Bindings present almost everywhere, unless explicitly
        # disabled.
        rollback = [ 'any_K_PAGEUP', 'any_KP_PAGEUP', 'K_AC_BACK', 'mousedown_4' ],
        screenshot = [ ],
        toggle_afm = [ ],
        toggle_fullscreen = [ 'K_F11' ],
        game_menu = [ 'K_ESCAPE', 'K_MENU', 'K_PAUSE', 'mouseup_3' ],
        hide_windows = [ 'mouseup_2', 'noshift_K_h' ],
        launch_editor = [ 'shift_K_e' ],  # developer
        dump_styles = [ ],
        reload_game = [ 'alt_K_r', 'shift_K_r' ],  # developer
        inspector = [ 'alt_K_i', 'shift_K_i' ],  # developer
        full_inspector = [ 'alt_shift_K_i' ],  # developer
        developer = [ 'alt_K_d', 'shift_K_d', ],  # developer
        quit = [ ],
        iconify = [ ],
        help = [ ],
        choose_renderer = ['alt_K_g', 'shift_K_g' ],
        progress_screen = [ 'alt_shift_K_p', 'meta_shift_K_p', 'K_F2' ],  # developer
        accessibility = [ ],
        bubble_editor = [ 'alt_K_b', 'shift_K_b' ],  # developer

        # Accessibility.
        self_voicing = [ ],
        clipboard_voicing = [ ],
        debug_voicing = [ ],

        # Say.
        rollforward = [ 'any_K_PAGEDOWN', 'any_KP_PAGEDOWN', 'mousedown_5', ],
        dismiss = [ 'K_RETURN', 'K_SPACE', 'K_KP_ENTER', 'K_SELECT', 'mouseup_1' ],
        dismiss_unfocused = [ ],

        # Pause.
        dismiss_hard_pause = [ ],

        # Focus.
        focus_left = [ 'any_K_LEFT', 'any_KP_LEFT' ],
        focus_right = [ 'any_K_RIGHT', 'any_KP_RIGHT' ],
        focus_up = [ 'any_K_UP', 'any_KP_UP' ],
        focus_down = [ 'any_K_DOWN', 'any_KP_DOWN' ],

        # Button.
        button_ignore = [ 'mousedown_1' ],
        button_select = [ 'K_RETURN', 'K_KP_ENTER', 'K_SELECT', 'mouseup_1',  ],
        button_alternate = [ 'mouseup_3' ],
        button_alternate_ignore = [ 'mousedown_3' ],

        # Input.
        input_backspace = [ 'any_K_BACKSPACE' ],
        input_enter = [ 'K_RETURN', 'K_KP_ENTER' ],
        input_next_line = [ 'shift_K_RETURN', 'shift_K_KP_ENTER' ],
        input_left = [ 'any_K_LEFT', 'any_KP_LEFT' ],
        input_right = [ 'any_K_RIGHT', 'any_KP_RIGHT' ],
        input_up = [ 'any_K_UP', 'any_KP_UP' ],
        input_down = [ 'any_K_DOWN', 'any_KP_DOWN' ],
        input_delete = [ 'any_K_DELETE', 'any_KP_DELETE' ],
        input_home = [ 'K_HOME', 'KP_HOME', 'meta_K_LEFT' ],
        input_end = [ 'K_END', 'KP_END', 'meta_K_RIGHT' ],
        input_copy = [ 'ctrl_noshift_K_INSERT', 'ctrl_noshift_K_c', 'meta_noshift_K_c' ],
        input_paste = [ 'shift_K_INSERT', 'ctrl_noshift_K_v', 'meta_noshift_K_v' ],
        input_jump_word_left = [ 'osctrl_K_LEFT', 'osctrl_KP_LEFT' ],
        input_jump_word_right = [ 'osctrl_K_RIGHT', 'osctrl_KP_RIGHT' ],
        input_delete_word = [ 'osctrl_K_BACKSPACE' ],
        input_delete_full = [ 'meta_K_BACKSPACE' ],

        # Viewport.
        viewport_leftarrow = [ 'any_K_LEFT', 'any_KP_LEFT' ],
        viewport_rightarrow = [ 'any_K_RIGHT', 'any_KP_RIGHT' ],
        viewport_uparrow = [ 'any_K_UP', 'any_KP_UP' ],
        viewport_downarrow = [ 'any_K_DOWN', 'any_KP_DOWN' ],
        viewport_wheelup = [ 'mousedown_4' ],
        viewport_wheeldown = [ 'mousedown_5' ],
        viewport_drag_start = [ 'mousedown_1' ],
        viewport_drag_end = [ 'mouseup_1' ],
        viewport_pageup = [ 'any_K_PAGEUP', 'any_KP_PAGEUP'],
        viewport_pagedown = [ 'any_K_PAGEDOWN', 'any_KP_PAGEDOWN' ],

        # These keys control skipping.
        skip = [ 'K_LCTRL', 'K_RCTRL' ],
        stop_skipping = [ ],
        toggle_skip = [ ],
        fast_skip = [ ],

        # Bar.
        bar_activate = [ 'mousedown_1', 'K_RETURN', 'K_KP_ENTER', 'K_SELECT' ],
        bar_deactivate = [ 'mouseup_1', 'K_RETURN', 'K_KP_ENTER', 'K_SELECT' ],
        bar_left = [ 'any_K_LEFT', 'any_KP_LEFT' ],
        bar_right = [ 'any_K_RIGHT', 'any_KP_RIGHT' ],
        bar_up = [ 'any_K_UP', 'any_KP_UP' ],
        bar_down = [ 'any_K_DOWN', 'any_KP_DOWN' ],

        # Delete a save.
        save_delete = [ 'K_DELETE', 'KP_DELETE' ],

        # Draggable.
        drag_activate = [ 'mousedown_1' ],
        drag_deactivate = [ 'mouseup_1' ],

        # Debug console.
        console = [ 'shift_K_o', 'alt_shift_K_o' ],  # developer
        console_exit = [ 'K_ESCAPE', 'K_MENU', 'K_PAUSE', 'mouseup_3' ],  # developer
        console_older = [ 'any_K_UP', 'any_KP_UP' ],  # developer
        console_newer = [ 'any_K_DOWN', 'any_KP_DOWN' ],  # developer

        # Director
        director = [ 'noshift_K_d' ],  # developer

        # Ignored (kept for backwards compatibility).
        toggle_music = [ ],
        viewport_up = [ ],
        viewport_down = [ ],

        # Profile commands.
        performance = [ 'K_F3' ],  # developer
        image_load_log = [ 'K_F4' ],  # developer
        profile_once = [ 'K_F8' ],  # developer
        memory_profile = [ 'K_F7' ],  # developer
    )
