import pygame
import cairo
import component.button as button
from component import *
import numpy as np
from enum import Enum
from pathlib import Path

from component.item_list import ItemList
from component.objects import ImageObject, TrashObject, TrashType, TrashBin
from component.text_area import create_text_box

from scenes import IndustryRoom, outdoor, PickUpGarage, TrashTruck


pygame.init()

# region CONST
class Scene(Enum):
    HOME = 0
    SORTING = 1
    OUTSIDE = 2
    WORKING = 3
    TRANSTITION = -1

WIDTH, HEIGHT = 1225, 689
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
items = [TrashObject(100,100, surface, "botol", TrashType.ORGANIC)]
# items = [TrashObject(100,100, surface, "botol", TrashType.ORGANIC), TrashObject(100,100,surface2,"Yam-Yam", TrashType.PLASTIC), TrashObject(100,100,surface,"3", TrashType.ORGANIC),
#         TrashObject(100,100,surface2,"4", TrashType.OTHERS), TrashObject(100,100,surface,"5", TrashType.OTHERS), TrashObject(100,100,surface2,"6", TrashType.ORGANIC)]
garbage = ItemList(items, start_pos=SCROLL_POS, spacing=SCROLL_SPACING, max_show=5, box_size=BOX_SIZE)  # tampil maksimal 3 item
# endregion

