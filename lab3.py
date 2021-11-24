from PIL import Image, ImageDraw
from math import *

from PIL import Image, ImageDraw
coord = []
n = 4 


with open('DS4.txt') as file:
    l = file.readlines()

for line in l:
    formatted_line = line[:-1].split(' ')
    single_coordinate = (int(formatted_line[0]), int(formatted_line[1]))
    coord.append(single_coordinate)

# Создание картинки 
out = Image.new("RGB", (960, 960), (255, 255, 255))
draw = ImageDraw.Draw(out)
# Заполнение  канвас  координатами
draw.point(coord, fill='green')

angle = 10 * (n + 1)
angle_in_radian = angle * pi/180
ox, oy = 480, 480

rotated_coord = []

for  c in coord:
    x = c[0]
    y = c[1]
    # Аффинные формулы для вращения каждой точки
    new_x = ox + (x - ox) * cos(angle_in_radian) - (y - oy) * sin(angle_in_radian)
    new_y = oy + (x - ox) * sin(angle_in_radian) + (y - oy) * cos(angle_in_radian)
    single_coordinate = (new_x, new_y)
    rotated_coord.append(single_coordinate)

# Заполнение  канвас  координатами
draw.point(rotated_coord, fill='blue')

# Вывод картинки
out.show()

# сохранение картинки 
out.save("result_image.jpg")
