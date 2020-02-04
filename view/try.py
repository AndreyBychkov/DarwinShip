import sys
import pygame

from pygame.locals import *

FPS = 60
fps_clock = pygame.time.Clock()

WHITE = (255, 255, 255)
RED = (255, 0, 0)

display_surf = pygame.display.set_mode((1700, 900))

alice_image = pygame.image.load('resources/Mia_chibi.png').convert_alpha()
alice_image = pygame.transform.scale(alice_image, (300, 300))
alice_image.set_colorkey(WHITE)

andrey_image = pygame.image.load('resources/Andrey.png').convert_alpha()
andrey_image = pygame.transform.scale(andrey_image, (300, 300))
andrey_image.set_colorkey(WHITE)


def move(x, y, dx, dy, direction):
    if direction == 'right':
        if x >= 1300:
            return x + dx, y, 'up'
        else:
            return x + dx, y, direction
    elif direction == 'left':
        if x <= 100:
            return x - dx, y, 'down'
        else:
            return x - dx, y, direction
    elif direction == 'up':
        if y <= 100:
            return x, y - dy, 'left'
        else:
            return x, y - dy, direction
    elif direction == 'down':
        if y >= 500:
            return x, y + dy, 'right'
        else:
            return x, y + dy, direction
    else:
        raise ValueError()


if __name__ == '__main__':
    pygame.display.set_caption('Hello Darwin!')

    alice_direction = 'right'
    alice_x = 800
    alice_y = 450

    andrey_direction = 'right'
    andrey_x = 250
    andrey_y = 450

    dx = 5
    dy = 5

    while True:
        display_surf.fill(WHITE)

        alice_x, alice_y, alice_direction = move(alice_x, alice_y, dx, dy, alice_direction)
        andrey_x, andrey_y, andrey_direction = move(andrey_x, andrey_y, dx, dy, andrey_direction)

        display_surf.blit(alice_image, (alice_x, alice_y))
        display_surf.blit(andrey_image, (andrey_x, andrey_y))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        fps_clock.tick(FPS)
