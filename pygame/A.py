import pygame as pg
# инициализация Pygame
pg.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# размеры доски, размер ячейки
field_size, cell_size = map(int, input().split())

# холст, на котором рисуем
screen = pg.display.set_mode((field_size, field_size))

# чтобы клетки вписывались в размер экрана, а то они как-то в боку получаются
right_size = int(field_size/cell_size)

for col in range(cell_size):
    for row in range(cell_size):
        if (col % 2 == 0):
            if (row % 2 == 0):
                color = BLACK
            else:
                color = WHITE
        else:
            if (row % 2 == 0):
                color = WHITE
            else:
                color = BLACK
        # первые два значения координаты верхнего левого угла прямоугольника
        # вторые ширина и высота
        pg.draw.rect(screen, color, (col * right_size, row *
                                     right_size, right_size, right_size))

# отрисовка кадра
pg.display.flip()

# ожидание закрытия окна
while pg.event.wait().type != pg.QUIT:
    pass

# завершение работы
pg.quit()
