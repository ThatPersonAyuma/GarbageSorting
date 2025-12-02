import cairo
import pygame
from . import convert
from math  import pi

# class BaseButton:
#     def __init__(self, x, y, w, h, callback,
#                 color=(0.27, 0.51, 0.70),
#                 hover_color=(0.39, 0.66, 0.82)) -> None:
#         self.rect = pygame.Rect(x, y, w, h)
#         self.callback = callback
#         self.normal_surf = 
#         self.hover_surf =
        
class Button():
    def __init__(self, x:int, y:int, w:int, h:int, text:str, font_size:int, callback, rotate:float,
                color:tuple[float,float,float]=(0.21, 0.28, 0.25),
                hover_color:tuple[float,float,float]=(0.10, 0.12, 0.11),
                name:str=""
                ):
        self.name = name
        self.callback = callback

        # Cairo color (RGB float 0–1)
        # self.color = color
        # self.hover_color = hover_color

        # Cache pygame surface
        self.normal_surf = self.render_cairo_button(color,rotate,font_size,text,w,h)
        self.hover_surf = self.render_cairo_button(hover_color,rotate,font_size,text,w,h)
        self.rect = pygame.Rect(x, y, self.normal_surf.get_width(), self.normal_surf.get_height())
        
    def render_cairo_button(self, rgb, rotate, font_size, text,w,h):
        surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
        ctx = cairo.Context(surf)
        ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        ctx.set_font_size(font_size)
        xb, yb, tw, th, xa, ya = ctx.text_extents(text)
        # surf = cairo.ImageSurface(cairo.FORMAT_ARGB32,
        #                         int(tw) + 20,
        #                         int(th) + 20)
        # ctx = cairo.Context(surf)

        # Rounded rectangle
        r = 10
        ctx.set_source_rgb(*rgb)
        self.rounded_rect(ctx, 0, 0, w, h, r)
        ctx.fill()

        # Draw text
        
        ctx.set_source_rgb(1, 1, 1)
        ctx.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        ctx.set_font_size(font_size)

        # xb, yb, tw, th, xa, ya = ctx.text_extents(self.text)

        ctx.save()
        ctx.translate(surf.get_width()/2, surf.get_height()/2)  # pindah origin ke tengah
        ctx.rotate(rotate)
        ctx.save()
        
        ctx.move_to(-tw/2 - xb, -th/2 - yb)

        # gambar teks dari tengah (dibalikkan setengah ukuran)
        # ctx.move_to(-tw/2 - xb, -th/2 - yb)
        ctx.show_text(text)
        ctx.restore()

        return convert.convert_cairo_to_pygame_surf(surf)

    @staticmethod
    def rounded_rect(ctx, x, y, w, h, r):
        ctx.new_sub_path()
        ctx.arc(x + w - r, y + r, r, -90 * (3.14/180), 0)
        ctx.arc(x + w - r, y + h - r, r, 0, 90 * (3.14/180))
        ctx.arc(x + r, y + h - r, r, 90 * (3.14/180), 180 * (3.14/180))
        ctx.arc(x + r, y + r, r, 180 * (3.14/180), 270 * (3.14/180))
        ctx.close_path()

    def draw(self, screen):
        mx, my = pygame.mouse.get_pos()
        # print(f"Image {self.normal_surf.get_rect()}, rect {self.rect}")
        if self.rect.collidepoint(mx, my):
            screen.blit(self.hover_surf, self.rect)
            return self.name
        else:
            screen.blit(self.normal_surf, self.rect)
            
        # pygame.draw.rect(screen, (0,0,0), self.rect, width=3)

    def click(self, pos:tuple[int,int]):
        if self.rect.collidepoint(pos):
            self.callback()
            
    @staticmethod
    def create_up_down_button(x1:int, y1:int, x2, y2, w:int, h:int, callback_up, callback_down):
        """
        direction: 'up' or 'down'
        """
        return (Button(x1, y1, w, h, "^", 24, callback_up, 0, color=(1,0,0)), Button(x2, y2, w, h, "^", 24, callback_down, pi,color=(0,0,1)))