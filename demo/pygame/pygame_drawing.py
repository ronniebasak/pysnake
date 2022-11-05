import pygame
import pygame.gfxdraw
from pygame import Vector2 as vec2

## initializes pygame
pygame.init()

# sets up the game window
width = 640
height= 480
size = (width, height) ## tuple

# draws the game window
window = pygame.display.set_mode(size)

# sets the window title
pygame.display.set_caption(f"Hello World")

clock = pygame.time.Clock() # a clock object
target_framerate = 60 # target FPS

colors = {
    'RED': pygame.Color(255, 0, 0),
    'GREEN': pygame.Color(0, 255, 0),
    'BLUE': pygame.Color(0, 0, 255),
    'BLACK': pygame.Color(0,0,0),
    'WHITE': pygame.Color(255, 255, 255)
}



def draw():
    # draws a blue circle
    center = vec2(window.get_size())/2
    pygame.gfxdraw.filled_circle(window, int(center.x), int(center.y), 50, colors['BLUE'])

    # draws two red squares
    rect_size = vec2(60, 60)
    pygame.gfxdraw.box(window, (center + vec2(100, -30), rect_size), colors['RED'])
    pygame.gfxdraw.box(window, (center + vec2(-160, -30), rect_size), colors['RED'])

    # draws text
    font = pygame.font.SysFont(None, 64)
    img = font.render('Hello, CITK', True, colors['WHITE'])
    window.blit(img, center - vec2(img.get_width()//2, 160) )


running = True
## sets up a game loop so that the game won't crash
while running:
    delta_time = clock.tick(target_framerate)
    window.fill(colors['BLACK']) # sets the background color to black
    draw()
    pygame.display.flip() # flips the display, something you need to do every frame

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # print("We have to quit")
            running = False
            pygame.quit()
            brea