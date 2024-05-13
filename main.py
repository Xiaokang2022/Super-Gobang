"""Entry Point"""

import tkintertools as tkt

from views import board, config, home, mode

__version__ = '2.0'
__author__ = 'Xiaokang2022'


class Application:
    """app"""

    def __init__(self) -> None:
        self.root = tkt.Tk('Super Gobang', 1600, 900)
        self.root.resizable(False, False)
        self.home = home.Page(self)
        self.setting = config.Page(self)
        self.single_mode = mode.Page(self, '单人模式', ['棋谱复盘', '人机对战', '电脑对抗'])
        self.multiple_mode = mode.Page(self, '多人模式', ['局域网联机', '双人对弈', '联网对抗'])
        self.board = board.Page(self)
        self.root.mainloop()


if __name__ == '__main__':
    Application()
