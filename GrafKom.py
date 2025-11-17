import cairo, math
WIDTH, HEIGHT = 900, 520
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

def rgb(r,g,b): return (r/255.0, g/255.0, b/255.0)

# background
ctx.rectangle(0,0,WIDTH,HEIGHT)
ctx.set_source_rgb(*rgb(255,255,255))
ctx.fill()

# sun
sun_x, sun_y, sun_r = 80, 70, 36
ctx.arc(sun_x, sun_y, sun_r, 0, 2*math.pi)
ctx.set_source_rgb(*rgb(255,221,87))
ctx.fill()
ctx.set_source_rgb(*rgb(255,183,45))
for i in range(12):
    angle = i * (2*math.pi/12)
    x1 = sun_x + math.cos(angle) * (sun_r + 6)
    y1 = sun_y + math.sin(angle) * (sun_r + 6)
    x2 = sun_x + math.cos(angle) * (sun_r + 18)
    y2 = sun_y + math.sin(angle) * (sun_r + 18)
    ctx.set_line_width(10)
    ctx.move_to(x1,y1)
    ctx.line_to(x2,y2)
    ctx.stroke()

# Kotak Rumah
house_x, house_y = 120, 170
house_w, house_h = 520, 280
ctx.rectangle(house_x, house_y, house_w, house_h)
ctx.set_source_rgb(*rgb(116,70,9))
ctx.fill()

# Atap
ctx.move_to(house_x-10, house_y)
ctx.line_to(house_x+house_w+10, house_y)
ctx.line_to(house_x+house_w-40, house_y-110)
ctx.line_to(house_x+60, house_y-110)
ctx.close_path()
ctx.set_source_rgb(*rgb(255,59,50))
ctx.fill()

# Cerobong Asap
chim_x = house_x + house_w - 130
chim_y = house_y - 150
chim_w, chim_h = 60, 80
ctx.rectangle(chim_x, chim_y, chim_w, chim_h)
ctx.set_source_rgb(*rgb(163,35,35))
ctx.fill()

# Pintu
door_x = house_x + 30
door_y = house_y + house_h - 170
door_w, door_h = 110, 170
ctx.rectangle(door_x, door_y, door_w, door_h)
ctx.set_source_rgb(*rgb(165,115,46))
ctx.fill()
ctx.set_line_width(6)
ctx.set_source_rgb(*rgb(130,86,29))
ctx.rectangle(door_x, door_y, door_w, door_h)
ctx.stroke()
ctx.arc(door_x + door_w - 20, door_y + door_h/2, 10, 0, 2*math.pi)
ctx.set_source_rgb(*rgb(255,212,51))
ctx.fill()

# Jendela
win_w = 120
win_x = house_x + house_w/2 + 10
win_y = house_y + 70
ctx.rectangle(win_x, win_y, win_w, win_w)
ctx.set_source_rgb(*rgb(111,237,236))
ctx.fill()
ctx.set_line_width(8)
ctx.set_source_rgb(*rgb(0,180,170))
ctx.rectangle(win_x, win_y, win_w, win_w)
ctx.stroke()

# Pagar Kayu
fence_x = house_x + house_w + 0
fence_y = house_y + house_h - 120
ctx.set_source_rgb(*rgb(211,138,30))
panel_w = 60
panel_h = 100
roof_h = 40
gap = 0

for i in range(4):
    px = fence_x + i * (panel_w + gap)
    py = fence_y + 20
    # persegi panjang
    ctx.rectangle(px, py, panel_w, panel_h)
    ctx.fill()
    # Segitiga atas
    ctx.move_to(px, py)
    ctx.line_to(px + panel_w/2, py - roof_h)
    ctx.line_to(px + panel_w, py)
    ctx.close_path()
    ctx.fill()


surface.write_to_png("house_pycairo.png")
