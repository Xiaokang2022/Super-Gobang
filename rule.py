"""游戏规则文件"""

import abc
import typing

import data
import dll
import file


class Law(abc.ABC):
    """抽象规则类"""

    wait_mode: bool | None = None  # 等待模式（联网，人机）
    regret_mode: bool | None = None  # 悔棋模式
    chat_mode: bool | None = None  # 聊天模式

    @classmethod
    @abc.abstractmethod
    def start(cls) -> None:
        """初始操作"""

    @classmethod
    @abc.abstractmethod
    def step(cls, x: int, y: int) -> int | None:
        """每步操作"""

    @classmethod
    @abc.abstractmethod
    def end(cls) -> None:
        """终止操作"""

    @classmethod
    @abc.abstractmethod
    def wait(cls) -> None:
        """等待操作"""


class DuoModeLaw(Law):
    """双人模式规则"""

    wait_mode: bool = False
    regret_mode: bool = False
    chat_mode: bool = False

    @typing.override
    @classmethod
    def start(cls) -> None:
        data.reset()
        data.player = True  # 我方

    @typing.override
    @classmethod
    def step(cls, x: int, y: int) -> int | None:
        data.add_step(x, y, data.player)
        data.player = False if data.player is True else True
        data.index += 1
        return dll.combo(data.lst, x, y)

    @typing.override
    @classmethod
    def end(cls) -> None:
        data.player = None  # 不再允许棋盘改动

    @typing.override
    @classmethod
    def wait(cls) -> None:
        pass


class ManualModeLaw(Law):
    """棋谱模式规则"""

    wait_mode: bool = False
    regret_mode: bool = True
    chat_mode: bool = False

    @typing.override
    @classmethod
    def start(cls) -> None:
        data.reset()
        data.steps = file.loadfile()

    @typing.override
    @classmethod
    def step(cls, x: int, y: int) -> int | None:
        data.player = None
        return dll.combo(data.lst, x, y)

    @typing.override
    @classmethod
    def end(cls) -> None:
        pass

    @typing.override
    @classmethod
    def wait(cls) -> None:
        pass


class AIModeLaw(Law):
    """人机模式规则"""

    wait_mode: bool = True
    regret_mode: bool = True
    chat_mode: bool = False

    @typing.override
    @classmethod
    def start(cls) -> None:
        data.reset()
        data.player = True  # 我方

    @typing.override
    @classmethod
    def step(cls, x: int, y: int) -> int | None:
        data.add_step(x, y, data.player)
        data.player = False if data.player is True else True
        data.index += 1
        return dll.combo(data.lst, x, y)

    @typing.override
    @classmethod
    def end(cls) -> None:
        data.player = None  # 不再允许棋盘改动

    @typing.override
    @classmethod
    def wait(cls, x: int, y: int, callback: typing.Callable[[int, int], typing.Any]) -> None:
        ax, ay = dll.compute(data.lst, x, y)
        callback(ax, ay)
