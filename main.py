import pygame
import cairo
import component.button as button
from component import *
import numpy as np
from enum import Enum

from component.item_list import ItemList
from component.objects import ImageObject, TrashObject, TrashType, TrashBin
from component.text_area import create_text_box


pygame.init()

# region CONST
class Scene(Enum):
    HOME = 0
    SORTING = 1
    OUTSIDE = 2
    WORKING = 3
    TRANSTITION = -1

WIDTH, HEIGHT = 1024, 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
SCROLL_POS = (int(WIDTH*(17/20)),120)
BOX_SIZE = (90, 90)
SCROLL_SPACING = 10
# endregion

# Create Button
font = pygame.font.SysFont(None, 24)
button_rect = pygame.Rect(100, 100, 200, 60)
button_color = (70, 130, 180)
hover_color  = (100, 160, 210)
text_surf = font.render("Klik Aku!", True, (255, 255, 255))

# Load or create background
scene_a = pygame.Surface((WIDTH, HEIGHT))
scene_a.fill((70, 80, 200))

scene_b = pygame.Surface((WIDTH, HEIGHT))
scene_b.fill((200, 90, 70))

current_scene = scene_a
next_scene = scene_b





width, height = 60, 60
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
ctx = cairo.Context(surface)

# Contoh gambar: lingkaran merah

# Buat Pygame surface
pygame_surface = convert.convert_cairo_to_pygame_surf(surface)

# Buat beberapa dummy object

# image = pygame.Surface((100, 100), pygame.SRCALPHA)
# pygame.draw.circle(image, (255,0,0), (50,50), 50)

# Posisi awal
# start_pos = (150, 150)
# pos = list(start_pos)

dragging = False
offset_x = offset_y = 0

running = True




