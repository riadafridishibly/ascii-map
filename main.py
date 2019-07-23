from itertools import groupby
import pygame
pygame.init()


# image width and height
width = 640
height = 800

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('BD map ASCII Encoder')

img_path = 'map.png'
img = pygame.image.load(img_path)
imgRect = img.get_rect()


# cell size
W, H = 10, 20
offsetX = W // 2
offsetY = H // 2


def drawRect(surf, loc):
    pygame.draw.rect(surf, (0, 0, 0), (*loc, W, H), 1)


def drawCircle(surf, loc):
    pygame.draw.circle(surf, (255, 0, 255), loc, 2, 2)


running = True
clock = pygame.time.Clock()

data = []

while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    screen.blit(img, imgRect)

    for j in range(height // H):
        for i in range(width // W):
            x, y = (i * W, j * H)
            drawRect(screen, (x, y))
            # move the points in the middle
            if img.get_at((x + offsetX, y + offsetY)) != (0, 0, 0, 0):
                drawCircle(screen, (x + offsetX, y + offsetY))
                print('*', end='')
                data.append(1)
            else:
                print(' ', end='')
                data.append(0)
        print()
        running = False

    pygame.display.flip()

pygame.quit()

group = [len(list(g)) for k, g in groupby(data)]
# remapping the chars
encodedString = ''.join([chr(126 - val) for val in group])

# This is the magic string
print(repr(encodedString))

