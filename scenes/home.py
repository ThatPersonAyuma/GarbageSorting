import cairo
import math

def get_home():
    # Buat surface dan context
    width, height = 1225, 689
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)
    ctx.set_source_rgb(0.53, 0.81, 0.92)
    ctx.paint()

    # Warna-warna
    biru_muda = (0.53, 0.81, 0.92)
    biru_tua = (0.2, 0.4, 0.6)
    putih = (1.0, 1.0, 1.0)
    kuning = (1.0, 1.0, 0.0)
    putih = (1.0, 1.0, 1.0)
    hijau = (0.2, 0.6, 0.2)
    hijau_tua = (0.1, 0.3, 0.5)
    abu_abu = (0.5, 0.5, 0.5)

    #==============================
    #    latar belakang Home
    #==============================

    #kotak rumput
    ctx.set_source_rgb(*hijau)
    ctx.rectangle(0, 400, 1225, 289)
    ctx.fill()

    # arc matahari
    ctx.set_source_rgb(*kuning)
    ctx.arc(1150, 70, 50, 0, 2 * math.pi)  # Matahari
    ctx.fill()

    # awan 1
    ctx.set_source_rgb(*putih)
    ctx.arc(300, 90, 30, 0, 2 * math.pi)
    ctx.arc(330, 80, 40, 0, 2 * math.pi)
    ctx.arc(370, 90, 30, 0, 2 * math.pi)
    ctx.arc(340, 100, 35, 0, 2 * math.pi)
    ctx.fill()

    # awan 2
    ctx.set_source_rgb(*putih)
    ctx.arc(500, 90, 25, 0, 2 * math.pi)
    ctx.arc(530, 70, 35, 0, 2 * math.pi)
    ctx.arc(570, 90, 25, 0, 2 * math.pi)
    ctx.arc(540, 100, 30, 0, 2 * math.pi)
    ctx.fill()

    # angin 
    ctx.set_source_rgb(*putih)
    ctx.move_to(100, 100)
    ctx.curve_to(150, 80, 200, 120, 250, 100)
    ctx.set_line_width(5)
    ctx.stroke()

    # angin 2
    ctx.set_source_rgb(*putih)
    ctx.move_to(100, 80)
    ctx.curve_to(150, 50, 150, 100, 250, 80)
    ctx.set_line_width(5)
    ctx.stroke()

    # Angin 3
    ctx.set_source_rgb(*putih)
    ctx.move_to(100, 60)
    ctx.curve_to(150, 30, 120, 80, 250, 60)
    ctx.set_line_width(5)
    ctx.stroke()

    # pabrik kelolah sampah
    ctx.set_source_rgb(*abu_abu)
    ctx.rectangle(800, 300, 300, 150)  # Bangunan pabrik
    ctx.fill()

    #pintu pabrik
    ctx.set_source_rgb(0.4, 0.2, 0.1)
    ctx.rectangle(820, 390, 40, 60)  # Pintu pabrik
    ctx.fill()

    # garasi pabrik
    ctx.set_source_rgb(0.3, 0.3, 0.3)
    ctx.rectangle(880, 340, 200, 110)  # Garasi pabrik
    ctx.fill()

    # garis garis garasi
    ctx.set_source_rgb(0.2, 0.2, 0.2)
    ctx.set_line_width(5)
    for i in range(345, 450, 15):
        ctx.move_to(880, i)
        ctx.line_to(1080, i)
        ctx.stroke()

    # pagar samping pabrik
    ctx.set_source_rgb(0.4, 0.2, 0.1)
    for i in range(600, 800, 40):
        ctx.rectangle(i, 400, 10, 40)  # Pagar samping pabrik
        ctx.fill()

    # garis pagar samping pabrik
    ctx.set_source_rgb(0.55, 0.27, 0.07)
    ctx.set_line_width(5)
    for j in range(410, 440, 15):
        ctx.move_to(600, j)
        ctx.line_to(800, j)
        ctx.stroke()

    # button  Start
    ctx.set_source_rgb(*biru_tua)
    ctx.rectangle(450, 320, 350, 90)  # Tombol Start
    ctx.fill()

    #button exit
    ctx.set_source_rgb(*biru_tua)
    ctx.rectangle(450, 480, 350, 90)  # Tombol Exit
    ctx.fill()

    # Game Name Tittle shadow
    ctx.set_source_rgb(0.2, 0.2, 0.2)
    ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(90)
    ctx.move_to(325, 205)
    ctx.show_text("Trash to Tiles")

    # Game Name Tittle
    ctx.set_source_rgb(1, 1, 1)
    ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(90)
    ctx.move_to(320, 200)
    ctx.show_text("Trash to Tiles")



    # Simpan
    return surface
