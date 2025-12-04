import random
import pygame
import cairo
import component.button as button
from component import *
from enum import Enum
from pathlib import Path

from component.item_list import ItemList
from component.objects import ImageObject, TrashObject, TrashType, TrashBin
from component.text_area import create_text_box

from scenes import IndustryRoom, outdoor, PickUpGarage, TrashTruck, home, Happyending, Badending, truckAndGarage, TrukDatang
from cairo_image import *

import copy

pygame.init()

# region CONST
class Scene(Enum):
    HOME = 0
    SORTING = 1
    OUTSIDE = 2
    WORKING = 3
    WELCOME = 4
    HAPPY = 5
    BADED = 6
    INTRO1 = 7
    INTRO2 = 8
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

# Goals Text Area



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
banana = TrashObject(100,100, bananapeel.get_banana(widthb, heightb), "Pisang", TrashType.ORGANIC)
botol_plt = TrashObject(100,100, botol_plastik.get_botol_plastik(widthb, heightb), "Botol Plastik", TrashType.PLASTIC)
apel_croak = TrashObject(100,100, eatenApple.get_eaten_apple(widthb, heightb), "Apel", TrashType.ORGANIC)
lampu = TrashObject(100,100, kacalampu.get_kaca_lampu(widthb, heightb), "Lampu", TrashType.OTHERS)
kaleng = TrashObject(100,100, kalengbekas.get_kaleng_bekas(widthb, heightb), "Kaleng", TrashType.OTHERS)
kemasan = TrashObject(100,100, kemasanPlastik.get_kemasan_plastik(widthb, heightb), "Kemasan Makanan", TrashType.PLASTIC)
items = [banana, botol_plt, apel_croak, lampu, kaleng, kemasan]
def get_rand_items(extra_count=8):
    rand_items = [i.clone() for i in items]
    for _ in range(extra_count):
        rand_items.append(random.choice(items).clone())
    random.shuffle(rand_items)
    random.shuffle(rand_items)
    return rand_items

rand_items = get_rand_items()
hold_items_trash = [i.clone() for i in rand_items] 
garbage = ItemList(rand_items, start_pos=SCROLL_POS, spacing=SCROLL_SPACING, max_show=5, box_size=BOX_SIZE)  # tampil maksimal 3 item
# endregion

# region TrashBin
width, height = 100, 160
spacing = 158
trash_bin = (115, 350)
trashbins = box_sampah.get_bins()
trashbean_plastic = TrashBin(trash_bin[0], trash_bin[1], trashbins[0], TrashType.PLASTIC, "Tempat Sampah Plastik")
surface1 = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
ctx1 = cairo.Context(surface1)
ctx1.set_source_rgb(0,1,0)
ctx1.paint()
trashbean_organic = TrashBin(trash_bin[0]+width+spacing, trash_bin[1], trashbins[1], TrashType.ORGANIC, "Tempat Sampah Organik")
surface2 = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
ctx2 = cairo.Context(surface2)
ctx2.set_source_rgb(190/255, 190/255, 190/255)
ctx2.paint()
trashbean_other = TrashBin(trash_bin[0]+2*(width+spacing), trash_bin[1], trashbins[2], TrashType.OTHERS, "Tempat Sampah Lainnya")
trashbeans = [trashbean_plastic, trashbean_organic, trashbean_other]
plastic_counter = 0
organic_counter = 0
pupuk_cair_counter = 0
paving_block_counter = 0
def reset_counter():
    global plastic_counter,organic_counter,pupuk_cair_counter,paving_block_counter, garbage
    garbage.refill(hold_items_trash)
    plastic_counter = 0
    organic_counter = 0
    pupuk_cair_counter = 0
    paving_block_counter = 0
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

def create_button_move_scene_call_welcome(next_state: Scene):
    def callback():
        global direction, in_transition, progress, state, next_scene
        direction = "left"
        in_transition = True
        progress = 0
        state = next_state
        next_scene = scene_b if current_scene == scene_a else scene_a
        reset_counter()
        start_timer()
    return callback

def create_button_move_scene_call_intro(next_state: Scene):
    def callback():
        global direction, in_transition, progress, state, next_scene
        direction = "left"
        in_transition = True
        progress = 0
        state = next_state
        next_scene = scene_b if current_scene == scene_a else scene_a
        scene_timer_start()
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

