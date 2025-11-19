import cairo
import numpy as np
import pygame

def convert_cairo_to_pygame_surf(surface: cairo.ImageSurface) -> pygame.Surface:
    # width, height = 200, 200
    # surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    # ctx = cairo.Context(surface)

    # # Contoh gambar: lingkaran merah
    # ctx.set_source_rgb(1, 0, 0)
    # ctx.arc(width/2, height/2, 50, 0, 2*3.14159)
    # ctx.fill()

    # Ambil data dari Pycairo
    data = surface.get_data()  # ini bytes
    arr = np.frombuffer(data, dtype=np.uint8)  # jadi array 1D
    arr = arr.reshape((surface.get_height(), surface.get_width(), 4))  # Pycairo ARGB32 = 4 channel

    # ARGB ke RGBA (Pygame pakai RGBA)
    arr = arr[:, :, [2, 1, 0, 3]]

    # Buat Pygame surface
    return pygame.image.frombuffer(arr.tobytes(), (surface.get_width(), surface.get_height()), 'RGBA')