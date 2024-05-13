"""棋盘数据"""

player: bool | None = None  # 当前方（True 为我方）
lst: list[list[bool | None]] = [[None] * 15 for _ in range(15)]  # 棋盘二维列表
steps: list[tuple[int, int, bool]] = []  # 步骤记录列表（x，y，下子方）
items: list[int] = []  # 棋子列表
index: int = 0  # 步骤记录索引


def reset() -> None:
    """清空数据"""
    global player, lst, index
    player = None
    lst = [[None] * 15 for _ in range(15)]
    steps.clear()
    items.clear()
    index = 0


def set_value(x: int, y: int, value: bool) -> None:
    """设置值"""
    lst[x][y] = value


def get_value(x: int, y: int) -> bool | None:
    """获取值"""
    return lst[x][y]


def add_step(x: int, y: int, player_: bool) -> None:
    """添加步骤"""
    steps.append((x, y, player_))


def is_undo() -> bool:
    """能否撤销"""
    if index == 0:
        return False
    return True


def is_redo() -> bool:
    """能否重做"""
    if index >= len(steps):
        return False
    return True
