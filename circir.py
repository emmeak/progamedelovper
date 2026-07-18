import pygame
pygame.init()
screen = pygame.display.set_mode((400,781))

class circir():
    def __init__(self, color, position, radius):
        self.screen = screen
        self.color = color
        self.position = position
        self.radius = radius

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.position, self.radius)

cirple = circir("Purple", (7, 7), 7)
elcric = circir("Navajo White", (654, 321), 543)
clecir = circir("Medium Aquamarine", (69, 96), 69)
iclerc = circir("Pale Violet Red", (516, 295), 349)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.fill("Light Slate Grey")
    cirple.draw()
    elcric.draw()
    clecir.draw()
    iclerc.draw()

    pygame.display.update()