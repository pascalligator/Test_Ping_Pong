import pygame
def keys():
    changes = [0, 0]
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                changes[0] = 1
            elif event.key == pygame.K_s:
                changes[0] = -1
            elif event.key == pygame.K_UP:
                changes[1] = 1
            elif event.key == pygame.K_DOWN:
                changes[1] = -1
    pygame.event.clear()
    return changes
