"""Setting Page"""

from tkinter import messagebox

import tkintertools as tkt

import configure
import main
import theme


class Page(tkt.Canvas):
    """Setting Page"""

    def __init__(self, app: "main.Application") -> None:
        super().__init__(app.root, 1600, 900, lock=True)
        self.app = app
        self.create_text(
            20, 20, text='选项设置', anchor='nw', font=(tkt.FONT, 40), fill='grey')
        self.create_text(20, 880, text='部分选项重启后生效', anchor='sw', fill='grey')

        tkt.Button(self, 1380, 20, 200, 50, text='重置', command=self.reset)
        tkt.Button(self, 1380, 830, 200, 50, text='确定',
                   command=lambda: (self.lock(False), app.home.lock(True), self.place_forget()))

        tkt.Label(self, 20, 100, 1560, 50, text='三连危险提示', justify='left',
                  color_outline=('', '#AAA'), color_fill=('', '#DDD'),
                  tooltip=tkt.ToolTip('当对方多个棋子相连达\n到 3 个时给出高亮提示'))
        tkt.Switch(self, 1510, 100 + 10, 30,
                   default=configure.config['HintWhenThreeCombo'],
                   on=lambda: configure.modify(HintWhenThreeCombo=True),
                   off=lambda: configure.modify(HintWhenThreeCombo=False))

        tkt.Label(self, 20, 150, 1560, 50, text='四连危险提示', justify='left',
                  color_outline=('', '#AAA'), color_fill=('', '#DDD'),
                  tooltip=tkt.ToolTip('当对方多个棋子相连达\n到 4 个时给出高亮提示'))
        tkt.Switch(self, 1510, 150 + 10, 30,
                   default=configure.config['HintWhenFourCombo'],
                   on=lambda: configure.modify(HintWhenFourCombo=True),
                   off=lambda: configure.modify(HintWhenFourCombo=False))

        tkt.Label(self, 20, 200, 1560, 50, text='中文 / 英文', justify='left',
                  color_outline=('', '#AAA'), color_fill=('', '#DDD'),
                  tooltip=tkt.ToolTip('切换 UI 显示的语言'))
        tkt.Switch(self, 1510, 200 + 10, 30,
                   default=configure.config['Language'],
                   on=lambda: configure.modify(Language=True),
                   off=lambda: configure.modify(Language=False))

        tkt.Label(self, 20, 250, 1560, 50, text='明亮 / 黑暗（实验性功能）', justify='left', color_outline=(
            '', '#AAA'), color_fill=('', '#DDD'), tooltip=tkt.ToolTip('切换 UI 的颜色主题'))
        tkt.Switch(self, 1510, 250 + 10, 30,
                   default=configure.config['Theme'], on=self.change_theme, off=self.change_theme)

        tkt.Label(self, 20, 300, 1560, 50, text='窗口化 / 全屏（实验性功能）', justify='left', color_outline=(
            '', '#AAA'), color_fill=('', '#DDD'), tooltip=tkt.ToolTip('切换窗口的显示方式'))
        tkt.Switch(self, 1510, 300 + 10, 30,
                   default=configure.config['FullScreen'],
                   )

        tkt.Label(self, 20, 350, 1560, 50, text='声音', justify='left', color_outline=(
            '', '#AAA'), color_fill=('', '#DDD'), tooltip=tkt.ToolTip('切换声音的开启和关闭'))
        tkt.Switch(self, 1510, 350 + 10, 30,
                   default=configure.config['Voice'],
                   on=lambda: configure.modify(Voice=True),
                   off=lambda: configure.modify(Voice=False))

        tkt.Label(self, 20, 400, 1560, 50, text='位置提示', justify='left', color_outline=(
            '', '#AAA'), color_fill=('', '#DDD'), tooltip=tkt.ToolTip('当鼠标移动到棋盘上时\n对应位置会出现高亮方框'))
        tkt.Switch(self, 1510, 400 + 10, 30,
                   default=configure.config['HintForPostion'],
                   on=lambda: configure.modify(HintForPostion=True),
                   off=lambda: configure.modify(HintForPostion=False))

        tkt.Label(self, 20, 450, 1560, 50, text='AI 搜索深度', justify='left', color_outline=(
            '', '#AAA'), color_fill=('', '#DDD'), tooltip=tkt.ToolTip('依据电脑算力自行选择\n数字越大，计算时间越长'))
        tkt.Entry(self, 1300, 450 + 5, 265 + 5, 40
                  ).set(str(configure.config['AISearchDepth']))
        tkt.Button(self, 1545, 450 + 6, 20, 17, text='▲',
                   font=(tkt.FONT, 10), color_outline=tkt.COLOR_NONE, color_fill=tkt.COLOR_NONE)
        tkt.Button(self, 1545, 450 + 2 + 23, 20, 17,
                   text='▼', font=(tkt.FONT, 10), color_outline=tkt.COLOR_NONE, color_fill=tkt.COLOR_NONE)

        tkt.Label(self, 20, 500, 1560, 50, text='服务器地址', justify='left', color_outline=(
            '', '#AAA'), color_fill=('', '#DDD'), tooltip=tkt.ToolTip('没事儿别动它就行，调试专用'))
        tkt.Entry(self, 1300, 500 + 5, 270,
                  40).set(configure.config['Address'])

    def change_theme(self) -> None:
        """change the theme of App"""
        color = theme.Light if configure.config['Theme'] else theme.Dark
        configure.modify(Theme=not configure.config['Theme'])
        for canvas in self.master.canvas():
            canvas.configure(**color.Canvas)
            for widget in canvas.widget():
                match widget.__class__:
                    case tkt.Label: widget.configure(**color.Label)
                    case tkt.Button: widget.configure(**color.Button)
                    case tkt.Entry: widget.configure(**color.Entry)
                    case tkt.Text: widget.configure(**color.Text)
                    case tkt.Switch:
                        widget.configure(**color.Switch)
                        widget._slider.state()
                widget.state()

    def reset(self) -> None:
        """重置设置"""
        if not messagebox.askyesno('Super Gobang', '你确定要重置所有设置选项？'):
            return
        configure.reset()
        messagebox.showinfo('Super Gobang', '已重置所有设置选项！')
