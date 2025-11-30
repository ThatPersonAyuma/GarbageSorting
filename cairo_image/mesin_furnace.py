import cairo
import math

W, H = 220, 317
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
ctx = cairo.Context(surface)

def c(r,g,b): return (r/255.0, g/255.0, b/255.0)

#palet warna
C_BACKGROUND = c(209, 211, 214)
C_FLOOR = c(114, 114, 114)
C_FURNACE_GREY = c(180, 180, 180)
C_FURNACE_DARK_GREY = c(150, 150, 150)
C_FURNACE_LIGHT_GREY = c(200, 200, 200)
C_RED_PANEL = c(200, 50, 50)
C_REFRACTORY_CREAM = c(230, 230, 200)
C_REFRACTORY_INNER = c(200, 200, 180)
C_INNER_DARK = c(100, 100, 80)
C_LINE = c(0, 0, 0)
C_BUTTON_RED = c(240, 50, 50)      
C_BUTTON_GREEN = c(50, 200, 50)
C_CONTROL_KNOB = c(100, 100, 100)
C_DETAILS = C_BUTTON_RED
C_INPUT_PORT = c(120, 120, 120)

#background
# ctx.set_source_rgb(*C_BACKGROUND)
# ctx.rectangle(0, 0, W, H)
# ctx.fill()

floor_y = int(H * 0.7)
# ctx.set_source_rgb(*C_FLOOR)
# ctx.rectangle(0, floor_y, W, H - floor_y)
# ctx.fill()

