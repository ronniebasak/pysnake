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

## sets up a game loop so that the game won't crash
while True:
    window.fill(pygame.Color(0,0,0)) # sets the background color to black
    pygame.display.flip() # flips the display, something you need to do every frame
