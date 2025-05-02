# 开发者菜单
screen screen_developer():
    frame:
        align (1.0, 0.0)
        vbox:
            textbutton "调试菜单" text_size 38 text_color "#AAAAAA" text_font "font/SourceHanSansLite.ttf"
            textbutton "开启声音" text_size 40:
                action ToggleMute("music")
            textbutton "手动播放" text_size 40:
                action Preference("auto-forward", "toggle")
            hbox:
                textbutton "index" text_size 36 text_color "#555555"
                if "game" in globals():
                    textbutton "[game.index]" text_size 36 text_color "#555555"

        background Solid("#333333CC")
