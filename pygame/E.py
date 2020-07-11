import pygame as pg
import math

pg.init()

back = (0, 0, 0)
radius = 200
screen = pg.display.set_mode((500, 500))

#вычисляем координаты точек
points = []
for i in range(1,361):
    x = int(math.cos(math.radians(i)) * radius) + 500 // 2
    y = int(math.sin(math.radians(i)) * radius) + 500 // 2
    points.append((x, y))

increase = 2
drawing = True
running = True
press = False
color = pg.Color('white').hsva

while running:
    for event in pg.event.get():
        press = False
        #выход
        if event.type == pg.QUIT:
            running = False
        #если рисуется и кнопка не нажата
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE and drawing and not press:
            press = True
            drawing = False
        #если не рисуется и кнопка не нажата
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE and not drawing and not press:
            press = True
            drawing = True
    if drawing:
        color = ((color[0] + 0.1) % 256,  color[1],  color[2],  color[3])
        screen.fill(back)
        #соединяем точки
        for i in range(360):
            pg.draw.aaline(screen, color, points[i], points[(round(i * increase)) % 360])
        #рисуем круг
        pg.draw.circle(screen, color, (500 // 2, 500 // 2), radius, 2)
        pg.display.flip()
        increase = increase + 0.01
# завершение работы
pg.quit()
