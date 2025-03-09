import pygame
pygame.init()

screen_width = 640
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))

screen. fill((255, 255, 255))

BLACK = (0, 0, 0)
RED = (255, 0, 0)

rect1 = pygame.Rect(0, 0, 200, 200)

rect1.center = (screen_width//2, screen_height//2)

pygame.draw.rect(screen, BLACK, rect1)


rect2 = pygame.Rect(270, 200, 100, 100)

rect2.center = rect2.center

pygame.draw.rect(screen, RED, rect2)

pygame.display.flip()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()