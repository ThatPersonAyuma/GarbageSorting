import cairo
import math

# Buat surface dan context
width, height = 1225, 689
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
ctx = cairo.Context(surface)

# hex rgb to decimal rgb
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) / 255.0 for i in (0, 2, 4))

# Background putih
ctx.set_source_rgb(1, 1, 1)
ctx.paint()

# Warna-warna
Hijau = (0.2, 0.6, 0.2)
Hijau2 = (0.15, 0.5, 0.15)
Hijau_tua = (0.1, 0.4, 0.1)
Hijau_tua2 = (0.05, 0.3, 0.05)
Hijau_muda = (0.4, 0.6, 0.4)
Hijau_muda2 = (0.6, 0.8, 0.6)

# truck body
ctx.set_source_rgb(*Hijau2)  # Hijau
ctx.rectangle(400, 170, 600, 280)  # Badan truk
ctx.fill()

# segitiga samping truk
ctx.set_source_rgb(*Hijau2)
ctx.move_to(1000, 170)   # Bawah kiri
ctx.line_to(1000, 450)   # Bawah kanan
ctx.line_to(1100, 450)   # Puncak atas
ctx.close_path()
ctx.fill()

# trapesium bawah truk
ctx.set_source_rgb(*Hijau2)
ctx.move_to(720, 450)   # Bawah kiri
ctx.line_to(1100, 450)   # Bawah kanan
ctx.line_to(1100, 550)   # Puncak atas
ctx.line_to(750, 550)   # Puncak atas
ctx.close_path()
ctx.fill()

# trapesium atas truk
ctx.set_source_rgb(*Hijau_muda)
ctx.move_to(820, 450)   # Bawah kiri
ctx.line_to(1080, 450)   # Bawah kanan
ctx.line_to(990, 200)   # Puncak atas
ctx.line_to(740, 200)   # Puncak atas
ctx.close_path()
ctx.fill()

# trapesium pintu truk
ctx.set_source_rgb(*Hijau_tua)
ctx.move_to(755, 250)   # Bawah kiri
ctx.line_to(960, 250)   # Bawah kanan
ctx.line_to(990, 200)   # Puncak atas
ctx.line_to(740, 200)   # Puncak atas
ctx.close_path()
ctx.fill()

# trapesium pintu truk2
ctx.set_source_rgb(*Hijau)
ctx.move_to(1030, 450)   # Bawah kiri
ctx.line_to(1080, 450)   # Bawah kanan
ctx.line_to(990, 200)   # Puncak atas
ctx.line_to(960, 250)   # Puncak atas
ctx.close_path()
ctx.fill()

# trapesium-trapesium kecil di badan truk
ctx.set_source_rgb(*Hijau_tua2)
i in range(5):
    x_offset = 410 + i * 115
    ctx.move_to(x_offset, 200)   # Bawah kiri
    ctx.line_to(x_offset + 80, 200)   # Bawah kanan
    ctx.line_to(x_offset + 80, 300)   # Puncak atas
    ctx.line_to(x_offset, 300)   # Puncak atas
    ctx.close_path()
    ctx.fill()

# #==============================
# #   dinding sisi ruang mesin
# #==============================

# # Dinding belakang (area terang atas)
# ctx.set_source_rgb(*gray_light)
# ctx.rectangle(53, 0, 1119, 268)
# ctx.fill()

# # dinding belakang (area terang sisi kiri)
# ctx.set_source_rgb(*gray_medium)
# ctx.rectangle(0, 0, 53, 268)
# ctx.fill()

# # dinding belakang (segitiga atas kiri bawah)
# ctx.set_source_rgb(*gray_medium)
# ctx.move_to(0, 440)   # Bawah kiri
# ctx.line_to(0, 265)   # Bawah kanan
# ctx.line_to(53, 260)   # Puncak atas
# ctx.close_path()
# ctx.fill()

# # dinding belakang (area terang sisi kanan)
# ctx.set_source_rgb(*gray_medium)
# ctx.rectangle(1172, 0, 54, 268)
# ctx.fill()

# # dinding belakang terang (segitiga atas kanan atas)
# ctx.set_source_rgb(*gray_medium)
# ctx.move_to(1172, 260)   # Bawah kiri
# ctx.line_to(1231, 440)   # Bawah kanan
# ctx.line_to(1231, 260)   # Puncak atas
# ctx.close_path()
# ctx.fill()

# # Dinding belakang (area gelap bawah)
# ctx.set_source_rgb(*gray_dark)
# ctx.rectangle(53, 260, 1119, 306)
# ctx.fill()

# # Dinding belakang (area gelap sisi kiri)
# ctx.set_source_rgb(*gray_dark_sha)
# ctx.rectangle(0, 440, 53, 260)
# ctx.fill()

# # dinding belakang (segitiga atas kiri atas)
# ctx.set_source_rgb(*gray_dark_sha)
# ctx.move_to(0, 440)   # Bawah kiri
# ctx.line_to(53, 440)   # Bawah kanan
# ctx.line_to(53, 260)   # Puncak atas
# ctx.close_path()
# ctx.fill()

# # dinding belakang (segitiga atas kiri bawah)
# ctx.set_source_rgb(*gray_dark_sha)
# ctx.move_to(0, 725)   # Bawah kiri
# ctx.line_to(0, 505)   # Bawah kanan
# ctx.line_to(54, 505)   # Puncak atas
# ctx.close_path()
# ctx.fill()

# # Dinding belakang (area gelap sisi kanan)
# ctx.set_source_rgb(*gray_dark_sha)
# ctx.rectangle(1172, 420, 54, 309)
# ctx.fill()

# # dinding belakang (segitiga atas kanan atas)
# ctx.set_source_rgb(*gray_dark_sha)
# ctx.move_to(1172, 440)   # Bawah kiri
# ctx.line_to(1172, 260)   # Bawah kanan
# ctx.line_to(1231, 440)   # Puncak atas
# ctx.close_path()
# ctx.fill()


# #==============================
# #     lantai ruang mesin
# #==============================

# # Lantai bawah (terang)
# ctx.set_source_rgb(*gray_medium)
# ctx.move_to(54, 505)
# ctx.line_to(1172, 505)
# ctx.line_to(1225, 689)
# ctx.line_to(0, 689)
# ctx.fill()

# # Radiator
# radiator_x = 77
# radiator_y = 24
# radiator_width = 155
# radiator_height = 90

# # Frame radiator
# ctx.set_source_rgb(0, 0, 0)
# ctx.set_line_width(3)
# ctx.rectangle(radiator_x, radiator_y, radiator_width, radiator_height)
# ctx.stroke()

# # Garis horizontal atas radiator
# ctx.set_line_width(2)
# ctx.move_to(radiator_x, radiator_y + 15)
# ctx.line_to(radiator_x + radiator_width, radiator_y + 15)
# ctx.stroke()

# # Panel vertikal radiator
# num_panels = 6
# panel_width = radiator_width / num_panels

# for i in range(num_panels):
#     x = radiator_x + i * panel_width + panel_width * 0.2
#     panel_w = panel_width * 0.6
    
#     # Panel utama
#     ctx.rectangle(x, radiator_y + 18, panel_w, radiator_height - 20)
#     ctx.stroke()

# # Meja kayu di pojok kiri bawah
# ctx.set_source_rgb(*wood_color)

# # Bentuk trapesium meja (perspektif)
# ctx.move_to(40, 580)
# ctx.line_to(375, 580)
# ctx.line_to(360, 700)
# ctx.line_to(0, 700)
# ctx.close_path()
# ctx.fill()


# Simpan
surface.write_to_png("TrashTruck.png")