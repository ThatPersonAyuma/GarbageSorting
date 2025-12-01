import cairo
import math

WIDTH, HEIGHT = 200, 200
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

# background
ctx.set_source_rgb(1, 1, 1)
ctx.paint()

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

# bekas gigitan
ctx.set_source_rgb(1, 1, 1)
ctx.arc(150, 80, 30, 0, math.pi * 2)
ctx.arc(145, 118, 30, 0, math.pi * 2)
ctx.fill()

# bekas gigitan kiri
ctx.set_source_rgb(1, 1, 1)
ctx.arc(30, 80, 30, 0, math.pi * 2)
ctx.arc(30, 118, 30, 0, math.pi * 2)
ctx.fill()

# daun
ctx.set_source_rgb(0.0, 0.6, 0.1)
ctx.move_to(90, 42)
ctx.curve_to(140, 0, 120, 50, 110, 70)
ctx.fill()

surface.write_to_png("apel_bekas.png")
