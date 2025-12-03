import pygame
import cairo
import numpy as np
from . import convert


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
        self.text = text
        self.font_size = font_size

        # Buat surface cairo tombol awal (tanpa hover)
        self.base_surface = self._render_cairo_surface(w, h, color)
        self.hover_surface = self._render_cairo_surface(w, h, hover_color)

        # Convert ke pygame.Surface
        self.base_surface = convert.convert_cairo_to_pygame_surf(self.base_surface)
        self.hover_surface = convert.convert_cairo_to_pygame_surf(self.hover_surface)

    def _render_cairo_surface(self, width, height, bg_color):
        """Render rectangle + teks dengan Pycairo"""
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
        ctx = cairo.Context(surface)

        # Background rectangle
        ctx.set_source_rgb(bg_color[0]/255, bg_color[1]/255, bg_color[2]/255)
        ctx.rectangle(0, 0, width, height)
        ctx.fill()

        # Draw text
        ctx.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        ctx.set_font_size(self.font_size)
        ctx.set_source_rgb(self.text_color[0]/255, self.text_color[1]/255, self.text_color[2]/255)

        # Hitung posisi teks supaya center
        xbearing, ybearing, tw, th, xadvance, yadvance = ctx.text_extents(self.text)
        x = (width - tw) / 2 - xbearing
        y = (height - th) / 2 - ybearing

        ctx.move_to(x, y)
        ctx.show_text(self.text)

        return surface

    def draw(self, screen):
        mx, my = pygame.mouse.get_pos()
        if self.rect.collidepoint(mx, my):
            screen.blit(self.hover_surface, self.rect.topleft)
        else:
            screen.blit(self.base_surface, self.rect.topleft)

    def collide_point(self, pos):
        return self.rect.collidepoint(pos)

    def click(self):
        mx, my = pygame.mouse.get_pos()
        return self.rect.collidepoint(mx, my)

# region Text home_screen
text_store = {}
def create_text_box(text:str, font_size:int,  bg_color:tuple[float,float,float,float]) -> pygame.Surface:
    global text_store
    if text in text_store:
        return text_store[text]
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1, 1)
    ctx = cairo.Context(surface)
    ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(font_size)
    xb, yb, tw, th, xa, ya = ctx.text_extents(text)
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32,
                            int(tw) + 20,
                            int(th) + 20)
    ctx = cairo.Context(surface)

    # Background
    ctx.set_source_rgba(*bg_color)
    ctx.paint()

    # Atur font
    ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(font_size)

    # Buat path teks
    
    
    ctx.save()
    ctx.translate(surface.get_width()/2, surface.get_height()/2)
    ctx.move_to(-tw/2 - xb, -th/2 - yb)
    ctx.text_path(text)

    # --- Stroke Outline ---
    ctx.set_source_rgb(0, 0, 0)      
    ctx.set_line_width(4)            
    ctx.stroke_preserve()            
    
    # --- Fill Isi ---
    ctx.set_source_rgb(1, 1, 1)      
    ctx.fill()
    ctx.restore()
    text_store[text] = convert.convert_cairo_to_pygame_surf(surface)
    return text_store[text]
# endregion