import pygame, time
from pygame.locals import *
from time import time

def main():

    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Pygame Keyboard Test')
    pygame.mouse.set_visible(0)

    start_time = end_time = 0

    down = 0
    up = 0
    total_time = []
    total = 0

    while True:

        for event in pygame.event.get():
            if(event.type == KEYDOWN):
                print("key pressed down")
                down = end_time-start_time
                print("measured time:", down)

            if (event.type == KEYUP):
                print("key pressed up")
                up = end_time-start_time
                print("measured time:",up )
                total = up - down
                print(total)
                total_time.append(total)


        end_time = time()


    start_time = time()


main()
