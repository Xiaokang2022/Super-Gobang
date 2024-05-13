"""Board Page"""

import threading
import tkinter
from tkinter import messagebox

import tkintertools as tkt

import configure
import data
import file
import main
import rule
import theme
import tool


class Page(tkt.Canvas):
    """"""

    law: rule.Law | None = None

    def __init__(self, app: "main.Application") -> None:
        super().__init__(app.root, 1600, 900, lock=True)
        self.create_rectangle(15 + 19, 15 + 19, 885 - 19,
                              885 - 19, width=4, fill='#DDD')
        self.create_text(450, 450, text='五子棋', fill='#CCC', font=('华文行楷', 150))

        for i in range(15):
            x = y = 15 + 29 + 58 * i
            self.create_text(x + 1, 880 + 1, text=chr(i + 65), fill='grey')
            self.create_text(x, 880, text=chr(i + 65), fill='#FF0000')
            self.create_text(20 + 1, y + 1, text=f'{15-i:02d}', fill='grey')
            self.create_text(20, y, text=f'{15-i:02d}', fill='#00FF00')
            self.create_line(x, 15 + 29, x, 885 - 29)
            self.create_line(15 + 29, y, 885 - 29, y)

        p = [15 + 29 + i * 58 for i in (3, 7, 11)]
        self.create_oval(p[1] - 5, p[1] - 5, p[1] + 5, p[1] + 5, fill='black')
        self.create_oval(p[0] - 5, p[0] - 5, p[0] + 5, p[0] + 5, fill='black')
        self.create_oval(p[0] - 5, p[2] - 5, p[0] + 5, p[2] + 5, fill='black')
        self.create_oval(p[2] - 5, p[0] - 5, p[2] + 5, p[0] + 5, fill='black')
        self.create_oval(p[2] - 5, p[2] - 5, p[2] + 5, p[2] + 5, fill='black')

        self.server = tkt.Label(self, 900, 15 + 19, 250, 300)
        tkt.Label(self, 900 + 10, 15 + 19 + 10, 230, 230, text='对方\n头像')
        self.server_pb = tkt.ProgressBar(
            self, 900 + 10, 15 + 19 + 260 - 5, 230, 30, mode='indeterminate')
        self.server_name = self.create_text(
            900 + 10 + 115, 260, text='AI', fill='grey')

        self.client = tkt.Label(self, 900, 15 + 19 + 300 + 20, 250, 300)
        tkt.Label(self, 900 + 10, 15 + 19 + 10 +
                  300 + 20, 230, 230, text='我方\n头像')
        self.client_pb = tkt.ProgressBar(
            self, 900 + 10, 15 + 19 + 260 + 300 + 20 - 5, 230, 30, mode='indeterminate')
        self.client_name = self.create_text(
            900 + 10 + 115, 260 + 320, text='Test', fill='grey')

        self.btn_undo = tkt.Button(self, 900, 15 + 19 + 300 + 20 + 300 + 20,
                                   250, 57, text='悔棋 / 回退', command=self.undo)
        self.btn_redo = tkt.Button(self, 900, 15 + 19 + 300 + 20 + 300 + 20 +
                                   67, 250, 57, text='撤销 / 前进', command=self.redo)
        tkt.Button(self, 900, 15 + 19 + 300 + 20 + 300 + 20 + 67 +
                   67, 250, 57, text='退出本局', command=self.quit_mode)

        self.record = tkt.Text(self, 1150 + 20, 15 + 19, 1600 -
                               15 - 19 - 1150 - 20, 500, read=True, font=('楷体', tkt.SIZE))
        self.chat_text = tkt.Text(self, 900 + 20 + 250, 15 + 19 + 500 + 20,
                                  1600 - 15 - 19 - 1150 - 20, 254, read=True, font=('楷体', tkt.SIZE))
        self.chat_entry = tkt.Entry(self, 900 + 20 + 250, 900 - 40 - 15 -
                                    19, 344, 40, text=('聊天栏', '点击以输入内容'), font=('楷体', tkt.SIZE))
        tkt.Button(self, 1600 - 15 - 19 - 40, 900 - 15 - 19 -
                   40, 40, 40, text='↑', command=self.chat_send)

        cx, cy = -2 * 58 + 29 + 15, -2 * 58 + 29 + 15
        self.mouse_cursor_red = [  # 对方上次位置（红色）
            self.create_line([(cx - 30, cy - 5), (cx - 30, cy - 30),
                             (cx - 5, cy - 30)], fill='#FF0000', width=3),
            self.create_line([(cx + 5, cy - 30), (cx + 30, cy - 30),
                             (cx + 30, cy - 5)], fill='#FF0000', width=3),
            self.create_line([(cx - 30, cy + 5), (cx - 30, cy + 30),
                             (cx - 5, cy + 30)], fill='#FF0000', width=3),
            self.create_line([(cx + 5, cy + 30), (cx + 30, cy + 30),
                             (cx + 30, cy + 5)], fill='#FF0000', width=3),
        ]
        self.mouse_cursor_green = [  # 我方上次位置（绿色）
            self.create_line([(cx - 30, cy - 5), (cx - 30, cy - 30),
                             (cx - 5, cy - 30)], fill='#00FF00', width=3),
            self.create_line([(cx + 5, cy - 30), (cx + 30, cy - 30),
                             (cx + 30, cy - 5)], fill='#00FF00', width=3),
            self.create_line([(cx - 30, cy + 5), (cx - 30, cy + 30),
                             (cx - 5, cy + 30)], fill='#00FF00', width=3),
            self.create_line([(cx + 5, cy + 30), (cx + 30, cy + 30),
                             (cx + 30, cy + 5)], fill='#00FF00', width=3),
        ]
        cx, cy = 7 * 58 + 29 + 15, 7 * 58 + 29 + 15
        self.mouse_cursor_blue = [  # 当前鼠标位置（蓝色）
            self.create_line([(cx - 30, cy - 5), (cx - 30, cy - 30),
                             (cx - 5, cy - 30)], fill='#0000FF', width=3),
            self.create_line([(cx + 5, cy - 30), (cx + 30, cy - 30),
                             (cx + 30, cy - 5)], fill='#0000FF', width=3),
            self.create_line([(cx - 30, cy + 5), (cx - 30, cy + 30),
                             (cx - 5, cy + 30)], fill='#0000FF', width=3),
            self.create_line([(cx + 5, cy + 30), (cx + 30, cy + 30),
                             (cx + 30, cy + 5)], fill='#0000FF', width=3),
        ]

        self.bind('<Motion>',
                  lambda event: (self.hightlight_blue(event), self._touch(event)))
        self.bind('<B1-Motion>',
                  lambda event: (self.hightlight_blue(event), self._click(event)))
        self.bind('<ButtonRelease-1>',
                  lambda event: (self.click(event), self._release(event)))
        self.bind('<Control-s>', lambda _: file.dumpfile(data.steps))

    def hightlight_red(self, x: int, y: int, pos: list[int] = [-2 * 58 + 29 + 15, -2 * 58 + 29 + 15]) -> None:
        """红标高亮"""
        cx, cy = x * 58 + 29 + 15, y * 58 + 29 + 15
        for i in range(4):
            self.move(self.mouse_cursor_red[i], cx - pos[0], cy - pos[1])
        pos[:] = [cx, cy]

    def hightlight_green(self, x: int, y: int, pos: list[int] = [-2 * 58 + 29 + 15, -2 * 58 + 29 + 15]) -> None:
        """绿标高亮"""
        cx, cy = x * 58 + 29 + 15, y * 58 + 29 + 15
        for i in range(4):
            self.move(self.mouse_cursor_green[i], cx - pos[0], cy - pos[1])
        pos[:] = [cx, cy]

    def hightlight_blue(self, event: tkinter.Event, pos: list[int] = [7 * 58 + 29 + 15, 7 * 58 + 29 + 15]) -> None:
        """黄标高亮"""
        cx = ((event.x - 15) // 58) * 58 + 29 + 15
        cy = ((event.y - 15) // 58) * 58 + 29 + 15
        if not (29 + 15 <= cx <= 900 - 29 - 15 and 29 + 15 <= cy <= 900 - 29 - 15):
            return
        if cx == pos[0] and cy == pos[1]:
            return
        for i in range(4):
            self.move(self.mouse_cursor_blue[i], cx - pos[0], cy - pos[1])
        pos[:] = [cx, cy]

    def mouse_cursor_flash(self, x: int, y: int, _item: int | None = None, _count: int = 0) -> None:
        """色标闪烁"""
        cx, cy = x * 58 + 29 + 15, y * 58 + 29 + 15
        if _count & 1:
            self.delete(_item)
        else:
            r = 36
            _item = self.create_polygon(
                (cx, cy-r), (cx+r, cy), (cx, cy+r), (cx-r, cy), outline='yellow', fill='', width=3)
        if _count < 5:
            self.after(200, self.mouse_cursor_flash, x, y, _item, _count + 1)

    def reset(self) -> None:
        """棋盘重置"""
        Page.law = None
        self.hightlight_red(-2, -2)
        self.hightlight_green(-2, -2)
        self.delete('piece')
        self.record.clear()
        self.chat_entry.clear()
        self.chat_entry.set_live(True)
        self.chat_text.clear()
        self.chat_text.set_live(True)
        self.btn_undo.set_live(True)
        self.btn_redo.set_live(True)
        self.client_pb.load(0)
        self.server_pb.load(0)

    def chat_send(self) -> None:
        """发送聊天信息"""
        chat_data = self.chat_entry.get()
        if chat_data:
            self.chat_entry.set('')
            self.chat_text.append(f'[{tool.gettime()}][我]{chat_data}\n')

    def play(self, mode: str) -> None:
        """开始游戏"""
        match mode:
            case '双人对弈':
                Page.law = rule.DuoModeLaw
            case '棋谱复盘':
                Page.law = rule.ManualModeLaw
            case _:
                messagebox.showinfo('Super Gobang', '此模式仍在开发中！')
                return
        self.master.title(f'Super Gobang - {mode}')
        self.place(x=0, y=0)
        self.lock(True)
        if not Page.law.chat_mode:
            self.chat_entry.set_live(False)
            self.chat_text.set_live(False)
        if not Page.law.regret_mode:
            self.btn_undo.set_live(False)
            self.btn_redo.set_live(False)
        self.law.start()

    def quit_mode(self) -> None:
        """退出游戏"""
        if messagebox.askyesno('Super Gobang', '确认退出本局？'):
            self.lock(False)
            self.place_forget()
            self.master.title('Super Gobang')
            self.reset()

    def click(self, event, _sys: bool = False) -> None:
        """下棋"""
        if data.player is None and not _sys:
            return
        if not data.player and self.law.wait_mode and not _sys:
            return
        x = (event.x - 15) // 58
        y = (event.y - 15) // 58
        if not (0 <= x <= 14 and 0 <= y <= 14) or data.get_value(x, y) is not None:
            return
        self.create_piece(x, y, data.player)
        if (combo := self.law.step(x, y)) == 5:
            self.win(data.steps[-1][-1])
            self.law.end()
        elif (configure.config['HintWhenFourCombo'] and combo == 4) or (configure.config['HintWhenThreeCombo'] and combo == 3):
            self.mouse_cursor_flash(x, y)
            self.bell()
        if not data.player and self.law.wait_mode:
            threading.Thread(
                target=self.law.wait, daemon=True, args=(x, y, self.click_by_sys)).start()

    def win(self, player: bool) -> None:
        """胜利播报"""
        winner = '黑' if player else '白'
        messagebox.showinfo('Super Gobang', f'{winner}方获胜！')

    def create_piece(self, x: int, y: int, player: bool) -> None:
        """落子"""
        cx = x*58 + 44
        cy = y*58 + 44
        fill = 'black' if player else 'white'
        piece = self.create_oval(
            cx - 25, cy - 25, cx + 25, cy + 25, outline='grey', fill=fill, tag='piece')
        data.set_value(x, y, player)
        data.items.append(piece)
        self.record.append(
            f'[{tool.gettime()}][{'黑' if player else '白'}] {chr(x + 65)} {f'{15-y:02d}'}\n')
        if player:
            self.hightlight_green(x, y)
        else:
            self.hightlight_red(x, y)

    def delete_piece(self, index: int) -> None:
        """收子"""
        self.delete(data.items.pop(index))

    def click_by_sys(self, x: int, y: int) -> None:
        """系统点击"""
        event = tkinter.Event()
        event.x = x*58 + 44
        event.y = y*58 + 44
        self.click(event, True)

    def redo(self) -> None:
        """撤销悔棋"""
        if not data.is_redo():
            messagebox.showinfo('Super Gobang', '当前无法进行【撤销/前进】操作！')
            return
        x, y, data.player = data.steps[data.index]
        self.click_by_sys(x, y)
        data.index += 1

    def undo(self) -> None:
        """悔棋"""
        if not data.is_undo():
            messagebox.showinfo('Super Gobang', '当前无法进行【悔棋/回退】操作！')
            return
        data.index -= 1
        self.delete_piece(data.index)
        record_text = '\n'.join(self.record.value.split('\n')[:-2]) + '\n'
        self.record.set(record_text)
