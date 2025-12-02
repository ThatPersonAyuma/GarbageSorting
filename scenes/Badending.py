import cairo

# Buat surface dan context
width, height = 1225, 689
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
ctx = cairo.Context(surface)

# Background putih
ctx.set_source_rgb(0, 0, 0)
ctx.paint()

# text warna putih di tengah
ctx.set_source_rgb(1, 1, 1)
ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
ctx.set_font_size(50)
text = "Yah kalah, coba lebih cepat!"
(x, y, width, height) = (width / 2 - 350, height / 2 - 25, 300, 50)
ctx.move_to(x, y + height)
ctx.show_text(text)
ctx.fill()

# simpan gambar
surface.write_to_png("badEnding.png")