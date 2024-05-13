"""一些工具"""

import time


def echo(lst: list[list[bool | None]]) -> None:
    """打印二维棋局列表"""
    for line in lst:
        print(*line)


def gettime() -> str:
    """按一定格式获取当前时间"""
    return time.strftime('%H:%M:%S', time.localtime())
