import pygame
import cairo
import component.button as button
from component import *
import numpy as np

from component.list_garbage import GarbageList
from component.object import ImageObject


pygame.init()

WIDTH, HEIGHT = 1024, 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Create Button
font = pygame.font.SysFont(None, 32)
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

# Button settings
BTN_WIDTH = 80
BTN_HEIGHT = 80

left_btn_rect  = pygame.Rect(20, HEIGHT//2 - 40, BTN_WIDTH, BTN_HEIGHT)
right_btn_rect = pygame.Rect(WIDTH - BTN_WIDTH - 20, HEIGHT//2 - 40, BTN_WIDTH, BTN_HEIGHT)

direction = "right"
in_transition = False
progress = 0.0



width, height = 200, 200
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
ctx = cairo.Context(surface)

# Contoh gambar: lingkaran merah
ctx.set_source_rgb(1, 0, 0)
ctx.arc(width/2, height/2, 50, 0, 2*3.14159)
ctx.fill()
obj1 = object.ImageObject(100, 100, 200,200, surface)
# Buat Pygame surface
pygame_surface = convert.convert_cairo_to_pygame_surf(surface, 200, 200)

# Buat beberapa dummy object
items = [ImageObject(100,100,200,200, surface, "1"), ImageObject(100,100,200,200,surface,"2"), ImageObject(100,100,200,200,surface,"3"),
         ImageObject(100,100,200,200,surface,"4"), ImageObject(100,100,200,200,surface,"5"), ImageObject(100,100,200,200,surface,"6")]
garbage = GarbageList(items, max_show=3)  # tampil maksimal 3 item
# image = pygame.Surface((100, 100), pygame.SRCALPHA)
# pygame.draw.circle(image, (255,0,0), (50,50), 50)

# Posisi awal
# start_pos = (150, 150)
# pos = list(start_pos)

dragging = False
offset_x = offset_y = 0

running = True

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


# --- Button renderer ---
def draw_buttons():
    pygame.draw.rect(screen, (50, 50, 50), left_btn_rect, 0, 10)
    pygame.draw.rect(screen, (50, 50, 50), right_btn_rect, 0, 10)

    font = pygame.font.SysFont(None, 40)
    left_text = font.render("<", True, (255,255,255))
    right_text = font.render(">", True, (255,255,255))

    screen.blit(left_text, (left_btn_rect.centerx - left_text.get_width()//2,
                            left_btn_rect.centery - left_text.get_height()//2))

    screen.blit(right_text, (right_btn_rect.centerx - right_text.get_width()//2,
                             right_btn_rect.centery - right_text.get_height()//2))


dragged_object = None
running = True
def main_sceen():
    global running, current_scene, dt, garbage, in_transition, dragging, dragged_object, offset_x, offset_y
        # mx, my = pygame.mouse.get_pos()
        # click = pygame.mouse.get_pressed()[0]

        # for e in pygame.event.get():
        #     if e.type == pygame.QUIT:
        #         running = False

        # # Hover effect
        # if button_rect.collidepoint(mx, my):
        #     pygame.draw.rect(screen, hover_color, button_rect)
        #     if click:
        #         print("Tombol ditekan!")
        # else:
        #     pygame.draw.rect(screen, button_color, button_rect)

        # Tampilkan teks
        
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if not in_transition:
            if e.type == pygame.MOUSEBUTTONDOWN:
                mx, my = e.pos
                if left_btn_rect.collidepoint(mx, my):
                    direction = "left"
                    in_transition = True
                    progress = 0
                    next_scene = scene_b if current_scene == scene_a else scene_a

                if right_btn_rect.collidepoint(mx, my):
                    direction = "right"
                    in_transition = True
                    progress = 0
                    next_scene = scene_b if current_scene == scene_a else scene_a
                    
                if obj1.collide_point((mx, my)):
                    dragging = True
                    # Hitung offset supaya drag smooth
                    offset_x = obj1.origin[0] - mx
                    offset_y = obj1.origin[1] - my
            
            elif e.type == pygame.MOUSEBUTTONUP:
                if dragging:
                    dragging = False
                    obj1.back_to_origin()
                    
            elif e.type == pygame.MOUSEMOTION:
                if dragging:
                    mx, my = e.pos
                    obj1.replace_pos(mx + offset_x, my + offset_y)

    # draw scene
    screen.blit(current_scene, (0, 0)) # use blit to draw
    # screen.blit(text_surf, (button_rect.x + 40, button_rect.y + 15))

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

    # UI buttons
    draw_buttons()
    # screen.blit(pygame_surface, (100, 100))
    
    obj1.draw(screen)
    garbage.draw(screen, start_pos=(50,50), spacing=10, box_size=(60,60))
    
    pygame.display.flip()
    
if __name__ == "__main__":
    while running:
        dt = clock.tick(60) / 1000
        main_sceen()