def exit():
    global state
    state = None
button_exit = button.Button(450, 480, 350, 90, "EXIT", 34, exit, 0)
button_play = button.Button(450, 320, 350, 90, "MULAI", 34, Nothing, 0)

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
    global dragged_index, trashbeans, state, current_scene, dt, garbage, dragging, dragged_object, offset_x, offset_y, direction, next_scene, hold_item, old_hi_rect, shredder_has_item, furnace_has_item, presser_has_item, shredder_bucket_has_item, paving_mold_has_item, presser_running, furnace_running, shredder_running, presser_timer, furnace_timer, shredder_timer, decomposer_running, decomposer_timer, decomp_stack_index, plastic_counter, organic_counter, pupuk_cair_counter, paving_block_counter, running, garbage, timer
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
                                trashbean.scale(120, 150)
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
                                    if len(garbage.inventory)==0:
                                        plastic_counter = 2
                                        organic_counter = 1
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
        if e.type == end_event:
            callbaack_to_bad()
        if e.type == timer_one_sec:
            timer -= 1
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
                    paving_block_counter += 1
                    if (pupuk_cair_counter==1 and paving_block_counter==2):
                        garbage.refill(hold_items_trash)
                    elif (pupuk_cair_counter==2 and paving_block_counter==4):
                        callbaack_to_happy()
            if decomposer_running:
                if decomposer_timer > 0:
                    decomposer_timer -= 1
                else:
                    decomposer_running = False
                    decomp_stack_index = len(decompose_stack)-1
                    pupuk_cair_counter+=1
                    if (pupuk_cair_counter==1 and paving_block_counter==2):
                        garbage.refill(hold_items_trash)
                    elif (pupuk_cair_counter==2 and paving_block_counter==4):
                        callbaack_to_happy()
                    # Logic
                    
    for trashbean in trashbeans:
        trashbean.draw(screen)
    if hold_item!=None:
        hold_item.draw(screen)
        screen.blit(hold_item.pygame_surface, hold_item.rect)
        # pass
    if dragging: 
        dragged_object.draw(screen)
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
    text_surf :pygame.Surface = create_text_box(get_timer_str(timer), 20, (0,0,0,0.5))
    screen.blit(text_surf, (0, 0))
    pygame.display.flip()
    
# endregion

# region Create Home Components
start = trash_bin
widthd = 3*(width+spacing)
heightd = trash_bin[1]
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, widthd-trash_bin[0], heightd)
next_to_sorting = ImageObject(trash_bin[0],trash_bin[1],surface,"Pilah Sampah")
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 250, 310)
next_to_outside = ImageObject(855,200,surface,"Pergi ke Luar")
# endregion

