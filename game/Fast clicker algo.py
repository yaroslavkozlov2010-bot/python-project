import pygame as pg
import random as rd

pg.init()

LIGHT_RED = (250, 128, 114)
window = pg.display.set_mode((500, 500))
window.fill(LIGHT_RED)

class Area():
    def __init__(self, rect, color):
        self.rect = rect
        self.color = color
    
    def set_color(self, color):
        self.color = color
    
    def fill(self):
        pg.draw.rect(window, self.color, self.rect)
    
    def draw_outline(self, outline_color, thinckness):
        pg.draw.rect(window, outline_color, self.rect, thinckness)

class Label(Area):
    def __init__(self, rect, color):
        super().__init__(rect, color)

    def set_text(self, text, font_size, text_color):
        self.image = pg.font.Font(None, font_size).render(text, True, text_color)
    
    def draw(self):
        self.fill()
        bounding_rect = self.image.get_bounding_rect(10)
        x = self.rect.x + 10
        y = self.rect.y + 40 
        window.blit(self.image, (x, y))
        window.blit(self.image, (x, y))
        self.draw_outline((80, 80, 255), 10)


cards = []
for i in range(4):
    card = Label(pg.Rect(70 + i * 100, 170, 70, 100), (255, 255, 0))
    card.set_text('click', 26, (0, 0, 0))
    cards.append(card)
    card.draw()

clock = pg.time.Clock()
while True:
    rnd_card_idx = rd.randint(0, 3)
    for i in range(4):
        if i == rnd_card_idx:
            cards[i].draw()
        else:
            cards[i].fill()
            cards[i].draw_outline((80, 80, 255), 10)

    pg.display.update()
    clock.tick(5)