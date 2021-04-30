from enum import IntEnum

class AnchorPoints(IntEnum):
    TOPLEFT = 1
    TOPRIGHT = 2
    BOTTOMRIGHT = 3
    BOTTOMLEFT = 4
    CENTER = 5

class ToggleStates(IntEnum):
    ON = 1
    OFF = 2

class Depths(IntEnum):
    BACKGROUND = 0
    MIDDLEGROUND = 1
    FOREGROUND = 2