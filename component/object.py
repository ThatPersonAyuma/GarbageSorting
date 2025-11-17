import pygame

class ImageObject:
    def __init__(self, x, y, image_path, scale=None):
        # load image
        self.image = pygame.image.load(image_path).convert_alpha()

        # optional scale
        if scale is not None:
            self.image = pygame.transform.scale(self.image, scale)

        # rect untuk posisi dan collide area
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def collide_point(self, pos):
        """Cek tabrakan dengan posisi mouse atau koordinat tertentu"""
        return self.rect.collidepoint(pos)

    def collide_object(self, other):
        """Cek tabrakan dengan object lain (yang juga punya rect)"""
        return self.rect.colliderect(other.rect)