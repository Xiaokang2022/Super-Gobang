"""C/C++ 编译 DLL 文件的调用"""

import ctypes

_PyDLL = ctypes.WinDLL('./PyDLL.dll')
"""DLL文件"""


def _lst_to_array(lst: list[list[bool | None]]) -> ctypes.Array[ctypes.Array[ctypes.c_int]]:
    """Python 二维棋局列表转换为 C 二维数组"""
    arr = (ctypes.c_int * 15 * 15)()
    for i, line in enumerate(lst):
        for j, value in enumerate(line):
            arr[i][j] = 1 if value is True else -1 if value is False else 0
    return arr


def combo(lst: list[list[bool | None]], x: int, y: int) -> int:
    """DLL API: 计算与最后落子同颜色的连续棋子个数"""
    arr = _lst_to_array(lst)
    return _PyDLL.combo(arr, x, y)


def compute(lst: list[list[bool | None]], x: int, y: int) -> tuple[int, int]:
    """AI 计算结果"""
    arr = _lst_to_array(lst)
    return _PyDLL.compute(arr, x, y)
