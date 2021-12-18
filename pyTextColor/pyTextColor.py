"""
pyTextColor File
"""
from pyTextColor import ANSI
from pyTextColor import Exceptions

ANSI = ANSI.data

_START = "\033["
_END = "\033[0m"

COLORS = ANSI['color']
BGCOLORS = ANSI['bgcolor']
STYLE = ANSI['style']


class pyTextColor:
    def __init__(self):
        self._pc = None  # Previous Color
        self._bc = None  # Previous Background Color

    def format_text(self, text, color="white", bgcolor="black", text_style="normal", bg_full_line=False):
        txt = ""
        color = color.strip().lower()
        bgcolor = bgcolor.strip().lower()
        try:
            if color.startswith("#") or bgcolor.startswith("#"):
                if color.startswith("#") and not bgcolor.startswith("#"):
                    tR, tG, tB = self._hex_to_rgb(color)
                    txt = f"{_START}{STYLE[text_style]};{BGCOLORS[bgcolor]}m{_START}38;2;{tR};{tG};{tB}m{text}"
                if bgcolor.startswith("#") and not color.startswith("#"):
                    fR, fG, fB = self._hex_to_rgb(bgcolor)
                    txt = f"{_START}{STYLE[text_style]};{COLORS[color]}m{_START}48;2;{fR};{fG};{fB}m{text}"
                if color.startswith("#") and bgcolor.startswith("#"):
                    tR, tG, tB = self._hex_to_rgb(color)
                    fR, fG, fB = self._hex_to_rgb(bgcolor)
                    txt = f"{_START}{STYLE[text_style]}m{_START}48;2;{fR};{fG};{fB}m{_START}38;2;{tR};{tG};{tB}m{text}"
            else:
                txt = f"{_START}{STYLE[text_style]};{COLORS[color]};{BGCOLORS[bgcolor]}m{text}"
            if not bg_full_line:
                txt += _END
        except KeyError:
            raise Exceptions.FormatError("The color/bgcolor/style values may be invalid! See the docs for help")
        return txt

    def color(self, color="white"):
        txt = ""
        color = color.strip().lower()
        try:
            if color.startswith("#"):
                tR, tG, tB = self._hex_to_rgb(color)
                txt = f"{_START}38;2;{tR};{tG};{tB}m"
            else:
                txt = f"{_START}{COLORS[color]}m"
            self._pc = color
        except KeyError:
            raise Exceptions.ColorError(f"Cannot find '{color}' in the colors list! Use HEX value instead")
        return txt

    def background(self, color="black"):
        txt = ""
        color = color.strip().lower()
        try:
            if color.startswith("#"):
                tR, tG, tB = self._hex_to_rgb(color)
                txt = f"{_START}48;2;{tR};{tG};{tB}m"
            else:
                txt = f"{_START}{BGCOLORS[color]}m"
            self._bc = color
        except KeyError:
            raise Exceptions.ColorError(f"Cannot find '{color}' in the colors list! Use HEX value instead")
        return txt

    def style(self, text_style="normal"):
        txt = ""
        try:
            if text_style == "normal":
                txt = f"{_START}{STYLE[text_style]}m{self.background(self._bc)}{self.color(self._pc)}"
            else:
                txt = f"{_START}{STYLE[text_style]}m"
        except KeyError:
            raise Exceptions.StyleError(f"Cannot find style '{text_style}' in the styles list")
        return txt

    def reset(self):
        return _END

    def pretty_print_help(self):
        color = self.color
        style = self.style
        bg = self.background
        reset = self.reset

        intro = "Simple Python Library to display text with color in Python Terminal!"
        docs = "https://github.com/Sid72020123/pyTextColor"

        main_text = f"""{reset()}\n{bg()}Welcome to {style("bold")}{color("yellow")}pyTextColor{reset()}{bg()} {style("italic")}{color("cyan")}Python Library{reset()}{bg()}\n{style("italic")}{color("green")}Introduction\n{style()}{color("magenta")}\t{intro}\n{style("italic")}{color("green")}Documentation\n{style()}{color("magenta")}\tFor Documentation, go to: {color("blue")}{style("underline")}{docs}{reset()}{bg()}\n{style("italic")}{color("green")}Credits\n{style()}{color("magenta")}\tThis Library is made by {color("cyan")}Siddhesh Chavan\n{bg("yellow")} {style("bold")}{color("black")}Note: {color("#ff0000")}This library can only be used in Terminal or other things which support the ANSI escape sequences.{reset()}"""
        print(main_text)

    def _hex_to_rgb(self, color):
        if len(color) != 7:
            raise Exceptions.ColorError(
                f"Invalid HEX color provided '{color}'. HEX colors should have a length of 7 along with the '#' sign")
        c = color.replace("#", "")
        i = 0
        result = []
        while i < len(c):
            txt = c[i] + c[i + 1]
            result.append(int(txt, 16))
            i += 2
        return result
