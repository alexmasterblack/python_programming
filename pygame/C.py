import pygame as pg

pg.init()

color = (142, 68, 173)
back = (255, 255, 255)

screen = pg.display.set_mode((500, 500))

pg.display.flip()

# MOUSEBUTTONDOWN нажатие кнопки
# MOUSEBUTTONUP отпускание
# MOUSEMOTION перещение мышки
# event.pos координаты происшествия,клика кортеж из двух чисел
rectangles = []
x0, y0 = 0, 0
running = True
press = True
drawing = False
while running:
    screen.fill(back)
    for event in pg.event.get():
        #выход
        if event.type == pg.QUIT:
            running = False
        #запоминаем координаты одного угла, когда нажимаем    
        if event.type == pg.MOUSEBUTTONDOWN:
            x0, y0 = event.pos
            w, h = 0, 0
            #когда рисуем не можем удалить рисунок
            press = False
            #процесс рисования
            drawing = True
        # можем двигать только левой кнопкой мыши
        # запоминаем текущие размеры
        if event.type == pg.MOUSEMOTION and event.buttons[0]:
            w, h = event.pos[0] - x0, event.pos[1] - y0
        #если отпустили клавишу, то добавляем координаты в массив
        if event.type == pg.MOUSEBUTTONUP:
            rectangles.append((x0, y0, w, h))
            press = True
            drawing = False
        #если хочу удалить фигуру, то чекаю, что кнопки зажата и эти кнопки ctrl + Z
        #key атрибут, который является целым числом, представляющим ключ на клавиатурe
        if event.type == pg.KEYDOWN and (event.key == pg.KMOD_LCTRL or event.key == pg.K_z):
            #удаляю последний элементв массиве
            if len(rectangles) > 0:
                del rectangles[-1]
    #рисование фигуры
    if drawing:
        pg.draw.rect(screen, color, (x0, y0, w, h), 2)
    #фигура останется
    for coords in rectangles:
        pg.draw.rect(screen, color, coords, 2)
    pg.display.flip()
# завершение работы
pg.quit()
