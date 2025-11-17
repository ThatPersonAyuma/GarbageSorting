import pygame
import cairo
from . import convert

class ImageObject:
    def __init__(self, x:int, y:int,  height:int, width:int, surface:cairo.ImageSurface, name=""):
        # load image
        self.cairo_surface = surface
        # optional scale
        self.pygame_surface: pygame.Surface = convert.convert_cairo_to_pygame_surf(surface, height, width)
        # rect untuk posisi dan collide area
        self.rect = self.pygame_surface.get_rect(topleft=(x, y))
        self.origin = self.rect.topleft
        self.name = name

    def draw(self, screen):
        screen.blit(self.pygame_surface, self.rect)

    def replace_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def back_to_origin(self):
        self.rect.x = self.origin[0]
        self.rect.y = self.origin[1]
    
    def collide_point(self, pos):
        """Cek tabrakan dengan posisi mouse atau koordinat tertentu"""
        return self.rect.collidepoint(pos)

    def collide_object(self, other: ImageObject):
        """Cek tabrakan dengan object lain (yang juga punya rect)"""
        return self.rect.colliderect(other.pygame_surface.get_rect())