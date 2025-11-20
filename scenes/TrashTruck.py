import cairo
import math

def create()->cairo.ImageSurface:
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
    Kuning = (1.0, 1.0, 0.0)
    Merah = (0.8, 0.1, 0.1)
    Abu_Tua = (0.3, 0.3, 0.3)
    Abu_Tua2 = (0.4, 0.4, 0.4)
    Abu_Tua3 = (0.2, 0.2, 0.2)
    Abu_Muda = (0.7, 0.7, 0.7)



    # roda belakang truk sisi kanan2
    ctx.set_source_rgb(*Abu_Tua3)
    ctx.arc(920, 520, 80, 60, 50 * math.pi)  # Roda belakang
    ctx.fill()

    # roda belakang truk sisi kanan
    ctx.set_source_rgb(*Abu_Tua)
    ctx.arc(880, 520, 80, 60, 50 * math.pi)  # Roda belakang
    ctx.fill()

    # vleg roda belakang truk
    ctx.set_source_rgb(*Abu_Muda)
    ctx.arc(880, 520, 50, 50, 50 * math.pi)  # Roda belakang
    ctx.fill()

    # kotak bawah truk
    ctx.set_source_rgb(0.3, 0.3, 0.3)
    ctx.rectangle(200, 450, 390, 20)  # Badan truk
    ctx.fill()

    # kotak bawah truk
    ctx.set_source_rgb(0, 0, 0)
    ctx.rectangle(700, 550, 390, 20)  # Badan truk
    ctx.fill()

    # kotak bawah truk2
    ctx.set_source_rgb(0.6, 0.6, 0.6)
    ctx.rectangle(870, 550, 160, 25)  # Badan truk
    ctx.fill()

    # kotak bawah truk3
    ctx.set_source_rgb(0.8, 0.8, 0.8)
    ctx.rectangle(880, 555, 140, 15)  # Badan truk
    ctx.fill()

    # truck body
    ctx.set_source_rgb(*Hijau2)  # Hijau
    ctx.rectangle(200, 170, 800, 280)  # Badan truk
    ctx.fill()

    # roda belakang truk gradasi2
    ctx.set_source_rgb(*Abu_Tua3)
    ctx.arc(660, 520, 80, 60, 50 * math.pi)  # Roda belakang
    ctx.fill()

    # roda belakang truk gradasi1
    ctx.set_source_rgb(*Abu_Tua)
    ctx.arc(630, 520, 80, 60, 50 * math.pi)  # Roda belakang
    ctx.fill()

    # roda belakang truk (kotak)
    ctx.set_source_rgb(*Abu_Tua)
    ctx.rectangle(600, 505, 30, 95)  # Roda belakang
    ctx.fill()

    #roda belakang truk
    ctx.set_source_rgb(*Abu_Tua2)
    ctx.arc(600, 520, 80, 50, 50 * math.pi)  # Roda belakang
    ctx.fill()

    # vleg roda belakang truk
    ctx.set_source_rgb(*Abu_Muda)
    ctx.arc(600, 520, 50, 50, 50 * math.pi)  # Roda belakang
    ctx.fill()

    # garis dalam vleg roda belakang truk
    ctx.set_source_rgb(1, 1, 1)
    for i in range(8):
        angle = i * (math.pi / 4)
        x_start = 600 + 0 * math.cos(angle)
        y_start = 520 + 0 * math.sin(angle)
        x_end = 600 + 50 * math.cos(angle)
        y_end = 520 + 50 * math.sin(angle)
        ctx.set_line_width(2)
        ctx.move_to(x_start, y_start)
        ctx.line_to(x_end, y_end)
        ctx.stroke()


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

    # trapesium gradasi truk
    ctx.set_source_rgb(*Hijau)
    ctx.move_to(720, 450)   # Bawah kiri
    ctx.line_to(805, 480)   # Bawah kanan
    ctx.line_to(805, 550)   # Puncak atas kanan
    ctx.line_to(730, 550)   # Puncak atas kiri
    ctx.close_path()
    ctx.fill()

    # trapesium gradasi truk2
    ctx.set_source_rgb(*Hijau)
    ctx.move_to(580, 170)   # Bawah kiri
    ctx.line_to(710, 170)   # Bawah kanan
    ctx.line_to(805, 480)   # Puncak atas kanan
    ctx.line_to(730, 550)   # Puncak atas kiri
    ctx.close_path()
    ctx.fill()

    # kotak gradasi truk
    ctx.set_source_rgb(*Hijau)
    ctx.rectangle(280, 170, 430, 280)  # Badan truk
    ctx.fill()

    # trapesium gradasi truk3
    ctx.set_source_rgb(*Hijau_tua)
    ctx.move_to(600, 190)   # Bawah kiri
    ctx.line_to(690, 190)   # Bawah kanan
    ctx.line_to(750, 395)   # Puncak atas kanan
    ctx.line_to(600, 395)   # Puncak atas kiri
    ctx.close_path()
    ctx.fill()

    # kotak gradasi truk4
    ctx.set_source_rgb(*Hijau_tua)
    ctx.rectangle(460, 190, 110, 205)  # Badan truk
    ctx.fill()

    # kotak gradasi truk5
    ctx.set_source_rgb(*Hijau_tua)
    ctx.rectangle(320, 190, 110, 205)  # Badan truk
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
    for i in range(2):
        x_offset = 755 + i * 125
        ctx.move_to(x_offset, 250)   # Bawah kiri
        ctx.line_to(x_offset + 80, 250)   # Bawah kanan
        ctx.line_to(x_offset + 102, 310)   # Puncak atas kanan
        ctx.line_to(x_offset + 20 , 310)   # Puncak atas kiri
        ctx.close_path()
        ctx.fill()

    ctx.set_source_rgb(*Hijau_tua2)
    for i in range(2):
        x_offset = 353 + i * 128
        ctx.move_to(x_offset + 505, 320)   # Bawah kiri
        ctx.line_to(x_offset + 425, 320)   # Bawah kanan
        ctx.line_to(x_offset + 445, 380)   # Puncak atas kiri
        ctx.line_to(x_offset + 525, 380)   # Puncak atas kanan
        ctx.close_path()
        ctx.fill()

    ctx.set_source_rgb(*Hijau_tua2)
    for i in range(2):
        x_offset = 480 + i * 130
        ctx.move_to(x_offset + 400, 390)   # Bawah kiri
        ctx.line_to(x_offset + 320, 390)   # Bawah kanan
        ctx.line_to(x_offset + 340, 450)   # Puncak atas kiri
        ctx.line_to(x_offset + 420, 450)   # Puncak atas kanan
        ctx.close_path()
        ctx.fill()

    # tiga kotak gradasi merah putih kesamping truk
    ctx.set_source_rgb(*Merah)
    for i in range(3):
        x_offset = 740 + i * 35
        ctx.rectangle(x_offset, 190, 20, 10)
        ctx.fill()

    ctx.set_source_rgb(1, 1, 1)
    for i in range(2):
        x_offset = 760 + i * 35
        ctx.rectangle(x_offset, 190, 15, 10)
        ctx.fill()

    ctx.set_source_rgb(*Merah)
    for i in range(3):
        x_offset = 900 + i * 35
        ctx.rectangle(x_offset, 190, 20, 10)
        ctx.fill()

    ctx.set_source_rgb(1, 1, 1)
    for i in range(2):
        x_offset = 920 + i * 35
        ctx.rectangle(x_offset, 190, 15, 10)
        ctx.fill()

    # kotak lampu truk kiri
    ctx.set_source_rgb(*Hijau_tua2)
    ctx.rectangle(825, 470, 60, 70)
    ctx.fill()

    # kotak lampu truk kiri (kuning)
    ctx.set_source_rgb(*Kuning)
    ctx.rectangle(835, 480, 40, 20)
    ctx.fill()

    # kotak lampu truk kiri (merah)
    ctx.set_source_rgb(*Merah)
    ctx.rectangle(835, 510, 40, 20)
    ctx.fill()

    # kotak lampu truk kanan
    ctx.set_source_rgb(*Hijau_tua2)
    ctx.rectangle(1025, 470, 60, 70)
    ctx.fill()

    # kotak lampu truk kanan (kuning)
    ctx.set_source_rgb(*Kuning)
    ctx.rectangle(1035, 480, 40, 20)
    ctx.fill()

    # kotak lampu truk kanan (merah)
    ctx.set_source_rgb(*Merah)
    ctx.rectangle(1035, 510, 40, 20)
    ctx.fill()

    # Kotak sebelah kotak lampu truk kiri
    ctx.set_source_rgb(*Hijau_tua2)
    ctx.rectangle(895, 460, 6, 125)
    ctx.fill()

    # garis untuk tangga truk belakang
    ctx.set_source_rgb(*Hijau_tua2)
    for i in range(8):
        y_offset = 460 + i * 15
        ctx.rectangle(890, y_offset, 115, 5)
        ctx.fill()

    # Kotak sebelah kotak lampu truk kanan
    ctx.set_source_rgb(*Hijau_tua2)
    ctx.rectangle(1005, 460, 6, 125)
    ctx.fill()

    # garis gradasi tangga truck belakang
    ctx.set_source_rgb(*Hijau_tua)
    for i in range(8):
        y_offset = 465 + i * 15
        ctx.rectangle(895, y_offset, 120, 5)
        ctx.fill()



    # Simpan
    return surface