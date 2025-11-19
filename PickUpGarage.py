import cairo
import math

# Buat surface dan context
width, height = 1225, 689
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
ctx = cairo.Context(surface)

# Background putih
ctx.set_source_rgb(1, 1, 1)
ctx.paint()

# Warna-warna
gray_light = (0.75, 0.75, 0.75)
gray_medium = (0.5, 0.5, 0.5)
gray_dark = (0.4, 0.4, 0.4)
gray_dark_sha = (0.3, 0.3, 0.3)
wood_color = (0.8, 0.6, 0.3)

#==============================
#   dinding sisi ruang mesin
#==============================

# Dinding belakang (area terang atas)
ctx.set_source_rgb(*gray_light)
ctx.rectangle(53, 0, 1119, 268)
ctx.fill()

# dinding belakang (area terang sisi kiri)
ctx.set_source_rgb(*gray_medium)
ctx.rectangle(0, 0, 53, 268)
ctx.fill()

# dinding belakang (segitiga atas kiri bawah)
ctx.set_source_rgb(*gray_medium)
ctx.move_to(0, 440)   # Bawah kiri
ctx.line_to(0, 265)   # Bawah kanan
ctx.line_to(53, 260)   # Puncak atas
ctx.close_path()
ctx.fill()

# dinding belakang (area terang sisi kanan)
ctx.set_source_rgb(*gray_medium)
ctx.rectangle(1172, 0, 54, 268)
ctx.fill()

# dinding belakang terang (segitiga atas kanan atas)
ctx.set_source_rgb(*gray_medium)
ctx.move_to(1172, 260)   # Bawah kiri
ctx.line_to(1231, 440)   # Bawah kanan
ctx.line_to(1231, 260)   # Puncak atas
ctx.close_path()
ctx.fill()

# Dinding belakang (area gelap bawah)
ctx.set_source_rgb(*gray_dark)
ctx.rectangle(53, 260, 1119, 306)
ctx.fill()

# Dinding belakang (area gelap sisi kiri)
ctx.set_source_rgb(*gray_dark_sha)
ctx.rectangle(0, 440, 53, 260)
ctx.fill()

# dinding belakang (segitiga atas kiri atas)
ctx.set_source_rgb(*gray_dark_sha)
ctx.move_to(0, 440)   # Bawah kiri
ctx.line_to(53, 440)   # Bawah kanan
ctx.line_to(53, 260)   # Puncak atas
ctx.close_path()
ctx.fill()

# dinding belakang (segitiga atas kiri bawah)
ctx.set_source_rgb(*gray_dark_sha)
ctx.move_to(0, 725)   # Bawah kiri
ctx.line_to(0, 505)   # Bawah kanan
ctx.line_to(54, 505)   # Puncak atas
ctx.close_path()
ctx.fill()

# Dinding belakang (area gelap sisi kanan)
ctx.set_source_rgb(*gray_dark_sha)
ctx.rectangle(1172, 420, 54, 309)
ctx.fill()

# dinding belakang (segitiga atas kanan atas)
ctx.set_source_rgb(*gray_dark_sha)
ctx.move_to(1172, 440)   # Bawah kiri
ctx.line_to(1172, 260)   # Bawah kanan
ctx.line_to(1231, 440)   # Puncak atas
ctx.close_path()
ctx.fill()

#===================================
# pintu garasi pick up mobil sampah
#===================================

# lubang pintu garasi (area atas lantai)
ctx.set_source_rgb(1, 1 , 1)
ctx.rectangle(150, 100, 600, 410)
ctx.fill()

#==============================
# gambar luar ruang mesin
#==============================

# langit biru
ctx.set_source_rgb(0.53, 0.81, 0.92)
ctx.rectangle(155, 105, 600, 270)
ctx.fill()

# awan putih
ctx.set_source_rgb(1, 1, 1) 
ctx.arc(300, 150, 30, 0, 2 * math.pi)
ctx.arc(330, 150, 40, 0, 2 * math.pi)
ctx.arc(370, 150, 30, 0, 2 * math.pi)
ctx.arc(340, 130, 35, 0, 2 * math.pi)
ctx.fill()

