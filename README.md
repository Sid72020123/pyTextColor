# pyTextColor v1.0

## Introduction

pyTextColor is a simple Python Library to display colorful outputs in Terminal, etc.

**Note: Your Terminal or any software in which you are going to print a text should support the ANSI Escape Sequences or
it may not work!**

## Install

To install this library, type ```pip install pyTextColor``` in the Terminal(command prompt)

## Import

To import the library, use the following code:

```python
import pyTextColor
```

## Print Basic Colored Output

See the following program to print a colorful text in Python!

```python
import pyTextColor  # Import the library

pytext = pyTextColor.pyTextColor()  # Create an object of the pyTextColor class

text = pytext.format_text(text="Hi!", color="white",
                          bgcolor="black")  # Format the text with the color/bgcolor of your choice

print(text)  # Print the text
```

The above program will give the output as:

![Image 1](https://u.cubeupload.com/Sid72020123/ptc1.png)

You can also change the style/color/background of the text!

Following is a list of all color names you can use for both background and text:

* black
* red
* green
* yellow
* blue
* magenta
* cyan
* white

**Note: You can also use HEX color values to color a text or background. Remember: HEX color values should have '#'
before the main color value**

Example Code:

```python
import pyTextColor

pytext = pyTextColor.pyTextColor()

text = pytext.format_text(text="This text will be printed out in yellow color with red background", color="#ff0000",
                          bgcolor="#FFFF00")  # HEX values

print(text)  # Print the text
```

The output of the above code will be:

![Image 2](https://u.cubeupload.com/Sid72020123/ptc2.png)

## Text Styles

There are many text styles you can use. Use the ```text_style``` parameter to change the text style. Example code:

```python
import pyTextColor

pytext = pyTextColor.pyTextColor()

text = pytext.format_text(text="I am bold text", color="#ff0000",
                          bgcolor="#FFFF00", text_style="bold")  # bold text

print(text)  # Print the text
```

The output of the above program will be:

![Image 3](https://u.cubeupload.com/Sid72020123/ptc3.png)

There are many text styles you can use! See the list of available styles:

* ```normal``` > for normal text
* ```bold``` > for bold text
* ```faint``` > for faint text
* ```italic``` > for italic text
* ```underline``` > for underlined text
* ```blink``` > for blinking text
* ```reverse``` > for reversed text. The color of the text will be changed to background color while the background
  color will be changed to text color
* ```hidden``` > for hidden text
* ```strikethrough``` > for strikethrough text

## Print the documentation

To pretty print the documentation for this library, run the following code:

```python
import pyTextColor

pytext = pyTextColor.pyTextColor()
pytext.pretty_print_help()  # Print the docs
```

The output will be:

![Image 4](https://u.cubeupload.com/Sid72020123/ptc4.png)

### Parameters of the ```format_text()``` function

The ```format_text()``` function has many parameters such as:

* ```text``` > The text you want
* ```color``` > The color you want
* ```bgcolor``` > The background color you want
* ```text_style``` > The text style you want
* ```bg_full_line``` > Set this to ```True``` if you want the background color to be printed on full line

## Make output fully customised?

See the following program to make the output fully customized:

```python
import pyTextColor

pytext = pyTextColor.pyTextColor()

color = pytext.color  # Color Function
style = pytext.style  # Style Function
bg = pytext.background  # Background Function
reset = pytext.reset  # Reset Function (To reset all styles/colors/etc.)

name = "Siddhesh"
age = 15
hobby = "programming"

text = f"""{bg("black")}{color("#ffffff")}Hi! I am {color("magenta")}{name}{color("#ffffff")}. I am {color("magenta")}{age}{color("#ffffff")} years old. My favourite hobby is {color("green")}{style("italic")}{hobby}{reset()}"""  # Make an f-string and edit the text

print(text)  # Print the output
```

The output will be:

![Image 5](https://u.cubeupload.com/Sid72020123/ptc5d.png)

**Remember to use the ```reset()``` function or the normal text will be printed out with styles when you print a text
below the styled text.**

## Thank you!