# region Home Space
def home_space():
    global  dt, state, screen,current_scene, in_transition, progress, shredder_has_item, furnace_has_item, presser_has_item, shredder_bucket_has_item, paving_mold_has_item, presser_running, furnace_running, shredder_running, presser_timer, furnace_timer, shredder_timer, decomposer_running, decomposer_timer, decomp_stack_index, pupuk_cair_counter, paving_block_counter, running, garbage, timer
    screen.blit(current_scene, (0, 0))
    hover_name = None
    pos = pygame.mouse.get_pos()
    if next_to_sorting.collide_point(pos):
        hover_name = next_to_sorting.name
    elif next_to_outside.collide_point(pos):
        hover_name = next_to_outside.name
    for e in pygame.event.get():
        if e.type == end_event:
            callbaack_to_bad()
        if e.type == timer_one_sec:
            timer -= 1
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
                    paving_mold_has_item = False
                    paving_block_counter+=1
                    if (pupuk_cair_counter==1 and paving_block_counter==2):
                        garbage.refill(hold_items_trash)
                    elif (pupuk_cair_counter==2 and paving_block_counter==4):
                        callbaack_to_happy()
            if decomposer_running:
                if decomposer_timer > 0:
                    decomposer_timer -= 1
                else:
                    decomposer_running = False
                    decomp_stack_index = len(decompose_stack)-1
                    pupuk_cair_counter+=1
                    if (pupuk_cair_counter==1 and paving_block_counter==2):
                        garbage.refill(hold_items_trash)
                    elif (pupuk_cair_counter==2 and paving_block_counter==4):
                        callbaack_to_happy()
                
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
    else:
        for trashbean in trashbeans:
            trashbean.draw(screen)
    # draw_buttons()
        if hold_item != None:
            hold_item.draw(screen)
            if hold_item.collide_point(pos):
                hover_name = hold_item.name
            if hold_item == trashbeans[0]: # plastik
                text_surf :pygame.Surface = create_text_box(f"Paving Block: {paving_block_counter}/4", 20, (0,0,0,0.5))
                screen.blit(text_surf, (500, 0))
            elif hold_item == trashbeans[1]: # organik
                text_surf :pygame.Surface = create_text_box(f"Pupuk Cair: {pupuk_cair_counter}/2", 20, (0,0,0,0.5))
                screen.blit(text_surf, (500, 0))
        else:
            text_surf :pygame.Surface = create_text_box(f"Pilah Sampah dan Ambil Salah Satu Tempat Sampah", 20, (0,0,0,0.5))
            screen.blit(text_surf, (400, 0))
        name = button_right.draw(screen)
        if name != None: hover_name=name
        next_to_sorting.draw(screen)
        next_to_outside.draw(screen)
        if hold_item!=None:hold_item.draw(screen)
        if hover_name!=None:
            text_surf :pygame.Surface = create_text_box(hover_name, 20, (0,0,0,0.5))
            x = pos[0]-text_surf.width//2
            if x+text_surf.get_width()>WIDTH:
                x = WIDTH-text_surf.get_width()
            elif x<0:
                x = 0
            screen.blit(text_surf, (x, pos[1] + 20))
        text_surf :pygame.Surface = create_text_box(get_timer_str(timer), 20, (0,0,0,0.5))
        screen.blit(text_surf, (0, 0))
        
    pygame.display.flip()
# endregion
    


# region Working Components
width, height = 220, 480
trash_bin = (240, 100)
spacing = BOX_SIZE[0]+5
# surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
# ctx = cairo.Context(surface)
# ctx.set_source_rgb(1,0,0)
# ctx.paint()
furnace_image = mesin_furnace.get_furnace()
presser_image = mesin_paving_block.get_presser()
shredder_image = mesin_shredder.get_shredder()
bucket_image = mesin_shredder.get_bucket()
mold = mesin_paving_block.get_paving_mold()
shredder = TrashBin(trash_bin[0], trash_bin[1]+130, shredder_image, TrashType.OBJECT, "Pencacah Plastik")
furnace = TrashBin(trash_bin[0]+width+spacing+10, trash_bin[1]+135, furnace_image, TrashType.OBJECT, "Mesin Peleleh Plastik")
presser = TrashBin(trash_bin[0]+2*(width+spacing), trash_bin[1]+95, presser_image, TrashType.OBJECT, "Mesin Penekan")
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, int(width*0.7), int(height*0.3))
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.5,0.5,0)
shredder_bucket = TrashObject(shredder.rect.x + int(width*0.28), shredder.rect.y+shredder.rect.height-bucket_image.get_height(), bucket_image, "Bak Penampung Cacahan", TrashType.OBJECT)
paving_mold = TrashObject(furnace.rect.x+int(width*0.08), furnace.rect.y+furnace.rect.height-mold.get_height(), mold, "Cetakan Paving", TrashType.OBJECT)
mold_hold_rect = pygame.Rect(presser.rect.x+int(width*0.1)-7, presser.rect.y+(presser.rect.height-mold.get_height())*2/3-13, mold.get_width(), mold.get_height())
# endregion
    
# region Working Logic
def create_time_text(time:int)->str:
    return str(time)+" detik"
    
# SHREDDER_TIME = 30
# FURNACE_TIME = 45
# PRESSER_TIME = 30
SHREDDER_TIME = 10
FURNACE_TIME = 15
PRESSER_TIME = 12
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
# endregiondecomposer_timer
    
