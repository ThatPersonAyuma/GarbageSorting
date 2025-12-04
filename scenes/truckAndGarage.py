from pathlib import Path
import cairo
import math

# ==========================================
# FUNGSI MENGGAMBAR TRUK
# ==========================================
def draw_truck(ctx):
    # Simpan state context
    ctx.save()
    
    # --- Penyesuaian Posisi dan Ukuran Truk (Updated) ---
    # Scale: 0.75 (Besar)
    # Translate: x=-60 (Lebih kiri), y=60 (Pas di lantai)
    ctx.translate(-60, 60)
    ctx.scale(0.75, 0.75)
    # ------------------------------------------

    # Warna-warna Truk
    Hijau = (0.2, 0.6, 0.2)
    Hijau2 = (0.15, 0.5, 0.15)
    Hijau_tua = (0.1, 0.4, 0.1)
    Hijau_tua2 = (0.05, 0.3, 0.05)
    Hijau_muda = (0.4, 0.6, 0.4)
    Kuning = (1.0, 1.0, 0.0)
    Merah = (0.8, 0.1, 0.1)
    Abu_Tua = (0.3, 0.3, 0.3)
    Abu_Tua2 = (0.4, 0.4, 0.4)
    Abu_Tua3 = (0.2, 0.2, 0.2)
    Abu_Muda = (0.7, 0.7, 0.7)

    # roda belakang truk sisi kanan2
    ctx.set_source_rgb(*Abu_Tua3)
    ctx.arc(920, 520, 80, 60, 50 * math.pi)
    ctx.fill()

    # roda belakang truk sisi kanan
    ctx.set_source_rgb(*Abu_Tua)
    ctx.arc(880, 520, 80, 60, 50 * math.pi)
    ctx.fill()

    # vleg roda belakang truk
    ctx.set_source_rgb(*Abu_Muda)
    ctx.arc(880, 520, 50, 50, 50 * math.pi)
    ctx.fill()

    # kotak bawah truk
    ctx.set_source_rgb(0.3, 0.3, 0.3)
    ctx.rectangle(200, 450, 390, 20)
    ctx.fill()

    # kotak bawah truk
    ctx.set_source_rgb(0, 0, 0)
    ctx.rectangle(700, 550, 390, 20)
    ctx.fill()

    # kotak bawah truk2
    ctx.set_source_rgb(0.6, 0.6, 0.6)
    ctx.rectangle(870, 550, 160, 25)
    ctx.fill()

    # kotak bawah truk3
    ctx.set_source_rgb(0.8, 0.8, 0.8)
    ctx.rectangle(880, 555, 140, 15)
    ctx.fill()

    # truck body
    ctx.set_source_rgb(*Hijau2)
    ctx.rectangle(200, 170, 800, 280)
    ctx.fill()

    # roda belakang truk gradasi2
    ctx.set_source_rgb(*Abu_Tua3)
    ctx.arc(660, 520, 80, 60, 50 * math.pi)
    ctx.fill()

    # roda belakang truk gradasi1
    ctx.set_source_rgb(*Abu_Tua)
    ctx.arc(630, 520, 80, 60, 50 * math.pi)
    ctx.fill()

    # roda belakang truk (kotak)
    ctx.set_source_rgb(*Abu_Tua)
    ctx.rectangle(600, 505, 30, 95)
    ctx.fill()

    #roda belakang truk
    ctx.set_source_rgb(*Abu_Tua2)
    ctx.arc(600, 520, 80, 50, 50 * math.pi)
    ctx.fill()

    # vleg roda belakang truk
    ctx.set_source_rgb(*Abu_Muda)
    ctx.arc(600, 520, 50, 50, 50 * math.pi)
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
    ctx.move_to(1000, 170)
    ctx.line_to(1000, 450)
    ctx.line_to(1100, 450)
    ctx.close_path()
    ctx.fill()

    # trapesium bawah truk
    ctx.set_source_rgb(*Hijau2)
    ctx.move_to(720, 450)
    ctx.line_to(1100, 450)
    ctx.line_to(1100, 550)
    ctx.line_to(750, 550)
    ctx.close_path()
    ctx.fill()

    # trapesium gradasi truk
    ctx.set_source_rgb(*Hijau)
    ctx.move_to(720, 450)
    ctx.line_to(805, 480)
    ctx.line_to(805, 550)
    ctx.line_to(730, 550)
    ctx.close_path()
    ctx.fill()

    # trapesium gradasi truk2
    ctx.set_source_rgb(*Hijau)
    ctx.move_to(580, 170)
    ctx.line_to(710, 170)
    ctx.line_to(805, 480)
    ctx.line_to(730, 550)
    ctx.close_path()
    ctx.fill()

    # kotak gradasi truk
    ctx.set_source_rgb(*Hijau)
    ctx.rectangle(280, 170, 430, 280)
    ctx.fill()

    # trapesium gradasi truk3
    ctx.set_source_rgb(*Hijau_tua)
    ctx.move_to(600, 190)
    ctx.line_to(690, 190)
    ctx.line_to(750, 395)
    ctx.line_to(600, 395)
    ctx.close_path()
    ctx.fill()

    # kotak gradasi truk4
    ctx.set_source_rgb(*Hijau_tua)
    ctx.rectangle(460, 190, 110, 205)
    ctx.fill()

    # kotak gradasi truk5
    ctx.set_source_rgb(*Hijau_tua)
    ctx.rectangle(320, 190, 110, 205)
    ctx.fill()


    # trapesium atas truk
    ctx.set_source_rgb(*Hijau_muda)
    ctx.move_to(820, 450)
    ctx.line_to(1080, 450)
    ctx.line_to(990, 200)
    ctx.line_to(740, 200)
    ctx.close_path()
    ctx.fill()

    # trapesium pintu truk
    ctx.set_source_rgb(*Hijau_tua)
    ctx.move_to(755, 250)
    ctx.line_to(960, 250)
    ctx.line_to(990, 200)
    ctx.line_to(740, 200)
    ctx.close_path()
    ctx.fill()

    # trapesium pintu truk2
    ctx.set_source_rgb(*Hijau)
    ctx.move_to(1030, 450)
    ctx.line_to(1080, 450)
    ctx.line_to(990, 200)
    ctx.line_to(960, 250)
    ctx.close_path()
    ctx.fill()

    # trapesium-trapesium kecil di badan truk
    ctx.set_source_rgb(*Hijau_tua2)
    for i in range(2):
        x_offset = 755 + i * 125
        ctx.move_to(x_offset, 250)
        ctx.line_to(x_offset + 80, 250)
        ctx.line_to(x_offset + 102, 310)
        ctx.line_to(x_offset + 20 , 310)
        ctx.close_path()
        ctx.fill()

    ctx.set_source_rgb(*Hijau_tua2)
    for i in range(2):
        x_offset = 353 + i * 128
        ctx.move_to(x_offset + 505, 320)
        ctx.line_to(x_offset + 425, 320)
        ctx.line_to(x_offset + 445, 380)
        ctx.line_to(x_offset + 525, 380)
        ctx.close_path()
        ctx.fill()

    ctx.set_source_rgb(*Hijau_tua2)
    for i in range(2):
        x_offset = 480 + i * 130
        ctx.move_to(x_offset + 400, 390)
        ctx.line_to(x_offset + 320, 390)
        ctx.line_to(x_offset + 340, 450)
        ctx.line_to(x_offset + 420, 450)
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

    # Kembalikan state context ke semula
    ctx.restore() 


