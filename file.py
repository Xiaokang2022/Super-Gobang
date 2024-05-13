"""棋谱文件的操作"""

import pickle
from tkinter import filedialog


def loadfile() -> list[tuple[int, int, bool]]:
    """读取文件"""
    if file := filedialog.askopenfile(
            'rb', filetypes=[('棋谱文件', ['.gobang'])], title='Super Gobang - 打开棋谱文件', initialdir='./manuals', defaultextension='.gobang'):
        return pickle.load(file)
    return []


def dumpfile(steps: list[tuple[int, int, bool]]) -> None:
    """保存文件"""
    if file := filedialog.asksaveasfile(
            'wb', filetypes=[('棋谱文件', ['.gobang'])], title='Super Gobang - 保存棋谱文件', initialdir='./manuals', defaultextension='.gobang'):
        return pickle.dump(steps, file)
    return None
