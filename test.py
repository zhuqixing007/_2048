import pygame



pygame.init()
screen = pygame.display.set_mode((300, 400))

screen.fill((230, 230, 230))
myrect = pygame.Rect([10, 20, 60, 60])
pygame.draw.rect(screen, (200,200,200), myrect, 1)
font = pygame.font.Font(None, 28)
text = font.render("Score:", 1, (10, 10, 10))
textpos = text.get_rect()
textpos.center = myrect.center
screen.blit(text, textpos)
while True:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()