import pygame
pygame.init()
screen = pygame.display.set_mode((690,690))

class irectangle():
    def __init__(self, color, diamention):
        self.screen = screen
        self.color = color
        self.diamention = diamention

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.diamention)

oobject = irectangle("Goldenrod", (232, 78, 232, 78))
o_oo_b_jeq = irectangle("Tomato", (1, 2, 112, 221))
object_questionmark = irectangle("Medium Aquamarine", (669, 0, 50, 690))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.fill("Blanched Almond")
    oobject.draw()
    o_oo_b_jeq.draw()
    object_questionmark.draw()

    pygame.display.update()