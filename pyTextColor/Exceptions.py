"""
The Exceptions Code
"""


class FormatError(Exception):
    """
    Raised when the format of style/color/bg is invalid or wrong
    """
    pass


class ColorError(Exception):
    """
    Raised when a color is invalid or wrong
    """
    pass


class StyleError(Exception):
    """
    Raised when a style is invalid or wrong
    """
