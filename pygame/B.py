import pygame as pg

pg.init()

color = (142, 68, 173)
back = (255, 255, 255)

start_x, start_y = 0, 0
size = 100

screen = pg.display.set_mode((300, 300))

pg.draw.rect(screen, color, (start_x, start_y, size, size))
pg.display.flip()

# MOUSEBUTTONDOWN нажатие кнопки
# MOUSEBUTTONUP отпускание
# MOUSEMOTION перещение мышки
# event.pos координаты происшествия,клика кортеж из двух чисел
running = True
moving = False
while running:
    screen.fill(back)
    for event in pg.event.get():
        # выход
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            moving = True
        # можем двигать только левой кнопкой мыши
        if event.type == pg.MOUSEMOTION and event.buttons[0] and moving:
            # rel относительное смещение по обоим осям, позиция относительно предыдущей позиции
            dx, dy = event.rel
            start_x = start_x + dx
            start_y = start_y + dy
        if event.type == pg.MOUSEBUTTONUP:
            moving = False

    pg.draw.rect(screen, color, (start_x, start_y, size, size))
    pg.display.flip()
# завершение работы
pg.quit()
