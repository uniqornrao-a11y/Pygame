import pygame
pygame.init()
screen = pygame.display.set_mode((400,500))
image=pygame.image.load("ccg_original.png")
pygame.display.set_caption("Pygame Window")
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    screen.fill((255,255,255))
    screen.blit(image,(200,150))
    pygame.display.flip()
pygame.quit()