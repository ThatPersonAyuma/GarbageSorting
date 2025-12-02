import cairo

def get_kemasan_plastik(wt, ht):
    WIDTH, HEIGHT = 240, 240
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)

    ctx.translate(-35, 0)
    ctx.scale(1.3,1.3)

    # bungkus utama
    ctx.set_source_rgb(1.0, 0.3, 0.3)
    ctx.rectangle(60, 60, 120, 60)
    ctx.fill()

    # lipatan kanan (perulangan segitiga)
    ctx.set_source_rgb(0.9, 0.25, 0.25)
    for i in range(6):
        ctx.move_to(195, 60 + i * 10)
        ctx.line_to(200, 65 + i * 10)
        ctx.line_to(195, 70 + i * 10)
        ctx.close_path()
        ctx.fill()

    # lipatan kanan
    ctx.rectangle(180, 60, 15, 60)
    ctx.fill()

    # lipatan kiri (perulangan segitiga)
    ctx.set_source_rgb(0.9, 0.25, 0.25)
    for i in range(6):
        ctx.move_to(45, 60 + i * 10)
        ctx.line_to(40, 65 + i * 10)
        ctx.line_to(45, 70 + i * 10)
        ctx.close_path()
        ctx.fill()

    # lipatan kiri
    ctx.rectangle(45, 60, 15, 60)
    ctx.fill()

    # bulatan tengah merk kemasan
    ctx.set_source_rgb(1.0, 1.0, 1.0)
    ctx.arc(120, 90, 20, 0, 2 * 3.14)
    ctx.fill()

    # huruf merk kemasan P
    ctx.set_source_rgb(1.0, 0.1, 0.1)
    ctx.set_line_width(5)
    ctx.move_to(110, 80)
    ctx.line_to(110, 100)
    ctx.line_to(120, 100)
    ctx.arc(120, 90, 10, 0, 3.14)
    ctx.line_to(110, 90)
    ctx.stroke()
    scaled_surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, wt, ht)
    ctx2 = cairo.Context(scaled_surface)

    sx = wt / WIDTH
    sy = ht / HEIGHT

    ctx2.scale(sx, sy)
    ctx2.set_source_surface(surface, 0, 0)
    ctx2.paint()
    return scaled_surface


