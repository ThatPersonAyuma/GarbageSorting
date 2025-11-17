import cairo

def create_zebra_cross(x, y):
    
    #>>> Section Plang Zebra Bawah <<<
    WIDTH, HEIGHT = 540, 300
    BAR_WIDTH = 15
    ctx.rectangle(x, y, WIDTH, HEIGHT)
    ctx.set_source_rgb(0, 0, 0)
    ctx.fill()
    ctx.set_source_rgb(1, 1, 1)
    # persegi panjang membentuk pola segitiga di ujung kiri bawah
    ctx.rectangle(15+x, HEIGHT / 2+y, BAR_WIDTH, 100)
    ctx.rectangle(30+x, HEIGHT / 2+y, BAR_WIDTH, 85)
    ctx.rectangle(45+x,HEIGHT / 2+y, BAR_WIDTH, 70)
    ctx.rectangle(60+x, HEIGHT / 2+y, BAR_WIDTH, 55)
    ctx.rectangle(75+x, HEIGHT / 2+y, BAR_WIDTH, 40)
    ctx.rectangle(90+x, HEIGHT / 2+y, BAR_WIDTH, 20)


    # garis miring pixelated 1 (Baw+xah kiri)
    ctx.rectangle(105+x, HEIGHT / 2+y + 86, BAR_WIDTH, 14)
    ctx.rectangle(120+x, HEIGHT / 2+y + 70, BAR_WIDTH, 30)
    ctx.rectangle(135+x, HEIGHT / 2+y + 55, BAR_WIDTH, 45)
    ctx.rectangle(150+x, HEIGHT / 2+y + 40, BAR_WIDTH, 60)
    ctx.rectangle(165+x, HEIGHT / 2+y + 20, BAR_WIDTH, 80)
    ctx.rectangle(180+x, HEIGHT / 2+y , BAR_WIDTH, 100)
    ctx.rectangle(195+x, HEIGHT / 2+y , BAR_WIDTH, 85)
    ctx.rectangle(210+x, HEIGHT / 2+y , BAR_WIDTH, 70)
    ctx.rectangle(225+x, HEIGHT / 2+y , BAR_WIDTH, 55)
    ctx.rectangle(240+x, HEIGHT / 2+y , BAR_WIDTH, 40)
    ctx.rectangle(255+x, HEIGHT / 2+y , BAR_WIDTH, 20)


    # garis miring pixelated 2 (Baw+xah kanan)
    ctx.rectangle(270+x, HEIGHT / 2+y + 86, BAR_WIDTH, 14)
    ctx.rectangle(285+x, HEIGHT / 2+y + 70, BAR_WIDTH, 30)
    ctx.rectangle(300+x, HEIGHT / 2+y + 55, BAR_WIDTH, 45)
    ctx.rectangle(315+x, HEIGHT / 2+y + 40, BAR_WIDTH, 60)
    ctx.rectangle(330+x, HEIGHT / 2+y + 20, BAR_WIDTH, 80)
    ctx.rectangle(345+x, HEIGHT / 2+y , BAR_WIDTH, 100)
    ctx.rectangle(360+x, HEIGHT / 2+y , BAR_WIDTH, 85)
    ctx.rectangle(375+x, HEIGHT / 2+y , BAR_WIDTH, 70)
    ctx.rectangle(390+x, HEIGHT / 2+y , BAR_WIDTH, 55)
    ctx.rectangle(405+x, HEIGHT / 2+y , BAR_WIDTH, 40)
    ctx.rectangle(420+x, HEIGHT / 2+y , BAR_WIDTH, 20)


    # persegi panjang membentuk pola segitiga di ujung kanan bawah
    ctx.rectangle(435+x, HEIGHT / 2+y + 86, BAR_WIDTH, 14)
    ctx.rectangle(450+x, HEIGHT / 2+y + 70, BAR_WIDTH, 30)
    ctx.rectangle(465+x, HEIGHT / 2+y + 55, BAR_WIDTH, 45)
    ctx.rectangle(480+x, HEIGHT / 2+y + 40, BAR_WIDTH, 60)
    ctx.rectangle(495+x, HEIGHT / 2+y + 20, BAR_WIDTH, 80)
    ctx.rectangle(510+x, HEIGHT / 2+y , BAR_WIDTH, 100)




    #>>> Section Plang Zebra Atas <<<


    # persegi panjang membentuk pola segitiga di ujung kiri atas
    ctx.rectangle(15+x, HEIGHT / 2+y - 130, BAR_WIDTH, 100)
    ctx.rectangle(30+x, HEIGHT / 2+y - 130, BAR_WIDTH, 85)
    ctx.rectangle(45+x, HEIGHT / 2+y - 130, BAR_WIDTH, 70)
    ctx.rectangle(60+x, HEIGHT / 2+y - 130, BAR_WIDTH, 55)
    ctx.rectangle(75+x, HEIGHT / 2+y - 130, BAR_WIDTH, 40)
    ctx.rectangle(90+x, HEIGHT / 2+y - 130, BAR_WIDTH, 20)


    # garis miring pixelated 1 (Ata+xs kiri)
    ctx.rectangle(105+x, HEIGHT / 2+y - 44, BAR_WIDTH, 14)
    ctx.rectangle(120+x, HEIGHT / 2+y - 60, BAR_WIDTH, 30)
    ctx.rectangle(135+x, HEIGHT / 2+y - 75, BAR_WIDTH, 45)
    ctx.rectangle(150+x, HEIGHT / 2+y - 90, BAR_WIDTH, 60)
    ctx.rectangle(165+x, HEIGHT / 2+y - 110, BAR_WIDTH, 80)
    ctx.rectangle(180+x, HEIGHT / 2+y - 130, BAR_WIDTH, 100)
    ctx.rectangle(195+x, HEIGHT / 2+y - 130, BAR_WIDTH, 85)
    ctx.rectangle(210+x, HEIGHT / 2+y - 130, BAR_WIDTH, 70)
    ctx.rectangle(225+x, HEIGHT / 2+y - 130, BAR_WIDTH, 55)
    ctx.rectangle(240+x, HEIGHT / 2+y - 130, BAR_WIDTH, 40)
    ctx.rectangle(255+x, HEIGHT / 2+y - 130, BAR_WIDTH, 20)


    # garis miring pixelated 2 (Ata+xs kanan)
    ctx.rectangle(270+x, HEIGHT / 2+y - 44, BAR_WIDTH, 14)
    ctx.rectangle(285+x, HEIGHT / 2+y - 60, BAR_WIDTH, 30)
    ctx.rectangle(300+x, HEIGHT / 2+y - 75, BAR_WIDTH, 45)
    ctx.rectangle(315+x, HEIGHT / 2+y - 90, BAR_WIDTH, 60)
    ctx.rectangle(330+x, HEIGHT / 2+y - 110, BAR_WIDTH, 80)
    ctx.rectangle(345+x, HEIGHT / 2+y - 130, BAR_WIDTH, 100)
    ctx.rectangle(360+x, HEIGHT / 2+y - 130, BAR_WIDTH, 85)
    ctx.rectangle(375+x, HEIGHT / 2+y - 130, BAR_WIDTH, 70)
    ctx.rectangle(390+x, HEIGHT / 2+y - 130, BAR_WIDTH, 55)
    ctx.rectangle(405+x, HEIGHT / 2+y - 130, BAR_WIDTH, 40)
    ctx.rectangle(420+x, HEIGHT / 2+y - 130, BAR_WIDTH, 20)


    # persegi panjang membentuk pola segitiga di ujung kanan atas
    ctx.rectangle(435+x, HEIGHT / 2+y - 44, BAR_WIDTH, 14)
    ctx.rectangle(450+x, HEIGHT / 2+y - 60, BAR_WIDTH, 30)
    ctx.rectangle(465+x, HEIGHT / 2+y - 75, BAR_WIDTH, 45)
    ctx.rectangle(480+x, HEIGHT / 2+y - 90, BAR_WIDTH, 60)
    ctx.rectangle(495+x, HEIGHT / 2+y - 110, BAR_WIDTH, 80)
    ctx.rectangle(510+x, HEIGHT / 2+y - 130, BAR_WIDTH, 100)


    ctx.fill()

