"""Home page"""

import math

import tkintertools as tkt
from tkintertools import tools_3d as t3d

import main
import theme


class Page(t3d.Space):
    """Home Page"""

    def __init__(self, app: "main.Application") -> None:
        super().__init__(app.root, 1600, 900, 0, 0)
        self.create_text(802, 182, text='五子棋', font=('华文行楷', 180), fill='grey')
        self.create_text(800, 180, text='五子棋', font=('华文行楷', 180), fill='gold')
        self.create_text(801, 281, text=f'Created with tkintertools {tkt.__version__}', font=(
            '华文行楷', 36), fill='grey')
        self.create_text(800, 280, text=f'Created with tkintertools {tkt.__version__}', font=(
            '华文行楷', 36), fill='orange')

        self.__info_shadow = self.create_text(
            1100 - 1, 120 + 1, text='泰酷辣!!', font='华文新魏', angle=-30, fill='grey')
        self.__info = self.create_text(
            1100, 120, text='泰酷辣!!', font='华文新魏', angle=-30, fill='red')

        tkt.Button(self, 550, 500, 500, 60, text='单 人 模 式', font=(tkt.FONT, 16),
                   command=lambda: (app.single_mode.place(
                       x=0, y=0), app.single_mode.lock(True), self.lock(False)),
                   **theme.Light.Button)
        tkt.Button(self, 550, 580, 500, 60, text='多 人 模 式', font=(tkt.FONT, 16),
                   command=lambda: (app.multiple_mode.place(
                       x=0, y=0), app.multiple_mode.lock(True), self.lock(False)),
                   **theme.Light.Button)
        tkt.Button(self, 550, 660, 240, 60, text='选 项', font=(tkt.FONT, 16),
                   command=lambda: (app.setting.place(
                       x=0, y=0), app.setting.lock(True), self.lock(False)),
                   **theme.Light.Button)
        tkt.Button(self, 810, 660, 240, 60, text='退 出', font=(tkt.FONT, 16),
                   command=app.root.quit, **theme.Light.Button)

        self.create_text(20, 880, text=f'Super Gobang v{main.__version__}', font=(
            tkt.FONT, 20), anchor='sw', fill='grey')
        self.create_text(1580, 880, text=f'Created by {main.__author__}', font=(
            tkt.FONT, 20), anchor='se', fill='grey')

        t3d.Cuboid(self, -450, -450, -180, 900, 900, 30,
                   color_outline_back='grey', color_outline_down='grey', color_outline_front='grey',
                   color_outline_left='grey', color_outline_right='grey', color_outline_up='grey')

        t3d.Side(self, [15 + 19 - 450, 15 + 19 - 450, -150], [15 + 19 - 450, 885 - 19 - 450, -150], [885 -
                 19 - 450, 885 - 19 - 450, -150], [885 - 19 - 450, 15 + 19 - 450, -150], width=4, outline='grey')

        t3d.Side(self, [-10, -10, -150], [-10, 10, -150], [10,
                 10, -150], [10, -10, -150], fill='grey', outline='grey')
        t3d.Side(self, [-230 - 10, -230 - 10, -150], [-230 - 10, -230 + 10, -150], [-230 +
                 10, -230 + 10, -150], [-230 + 10, -230 - 10, -150], fill='grey', outline='grey')
        t3d.Side(self, [-230 - 10, 230 - 10, -150], [-230 - 10, 230 + 10, -150], [-230 +
                 10, 230 + 10, -150], [-230 + 10, 230 - 10, -150], fill='grey', outline='grey')
        t3d.Side(self, [230 - 10, 230 - 10, -150], [230 - 10, 230 + 10, -150], [230 +
                 10, 230 + 10, -150], [230 + 10, 230 - 10, -150], fill='grey', outline='grey')
        t3d.Side(self, [230 - 10, -230 - 10, -150], [230 - 10, -230 + 10, -150], [230 +
                 10, -230 + 10, -150], [230 + 10, -230 - 10, -150], fill='grey', outline='grey')

        for i in range(15):
            x = y = 15 + 29 + 58 * i
            t3d.Text3D(self, [x - 450, 15 + 29 - 450 - 20, -
                              150 + 20], text=chr(i + 65), fill='#FF0000')
            t3d.Text3D(self, [15 + 29 - 450 - 20, y - 450, -150 + 20],
                       text=f'{i+1:02d}', fill='#00FF00')
            t3d.Line(self, [x - 450, 15 + 29 - 450, -150],
                     [x - 450, 885 - 29 - 450, -150], fill='grey')
            t3d.Line(self, [15 + 29 - 450, y - 450, -150],
                     [885 - 29 - 450, y - 450, -150], fill='grey')

        self.animation: tuple[tkt.Animation, tkt.Animation] = (
            tkt.Animation(self, 500, controller=(
                lambda t: 1-t**2, -1, 1), loop=True, callback=self._an_info, fps=45),
            tkt.Animation(self, 500, loop=True, callback=self._an_3d, fps=45))

        self.an_start()

    def an_start(self) -> None:
        """start animation of home"""
        for an in self.animation:
            an.run()

    def an_shutdown(self) -> None:
        """shutdown animation of home"""
        for an in self.animation:
            an.shutdown()

    def _an_info(self, p: float) -> None:
        """animation of info"""
        size = -round(p*30*math.sqrt(self.rx * self.ry))-30
        self.itemconfigure(self.__info_shadow, font=('华文新魏', size))
        self.itemconfigure(self.__info, font=('华文新魏', size))

    def _an_3d(self, _: float) -> None:
        """animation for 3D"""
        for side in self.items_3d():
            side.rotate(dx=0.01, axis=[[0, 0, 0], [0, 0, 1]])
            side.update()
        self.space_sort()
