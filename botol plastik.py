import cairo

WIDTH, HEIGHT = 200, 260
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

ctx.set_source_rgb(1, 1, 1)
ctx.paint()

# leher botol trapesium
ctx.set_source_rgb(0.6, 1.0, 1.0)
ctx.move_to(85, 50)
ctx.line_to(115, 50)
ctx.line_to(130, 70)
ctx.line_to(70, 70)
ctx.close_path()
ctx.fill()


# badan botol
ctx.set_source_rgb(0.3, 0.7, 1.0)
ctx.rectangle(70, 70, 60, 50)
ctx.fill()

# trapezium bawah botol
ctx.set_source_rgb(0.6, 1.0, 1.0)
ctx.move_to(70, 120)
ctx.line_to(130, 120)
ctx.line_to(125, 125)
ctx.line_to(75, 125)
ctx.close_path()
ctx.fill()

#trapesium tengah botol
ctx.set_source_rgb(0.6, 1.0, 1.0)
ctx.move_to(75, 125)
ctx.line_to(125, 125)
ctx.line_to(130, 130)
ctx.line_to(70, 130)
ctx.close_path()
ctx.fill()

# dasar botol
ctx.set_source_rgb(0.6, 1.0, 1.0)
ctx.rectangle(70, 130, 60, 100)
ctx.fill()

# tutup botol
ctx.set_source_rgb(0.1, 0.3, 0.6)
ctx.rectangle(85, 30, 30, 20)
ctx.fill()

surface.write_to_png("botol_plastik.png")
