import pygame
import cairo
from . import convert
import enum

class ImageObject:
    def __init__(self, x:int, y:int, surface:cairo.ImageSurface, name:str=""):
        # load image
        self.cairo_surface = surface
        # optional scale
        self.pygame_surface: pygame.Surface = convert.convert_cairo_to_pygame_surf(surface)
        # rect untuk posisi dan collide area
        self.rect:pygame.Rect = self.pygame_surface.get_rect(topleft=(x, y))
        self.origin = self.rect.topleft
        self.name = name
        # self.old_rect = None

    def draw(self, screen):
        screen.blit(self.pygame_surface, self.rect)
        pygame.draw.rect(screen, (255,255,255), self.rect, 3)

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
        return self.rect.colliderect(other.rect)
    
    def scale(self, wt:int, ht:int):
        old_surface = self.cairo_surface
        ow = old_surface.get_width()
        oh = old_surface.get_height()

        new_surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, wt, ht)
        ctx = cairo.Context(new_surface)
        sx = wt / ow
        sy = ht / oh
        
        ctx.scale(sx, sy)
        
        ctx.set_source_surface(old_surface, 0, 0)
        ctx.paint()
        # self.old_rect = self.rect
        # x, y, w, h = self.rect
        # self.rect = pygame.Rect(x * sx, y * sy, w * sx, h * sy)
        self.pygame_surface = convert.convert_cairo_to_pygame_surf(new_surface)
            
    def return_scale(self):
        self.pygame_surface = convert.convert_cairo_to_pygame_surf(self.cairo_surface)
        # self.rect = self.old_rect
    
class TrashType(enum.Enum):
    ORGANIC = "Organik"
    PLASTIC = "Plastik"
    OTHERS = "Lainnya"
    OBJECT = "OBJECT" # Use this for just an object
    
class TrashObject(ImageObject):
    def __init__(self, x: int, y: int, surface: cairo.ImageSurface, name:str, type: TrashType):
        super().__init__(x, y, surface, name)
        self.type = type
        self.is_dragged = False
        
    
class TrashBin(ImageObject):
    def __init__(self, x: int, y: int, surface: cairo.ImageSurface, bin_type:TrashType, name: str = ""):
        super().__init__(x, y, surface, name)
        self.bin_type = bin_type
        
    def is_valid_trash(self, trash_type:TrashType):
        return trash_type == self.bin_type
    
# class StackStore(ImageObject):
#     def __init__(self, x: int, y: int, surface: cairo.ImageSurface, name: str = ""):
#         super().__init__(x, y, surface, name)
#         self.cache = 
#         self.check = 