# region Working Space
def working_space():
    global  dt, state, screen,current_scene, in_transition, progress, dragging, dragged_object, offset_x, offset_y, hold_item, mold_hold_rect, shredder_has_item, furnace_has_item, presser_has_item, shredder_bucket_has_item, paving_mold_has_item, presser_running, furnace_running, shredder_running, presser_timer, furnace_timer, shredder_timer, decomposer_running, decomposer_timer, decomp_stack_index, plastic_counter, pupuk_cair_counter, paving_block_counter, garbage, timer
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
                        if dragged_object is trashbean_plastic and plastic_counter> 0 and not shredder_has_item and not shredder_running  and shredder.collide_object(dragged_object):
                            shredder_has_item = True
                            plastic_counter -= 1
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
        if e.type == end_event:
            callbaack_to_bad()  
        if e.type == timer_one_sec:
            timer -= 1
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
                    paving_block_counter+=1
                    if (pupuk_cair_counter==1 and paving_block_counter==2):
                        garbage.refill(hold_items_trash)
                    elif (pupuk_cair_counter==2 and paving_block_counter==4):
                        callbaack_to_happy()
            if decomposer_running:
                if decomposer_timer > 0:
                    decomposer_timer -= 1
                else:
                    decomposer_running = False
                    decomp_stack_index = len(decompose_stack)-1
                    pupuk_cair_counter+=1
                    if (pupuk_cair_counter==1 and paving_block_counter==2):
                        garbage.refill(hold_items_trash)
                    elif (pupuk_cair_counter==2 and paving_block_counter==4):
                        callbaack_to_happy()
            
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
    else:
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
        if hold_item != None:
            hold_item.draw(screen)
            if hold_item.collide_point(pos):
                hover_name = hold_item.name
            if hold_item == trashbeans[0]: # plastik
                text_surf :pygame.Surface = create_text_box(f"Paving Block: {paving_block_counter}/4", 20, (0,0,0,0.5))
                screen.blit(text_surf, (500, 0))
            elif hold_item == trashbeans[1]: # organik
                text_surf :pygame.Surface = create_text_box(f"Pupuk Cair: {pupuk_cair_counter}/2", 20, (0,0,0,0.5))
                screen.blit(text_surf, (500, 0))
        else:
            text_surf :pygame.Surface = create_text_box(f"Pilah Sampah dan Ambil Salah Satu Tempat Sampah", 20, (0,0,0,0.5))
            screen.blit(text_surf, (400, 0))
        if hover_name!=None:
            # print(hover_name)
            text_surf :pygame.Surface = create_text_box(hover_name, 20, (0,0,0,0.5))
            x = pos[0]-text_surf.width//2
            if x+text_surf.get_width()>WIDTH:
                x = WIDTH-text_surf.get_width()
            elif x<0:
                x = 0
            screen.blit(text_surf, (x, pos[1] + 20))
        if shredder_timer>0:screen.blit(create_text_box(create_time_text(shredder_timer), 20, (0,0,0,0.5)), (shredder.rect.topleft[0]+65, shredder.rect.topleft[1]))
        if furnace_timer>0:screen.blit(create_text_box(create_time_text(furnace_timer), 20, (0,0,0,0.5)), (furnace.rect.topleft[0]+63, furnace.rect.topleft[1]))
        if presser_timer>0:screen.blit(create_text_box(create_time_text(presser_timer), 20, (0,0,0,0.5)), (presser.rect.topleft[0]+65, presser.rect.topleft[1]))
        text_surf :pygame.Surface = create_text_box(get_timer_str(timer), 20, (0,0,0,0.5))
        screen.blit(text_surf, (0, 0))
    pygame.display.flip()
# endregion


# region Outside Components
air = ember_air.get_ember_air()
water = TrashObject(100,100, air, "Air", TrashType.OTHERS)
water.scale(widthb, heightb)
decomp_img = botol_bakteri.get_m3bottle()
decomp_starter = TrashObject(100,100,decomp_img,"Bakteri Starter", TrashType.OTHERS)
decomp_starter.scale(widthb, heightb)
items = [water, decomp_starter]
outside_items = ItemList(items, (SCROLL_POS[0], SCROLL_POS[1]-25), SCROLL_SPACING, 2,BOX_SIZE)
decomp_bin_img = trashbins[3]
decompose_bin = TrashObject(350,250, decomp_bin_img, "Ember Dekompos", TrashType.OTHERS)
decompose_stack = [decomp_starter, trashbean_organic, water]
decomp_stack_index = len(decompose_stack)-1
DECOMPOSER_TIME = 25
decomposer_timer = 0 
decomposer_running = False
def fertilizer_created():
    pass
