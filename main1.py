from matrix import *

f = open('pic.ppm','w')
finalstr = 'P3 500 500 255 '

screen = new_screen()
color = [255,255,255]
matrix = new_matrix()
screen = draw_lines(matrix,screen,color)
# print_matrix(matrix)\

for y in range(500):
    for x in range(500):
        for i in screen[y][x]:
            finalstr += f'{i} '
f.write(finalstr)