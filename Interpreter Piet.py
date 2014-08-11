"""
####EN:
Interpreter language Piet.

####RU:
Интерпретатор языка Piet.
"""

# import sys
# import argparse
import os
import sys
from PIL import Image

__author__ = 'ipetrash'


# def create_parser():
#     parser = argparse.ArgumentParser(description='Interpreter language Piet.')
#     parser.add_argument("path", help="Path to image file")
#     return parser

#
# Используется 20 различных цветов (таблица справа). 18 цветов первых трёх строк в таблице связаны циклически двумя
# следующими циклами:
# Цикл оттенков: красный → жёлтый → зелёный → голубой → синий → фиолетовый → красный
# Цикл яркости: светлый → нормальный → тёмный → светлый

light_operand_color = [
    "#ffc0c0",  # light red
    "#ffffc0",  # light yellow
    "#c0ffc0",  # light green
    "#c0ffff",  # light cyan
    "#c0c0ff",  # light blue
    "#ffc0ff",  # light magenta
]

operand_color = [
    "#ff0000",  # red
    "#ffff00",  # yellow
    "#00ff00",  # green
    "#00ffff",  # cyan
    "#0000ff",  # blue
    "#ff00ff",  # magenta
]

dark_operand_color = [
    "#c00000",  # dark red
    "#c0c000",  # dark yellow
    "#00c000",  # dark green
    "#00c0c0",  # dark cyan
    "#0000c0",  # dark blue
    "#c000c0",  # dark magenta
]

special_operand_color = [
   "#ffffff",  # white
   "#000000",  # black
]


def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def main():
    file_name = r"D:\My_Projects\Python\Interpreters\Interpreter Piet\examples\hello_world_2_Piet.png"
    if not os.path.exists(file_name):
        print("File %s not exist!" % file_name)
        return 1

    # stack = []

    image = Image.open(file_name, mode="r")  # Open for read
    image = image.convert("RGB")  # Need rgb-image
    width, height = image.size


    arr = []
    for i in range(height):
        arr.append([])
        for j in range(width):
            r, g, b = image.getpixel((i, j))
            rgb = rgb2hex(r, g, b)  # return as hex-string
            arr[i].append(rgb)

    for row in arr:
        print(row)

    return 0


if __name__ == '__main__':
    # parser = create_parser()
    #
    # if len(sys.argv) is 1:
    #     parser.print_help()
    # else:
    #     args = parser.parse_args()
    #     file_name = args.path

    code = main()
    sys.exit(code)