# endregion

# region Outside Space
def outside_space():
    global  dt, state, screen,current_scene, in_transition, progress, dragging, dragged_index, dragged_object, offset_x, offset_y, decompose_stack, decomp_stack_index, hold_item, shredder_has_item, furnace_has_item, presser_has_item, shredder_bucket_has_item, paving_mold_has_item, presser_running, furnace_running, shredder_running, presser_timer, furnace_timer, shredder_timer, decomposer_running, decomposer_timer, organic_counter, pupuk_cair_counter, paving_block_counter, running, rand_items, garbage, timer
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
                        if decomp_stack_index >= 0 and organic_counter>0 and dragged_object is decompose_stack[decomp_stack_index]:
                            decomp_stack_index-=1
                            if decomp_stack_index<0:
                                organic_counter-=1
                                decomposer_timer = DECOMPOSER_TIME
                                decomposer_running = True
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
                    
        if e.type == end_event:
            callbaack_to_bad()
        if e.type == timer_one_sec:
            timer -= 1
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
                    paving_block_counter+=1
                    if (pupuk_cair_counter==1 and paving_block_counter==2):
                        garbage.refill(hold_items_trash)
                    elif (pupuk_cair_counter==2 and paving_block_counter==4):
                        callbaack_to_happy()
            if decomposer_running:
                if decomposer_timer > 0:
                    decomposer_timer -= 1
                else:
                    decomposer_running = False
                    decomp_stack_index = len(decompose_stack)-1
                    pupuk_cair_counter+=1
                    if (pupuk_cair_counter==1 and paving_block_counter==2):
                        garbage.refill(hold_items_trash)
                    elif (pupuk_cair_counter==2 and paving_block_counter==4):
                        callbaack_to_happy()
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
    else:
        decompose_bin.draw(screen)
        if dragging: 
            dragged_object.draw(screen)
        if hold_item != None:
            hold_item.draw(screen)
            if hold_item.collide_point(pos):
                hover_name = hold_item.name
            if hold_item == trashbeans[0]: # plastik
                text_surf :pygame.Surface = create_text_box(f"Paving Block: {paving_block_counter}/4", 20, (0,0,0,0.5))
                screen.blit(text_surf, (500, 0))
            elif hold_item == trashbeans[1]: # organik
                text_surf :pygame.Surface = create_text_box(f"Pupuk Cair: {pupuk_cair_counter}/2", 20, (0,0,0,0.5))
                screen.blit(text_surf, (500, 0))
        else:
            text_surf :pygame.Surface = create_text_box(f"Pilah Sampah dan Ambil Salah Satu Tempat Sampah", 20, (0,0,0,0.5))
            screen.blit(text_surf, (400, 0))
        if decompose_bin.collide_point(pos):
            hover_name = decompose_bin.name
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
        if decomposer_timer>0:screen.blit(create_text_box(create_time_text(decomposer_timer), 20, (0,0,0,0.5)), (decompose_bin.rect.midtop[0]-45, decompose_bin.rect.midtop[1]))
        text_surf :pygame.Surface = create_text_box(get_timer_str(timer), 20, (0,0,0,0.5))
        screen.blit(text_surf, (0, 0))
    pygame.display.flip()
# endregion
    
def welcome_scene():
    global  dt, state, screen, current_scene, in_transition, progress
    screen.blit(current_scene, (0, 0))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            state = None
        if not in_transition:
            if e.type == pygame.MOUSEBUTTONDOWN:
                mx, my = e.pos
                
                button_exit.click((mx, my))
                button_play.click((mx, my)) 
                
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
    else:
        button_exit.draw(screen)
        button_play.draw(screen)        
    
    pygame.display.flip()
    
def ending_scene():
    global  dt, state, screen, current_scene, in_transition, progress
    screen.blit(current_scene, (0, 0))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            state = None
        if not in_transition:
            if e.type == pygame.MOUSEBUTTONDOWN:
                mx, my = e.pos
                
                button_exit.click((mx, my))
                button_play.click((mx, my)) 
                
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
    else:
        button_exit.draw(screen)
        button_play.draw(screen)        
    
    
    pygame.display.flip()

    

