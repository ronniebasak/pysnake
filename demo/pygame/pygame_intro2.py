import pygame

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

## sets up a game loop so that the game won't crash
while True:
    delta_time = clock.tick(target_framerate)
    window.fill(pygame.Color(255,0,0)) # sets the background color to black
    pygame.display.flip() # flips the display, something you need to do every frame

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("We have to quit")
            pygame.quit()
            break
