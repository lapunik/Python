import pygame
import math

# Inicializace Pygame
pygame.init()

# Nastavení okna
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Barva hexagonu
hex_color = (100, 100, 100)

# Souřadnice hexagonu
hex_radius = 75
hex_center = (400, 300)
angle = 2 * math.pi / 6
hex_points = [(hex_center[0] + hex_radius * math.cos(i * angle), hex_center[1] + hex_radius * math.sin(i * angle)) for i in range(6)]

# Hlavní smyčka hry
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detekce kliknutí na hexagon
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if math.dist((x, y), hex_center) <= hex_radius:
                print("Hexagon byl stisknut!")

    # Vykreslení hexagonu
    screen.fill((0, 0, 0))
    pygame.draw.polygon(screen, hex_color, hex_points)
    pygame.display.flip()

pygame.quit()