def creat_blue(x, y):
    WIDTH, HEIGHT = 800, 200

    block_width = 80
    block_height = 40
    y_pos = HEIGHT - block_height - 1
    blue_color = (0.0, 0.3, 0.8)


    for i in range(0, WIDTH, block_width * 2):
        ctx.set_source_rgb(*blue_color)
        ctx.rectangle(i+x, y_pos+y, block_width, block_height)
        ctx.fill()


    rect_width = 800
    rect_height = 2
    rect_x = 0
    rect_y = y_pos - rect_height


    ctx.set_source_rgb(0.2, 0.5, 0.9)
    ctx.rectangle(rect_x+x, rect_y+y, rect_width, rect_height)
    ctx.fill()


    ctx.set_source_rgb(0.2, 0.5, 0.9)
    ctx.rectangle(0+x, HEIGHT+y - rect_height, rect_width, rect_height)
    ctx.fill()

def create_coklat(x, y):
    WIDTH, HEIGHT = 500, 300
    BAR_WIDTH = 15

    ctx.set_source_rgb(0.71, 0.47, 0.26)
    ctx.rectangle(100+x, y+ HEIGHT / 2, BAR_WIDTH, 60)
    ctx.rectangle(115+x, y+ HEIGHT / 2 - 10, BAR_WIDTH, 90)
    ctx.rectangle(130+x, y+ HEIGHT / 2 - 22, BAR_WIDTH, 120)
    ctx.rectangle(145+x, y+ HEIGHT / 2 - 34, BAR_WIDTH, 150)
    ctx.rectangle(160+x, y+ HEIGHT / 2 - 48, BAR_WIDTH, 170)
    ctx.rectangle(175+x, y+ HEIGHT / 2 - 62, BAR_WIDTH, 190)
    ctx.rectangle(190+x, y+ HEIGHT / 2 - 76, BAR_WIDTH, 210)
    ctx.rectangle(205+x, y+ HEIGHT / 2 - 90, BAR_WIDTH, 230)
    ctx.rectangle(220+x, y+ HEIGHT / 2 - 104, BAR_WIDTH, 250)
    ctx.rectangle(235+x, y+ HEIGHT / 2 - 104, BAR_WIDTH, 250)
    ctx.rectangle(250+x, y+ HEIGHT / 2 - 104, BAR_WIDTH, 250)
    ctx.rectangle(265+x, y+ HEIGHT / 2 - 104, BAR_WIDTH, 250)
    ctx.rectangle(280+x, y+ HEIGHT / 2 - 104, BAR_WIDTH, 250)
    ctx.rectangle(295+x, y+ HEIGHT / 2 - 104, BAR_WIDTH, 250)
    ctx.rectangle(310+x, y+ HEIGHT / 2 - 90, BAR_WIDTH, 230)
    ctx.rectangle(325+x, y+ HEIGHT / 2 - 76, BAR_WIDTH, 210)
    ctx.rectangle(340+x, y+ HEIGHT / 2 - 62, BAR_WIDTH, 190)
    ctx.rectangle(355+x, y+ HEIGHT / 2 - 48, BAR_WIDTH, 170)
    ctx.rectangle(370+x, y+ HEIGHT / 2 - 34, BAR_WIDTH, 150)
    ctx.rectangle(385+x, y+ HEIGHT / 2 - 22, BAR_WIDTH, 120)
    ctx.rectangle(400+x, y+ HEIGHT / 2 - 10, BAR_WIDTH, 90)
    ctx.rectangle(415+x, y+ HEIGHT / 2, BAR_WIDTH, 60)

    ctx.fill()