def scene_intro1(callback):
    global  dt, state, screen, current_scene, in_transition, progress
    screen.blit(current_scene, (0, 0))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            state = None
        if e.type == three_sec:
            callback()
                
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
         
    
    pygame.display.flip()
    
def scene_intro2(callback):
    global  dt, state, screen, current_scene, in_transition, progress
    screen.blit(current_scene, (0, 0))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            state = None
        if e.type == three_sec:
            callback()
            
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
    
    pygame.display.flip()
    
    
time = 300
timer = time
def get_timer_str(time: int):
    global timer 
    minut = time//60
    reminder = time%60
    if reminder <10:
        return f"0{minut}:0{reminder}"
    else:
        return f"0{minut}:{reminder}"
    
    
if __name__ == "__main__":
    
    state = Scene.WELCOME
    hold_item = None
    old_hi_rect = None
    hold_item_rect = pygame.Rect(640, 530, 120, 150)
    callback_to_working = create_button_move_scene_call(Scene.WORKING)
    callback_to_home = create_button_move_scene_call(Scene.HOME)
    callback_to_home_reset = create_button_move_scene_call_welcome(Scene.HOME)
    callback_to_outside = create_button_move_scene_call(Scene.OUTSIDE)
    callbaack_to_happy = create_button_move_scene_call(Scene.HAPPY)
    callbaack_to_bad = create_button_move_scene_call(Scene.BADED)
    callbaack_to_intro1 = create_button_move_scene_call_intro(Scene.INTRO1)
    callbaack_to_intro2 = create_button_move_scene_call(Scene.INTRO2)
    
    working_scene = convert.convert_cairo_to_pygame_surf(IndustryRoom.create())
    outside_sceen = convert.convert_cairo_to_pygame_surf(outdoor.create())
    home_scene_bg = convert.convert_cairo_to_pygame_surf(PickUpGarage.create())
    pickup_truck = convert.convert_cairo_to_pygame_surf(TrashTruck.create())
    welcome = convert.convert_cairo_to_pygame_surf(home.get_home())
    intro = convert.convert_cairo_to_pygame_surf(truckAndGarage.create())
    
    current_scene = welcome
    
    truck_datang = convert.convert_cairo_to_pygame_surf(TrukDatang.get_truck_datang())
    happyend = convert.convert_cairo_to_pygame_surf(Happyending.get_happy())
    badend = convert.convert_cairo_to_pygame_surf(Badending.get_bad())
    
    end_event = pygame.USEREVENT + 2
    timer_one_sec = pygame.USEREVENT + 3
    three_sec = pygame.USEREVENT + 4
    
    def start_timer():
        global end_event, timer, timer_one_sec
        pygame.time.set_timer(end_event, 0)
        pygame.time.set_timer(end_event, time*1000, loops=1)
        timer = time
        pygame.time.set_timer(timer_one_sec, 0)
        pygame.time.set_timer(timer_one_sec, 1000, loops=time)
        
    def scene_timer_start():
        global three_sec
        pygame.time.set_timer(three_sec, 0)
        pygame.time.set_timer(three_sec, 5000, loops=2) 
    # Folder tempat asset
    ASSET_DIR = Path(__file__).parent / "assets"

    # Load musik
    pygame.mixer.music.load(ASSET_DIR / "bg.mp3")
    pygame.mixer.init()
    pygame.mixer.music.play(-1)
    while running:
        dt = clock.tick(60) / 1000
        match state:
            case Scene.WELCOME:
                next_scene = welcome
                button_play.callback = callbaack_to_intro1
                welcome_scene()
            case Scene.INTRO1:
                next_scene = intro
                scene_intro1(callbaack_to_intro2)
            case Scene.INTRO2:
                next_scene = truck_datang
                scene_intro2(callback_to_home_reset)
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
            case Scene.HAPPY:
                next_scene = happyend
                button_play.callback = callback_to_home_reset
                ending_scene()
            case Scene.BADED:
                next_scene = badend
                button_play.callback = callback_to_home_reset
                ending_scene()
            case _:
                break