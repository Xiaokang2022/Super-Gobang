"""Mode choose Page"""

import math

import tkintertools as tkt

import main
import theme


class Page(tkt.Canvas):
    """"""

    def __init__(self, app: "main.Application", title: str, mode_list: list[str]) -> None:
        """初始化"""
        super().__init__(app.root, 1600, 900, lock=True)
        self.create_text(20, 20, text=title, anchor='nw',
                         font=(tkt.FONT, 40), fill='grey')
        tkt.Button(self, 1380, 20, 200, 50, text='返回', command=lambda: (
            self.lock(False), app.home.lock(True), self.place_forget()))

        self.info = self.create_text(
            800, 800, text='—— 请选择你的游戏模式 ——', fill='grey')

        self.modes = [tkt.Button(self, 260 + i*380, 250, 320, 400, radius=10, text=mode_list[i], font=(
            tkt.FONT, 16), command=lambda i=i: app.board.play(mode_list[i])) for i in range(3)]
        self._animation()

    def _animation(self) -> None:
        """动画"""
        for btn in self.modes:
            btn.command_ex['normal'] = lambda btn=btn: (
                self.itemconfigure(self.info, text='—— 请选择你的游戏模式 ——'),
                tkt.Animation(btn, 250,  controller=(
                    math.sin, 0, math.pi/2), translation=(0, 75*self.ry)).run()
            )
            btn.command_ex['touch'] = lambda btn=btn: (
                self.itemconfigure(self.info, text=f'—— {btn.value} ——'),
                tkt.Animation(btn, 250,  controller=(
                    math.sin, 0, math.pi/2), translation=(0, -75*self.ry)).run()
            )
            btn.command_ex['click'] = tkt.Animation(btn, 250,  controller=(
                math.sin, 0, math.pi/2), translation=(0, 75*self.ry)).run