def create_orange(x, y):
    WIDTH, HEIGHT = 400, 300

    body_x, body_y = 60, 18
    body_w, body_h = 300, 210
    ctx.set_source_rgb(224/255, 103/255, 12/255)  
    ctx.rectangle(body_x+x, body_y+y, body_w, body_h)
    ctx.fill()


    ctx.rectangle(x+28, y+100, 40, 40)
    ctx.fill()


    ctx.rectangle(x+body_y + body_w - 20,y+ body_y, 40, 40)
    ctx.fill()


    feet_h = 30
    feet_y = body_y + body_h - 3
    foot_w = 48
    foot_positions = [body_x+10, body_x+110, body_x+220]
    for fx in foot_positions:
        ctx.rectangle(x+fx, y+feet_y, foot_w, feet_h)
    ctx.fill()


    panel_w = 54
    panel_h = 150
    panel_y = body_y + 40
    panel_xs = [body_x + 10, body_x + 110, body_x + 210]


    ctx.set_line_width(2)
    ctx.set_source_rgb(201/255, 74/255, 7/255)  
    for px in panel_xs:
        ctx.rectangle(x+px, y+panel_y, panel_w, panel_h)
        ctx.stroke()
        
# region Flower Function
def create_flower(center: tuple[int], height: int) -> None:
    width = height/3 
    ctx.rectangle(center[0] - width/2, center[1]-height/2, width, height)
    ctx.rectangle(center[0] - height/2, center[1] - width/2, height, width)
    ctx.move_to(center[0] - height/2, center[1] - width/2)
    ctx.line_to((center[0] - width/2),(center[1]-height/2))
    ctx.line_to((center[0] - width/2)+2*width, (center[1]-height/2)+2*width)
    ctx.line_to((center[0] - height/2)+2*width, (center[1] - width/2)+2*width)
    ctx.close_path()
    ctx.move_to(center[0] - height/2, center[1] + width/2)
    ctx.line_to((center[0] + width/2),(center[1]-height/2))
    ctx.line_to((center[0] - width/2)+2*width, (center[1]-height/2)+width)
    ctx.line_to((center[0] - height/2)+width, (center[1] - width/2)+2*width)
    ctx.close_path()
    # ctx.stroke()
    pass
