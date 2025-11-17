import cairo

WIDTH, HEIGHT = 540, 300
BAR_WIDTH = 15

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

ctx.set_source_rgb(0, 0, 0)
ctx.paint()

ctx.set_source_rgb(1, 1, 1)

#>>> Section Plang Zebra Bawah <<<

# persegi panjang membentuk pola segitiga di ujung kiri bawah
ctx.rectangle(15, HEIGHT / 2, BAR_WIDTH, 100)
ctx.rectangle(30, HEIGHT / 2, BAR_WIDTH, 85)
ctx.rectangle(45, HEIGHT / 2, BAR_WIDTH, 70)
ctx.rectangle(60, HEIGHT / 2, BAR_WIDTH, 55)
ctx.rectangle(75, HEIGHT / 2, BAR_WIDTH, 40)
ctx.rectangle(90, HEIGHT / 2, BAR_WIDTH, 20)

# garis miring pixelised 1 (Bawah kiri)
ctx.rectangle(105, HEIGHT / 2 + 86, BAR_WIDTH, 14)
ctx.rectangle(120, HEIGHT / 2 + 70, BAR_WIDTH, 30)
ctx.rectangle(135, HEIGHT / 2 + 55, BAR_WIDTH, 45)
ctx.rectangle(150, HEIGHT / 2 + 40, BAR_WIDTH, 60)
ctx.rectangle(165, HEIGHT / 2 + 20, BAR_WIDTH, 80)
ctx.rectangle(180, HEIGHT / 2 , BAR_WIDTH, 100)
ctx.rectangle(195, HEIGHT / 2 , BAR_WIDTH, 85)
ctx.rectangle(210, HEIGHT / 2 , BAR_WIDTH, 70)
ctx.rectangle(225, HEIGHT / 2 , BAR_WIDTH, 55)
ctx.rectangle(240, HEIGHT / 2 , BAR_WIDTH, 40)
ctx.rectangle(255, HEIGHT / 2 , BAR_WIDTH, 20)

# garis miring pixelised 2 (Bawah kanan)
ctx.rectangle(270, HEIGHT / 2 + 86, BAR_WIDTH, 14)
ctx.rectangle(285, HEIGHT / 2 + 70, BAR_WIDTH, 30)
ctx.rectangle(300, HEIGHT / 2 + 55, BAR_WIDTH, 45)
ctx.rectangle(315, HEIGHT / 2 + 40, BAR_WIDTH, 60)
ctx.rectangle(330, HEIGHT / 2 + 20, BAR_WIDTH, 80)
ctx.rectangle(345, HEIGHT / 2 , BAR_WIDTH, 100)
ctx.rectangle(360, HEIGHT / 2 , BAR_WIDTH, 85)
ctx.rectangle(375, HEIGHT / 2 , BAR_WIDTH, 70)
ctx.rectangle(390, HEIGHT / 2 , BAR_WIDTH, 55)
ctx.rectangle(405, HEIGHT / 2 , BAR_WIDTH, 40)
ctx.rectangle(420, HEIGHT / 2 , BAR_WIDTH, 20)

# persegi panjang membentuk pola segitiga di ujung kanan bawah
ctx.rectangle(435, HEIGHT / 2 + 86, BAR_WIDTH, 14)
ctx.rectangle(450, HEIGHT / 2 + 70, BAR_WIDTH, 30)
ctx.rectangle(465, HEIGHT / 2 + 55, BAR_WIDTH, 45)
ctx.rectangle(480, HEIGHT / 2 + 40, BAR_WIDTH, 60)
ctx.rectangle(495, HEIGHT / 2 + 20, BAR_WIDTH, 80)
ctx.rectangle(510, HEIGHT / 2 , BAR_WIDTH, 100)


#>>> Section Plang Zebra Atas <<<

# persegi panjang membentuk pola segitiga di ujung kiri atas
ctx.rectangle(15, HEIGHT / 2 - 130, BAR_WIDTH, 100)
ctx.rectangle(30, HEIGHT / 2 - 130, BAR_WIDTH, 85)
ctx.rectangle(45, HEIGHT / 2 - 130, BAR_WIDTH, 70)
ctx.rectangle(60, HEIGHT / 2 - 130, BAR_WIDTH, 55)
ctx.rectangle(75, HEIGHT / 2 - 130, BAR_WIDTH, 40)
ctx.rectangle(90, HEIGHT / 2 - 130, BAR_WIDTH, 20)

# garis miring pixelised 1 (Atas kiri)
ctx.rectangle(105, HEIGHT / 2 - 44, BAR_WIDTH, 14)
ctx.rectangle(120, HEIGHT / 2 - 60, BAR_WIDTH, 30)
ctx.rectangle(135, HEIGHT / 2 - 75, BAR_WIDTH, 45)
ctx.rectangle(150, HEIGHT / 2 - 90, BAR_WIDTH, 60)
ctx.rectangle(165, HEIGHT / 2 - 110, BAR_WIDTH, 80)
ctx.rectangle(180, HEIGHT / 2 - 130, BAR_WIDTH, 100)
ctx.rectangle(195, HEIGHT / 2 - 130, BAR_WIDTH, 85)
ctx.rectangle(210, HEIGHT / 2 - 130, BAR_WIDTH, 70)
ctx.rectangle(225, HEIGHT / 2 - 130, BAR_WIDTH, 55)
ctx.rectangle(240, HEIGHT / 2 - 130, BAR_WIDTH, 40)
ctx.rectangle(255, HEIGHT / 2 - 130, BAR_WIDTH, 20)

# garis miring pixelised 2 (Atas kanan)
ctx.rectangle(270, HEIGHT / 2 - 44, BAR_WIDTH, 14)
ctx.rectangle(285, HEIGHT / 2 - 60, BAR_WIDTH, 30)
ctx.rectangle(300, HEIGHT / 2 - 75, BAR_WIDTH, 45)
ctx.rectangle(315, HEIGHT / 2 - 90, BAR_WIDTH, 60)
ctx.rectangle(330, HEIGHT / 2 - 110, BAR_WIDTH, 80)
ctx.rectangle(345, HEIGHT / 2 - 130, BAR_WIDTH, 100)
ctx.rectangle(360, HEIGHT / 2 - 130, BAR_WIDTH, 85)
ctx.rectangle(375, HEIGHT / 2 - 130, BAR_WIDTH, 70)
ctx.rectangle(390, HEIGHT / 2 - 130, BAR_WIDTH, 55)
ctx.rectangle(405, HEIGHT / 2 - 130, BAR_WIDTH, 40)
ctx.rectangle(420, HEIGHT / 2 - 130, BAR_WIDTH, 20)

# persegi panjang membentuk pola segitiga di ujung kanan atas
ctx.rectangle(435, HEIGHT / 2 - 44, BAR_WIDTH, 14)
ctx.rectangle(450, HEIGHT / 2 - 60, BAR_WIDTH, 30)
ctx.rectangle(465, HEIGHT / 2 - 75, BAR_WIDTH, 45)
ctx.rectangle(480, HEIGHT / 2 - 90, BAR_WIDTH, 60)
ctx.rectangle(495, HEIGHT / 2 - 110, BAR_WIDTH, 80)
ctx.rectangle(510, HEIGHT / 2 - 130, BAR_WIDTH, 100)

ctx.fill()

surface.write_to_png("plang_zebra.png")

