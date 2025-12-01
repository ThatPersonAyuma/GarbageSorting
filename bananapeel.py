import cairo

WIDTH, HEIGHT = 250, 200
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

ctx.set_source_rgb(1, 1, 1)
ctx.paint()

# bekas kulit pisang
ctx.set_source_rgb(1, 0.9, 0.1)
ctx.move_to(50, 150)
ctx.curve_to(80, 130, 140, 120, 150, 150)
ctx.line_to(130, 160)
ctx.curve_to(110, 180, 110, 150, 50, 160)
ctx.close_path()
ctx.fill()

# kulit pisang bawah
ctx.set_source_rgb(1, 0.8, 0.0)
ctx.move_to(50, 160)
ctx.curve_to(80, 140, 130, 130, 140, 155)
ctx.line_to(125, 165)
ctx.curve_to(100, 175, 100, 150, 60, 170)
ctx.close_path()
ctx.fill()

# hijau tangkai kulit pisang atas
ctx.set_source_rgb(0.0, 0.6, 0.1) 
ctx.move_to(45, 150)
ctx.line_to(45, 160)
ctx.line_to(50, 160)
ctx.line_to(50, 150)
ctx.close_path()
ctx.fill()

# hijau tangkai kulit pisang bawah
ctx.set_source_rgb(0.0, 0.6, 0.1) 
ctx.move_to(45, 160)
ctx.line_to(55, 175)
ctx.line_to(60, 170)
ctx.line_to(50, 155)
ctx.close_path()
ctx.fill()

# hijau ujung kulit pisang atas
ctx.set_source_rgb(0.0, 0.6, 0.1)
ctx.move_to(45, 170)
ctx.line_to(50, 165)
ctx.line_to(45, 160)
ctx.line_to(35, 170)
ctx.close_path()
ctx.fill()

surface.write_to_png("kulit_pisang.png")
