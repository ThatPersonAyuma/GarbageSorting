import pygame

class Button:
    def __init__(self, x, y, w, h, text, callback,
                 color=(70,130,180), hover=(100,160,210)):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.hover = hover
        self.text = text
        self.callback = callback
        self.font = pygame.font.SysFont(None, 32)

    def draw(self, screen):
        mx, my = pygame.mouse.get_pos()
        if self.rect.collidepoint(mx, my):
            pygame.draw.rect(screen, self.hover, self.rect, border_radius=10)
        else:
            pygame.draw.rect(screen, self.color, self.rect, border_radius=10)

        txt = self.font.render(self.text, True, (255,255,255))
        screen.blit(txt, (self.rect.x + (self.rect.width - txt.get_width())/2,
                          self.rect.y + (self.rect.height - txt.get_height())/2))

    def click(self):
        mx, my = pygame.mouse.get_pos()
        if self.rect.collidepoint(mx, my):
            self.callback()
