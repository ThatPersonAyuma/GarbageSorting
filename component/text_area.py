import pygame

class TextButton:
    def __init__(self, x, y, w, h, text, 
                 font_size=28,
                 color=(60, 140, 200),
                 hover_color=(90, 170, 230),
                 text_color=(255, 255, 255)):

        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.font = pygame.font.SysFont(None, font_size)
        self.text = text

    def draw(self, screen):
        # Cek hover
        mx, my = pygame.mouse.get_pos()
        if self.rect.collidepoint(mx, my):
            pygame.draw.rect(screen, self.hover_color, self.rect, border_radius=10)
        else:
            pygame.draw.rect(screen, self.color, self.rect, border_radius=10)

        # Render teks
        txt = self.font.render(self.text, True, self.text_color)
        screen.blit(
            txt,
            (self.rect.x + (self.rect.width - txt.get_width()) / 2,
             self.rect.y + (self.rect.height - txt.get_height()) / 2)
        )

    def collide_point(self, pos):
        """Cek tabrakan dengan kursor mouse atau posisi tertentu"""
        return self.rect.collidepoint(pos)

    def click(self):
        """Mengembalikan True saat tombol diklik"""
        mx, my = pygame.mouse.get_pos()
        if self.rect.collidepoint(mx, my):
            return True
        return False