# endregion

# region create merah
def create_merah():
    ctx.rectangle(365, 420, 200, 20)

    ctx.rectangle(1100, 480, 60, 15)

    ctx.rectangle(1100, 400, 20, 10)

    ctx.rectangle(1120, 390, 25, 15)
    ctx.rectangle(1140, 394, 120, 15)

    ctx.rectangle(1120, 300, 25, 15)

    ctx.rectangle(1135, 290, 25, 15)

    ctx.rectangle(1150, 295, 70, 15)

    ctx.rectangle(1220, 305, 50, 15)

    create_flower(center=(980,520), height=50)
    create_flower(center=(1000,410), height=50)
    create_flower(center=(950,370), height=50)
    create_flower(center=(970,315), height=50)
    create_flower(center=(985,260), height=50)
    create_flower(center=(1060,230), height=50)
    create_flower(center=(900,400), height=50)
    create_flower(center=(860,360), height=50)
    create_flower(center=(800,415), height=50)
    create_flower(center=(730,480), height=50)
    create_flower(center=(730,350), height=50)
    create_flower(center=(790,320), height=50)

    create_flower(center=(770,260), height=20)
    create_flower(center=(775,240), height=20)
    create_flower(center=(750,250), height=20)
    create_flower(center=(720,270), height=20)
    create_flower(center=(700,298), height=20)
    create_flower(center=(650,305), height=20)

    create_flower(center=(370, 370), height=20)
    create_flower(center=(385, 350), height=20)
    create_flower(center=(410, 360), height=20)
    create_flower(center=(400, 325), height=20)

    create_flower(center=(500, 480), height=20)
    create_flower(center=(380, 510), height=20)
    create_flower(center=(300, 530), height=20)
    create_flower(center=(310, 570), height=20)
    create_flower(center=(300, 610), height=20)
    create_flower(center=(290, 630), height=20)
    create_flower(center=(260, 610), height=20)
    create_flower(center=(250, 620), height=20)
    create_flower(center=(263, 630), height=20)
    create_flower(center=(270, 660), height=20)
    create_flower(center=(320, 655), height=20)
    create_flower(center=(348, 600), height=20)
    create_flower(center=(375, 585), height=20)
    create_flower(center=(395, 560), height=20)
    create_flower(center=(380, 640), height=20)
    create_flower(center=(420, 655), height=20)

    create_flower(center=(645, 590), height=20)
    create_flower(center=(630, 560), height=20)
    create_flower(center=(664, 530), height=20)
    create_flower(center=(700, 516), height=20)

    create_flower(center=(400, 180), height=20)
    create_flower(center=(420, 190), height=20)
    create_flower(center=(440, 172), height=20)
    create_flower(center=(468, 162), height=20)
    create_flower(center=(520, 175), height=20)
    create_flower(center=(520, 100), height=20)
    create_flower(center=(450, 115), height=20)
    create_flower(center=(414, 110), height=20)
    create_flower(center=(490, 80), height=20)
    create_flower(center=(585, 80), height=20)
    create_flower(center=(620, 84), height=20)
    create_flower(center=(640, 88), height=20)
    create_flower(center=(660, 76), height=20)
    create_flower(center=(690, 55), height=20)
    create_flower(center=(624, 52), height=20)

    create_flower(center=(900, 670), height=20)
    create_flower(center=(870, 540), height=20)
    create_flower(center=(828, 478), height=20)
    create_flower(center=(960, 468), height=20)
    create_flower(center=(1050, 448), height=20)
    create_flower(center=(1080, 490), height=20)
    create_flower(center=(1080, 535), height=20)
    create_flower(center=(1130, 535), height=20)

    create_flower(center=(1460, 535), height=20)
    create_flower(center=(1540, 510), height=20)
    create_flower(center=(1575, 480), height=20)
    create_flower(center=(1585, 550), height=20)
    create_flower(center=(1610, 497), height=20)
    create_flower(center=(1620, 450), height=20)
    create_flower(center=(1660, 530), height=20)
    create_flower(center=(1690, 530), height=20)
    create_flower(center=(1690, 480), height=20)
    create_flower(center=(1698, 580), height=20)
    create_flower(center=(1698, 680), height=20)
    create_flower(center=(1660, 670), height=20)
    create_flower(center=(1810, 690), height=20)
    create_flower(center=(1844, 712), height=20)
    create_flower(center=(1840, 650), height=20)
    create_flower(center=(1790, 620), height=20)
    create_flower(center=(1786, 485), height=20)
    create_flower(center=(1840, 454), height=20)
    create_flower(center=(1868, 470), height=20)
    ctx.fill()
# endregion

# region Initialize
WIDTH, HEIGHT = 2000, 1200

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

ctx.set_source_rgb(1, 1, 1)
ctx.paint()

ctx.set_source_rgb(1, 0, 0)
ctx.rectangle(0, 465, 370, 20)
# endregion

create_merah()
creat_blue(0, 700)
creat_blue(800, 700)
creat_blue(1600, 700)
create_coklat(900, 560)
create_coklat(1440, 520)
create_zebra_cross(560,600)
create_orange(1000, 760)
surface.write_to_png("result.png")

# Ini source code nya