# awan putih2
ctx.set_source_rgb(1, 1, 1)
ctx.arc(500, 200, 25, 0, 2 * math.pi)
ctx.arc(530, 200, 35, 0, 2 * math.pi)
ctx.arc(570, 200, 25, 0, 2 * math.pi)
ctx.arc(540, 180, 30, 0, 2 * math.pi)
ctx.fill()

#kotak rumput
ctx.set_source_rgb(0.3, 0.7, 0.3)
ctx.rectangle(155, 375, 600, 140)
ctx.fill()

#loop rumput
ctx.set_source_rgb(0, 0.5, 0)
for i in range(12):
    x = 160 + i * 50
    ctx.move_to(x, 505)
    ctx.line_to(x + 5, 485)
    ctx.line_to(x + 15, 505)
    ctx.fill()

# loop rumput2
ctx.set_source_rgb(0, 0.6, 0)
for i in range(12):
    x = 185 + i * 50
    ctx.move_to(x, 475)
    ctx.line_to(x + 5, 490)
    ctx.line_to(x + 15, 490)
    ctx.fill()

#==============================

# kotak garasi atas
ctx.set_source_rgb(0.5, 0.5, 0.5)
ctx.rectangle(150, 30, 600, 80)
ctx.fill()

# bingkai pintu garasi atas (kiri)
ctx.set_source_rgb(0.4, 0.4, 0.4)
ctx.rectangle(140, 20, 15, 400)
ctx.fill()

# bingkai pintu garasi atas (kanan)
ctx.set_source_rgb(0.4, 0.4, 0.4)
ctx.rectangle(745, 20, 15, 400)
ctx.fill()

# bingkai pintu garasi (atas)
ctx.set_source_rgb(0.4, 0.4, 0.4)
ctx.rectangle(140, 20, 620, 15)
ctx.fill()

# garis-garis pintu garasi
ctx.set_source_rgb(0.9, 0.9, 0.9)
for i in range(1, 4):
    y = 100 + i * 50
    ctx.move_to(150, 35*i)
    ctx.line_to(750, 35*i)
    ctx.set_line_width(3)
    ctx.stroke()

# bingkai pintu garasi (kiri)
ctx.set_source_rgb(0.3, 0.3, 0.3)
ctx.rectangle(140, 110, 15, 400)
ctx.fill()

# bingkai pintu garasi (kanan)
ctx.set_source_rgb(0.3, 0.3, 0.3)
ctx.rectangle(745, 110, 15, 400)
ctx.fill()

# pintu kayu garasi
ctx.set_source_rgb(*wood_color)
ctx.rectangle(860, 205, 240, 300)
ctx.fill()

# bingkai pintu kayu garasi
ctx.set_source_rgb(0.4, 0.2, 0.1)
ctx.rectangle(855, 200, 250, 10)  # atas
ctx.fill()
ctx.rectangle(855, 200, 10, 310)  # kiri
ctx.fill()
ctx.rectangle(1095, 200, 10, 310)  # kanan
ctx.fill()
ctx.rectangle(855, 500, 250, 10)  # bawah
ctx.fill()

# kotak-kotak pintu kayu garasi
ctx.set_source_rgb(0.6, 0.4, 0.2)
for i in range(2):
    for j in range(2):
        x = 875 + i * 115
        y = 220 + j * 150
        ctx.rectangle(x, y, 95, 120)
        ctx.fill()

# gagang pintu kayu garasi
ctx.set_source_rgb(0.2, 0.2, 0)
ctx.arc(1070, 355, 14, 0, 2 * math.pi)
ctx.fill()

# gagang pintu kayu garasi
ctx.set_source_rgb(1, 1, 0)
ctx.arc(1069, 354, 13, 0, 2 * math.pi)
ctx.fill()

#==============================
#     lantai ruang mesin
#==============================

# Lantai bawah (terang)
ctx.set_source_rgb(*gray_medium)
ctx.move_to(54, 505)
ctx.line_to(1172, 505)
ctx.line_to(1225, 689)
ctx.line_to(0, 689)
ctx.fill()

# Simpan
surface.write_to_png("PickUpGarage.png")
