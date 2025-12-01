import cairo
import math

WIDTH, HEIGHT = 220, 260
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

ctx.set_source_rgb(1, 1, 1)
ctx.paint()

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

surface.write_to_png("kaca_lampu.png")
