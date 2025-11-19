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
Biru_Muda = (0.53, 0.81, 0.92)
Biru_Muda2 = (0.4, 0.6, 0.8)
Biru_Tua = (0.2, 0.4, 0.6)
Biru_Tua2 = (0.1, 0.3, 0.5)
Kuning = (1.0, 1.0, 0.0)
Coklat_tua = (0.4, 0.2, 0.1)
Hijau = (0.2, 0.6, 0.2)
Hijau2 = (0.3, 0.7, 0.3)

#==============================
#    latar belakang outdoor
#==============================

#kotak rumput
ctx.set_source_rgb(*Hijau2)
ctx.rectangle(0, 400, 1225, 289)
ctx.fill()  

#kotak langit
ctx.set_source_rgb(*Biru_Muda)
ctx.rectangle(0, 0, 1225, 400)
ctx.fill()

#matahari
ctx.set_source_rgb(*Kuning)
ctx.arc(1150, 70, 50, 0, 2 * math.pi)  # Matahari
ctx.fill()

# awan putih
ctx.set_source_rgb(1, 1, 1) 
ctx.arc(300, 90, 30, 0, 2 * math.pi)
ctx.arc(330, 80, 40, 0, 2 * math.pi)
ctx.arc(370, 90, 30, 0, 2 * math.pi)
ctx.arc(340, 100, 35, 0, 2 * math.pi)
ctx.fill()

# awan putih2
ctx.set_source_rgb(1, 1, 1) 
ctx.arc(500, 90, 25, 0, 2 * math.pi)
ctx.arc(530, 70, 35, 0, 2 * math.pi)
ctx.arc(570, 90, 25, 0, 2 * math.pi)
ctx.arc(540, 100, 30, 0, 2 * math.pi)
ctx.fill()

#awan putih3
ctx.set_source_rgb(1, 1, 1)
ctx.arc(800, 120, 20, 0, 2 * math.pi)
ctx.arc(825, 100, 30, 0, 2 * math.pi)
ctx.arc(860, 120, 20, 0, 2 * math.pi)
ctx.arc(835, 130, 25, 0, 2 * math.pi)
ctx.fill()

# loop pagar kayu
ctx.set_source_rgb(*Coklat_tua)
for i in range(2, 1225, 40):
    ctx.rectangle(i, 300, 20, 120)  # Pagar kayu
    ctx.fill()

# garis pagar kayu
ctx.set_source_rgb(0.55, 0.27, 0.07)
ctx.set_line_width(10)
for j in range(320, 400, 40):
    ctx.move_to(0, j)
    ctx.line_to(1225, j)
    ctx.stroke()


#==============================

# save gambar
surface.write_to_png("outdoor.png")