# ==========================================
# FUNGSI UTAMA (PickUpGarage.py + Truk)
# ==========================================

def create() -> cairo.ImageSurface:
    # Buat surface dan context
    width, height = 1225, 689
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)

    # Background putih
    ctx.set_source_rgb(1, 1, 1)
    ctx.paint()

    # Warna-warna Garasi
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

    # ======================================================
    # MEMASUKKAN TRUK DISINI DENGAN CLIPPING
    # ======================================================
    
    # 1. Simpan state sebelum clipping
    ctx.save()

    # 2. Definisikan area yang boleh digambar (lubang pintu garasi)
    #    Koordinatnya sama dengan 'lubang pintu garasi' (x=150, y=100, w=600, h=410)
    ctx.rectangle(150, 100, 600, 410)
    
    # 3. Aktifkan clipping. Gambar selanjutnya HANYA muncul di dalam kotak di atas.
    ctx.clip()

    # 4. Gambar truk (yang sebagian akan terpotong oleh clip)
    draw_truck(ctx)

    # 5. Kembalikan state (menghapus clipping) agar gambar selanjutnya normal
    ctx.restore()

    # ======================================================

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

    # Poster
    try:
        ASSET_DIR = Path(__file__).parent.parent / "assets"
        if (ASSET_DIR / "jkwgbrn.png").exists():
            img = cairo.ImageSurface.create_from_png(str(ASSET_DIR / "jkwgbrn.png"))
            ctx.translate(855+((120/img.get_width())*img.get_width())//2, 200-(90/img.get_height())*img.get_height())
            ctx.scale(120/img.get_width(), 90/img.get_height())
            ctx.set_source_surface(img, 0, 0)
            ctx.paint()
    except Exception as e:
        pass
    
    # Simpan
    return surface

if __name__ == "__main__":
    surface = create()
    surface.write_to_png("GarageWithTruck_Clipped.png")