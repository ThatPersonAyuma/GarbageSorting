import cairo
import math

def get_kaca_lampu(wt, ht):
    WIDTH, HEIGHT = 260, 260
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)

    ctx.translate(-25, -30)
    ctx.scale(1.4,1.4)

    # bola lampu
    ctx.set_source_rgb(0.9, 0.9, 1)
    ctx.arc(110, 100, 60, 0, math.pi * 2)
    ctx.fill()

    # fitting lampu
    ctx.set_source_rgb(0.5, 0.5, 0.5)
    ctx.rectangle(85, 155, 50, 40)
    ctx.fill()

    # ulir fitting
    ctx.set_source_rgb(0.3, 0.3, 0.3)
    for i in range(5):
        ctx.move_to(85, 155 + i * 8)
        ctx.line_to(140, 155 + i * 8)
        ctx.line_to(135, 160 + i * 8)
        ctx.line_to(80, 160 + i * 8)
        ctx.close_path()
        ctx.fill()
    scaled_surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, wt, ht)
    ctx2 = cairo.Context(scaled_surface)

    sx = wt / WIDTH
    sy = ht / HEIGHT

    ctx2.scale(sx, sy)
    ctx2.set_source_surface(surface, 0, 0)
    ctx2.paint()
    return scaled_surface