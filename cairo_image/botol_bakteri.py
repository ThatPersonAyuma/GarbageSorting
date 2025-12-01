import cairo
import math

W, H = 800, 1000 
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 550, 550)
ctx = cairo.Context(surface)

def c(r,g,b): return (r/255.0, g/255.0, b/255.0)

# Palet Warna
C_BACKGROUND = c(255, 255, 255) 
C_BOTTLE_YELLOW = c(255, 230, 0) 
C_CAP_BLACK = c(30, 30, 30)     
C_LINE = c(0, 0, 0)             
C_TEXT_BLACK = c(0, 0, 0)       

#background
# ctx.set_source_rgb(*C_BACKGROUND)
# ctx.rectangle(0, 0, W, H)
# ctx.fill()

#bagian botol
BOTTLE_CENTER_X = W // 2
BOTTLE_BASE_Y = H * 0.75 # Posisi dasar botol
BOTTLE_WIDTH = 250
BOTTLE_HEIGHT = 500
BOTTOM_CURVE_DEPTH = 100 #lengkungan U di bagian bawah

#botol
def draw_em4_bottle(cx, cy_base, width, height):
    ctx.save()
    ctx.translate(cx, cy_base)

    # 1. Base Melengkung (U-shape)
    ctx.move_to(-width * 0.4, 0)
    
    #setengah lingkaran di bawah
    ctx.curve_to(-width * 0.5, BOTTOM_CURVE_DEPTH * 0.5, 
                 -width * 0.5, BOTTOM_CURVE_DEPTH,  
                 0, BOTTOM_CURVE_DEPTH)            # Paling bawah
    ctx.curve_to(width * 0.5, BOTTOM_CURVE_DEPTH, 
                 width * 0.5, BOTTOM_CURVE_DEPTH * 0.5, 
                 width * 0.4, 0)                   # Titik kanan bawah
    
    # 2. Body Kanan (Naik ke atas)
    ctx.line_to(width * 0.4, -height * 0.6) 
    ctx.curve_to(width * 0.4, -height * 0.7, 
                 width * 0.3, -height * 0.75,
                 width * 0.2, -height * 0.8)
                 
    # 3. Leher
    ctx.line_to(-width * 0.2, -height * 0.8) 
    
    # 4. Body Kiri (Turun)
    ctx.curve_to(-width * 0.3, -height * 0.75, 
                 -width * 0.4, -height * 0.7,
                 -width * 0.4, -height * 0.6)
    
    ctx.close_path() 

    ctx.set_source_rgb(*C_BOTTLE_YELLOW)
    ctx.fill_preserve() 
    ctx.set_source_rgb(*C_LINE)
    ctx.set_line_width(4)
    ctx.stroke() 

    # Cap (Tutup)
    CAP_WIDTH = width * 0.3
    CAP_HEIGHT = height * 0.1
    CAP_Y = -height * 0.8 

    ctx.set_source_rgb(*C_CAP_BLACK)
    ctx.rectangle(-CAP_WIDTH/2, CAP_Y - CAP_HEIGHT, CAP_WIDTH, CAP_HEIGHT)
    ctx.fill_preserve()
    ctx.set_source_rgb(*C_LINE)
    ctx.set_line_width(4)
    ctx.stroke()
    
    # Detail tutup (garis horizontal)
    ctx.set_line_width(2)
    ctx.move_to(-CAP_WIDTH/2, CAP_Y - CAP_HEIGHT * 0.5)
    ctx.line_to(CAP_WIDTH/2, CAP_Y - CAP_HEIGHT * 0.5)
    ctx.stroke()
    ctx.move_to(-CAP_WIDTH/2, CAP_Y - CAP_HEIGHT * 0.75)
    ctx.line_to(CAP_WIDTH/2, CAP_Y - CAP_HEIGHT * 0.75)
    ctx.stroke()


    # Teks "EM4"
    ctx.set_source_rgb(*C_TEXT_BLACK)
    ctx.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(80) 
    
    text = "EM4"
    xbearing, ybearing, t_width, t_height, xadvance, yadvance = ctx.text_extents(text)
    ctx.move_to( -t_width/2, -height * 0.45 + t_height/2) 
    ctx.show_text(text)

    ctx.restore()

def get_m3bottle():
    draw_em4_bottle(550/2, 450, BOTTLE_WIDTH, BOTTLE_HEIGHT)
    return surface
# surface.write_to_png("botol_bakteri.png")
# print("Selesai: botol_bakteri.png")