# region GrbageList & TrashItems
widthb, heightb = 90, 90
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, widthb, heightb)
ctx = cairo.Context(surface)
ctx.set_source_rgb(1, 0, 0)
ctx.arc(widthb/2, heightb/2, heightb//2, 0, 2*3.14159)
ctx.fill()
surface2 = cairo.ImageSurface(cairo.FORMAT_ARGB32, widthb, heightb)
ctxa = cairo.Context(surface2)
ctxa.set_source_rgb(0, 1, 0)
ctxa.arc(widthb/2, heightb/2, heightb//2, 0, 2*3.14159)
ctxa.fill()
items = [TrashObject(100,100, surface, "botol", TrashType.ORGANIC), TrashObject(100,100,surface2,"Yam-Yam", TrashType.PLASTIC), TrashObject(100,100,surface,"3", TrashType.ORGANIC),
         TrashObject(100,100,surface2,"4", TrashType.OTHERS), TrashObject(100,100,surface,"5", TrashType.OTHERS), TrashObject(100,100,surface2,"6", TrashType.ORGANIC)]
garbage = ItemList(items, start_pos=SCROLL_POS, spacing=SCROLL_SPACING, max_show=5, box_size=BOX_SIZE)  # tampil maksimal 3 item
# endregion

# region TrashBin
width, height = 100, 160
trash_bin = (170, 500)
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
ctx = cairo.Context(surface)
ctx.set_source_rgb(1,1,0)
ctx.paint()
trashbean_plastic = TrashBin(trash_bin[0], trash_bin[1], surface, TrashType.PLASTIC, "Tempat Sampah Plastik")
surface1 = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
ctx1 = cairo.Context(surface1)
ctx1.set_source_rgb(0,1,0)
ctx1.paint()
trashbean_organic = TrashBin(trash_bin[0]+130, trash_bin[1], surface1, TrashType.ORGANIC, "Tempat Sampah Organik")
surface2 = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
ctx2 = cairo.Context(surface2)
ctx2.set_source_rgb(190/255, 190/255, 190/255)
ctx2.paint()
trashbean_other = TrashBin(trash_bin[0]+260, trash_bin[1], surface2, TrashType.OTHERS, "Tempat Sampah Lainnya")
trashbeans = [trashbean_plastic, trashbean_organic, trashbean_other]
# endregion

# region Buttons
w=60;h=50
btn_up, btn_down = button.Button.create_up_down_button(
    x1=garbage.start_pos[0]+abs(w-garbage.box_size[0]//2), y1=garbage.start_pos[1]-h-garbage.spacing,      # posisi tombol atas
    x2=garbage.start_pos[0]+abs(w-garbage.box_size[0]//2), y2=garbage.start_pos[1]+(garbage.spacing*(garbage.max_show-1))+garbage.box_size[1]*garbage.max_show+garbage.spacing,     # posisi tombol bawah
    w=w, h=h,
    callback_up=garbage.scroll_up,
    callback_down=garbage.scroll_down
)
def Nothing():
    pass

def create_button_move_scene_call(next_state: Scene):
    def callback():
        global direction, in_transition, progress, state, next_scene
        direction = "left"
        in_transition = True
        progress = 0
        state = next_state
        next_scene = scene_b if current_scene == scene_a else scene_a
    return callback

# Button settings
BTN_WIDTH = 80
BTN_HEIGHT = 80

BTN_MARGIN = 20

direction = "right"
in_transition = False
progress = 0.0

w_lf =80 ;h_lf=60
button_left = button.Button(BTN_MARGIN,(HEIGHT//2)-w_lf//2, w_lf, h_lf, "<", 34, Nothing, 0, )
button_right = button.Button(WIDTH-BTN_MARGIN-w_lf,(HEIGHT//2)-w_lf//2, w_lf, h_lf, ">", 34, Nothing, 0)

# endregion

toggle_button = button.Button(WIDTH//3, HEIGHT-100,150,50, "Click Me", 24, Nothing, 0)
# --- Transition mask using cairo ---
def create_wipe_mask(progress, direction):
    cairo_surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(cairo_surface)
    
    w = int(progress * WIDTH)

    if direction == "right":
        ctx.rectangle(0, 0, w, HEIGHT)
    else:
        ctx.rectangle(WIDTH - w, 0, w, HEIGHT)

    ctx.set_source_rgba(1, 1, 1, 1)
    ctx.fill()

    buf = cairo_surface.get_data()
    return pygame.image.frombuffer(buf, (WIDTH, HEIGHT), "ARGB")


# running = True
# region Sorting Scene
dragged_object:objects.TrashObject
dragged_index:int
def sorting_sceen():
    global dragged_index, trashbeans, state, current_scene, dt, garbage, dragging, dragged_object, offset_x, offset_y, direction, next_scene
    screen.blit(current_scene, (0, 0))
    
    pos=pygame.mouse.get_pos()
    hover_name = None
    for obj in garbage.get():
        if obj.collide_point(pos):
            hover_name = f"{obj.name}, {obj.type.value}"
    for obj in trashbeans:
        if obj.collide_point(pos):
            hover_name = f"{obj.name}"
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            state = None
        if not in_transition:
            if e.type == pygame.MOUSEBUTTONDOWN:
                mx, my = e.pos
            
                for index, obj in enumerate(garbage.get()):
                    if obj.collide_point((mx, my)):
                        dragging = True;dragged_object=obj;obj.is_dragged=True;dragged_index=index
                        # Hitung offset supaya drag smooth
                        offset_x = (obj.rect[0] - mx)
                        offset_y = (obj.rect[1] - my)
                        break
                btn_up.click((mx, my))
                btn_down.click((mx, my))
            
            elif e.type == pygame.MOUSEBUTTONUP:
                if dragging:
                    dragging = False;dragged_object.is_dragged=False
                    if isinstance(dragged_object, TrashObject):
                        for trashbin in trashbeans:
                            if trashbin.collide_object(dragged_object):
                                if trashbin.is_valid_trash(dragged_object.type):
                                    garbage.pop(dragged_index)
                                    if len(garbage.inventory)==0:
                                        state = Scene.HOME
                                    break
                                else:
                                    print("wrong")
                            
                    dragged_object.back_to_origin()
                    
            elif e.type == pygame.MOUSEMOTION:
                if dragging:
                    mx, my = e.pos
                    dragged_object.replace_pos(mx + offset_x, my + offset_y)
                    

    for trashbean in trashbeans:
        trashbean.draw(screen)
    
    if dragging: 
        dragged_object.draw(screen)
        pygame.draw.rect(screen, (0, 0, 0), dragged_object.rect, 2)
    garbage.draw(screen)
    btn_up.draw(screen)
    btn_down.draw(screen)
    toggle_button.draw(screen)
    if hover_name!=None:
        text_surf :pygame.Surface = create_text_box(hover_name, 20, (0,0,0,0.5))
        x = pos[0]-text_surf.width//2
        if x+text_surf.get_width()>WIDTH:
            x = WIDTH-text_surf.get_width()
        elif x<0:
            x = 0
        screen.blit(text_surf, (pos[0]-text_surf.width//2, pos[1] + 20))
    
    pygame.display.flip()
    
# endregion

# region Create Home Components
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
ctx = cairo.Context(surface)
ctx.set_source_rgb(1,1,0)
ctx.paint()
next_to_sorting = ImageObject(200,400,surface,"Pilah Sampah")
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0,1,0)
ctx.paint()
next_to_outside = ImageObject(750,250,surface,"Pergi ke Luar")
# endregion

# region Home Space
def home_sceen():
    global  dt, state, screen,current_scene, in_transition, progress
    screen.blit(current_scene, (0, 0))
    hover_name = None
    pos = pygame.mouse.get_pos()
    if next_to_sorting.collide_point(pos):
        hover_name = next_to_sorting.name
    elif next_to_outside.collide_point(pos):
        hover_name = next_to_outside.name
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            state = None
        if not in_transition:
            if e.type == pygame.MOUSEBUTTONDOWN:
                mx, my = e.pos

                button_right.click((mx, my))
                
                if next_to_sorting.collide_point((mx,my)):
                    if len(garbage.inventory)>0:
                        state = Scene.SORTING
                
                elif next_to_outside.collide_point((mx,my)):
                    state = Scene.OUTSIDE
                
    # transition
    if in_transition:
        progress += dt * 1.2
        progress = min(progress, 1)

        mask = create_wipe_mask(progress, direction)

        scene_temp = next_scene.copy()
        scene_temp.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        screen.blit(scene_temp, (0, 0))

        if progress >= 1:
            current_scene = next_scene
            in_transition = False
            
    # draw_buttons()
    name = button_right.draw(screen)
    if name != None: hover_name=name
    next_to_sorting.draw(screen)
    next_to_outside.draw(screen)
    if hover_name!=None:
        # print(hover_name)
        text_surf :pygame.Surface = create_text_box(hover_name, 20, (0,0,0,0.5))
        x = pos[0]-text_surf.width//2
        if x+text_surf.get_width()>WIDTH:
            x = WIDTH-text_surf.get_width()
        elif x<0:
            x = 0
        screen.blit(text_surf, (x, pos[1] + 20))
        
    pygame.display.flip()
# endregion
    

    
    
# region Working Space
def working_space():
    global  dt, state, screen,current_scene, in_transition, progress
    screen.blit(current_scene, (0, 0))
    pos = pygame.mouse.get_pos()
    hover_name = None
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            state = None
        if not in_transition:
            if e.type == pygame.MOUSEBUTTONDOWN:
                mx, my = e.pos
                button_left.click((mx, my))
                
    if in_transition:
        progress += dt * 1.2
        progress = min(progress, 1)

        mask = create_wipe_mask(progress, direction)

        scene_temp = next_scene.copy()
        scene_temp.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        screen.blit(scene_temp, (0, 0))

        if progress >= 1:
            current_scene = next_scene
            in_transition = False
            
    name = button_left.draw(screen)
    if name != None: hover_name=name
    if hover_name!=None:
        # print(hover_name)
        text_surf :pygame.Surface = create_text_box(hover_name, 20, (0,0,0,0.5))
        x = pos[0]-text_surf.width//2
        if x+text_surf.get_width()>WIDTH:
            x = WIDTH-text_surf.get_width()
        elif x<0:
            x = 0
        screen.blit(text_surf, (x, pos[1] + 20))
    pygame.display.flip()
# endregion


# region Outside Components
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, widthb, heightb)
ctx = cairo.Context(surface)
ctx.set_source_rgb(1, 0, 0)
ctx.arc(widthb/2, heightb/2, heightb//2, 0, 2*3.14159)
ctx.fill()
surface2 = cairo.ImageSurface(cairo.FORMAT_ARGB32, widthb, heightb)
ctxa = cairo.Context(surface2)
ctxa.set_source_rgb(0, 1, 0)
ctxa.arc(widthb/2, heightb/2, heightb//2, 0, 2*3.14159)
ctxa.fill()
items = [TrashObject(100,100, surface, "Air", TrashType.OTHERS), TrashObject(100,100,surface2,"Bakteri Starter", TrashType.OTHERS)]
outside_items = ItemList(items, (SCROLL_POS[0], SCROLL_POS[1]-25), SCROLL_SPACING, 2,BOX_SIZE)
# endregion

# region Outside Space
def outside_space():
    global  dt, state, screen,current_scene, in_transition, progress, dragging, dragged_index, dragged_object, offset_x, offset_y
    
    screen.blit(current_scene, (0, 0))
    hover_name = None
    pos = pygame.mouse.get_pos()
    for obj in outside_items.get():
        if obj.collide_point(pos):
            hover_name = obj.name
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            state = None
        if not in_transition:
            if e.type == pygame.MOUSEBUTTONDOWN:
                mx, my = e.pos
                button_left.click((mx, my))
                
                for index, obj in enumerate(outside_items.get()):
                    if obj.collide_point((mx, my)):
                        dragging = True;dragged_object=obj;obj.is_dragged=True;dragged_index=index
                        # Hitung offset supaya drag smooth
                        offset_x = (obj.rect[0] - mx)
                        offset_y = (obj.rect[1] - my)
                        break
                btn_up.click((mx, my))
                btn_down.click((mx, my))
            
            elif e.type == pygame.MOUSEBUTTONUP:
                if dragging:
                    dragging = False;dragged_object.is_dragged=False
                    dragged_object.back_to_origin()
                
            elif e.type == pygame.MOUSEMOTION:
                if dragging:
                    mx, my = e.pos
                    dragged_object.replace_pos(mx + offset_x, my + offset_y)
                    
    # transition
    if in_transition:
        progress += dt * 1.2
        progress = min(progress, 1)

        mask = create_wipe_mask(progress, direction)

        scene_temp = next_scene.copy()
        scene_temp.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        screen.blit(scene_temp, (0, 0))

        if progress >= 1:
            current_scene = next_scene
            in_transition = False
            
    if dragging: 
        dragged_object.draw(screen)
        pygame.draw.rect(screen, (0, 0, 0), dragged_object.rect, 2)
        
    name = button_left.draw(screen)
    if name != None: hover_name=name
    outside_items.draw(screen)
    if hover_name!=None:
        # print(hover_name)
        text_surf :pygame.Surface = create_text_box(hover_name, 20, (0,0,0,0.5))
        x = pos[0]-text_surf.width//2
        if x+text_surf.get_width()>WIDTH:
            x = WIDTH-text_surf.get_width()
        elif x<0:
            x = 0
        screen.blit(text_surf, (x, pos[1] + 20))
        
    pygame.display.flip()
# endregion
    
if __name__ == "__main__":
    state = Scene.HOME
    home_callback = create_button_move_scene_call(Scene.WORKING)
    outside_callback = create_button_move_scene_call(Scene.HOME)
    while running:
        dt = clock.tick(60) / 1000
        # sorting_sceen()
        match state:
            case Scene.HOME:
                button_right.name = "Pergi ke Ruang Kerajinan"
                button_right.callback = home_callback
                home_sceen()
            case Scene.SORTING:
                sorting_sceen()
            case Scene.OUTSIDE:
                button_left.name = "Kembali ke Ruang Pemilahan"
                button_left.callback = outside_callback
                outside_space()
            case Scene.WORKING:
                button_left.name = "Kembali ke Ruang Pemilahan"
                button_left.callback = outside_callback
                working_space()
            case Scene.TRANSTITION:
                state = Scene.HOME
            case _:
                break