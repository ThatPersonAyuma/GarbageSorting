import cairo
import math

W, H = 500, 500
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
ctx = cairo.Context(surface)

def c(r,g,b): return (r/255, g/255, b/255)

#background
# ctx.set_source_rgb(*c(255,255,255))
# ctx.paint()

#ember
x = W/2
top_y = 150-40
top_rx = 160
top_ry = 40
bottom_rx = 130
bottom_ry = 28
height = 360
def get_ember_air():
    # Top ellipse (rim)
    ctx.save()
    ctx.translate(x, top_y)
    ctx.set_source_rgb(*c(180,180,180))
    ctx.arc(0, 0, 1, 0, 2*math.pi)
    ctx.fill()
    ctx.restore()

    # Body
    ctx.set_source_rgb(*c(200,200,200))
    ctx.move_to(x - top_rx, top_y)
    ctx.line_to(x - bottom_rx, top_y + height)
    ctx.line_to(x + bottom_rx, top_y + height)
    ctx.line_to(x + top_rx, top_y)
    ctx.fill()

    # Bottom ellipse
    ctx.save()
    ctx.translate(x, top_y + height)
    ctx.scale(bottom_rx, bottom_ry)
    ctx.set_source_rgb(*c(150,150,150))
    ctx.arc(0, 0, 1, 0, 2*math.pi)
    ctx.fill()
    ctx.restore()

    #air
    ctx.save()
    ctx.translate(x, top_y + 5)
    ctx.scale(top_rx - 10, top_ry - 8)
    ctx.set_source_rgb(*c(120,190,255))   
    ctx.arc(0, 0, 1, 0, 2*math.pi)
    ctx.fill()
    ctx.restore()

    #gagang ember
    left_x = x - 152   
    right_x = x + 152 
    gagang_y = top_y - 10 

    ctx.set_line_width(10)
    ctx.set_source_rgb(*c(90,90,90))

    # Titik kiri gagang
    ctx.arc(left_x, gagang_y, 10, 0, 2*math.pi)
    ctx.fill()

    # Titik kanan gagang
    ctx.arc(right_x, gagang_y, 10, 0, 2*math.pi)
    ctx.fill()

    # Lengkungan gagang
    ctx.set_line_width(12)
    ctx.move_to(left_x, gagang_y)
    ctx.curve_to(x - 80, gagang_y - 120, x + 80, gagang_y - 120, right_x, gagang_y)
    ctx.stroke()
    return surface
    # Save
    # surface.write_to_png("ember_air.png")
    # print("selesai : ember_air.png")
# get_ember_air()