"""配置文件的操作"""

import json
import typing

CONFIG_PATH = './config.json'


class ConfigDict(typing.TypedDict):
    """配置字典"""
    HintWhenThreeCombo: bool
    HintWhenFourCombo: bool
    HintForPostion: bool
    Language: bool
    Theme: bool
    FullScreen: bool
    Voice: bool
    AISearchDepth: int
    Address: str


DEFAULT_CONFIG: ConfigDict = {
    "HintWhenThreeCombo": True,
    "HintWhenFourCombo": True,
    "HintForPostion": True,
    "Language": True,
    "Theme": False,
    "FullScreen": False,
    "Voice": True,
    "AISearchDepth": 3,
    "Address": "127.0.0.1"
}


def _load() -> ConfigDict:
    """加载配置"""
    with open(CONFIG_PATH, encoding='utf-8') as file:
        return json.load(file)


def modify(**kw: typing.Unpack[ConfigDict]) -> None:
    """修改配置"""
    for key, value in kw.items():
        config[key] = value
    with open(CONFIG_PATH, 'w', encoding='utf-8') as file:
        json.dump(config, file, indent=4)


def reset() -> None:
    """重置配置"""
    modify(**DEFAULT_CONFIG)


config: ConfigDict = _load()
