import pygame
import pygame.gfxdraw
from pygame import Vector2 as vec2
import time
import math

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



def draw(delta_time, elapsed_time):
    # draws a blue circle
    center = vec2(window.get_size())/2
    # print(delta_time, elapsed_time)
    radius = 100

    pygame.gfxdraw.line(window, int(center.x), int(center.y), elapsed_time//10, int(center.y), colors['BLUE'])

    rct = radius*math.cos(elapsed_time/1000) + center.x
    rst = radius*math.sin(elapsed_time/1000) + center.y
    pygame.gfxdraw.line(window, int(center.x), int(center.y), int(rct), int(rst), colors['GREEN'])


running = True
## sets up a game loop so that the game won't crash
elapsed_time = 0
while running:
    delta_time = clock.tick(target_framerate)
    elapsed_time += delta_time
    window.fill(colors['BLACK']) # sets the background color to black
    draw(delta_time, elapsed_time)
    pygame.display.flip() # flips the display, something you need to do every frame

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # print("We have to quit")
            running = False
            pygame.quit()
            break