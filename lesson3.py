# ДЗ урок 2
# 1. Вычисление площади круга: Напишите функцию, которая
# вычисляет площадь круга на основе радиуса. В этой задаче радиус
# должен быть глобальной переменной.

'''import math # импорт модуля
r = 6 # радиус
pi = 3.141592653589793
area = math.pi * r ** 2 # формула площади круга
print("Площадь круга равна: ", area)'''

def calculate_sq_circle (r):
    "Рассчет площади круга"
    pi = 3.141592653589793
    area = pi * r ** 2 # формула площади круга
    return area

a = calculate_sq_circle(2)
# print("Площадь круга равна: ",int(a))

# 3. Счетчик букв в строке: Напишите функцию, которая принимает
# строку и символ, а затем подсчитывает количество раз, которое этот
# символ встречается в строке.

def get_number(stroka, simb):
    a = 0
    for i in stroka:
        if i == simb:
            a += 1
    print(a)

# get_number("Hello", "!")

from pygamelib import engine
my_board = engine.Board()
"""
    name (str) – the name of the Board
    player_starting_position (list) – coordinates at which Game will place the player on change_level().
    ui_border_left (str) – A string that represents the left border.
    ui_border_right (str) – A string that represents the right border.
    ui_border_top (str) – A string that represents the top border.
    ui_border_bottom (str) – A string that represents the bottom border.
    ui_board_void_cell (str) – A string that represents an empty cell.
    parent (Game) – The parent object (usually the Game object). than 80 rows and columns.
    DISPLAY_SIZE_WARNINGS (bool) – A boolean to show or hide the warning about boards bigger than 80 rows and columns.
"""
my_board.ui_border_left = "o"
my_board.ui_border_right = "o"
my_board.ui_border_top = "_"
my_board.ui_border_bottom = "_"
# my_board.display() # показать результат (рабочая область)

from pygamelib import engine
from pygamelib.assets import graphics
from pygamelib import board_items
from pygamelib.gfx import core
from pygamelib import constants

new_board = engine.Board(ui_borders=graphics.MAGENTA_SQUARE, ui_board_void_cell=graphics.CYAN_SQUARE)
new_board.place_item( board_items.Wall(model=graphics.RED_SQUARE), -1, -1)
new_board.place_item(board_items.Door(model=graphics.BLACK_SQUARE), 0, 0)
new_board.place_item(board_items.Camera(model=graphics.BLACK_SQUARE), 0, 3)
player = new_board.item(2, 2)
player.sprixel = core.Sprixel("@-", bg_color=core.Color(40,44,52), is_bg_transparent=True)
new_board.place_item(board_items.Movable(model=graphics.RED_SQUARE), -1, 0)

#new_board.move(player,constants.RIGHT)
new_board.display()