# region TrashBin
width, height = 100, 160
spacing = BOX_SIZE[0]+10
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
trashbean_organic = TrashBin(trash_bin[0]+width+spacing, trash_bin[1], surface1, TrashType.ORGANIC, "Tempat Sampah Organik")
surface2 = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
ctx2 = cairo.Context(surface2)
ctx2.set_source_rgb(190/255, 190/255, 190/255)
ctx2.paint()
trashbean_other = TrashBin(trash_bin[0]+2*(width+spacing), trash_bin[1], surface2, TrashType.OTHERS, "Tempat Sampah Lainnya")
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
button_left = button.Button(BTN_MARGIN,(HEIGHT//2)-w_lf//2, w_lf, h_lf, "<", 34, Nothing, 0)
button_right = button.Button(WIDTH-BTN_MARGIN-w_lf,(HEIGHT//2)-w_lf//2, w_lf, h_lf, ">", 34, Nothing, 0)

# endregion

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
def sorting_space():
    global dragged_index, trashbeans, state, current_scene, dt, garbage, dragging, dragged_object, offset_x, offset_y, direction, next_scene, hold_item, old_hi_rect, shredder_has_item, furnace_has_item, presser_has_item, shredder_bucket_has_item, paving_mold_has_item, presser_running, furnace_running, shredder_running, presser_timer, furnace_timer, shredder_timer, decomposer_running, decomposer_timer, decomp_stack_index
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
                if hold_item==None:
                    if len(garbage.inventory)==0:
                        for trashbean in trashbeans[:-1]:
                            if trashbean.collide_point((mx, my)):
                                trashbean.scale(BOX_SIZE[0], BOX_SIZE[1])
                                hold_item = trashbean
                                old_hi_rect = trashbean.rect
                                trashbean.rect = hold_item_rect.copy()
                else:
                    if hold_item.collide_point((mx, my)):
                        dragging = True;dragged_object=hold_item
                        offset_x = (hold_item.rect[0] - mx)
                        offset_y = (hold_item.rect[1] - my)
                        break
                    
                btn_up.click((mx, my))
                btn_down.click((mx, my))
                if hold_item!=None:button_left.click((mx, my))

            elif e.type == pygame.MOUSEBUTTONUP:
                if dragging:
                    dragging = False;dragged_object.is_dragged=False
                    if isinstance(dragged_object, TrashObject):
                        for trashbin in trashbeans:
                            if trashbin.collide_object(dragged_object):
                                if trashbin.is_valid_trash(dragged_object.type):
                                    garbage.pop(dragged_index)
                                else:
                                    print("wrong")
                    if isinstance(dragged_object, TrashBin):
                        if old_hi_rect==None:
                            raise ValueError("old_hi_rect must have value here")
                        if old_hi_rect.colliderect(dragged_object.rect):
                            dragged_object.return_scale()
                            hold_item = None
                            dragged_object.rect = old_hi_rect
                        else:
                            dragged_object.rect = hold_item_rect.copy()
                    else:
                        dragged_object.back_to_origin()
                    
            elif e.type == pygame.MOUSEMOTION:
                if dragging:
                    mx, my = e.pos
                    dragged_object.replace_pos(mx + offset_x, my + offset_y)
        if e.type == TIMER_EVENT:
            if shredder_running:
                if shredder_timer > 0: 
                    shredder_timer -= 1
                else:
                    shredder_running = False
                    shredder_has_item = False
                    shredder_bucket_has_item = True
                    # Logic
            if furnace_running:
                if furnace_timer > 0: 
                    furnace_timer -= 1
                else:
                    furnace_running = False
                    furnace_has_item = False
                    paving_mold_has_item = True
            if presser_running:
                if presser_timer > 0: 
                    presser_timer -= 1
                else:
                    presser_running = False
                    presser_has_item = False
            if decomposer_running:
                if decomposer_timer > 0:
                    decomposer_timer -= 1
                else:
                    decomposer_running = False
                    decomp_stack_index = len(decompose_stack)-1
                    # Logic
                    
    for trashbean in trashbeans:
        trashbean.draw(screen)
    if hold_item!=None:
        hold_item.draw(screen)
        screen.blit(hold_item.pygame_surface, hold_item.rect)
        # pass
    if dragging: 
        dragged_object.draw(screen)
        pygame.draw.rect(screen, (0, 0, 0), dragged_object.rect, 2)
    garbage.draw(screen)
    if len(garbage.inventory)!=0:
        btn_up.draw(screen)
        btn_down.draw(screen)

    if hover_name!=None:
        text_surf :pygame.Surface = create_text_box(hover_name, 20, (0,0,0,0.5))
        x = pos[0]-text_surf.width//2
        if x+text_surf.get_width()>WIDTH:
            x = WIDTH-text_surf.get_width()
        elif x<0:
            x = 0
        screen.blit(text_surf, (pos[0]-text_surf.width//2, pos[1] + 20))
    if hold_item!=None:
        name = button_left.draw(screen)
        if name != None: hover_name=name
    pygame.display.flip()
    
# endregion

# region Create Home Components
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
ctx = cairo.Context(surface)
ctx.set_source_rgb(1,1,0)
ctx.paint()
next_to_sorting = ImageObject(200,400,surface,"Pilah Sampah")
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 250, 310)
next_to_outside = ImageObject(855,200,surface,"Pergi ke Luar")
# endregion

# region Home Space
def home_space():
    global  dt, state, screen,current_scene, in_transition, progress, shredder_has_item, furnace_has_item, presser_has_item, shredder_bucket_has_item, paving_mold_has_item, presser_running, furnace_running, shredder_running, presser_timer, furnace_timer, shredder_timer, decomposer_running, decomposer_timer, decomp_stack_index
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
                    if len(garbage.inventory)>0 or hold_item!=None:
                        state = Scene.SORTING
                
                elif next_to_outside.collide_point((mx,my)):
                    state = Scene.OUTSIDE
                    callback_to_outside()
                    
        if e.type == TIMER_EVENT:
            if shredder_running:
                if shredder_timer > 0: 
                    shredder_timer -= 1
                else:
                    shredder_running = False
                    shredder_has_item = False
                    shredder_bucket_has_item = True
                    # Logic
            if furnace_running:
                if furnace_timer > 0: 
                    furnace_timer -= 1
                else:
                    furnace_running = False
                    furnace_has_item = False
                    paving_mold_has_item = True
            if presser_running:
                if presser_timer > 0: 
                    presser_timer -= 1
                else:
                    presser_running = False
                    presser_has_item = False
            if decomposer_running:
                if decomposer_timer > 0:
                    decomposer_timer -= 1
                else:
                    decomposer_running = False
                    decomp_stack_index = len(decompose_stack)-1
                
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
    if hold_item != None:
        hold_item.draw(screen)
        if hold_item.collide_point(pos):
            hover_name = hold_item.name
    name = button_right.draw(screen)
    if name != None: hover_name=name
    next_to_sorting.draw(screen)
    next_to_outside.draw(screen)
    if hold_item!=None:hold_item.draw(screen)
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
    


# region Working Components
width, height = 100, 160
trash_bin = (370, 300)
spacing = BOX_SIZE[0]+5
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
ctx = cairo.Context(surface)
ctx.set_source_rgb(1,0,0)
ctx.paint()
shredder = TrashBin(trash_bin[0], trash_bin[1], surface, TrashType.OBJECT, "Pencacah Plastik")
furnace = TrashBin(trash_bin[0]+width+spacing, trash_bin[1], surface, TrashType.OBJECT, "Mesin Peleleh Plastik")
presser = TrashBin(trash_bin[0]+2*(width+spacing), trash_bin[1], surface, TrashType.OBJECT, "Mesin Penekan")
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, int(width*0.7), int(height*0.3))
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.5,0.5,0)
shredder_bucket = TrashObject(shredder.rect.x + int(width*0.15), shredder.rect.y+shredder.rect.height-surface.get_height(), surface, "Bak Penampung Cacahan", TrashType.OBJECT)
paving_mold = TrashObject(furnace.rect.x+int(width*0.15), furnace.rect.y+furnace.rect.height-surface.get_height(), surface, "Cetakan Paving", TrashType.OBJECT)
mold_hold_rect = pygame.Rect(presser.rect.x+int(width*0.15), presser.rect.y+(presser.rect.height-surface.get_height())*2/3, surface.get_width(), surface.get_height())
# endregion
    
# region Working Logic
def create_time_text(time:int)->str:
    return str(time)+" detik"
    
SHREDDER_TIME = 30
FURNACE_TIME = 45
PRESSER_TIME = 30
shredder_timer:int = 0
furnace_timer:int = 0
presser_timer:int = 0
shredder_running=False
furnace_running=False
presser_running=False 
TIMER_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TIMER_EVENT, 1000)
shredder_has_item = False
furnace_has_item = False
presser_has_item = False
shredder_bucket_has_item = False
paving_mold_has_item = False
# endregion
    
# region Working Space
def working_space():
    global  dt, state, screen,current_scene, in_transition, progress, dragging, dragged_object, offset_x, offset_y, hold_item, mold_hold_rect, shredder_has_item, furnace_has_item, presser_has_item, shredder_bucket_has_item, paving_mold_has_item, presser_running, furnace_running, shredder_running, presser_timer, furnace_timer, shredder_timer, decomposer_running, decomposer_timer, decomp_stack_index
    screen.blit(current_scene, (0, 0))
    pos = pygame.mouse.get_pos()
    hover_name = None
    if furnace.collide_point(pos):
        hover_name = furnace.name
    elif shredder.collide_point(pos):
        hover_name = shredder.name
    elif presser.collide_point(pos):
        hover_name = presser.name
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            state = None
        if not in_transition:
            if e.type == pygame.MOUSEBUTTONDOWN:
                mx, my = e.pos
                button_left.click((mx, my))
                if hold_item != None:
                    if hold_item.collide_point((mx, my)):
                        dragging = True;dragged_object=hold_item
                        offset_x = (hold_item.rect[0] - mx)
                        offset_y = (hold_item.rect[1] - my)
                if not shredder_running and shredder_bucket.collide_point((mx, my)):
                    dragging = True;dragged_object=shredder_bucket
                    offset_x = (shredder_bucket.rect[0] - mx)
                    offset_y = (shredder_bucket.rect[1] - my)
                elif not furnace_running and not presser_running and paving_mold.collide_point((mx, my)):
                    dragging = True;dragged_object=paving_mold
                    offset_x = (paving_mold.rect[0] - mx)
                    offset_y = (paving_mold.rect[1] - my)
                elif shredder_has_item and not shredder_bucket_has_item and not shredder_running and shredder.collide_point((mx, my)):
                    shredder_running = True; shredder_timer = SHREDDER_TIME
                elif furnace_has_item and not furnace_running and not paving_mold_has_item and not presser_has_item and furnace.collide_point((mx, my)):
                    furnace_running = True; furnace_timer = FURNACE_TIME
                elif presser_has_item and not presser_running and paving_mold_has_item and presser.collide_point((mx, my)):
                    presser_running = True; presser_timer = PRESSER_TIME
                    
            elif e.type == pygame.MOUSEBUTTONUP:
                if dragging:
                    dragging = False;dragged_object.is_dragged=False
                    if dragged_object is hold_item:
                        if dragged_object is trashbean_plastic and not shredder_has_item and not shredder_running  and shredder.collide_object(dragged_object):
                            shredder_has_item = True
                            print("Taruh sampah plastik di shredder")
                        dragged_object.rect = hold_item_rect.copy()
                    elif dragged_object is shredder_bucket:
                        if shredder_bucket_has_item and not furnace_running and not furnace_has_item and furnace.collide_object(dragged_object):
                            furnace_has_item = True
                            shredder_bucket_has_item = False
                            print("shradded telah ditamabahkan ke furnace")
                        dragged_object.back_to_origin()
                    elif dragged_object is paving_mold:
                        if paving_mold_has_item:
                            if presser.collide_object(dragged_object):
                                dragged_object.origin, mold_hold_rect = mold_hold_rect, dragged_object.origin
                                presser_has_item = True
                        else:
                            if not paving_mold_has_item and presser_has_item and furnace.collide_object(dragged_object):
                                dragged_object.origin, mold_hold_rect = mold_hold_rect, dragged_object.origin
                                presser_has_item = False
                        dragged_object.back_to_origin()
                    
            elif e.type == pygame.MOUSEMOTION:
                if dragging:
                    mx, my = e.pos
                    dragged_object.replace_pos(mx + offset_x, my + offset_y)
            
        if e.type == TIMER_EVENT:
            if shredder_running:
                if shredder_timer > 0: 
                    shredder_timer -= 1
                else:
                    shredder_running = False
                    shredder_has_item = False
                    shredder_bucket_has_item = True
                    # Logic
            if furnace_running:
                if furnace_timer > 0: 
                    furnace_timer -= 1
                else:
                    furnace_running = False
                    furnace_has_item = False
                    paving_mold_has_item = True
            if presser_running:
                if presser_timer > 0: 
                    presser_timer -= 1
                else:
                    presser_running = False
                    paving_mold_has_item = False
            if decomposer_running:
                if decomposer_timer > 0:
                    decomposer_timer -= 1
                else:
                    decomposer_running = False
                    decomp_stack_index = len(decompose_stack)-1
            
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
    if shredder_bucket.collide_point(pos):
        hover_name = shredder_bucket.name
    elif paving_mold.collide_point(pos):
        hover_name = paving_mold.name
    furnace.draw(screen)
    shredder.draw(screen)
    presser.draw(screen)
    shredder_bucket.draw(screen)
    paving_mold.draw(screen)
    if dragging: 
        dragged_object.draw(screen)
        pygame.draw.rect(screen, (0, 0, 0), dragged_object.rect, 2)
    if hold_item != None:
        hold_item.draw(screen)
        if hold_item.collide_point(pos):
            hover_name = hold_item.name
    if hover_name!=None:
        # print(hover_name)
        text_surf :pygame.Surface = create_text_box(hover_name, 20, (0,0,0,0.5))
        x = pos[0]-text_surf.width//2
        if x+text_surf.get_width()>WIDTH:
            x = WIDTH-text_surf.get_width()
        elif x<0:
            x = 0
        screen.blit(text_surf, (x, pos[1] + 20))
    if shredder_timer>0:screen.blit(create_text_box(create_time_text(shredder_timer), 20, (0,0,0,0.5)), shredder.rect.topleft)
    if furnace_timer>0:screen.blit(create_text_box(create_time_text(furnace_timer), 20, (0,0,0,0.5)), furnace.rect.topleft)
    if presser_timer>0:screen.blit(create_text_box(create_time_text(presser_timer), 20, (0,0,0,0.5)), presser.rect.topleft)
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
water = TrashObject(100,100, surface, "Air", TrashType.OTHERS)
decomp_starter = TrashObject(100,100,surface2,"Bakteri Starter", TrashType.OTHERS)
items = [water, decomp_starter]
outside_items = ItemList(items, (SCROLL_POS[0], SCROLL_POS[1]-25), SCROLL_SPACING, 2,BOX_SIZE)
surface2 = cairo.ImageSurface(cairo.FORMAT_ARGB32, widthb, int(heightb*1.4))
ctxa = cairo.Context(surface2)
ctxa.set_source_rgb(0, 1, 0)
ctxa.paint()
decompose_bin = TrashObject(350,450, surface2, "Ember Dekompos", TrashType.OTHERS)
decompose_stack = [decomp_starter, trashbean_organic, water]
decomp_stack_index = len(decompose_stack)-1
DECOMPOSER_TIME = 60 
decomposer_timer = 0 
decomposer_running = False
def fertilizer_created():
    pass
# endregion

# region Outside Space
def outside_space():
    global  dt, state, screen,current_scene, in_transition, progress, dragging, dragged_index, dragged_object, offset_x, offset_y, decompose_stack, decomp_stack_index, hold_item, shredder_has_item, furnace_has_item, presser_has_item, shredder_bucket_has_item, paving_mold_has_item, presser_running, furnace_running, shredder_running, presser_timer, furnace_timer, shredder_timer, decomposer_running, decomposer_timer
    screen.blit(current_scene, (0, 0))
    hover_name = None
    pos = pygame.mouse.get_pos()
    for obj in outside_items.get():
        if obj.collide_point(pos):
            hover_name = obj.name
    if decompose_bin.collide_point(pos):
        hover_name = decompose_bin.name
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
                if hold_item != None:
                    if hold_item.collide_point((mx, my)):
                        dragging = True;dragged_object=hold_item
                        offset_x = (hold_item.rect[0] - mx)
                        offset_y = (hold_item.rect[1] - my)
                        break
            
            elif e.type == pygame.MOUSEBUTTONUP:
                if dragging:
                    dragging = False;dragged_object.is_dragged=False
                    if decompose_bin.collide_object(dragged_object):
                        if decomp_stack_index >= 0 and dragged_object is decompose_stack[decomp_stack_index]:
                            print(dragged_object.name, decompose_stack[decomp_stack_index].name)
                            decomp_stack_index-=1
                            if decomp_stack_index<0:
                                print("yeyeyyey")
                                decomposer_timer = DECOMPOSER_TIME
                                decomposer_running = True
                        else:
                            print("wrong", dragged_object)
                    if isinstance(dragged_object, TrashBin):
                        if old_hi_rect==None:
                            raise ValueError("old_hi_rect must have value here")
                        dragged_object.rect = hold_item_rect.copy()
                    else:
                        dragged_object.back_to_origin()
                
            elif e.type == pygame.MOUSEMOTION:
                if dragging:
                    mx, my = e.pos
                    dragged_object.replace_pos(mx + offset_x, my + offset_y)
                    
        if e.type == TIMER_EVENT:
            if shredder_running:
                if shredder_timer > 0: 
                    shredder_timer -= 1
                else:
                    shredder_running = False
                    shredder_has_item = False
                    shredder_bucket_has_item = True
                    # Logic
            if furnace_running:
                if furnace_timer > 0: 
                    furnace_timer -= 1
                else:
                    furnace_running = False
                    furnace_has_item = False
                    paving_mold_has_item = True
            if presser_running:
                if presser_timer > 0: 
                    presser_timer -= 1
                else:
                    presser_running = False
                    presser_has_item = False
            if decomposer_running:
                if decomposer_timer > 0:
                    decomposer_timer -= 1
                else:
                    decomposer_running = False
                    decomp_stack_index = len(decompose_stack)-1
                    # Logic
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
    if hold_item != None:
        hold_item.draw(screen)
        if hold_item.collide_point(pos):
            hover_name = hold_item.name
    name = button_left.draw(screen)
    if name != None: hover_name=name
    outside_items.draw(screen)
    decompose_bin.draw(screen)
    if hover_name!=None:
        # print(hover_name)
        text_surf :pygame.Surface = create_text_box(hover_name, 20, (0,0,0,0.5))
        x = pos[0]-text_surf.width//2
        if x+text_surf.get_width()>WIDTH:
            x = WIDTH-text_surf.get_width()
        elif x<0:
            x = 0
        screen.blit(text_surf, (x, pos[1] + 20))
    if decomposer_timer>0:screen.blit(create_text_box(create_time_text(decomposer_timer), 20, (0,0,0,0.5)), decompose_bin.rect.topleft)
    pygame.display.flip()
# endregion
    
if __name__ == "__main__":
    state = Scene.HOME
    hold_item = None
    old_hi_rect = None
    hold_item_rect = pygame.Rect(640, 530, BOX_SIZE[0], BOX_SIZE[1])
    callback_to_working = create_button_move_scene_call(Scene.WORKING)
    callback_to_home = create_button_move_scene_call(Scene.HOME)
    callback_to_outside = create_button_move_scene_call(Scene.OUTSIDE)
    working_scene = convert.convert_cairo_to_pygame_surf(IndustryRoom.create())
    outside_sceen = convert.convert_cairo_to_pygame_surf(outdoor.create())
    home_scene_bg = convert.convert_cairo_to_pygame_surf(PickUpGarage.create())
    pickup_truck = convert.convert_cairo_to_pygame_surf(TrashTruck.create())
    current_scene = home_scene_bg
    # Folder tempat asset
    ASSET_DIR = Path(__file__).parent / "assets"

    # Load musik
    pygame.mixer.music.load(ASSET_DIR / "bg.mp3")
    pygame.mixer.init()
    pygame.mixer.music.play(-1)
    while running:
        dt = clock.tick(60) / 1000
        match state:
            case Scene.HOME:
                next_scene = home_scene_bg
                button_right.name = "Pergi ke Ruang Kerajinan"
                button_right.callback = callback_to_working
                home_space()
            case Scene.SORTING:
                button_left.name = "Kembali"
                button_left.callback = callback_to_home
                sorting_space()
            case Scene.OUTSIDE:
                next_scene = outside_sceen
                button_left.name = "Kembali ke Ruang Pemilahan"
                button_left.callback = callback_to_home
                outside_space()
            case Scene.WORKING:
                next_scene = working_scene
                button_left.name = "Kembali ke Ruang Pemilahan"
                button_left.callback = callback_to_home
                working_space()
            case Scene.TRANSTITION:
                state = Scene.HOME
            case _:
                break