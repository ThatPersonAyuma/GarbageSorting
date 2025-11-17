import pygame
import cairo
import component.button as button

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


running = True
while running:
    dt = clock.tick(60) / 1000

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

        if e.type == pygame.MOUSEBUTTONDOWN and not in_transition:
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

    pygame.display.flip()