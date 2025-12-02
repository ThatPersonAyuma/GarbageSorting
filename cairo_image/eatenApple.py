import cairo
import math

def get_eaten_apple(wt, ht):
    WIDTH, HEIGHT = 200, 200
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)

    # apel sisi kanan
    ctx.set_source_rgb(0.8, 0.1, 0.1)
    ctx.arc(110, 100, 60, 0, math.pi * 2)
    ctx.fill()

    # apel sisi kiri
    ctx.set_source_rgb(0.8, 0.1, 0.1)
    ctx.arc(80, 100, 60, 0, math.pi * 2)
    ctx.fill()

    # daging apel
    ctx.set_source_rgb(1, 0.8, 0.6)
    ctx.arc(140, 80, 30, 0, math.pi * 2)
    ctx.arc(135, 118, 30, 0, math.pi * 2)
    ctx.fill()

    # daging apel kiri
    ctx.set_source_rgb(1, 0.8, 0.6)
    ctx.arc(45, 80, 25, 0, math.pi * 2)
    ctx.arc(45, 118, 25, 0, math.pi * 2)
    ctx.fill()

    ctx.set_operator(cairo.OPERATOR_CLEAR)     # hapus area berikut

    # gigitan kanan
    ctx.arc(150, 80, 30, 0, math.pi * 2)
    ctx.arc(145, 118, 30, 0, math.pi * 2)
    ctx.fill()

    # gigitan kiri
    ctx.arc(30, 80, 30, 0, math.pi * 2)
    ctx.arc(30, 118, 30, 0, math.pi * 2)
    ctx.fill()

    ctx.set_operator(cairo.OPERATOR_OVER)      # kembalikan operator

    # daun
    ctx.set_source_rgb(0.0, 0.6, 0.1)
    ctx.move_to(90, 42)
    ctx.curve_to(140, 0, 120, 50, 110, 70)
    ctx.fill()
    scaled_surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, wt, ht)
    ctx2 = cairo.Context(scaled_surface)

    sx = wt / WIDTH
    sy = ht / HEIGHT

    ctx2.scale(sx, sy)
    ctx2.set_source_surface(surface, 0, 0)
    ctx2.paint()
    return scaled_surface
