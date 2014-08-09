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
from PySide import QtGui
from PySide import QtCore

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

#ffc0c0 light red
#ffffc0 light yellow
#c0ffc0 light green
#c0ffff light cyan
#c0c0ff light blue
#ffc0ff light magenta
light_operand_color = ["#ffc0c0", "#ffffc0", "#c0ffc0", "#c0ffff", "#c0c0ff", "#ffc0ff"]

#ff0000 red
#ffff00 yellow
#00ff00 green
#00ffff cyan
#0000ff blue
#ff00ff magenta
operand_color = ["#ff0000", "#ffff00", "#00ff00", "#00ffff", "#0000ff", "#ff00ff"]

#c00000 dark red
#c0c000 dark yellow
#00c000 dark green
#00c0c0 dark cyan
#0000c0 dark blue
#c000c0 dark magenta
dark_operand_color = ["#c00000", "#c0c000", "#00c000", "#00c0c0", "#0000c0", "#c000c0"]

#ffffff white
#000000 black

def main():
    # app = QtGui.QApplication(sys.argv)
    QtGui.QApplication(sys.argv)

    file_name = r"D:\My_Projects\Python\Interpreters\Interpreter Piet\examples\hello_world_2_Piet.png"
    if not os.path.exists(file_name):
        print("File %s not exist!" % file_name)
        return 1

    # stack = []

    image = QtGui.QImage(file_name)
    for i in range(image.height()):
        for j in range(image.width()):
            color = image.pixel(i, j)
            name_color = QtGui.QColor(color).name()
            if name_color in light_operand_color:
                name_color += "-"
            elif name_color in operand_color:
                name_color += "="
            elif name_color in dark_operand_color:
                name_color += "+"
            elif name_color == "#ffffff":
                name_color += "w"
            elif name_color == "#000000":
                name_color += "b"
            print(name_color, end=' ')
        print()

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