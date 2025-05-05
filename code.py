from traceback import print_tb
from pathlib import Path
import requests
import pygame
import sys
import os
import random

pygame.init()
while run:
    for i in pygame.event.get():  # Обработчик событий
        if i.type == pygame.QUIT:
            run = False
        if i.type == pygame.USEREVENT and button_start == True:
            counter += 1
            text = str(counter).rjust(3)  # Таймер
        elif i.type == MOUSEBUTTONDOWN:
            moving = True
        elif i.type == MOUSEBUTTONUP:
            moving = False
        elif i.type == MOUSEMOTION and moving:
            button_start = True
            for n in range(len(rect_arry)):
                if rect_arry[n].collidepoint(i.pos):
                    rect_arry[n].move_ip(i.rel)  # Передвижение картинки

                    if 30 >= rect_arry[n].left:
                        rect_arry[n].move_ip(20, 0)  # Если выходит за границу то сдвинуть в сторону
                    elif 950 <= rect_arry[n].right:
                        rect_arry[n].move_ip(-20, 0)  # Если выходит за границу то сдвинуть в сторону
                    elif 30 >= rect_arry[n].top:
                        rect_arry[n].move_ip(0, 20)  # Если выходит за границу то сдвинуть в сторону
                    elif 750 <= rect_arry[n].bottom:
                        rect_arry[n].move_ip(0, -20)  # Если выходит за границу то сдвинуть в сторону

        if i.type == pygame.MOUSEBUTTONDOWN:

            if 1000 <= mouse[0] <= 1200 and 0 <= mouse[1] <= 100:  # Область для кнопки старта
                button_start = True
            elif 1000 <= mouse[0] <= 1200 and 100 <= mouse[1] <= 200:  # Область для кнопки стоп
                button_start = False
            elif 1000 <= mouse[0] <= 1200 and 600 <= mouse[1] <= 700:  # Кнопка рестарт
                run = False

    for k in range(len(rect_arry)):
        screen.blit(image[k], (rect_arry[k].x, rect_arry[k].y))  # Отрисовка картинок