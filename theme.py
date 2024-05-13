"""Theme file"""

from tkintertools import constants


class Light:
    """Light Theme"""

    Canvas = {
        "bg": "#F1F1F1"
    }

    Label = {
        "color_fill": ('', '#DDD'),
        "color_outline": ('', '#AAA'),
        "color_text": ('#333', '#333'),
    }

    Button = {
        "color_fill": constants.COLOR_FILL_BUTTON,
        "color_outline": constants.COLOR_OUTLINE_BUTTON,
        "color_text": constants.COLOR_TEXT,
    }

    Entry = {
        "color_fill": constants.COLOR_FILL_ENTRY,
        "color_outline": constants.COLOR_OUTLINE_ENTRY,
        "color_text": constants.COLOR_TEXT,
    }

    Text = {
        "color_fill": constants.COLOR_FILL_TEXT,
        "color_outline": constants.COLOR_OUTLINE_TEXT,
        "color_text": constants.COLOR_TEXT,
    }

    Switch = {
        "color_fill_on": constants.COLOR_FILL_ON,
        "color_fill_off": constants.COLOR_FILL_OFF,
        "color_outline_on": constants.COLOR_OUTLINE_ON,
        "color_outline_off": constants.COLOR_OUTLINE_OFF,
        "color_fill_slider": constants.COLOR_FILL_SLIDER,
        "color_outline_slider": constants.COLOR_OUTLINE_SLIDER,
    }


class Dark:
    """Dark Theme"""

    Canvas = {
        "bg": "#1F1F1F"
    }

    Label = {
        "color_fill": ('', '#333'),
        "color_outline": ('', '#666'),
        "color_text": ('#CCC', '#CCC'),
    }

    Button = {
        "color_fill": ('#333333', '#555555', '#777777'),
        "color_outline": ('#999999', '#CCCCCC', '#FFFFFF'),
        "color_text": ('#999999', '#CCCCCC', '#FFFFFF'),
    }

    Entry = {
        "color_fill": ('#111', '#111', '#111'),
        "color_outline": ('#666', '#999', 'orange'),
        "color_text": ('#CCC', '#CCC', '#CCC'),
    }

    Text = {
        "color_fill": constants.COLOR_FILL_TEXT,
        "color_outline": constants.COLOR_OUTLINE_TEXT,
        "color_text": constants.COLOR_TEXT,
    }

    Switch = {
        "color_fill_on": constants.COLOR_FILL_ON,
        "color_fill_off": constants.COLOR_FILL_OFF,
        "color_outline_on": constants.COLOR_OUTLINE_ON,
        "color_outline_off": constants.COLOR_OUTLINE_OFF,
        "color_fill_slider": constants.COLOR_FILL_SLIDER,
        "color_outline_slider": constants.COLOR_OUTLINE_SLIDER,
    }