#mesin
CENTER_X = (W // 2)
FURNACE_BASE_Y_COORD = floor_y + 75
SCALE = 1.0

def draw_detailed_furnace(cx, cy_base, scale=1.0):
    ctx.save()
    ctx.translate(cx, cy_base)
    # sx = scale[0] / bin_w
    # sy = scale[1] / bin_h
    # ctx.scale(sx, sy)
    ctx.scale(220/500, 317/720)

    F_WIDTH = 500
    F_HEIGHT = 500

    #bagian kaki
    LEG_W = 60
    LEG_H = 50
    ctx.set_source_rgb(*C_FURNACE_DARK_GREY)
    ctx.rectangle(-F_WIDTH/2, 0, LEG_W, LEG_H)
    ctx.rectangle(F_WIDTH/2 - LEG_W, 0, LEG_W, LEG_H)
    ctx.fill()
    ctx.set_source_rgb(*C_LINE)
    ctx.set_line_width(2)
    ctx.rectangle(-F_WIDTH/2, 0, LEG_W, LEG_H)
    ctx.stroke()
    ctx.rectangle(F_WIDTH/2 - LEG_W, 0, LEG_W, LEG_H)
    ctx.stroke()

    #bagian bawah yg merah
    RED_PANEL_H = 100
    RED_PANEL_Y = -RED_PANEL_H
    ctx.set_source_rgb(*C_RED_PANEL)
    ctx.rectangle(-F_WIDTH/2, RED_PANEL_Y, F_WIDTH, RED_PANEL_H)
    ctx.fill_preserve()
    ctx.set_source_rgb(*C_LINE)
    ctx.set_line_width(2)
    ctx.stroke()

    #body mesin
    BODY_H = 300
    BODY_Y = RED_PANEL_Y - BODY_H
    ctx.set_source_rgb(*C_FURNACE_GREY)
    ctx.rectangle(-F_WIDTH/2, BODY_Y, F_WIDTH, BODY_H)
    ctx.fill_preserve()
    ctx.set_source_rgb(*C_LINE)
    ctx.set_line_width(2)
    ctx.stroke()

    #panel atas
    TOP_PANEL_H = F_HEIGHT - BODY_H - RED_PANEL_H
    TOP_PANEL_Y = BODY_Y - TOP_PANEL_H
    ctx.set_source_rgb(*C_FURNACE_LIGHT_GREY)
    ctx.rectangle(-F_WIDTH/2, TOP_PANEL_Y, F_WIDTH, TOP_PANEL_H)
    ctx.fill_preserve()
    ctx.set_source_rgb(*C_LINE)
    ctx.set_line_width(2)
    ctx.stroke()

    #pintu tungku
    DOOR_W = F_WIDTH * 0.7
    DOOR_H = BODY_H * 0.7
    DOOR_X_OFFSET = -DOOR_W/2
    DOOR_Y_OFFSET = BODY_Y + (BODY_H - DOOR_H)/2

    #bingkai luar pintu
    ctx.set_source_rgb(*C_REFRACTORY_CREAM)
    ctx.rectangle(DOOR_X_OFFSET, DOOR_Y_OFFSET, DOOR_W, DOOR_H)
    ctx.fill_preserve()
    ctx.set_source_rgb(*C_LINE)
    ctx.set_line_width(2)
    ctx.stroke()

    #bagian dlm pintu
    INNER_DOOR_MARGIN = 30
    ctx.set_source_rgb(*C_REFRACTORY_INNER)
    ctx.rectangle(DOOR_X_OFFSET + INNER_DOOR_MARGIN, DOOR_Y_OFFSET + INNER_DOOR_MARGIN,
                  DOOR_W - 2 * INNER_DOOR_MARGIN, DOOR_H - 2 * INNER_DOOR_MARGIN)
    ctx.fill_preserve()
    ctx.set_source_rgb(*C_LINE)
    ctx.set_line_width(2)
    ctx.stroke()

    #bagian dlm tungku
    INNERMOST_MARGIN = 10
    ctx.set_source_rgb(*C_INNER_DARK)
    ctx.rectangle(DOOR_X_OFFSET + INNER_DOOR_MARGIN + INNERMOST_MARGIN,
                  DOOR_Y_OFFSET + INNER_DOOR_MARGIN + INNERMOST_MARGIN,
                  DOOR_W - 2 * INNER_DOOR_MARGIN - 2 * INNERMOST_MARGIN,
                  DOOR_H - 2 * INNER_DOOR_MARGIN - 2 * INNERMOST_MARGIN)
    ctx.fill()

    #untuk masukin sampah (lubang)
    INPUT_W = 150
    INPUT_H = 30
    INPUT_X = -INPUT_W / 2
    INPUT_Y = BODY_Y + 10

    ctx.set_source_rgb(*C_INPUT_PORT)
    ctx.rectangle(INPUT_X, INPUT_Y, INPUT_W, INPUT_H)
    ctx.fill_preserve()
    ctx.set_source_rgb(*C_LINE)
    ctx.set_line_width(2)
    ctx.stroke()

    ctx.set_source_rgb(*c(80, 80, 80))
    ctx.rectangle(INPUT_X + 5, INPUT_Y + 5, INPUT_W - 10, INPUT_H - 10)
    ctx.fill()

    #button merah
    KNOB_R = 25
    KNOB_X = F_WIDTH / 2 - 50
    KNOB_Y = BODY_Y + 40

    ctx.set_source_rgb(*C_BUTTON_RED)
    ctx.arc(KNOB_X, KNOB_Y, KNOB_R, 0, 2 * math.pi)
    ctx.fill_preserve() 
    ctx.set_source_rgb(*C_LINE)
    ctx.set_line_width(3)
    ctx.stroke() 

    #bagian atas
    BEAM_W = 20
    BEAM_H = 150
    BEAM_Y = TOP_PANEL_Y - BEAM_H

    ctx.set_source_rgb(*C_FURNACE_DARK_GREY)
    ctx.rectangle(-F_WIDTH/2 + 20, BEAM_Y, BEAM_W, BEAM_H)
    ctx.fill_preserve()
    ctx.set_source_rgb(*C_LINE)
    ctx.set_line_width(2)
    ctx.stroke()

    ctx.set_source_rgb(*C_FURNACE_DARK_GREY)
    ctx.rectangle(F_WIDTH/2 - 20 - BEAM_W, BEAM_Y, BEAM_W, BEAM_H)
    ctx.fill_preserve()
    ctx.set_source_rgb(*C_LINE)
    ctx.set_line_width(2)
    ctx.stroke()

    #balok bagian atas
    HORZ_BEAM_WIDTH = F_WIDTH - 2 * 20
    HORZ_BEAM_H = 20
    ctx.set_source_rgb(*C_FURNACE_DARK_GREY)
    ctx.rectangle(-F_WIDTH/2 + 20, BEAM_Y - HORZ_BEAM_H, HORZ_BEAM_WIDTH, HORZ_BEAM_H)
    ctx.fill_preserve()
    ctx.set_source_rgb(*C_LINE)
    ctx.set_line_width(2)
    ctx.stroke()

    HINGE_W = 15
    HINGE_H = 80
    ctx.set_source_rgb(*C_FURNACE_DARK_GREY)
    ctx.rectangle(-F_WIDTH/2 + 20 + BEAM_W, TOP_PANEL_Y + 5, HINGE_W, HINGE_H)
    ctx.rectangle(F_WIDTH/2 - 20 - BEAM_W - HINGE_W, TOP_PANEL_Y + 5, HINGE_W, HINGE_H)
    ctx.fill()
    ctx.set_source_rgb(*C_LINE)
    ctx.set_line_width(2)
    ctx.rectangle(-F_WIDTH/2 + 20 + BEAM_W, TOP_PANEL_Y + 5, HINGE_W, HINGE_H)
    ctx.stroke()
    ctx.rectangle(F_WIDTH/2 - 20 - BEAM_W - HINGE_W, TOP_PANEL_Y + 5, HINGE_W, HINGE_H)
    ctx.stroke()

    ctx.restore()

def get_furnace():
    draw_detailed_furnace(CENTER_X, FURNACE_BASE_Y_COORD, scale=SCALE)
    return surface
# draw_detailed_furnace(CENTER_X, FURNACE_BASE_Y_COORD, scale=SCALE)
# ctx.set_source_rgb(0,0,0)
# ctx.move_to(800, 0)
# ctx.line_to(550, 650)
# ctx.stroke()
# surface.write_to_png("mesin_furnace.png")
# print("Selesai: mesin_furnace.png")
