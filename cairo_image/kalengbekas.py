import cairo

def get_kaleng_bekas(wt, ht):
    WIDTH, HEIGHT = 260, 260
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)

    ctx.translate(-25, -25)
    ctx.scale(1.3,1.3)

    # badan kaleng
    ctx.set_source_rgb(1, 0.1, 0.1)
    ctx.rectangle(80, 60, 80, 130)
    ctx.fill()

    # trapesium atas kaleng
    ctx.set_source_rgb(0.5, 0.5, 0.5)
    ctx.move_to(80, 60)
    ctx.line_to(160, 60)   
    ctx.line_to(155, 50)
    ctx.line_to(85, 50)
    ctx.close_path()
    ctx.fill()

    # kotak atas kaleng
    ctx.set_source_rgb(0.7, 0.7, 0.7)
    ctx.rectangle(82, 50, 75, 2)
    ctx.fill()

    # jajargenjang tengah kaleng
    ctx.set_source_rgb(1, 1, 1)
    ctx.move_to(80, 190)
    ctx.line_to(110, 190)
    ctx.line_to(140, 60)
    ctx.line_to(110, 60)
    ctx.close_path()
    ctx.fill()

    # trapesium bawah kaleng
    ctx.set_source_rgb(0.5, 0.5, 0.5)
    ctx.move_to(80, 190)
    ctx.line_to(160, 190)
    ctx.line_to(155, 200)
    ctx.line_to(85, 200)
    ctx.close_path()
    ctx.fill()

    # kotak bawah kaleng
    ctx.set_source_rgb(0.7, 0.7, 0.7)
    ctx.rectangle(82, 198, 75, 2)
    ctx.fill()
    scaled_surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, wt, ht)
    ctx2 = cairo.Context(scaled_surface)

    sx = wt / WIDTH
    sy = ht / HEIGHT

    ctx2.scale(sx, sy)
    ctx2.set_source_surface(surface, 0, 0)
    ctx2.paint()
    return scaled_surface


