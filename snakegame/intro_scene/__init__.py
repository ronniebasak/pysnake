import pygame
import pygame.gfxdraw
from pygame import Vector2 as vec2
from typing import List
import time
import math
from ..events import SwitchSceneEvent

class IntroScene:
    def __init__(self):
        self.world: List = []
        pygame.display.set_caption("Init Title")
        self.running = True
        self.bg_color = (38,38,38)
        self.text_color = pygame.Color(22,186,197)

        self.title = "CITK x Python"
        self.subtitle = "Click anywhere to continue"
        self.title_img = None
        self.click_img = None
        # adding snake to our world
        self.world += [
        ]

        self.image = pygame.image.load('assets/logo.png')

        self.window: pygame.Surface = None
        self.init_time = None


    def scene_init(self, window, clock, world_state):
        self.window: pygame.Surface = window
        self.clock = clock
        self.world_state = world_state

        print("Initializing Fonts")
        self.font = pygame.font.SysFont("Calibri", 64)
        print("Fonts initialized")
        self.title_img = self.font.render(self.title, True, self.text_color)


        self.font2 = pygame.font.SysFont("Calibri", 32)
        self.click_img = self.font2.render(self.subtitle, True, self.text_color)

        self.init_time = time.time()
        self.init = True


    def draw_title(self):
        dt = time.time() - self.init_time
        ## center of the window
        center =  vec2(self.window.get_size())/2

        ## center of the image
        imgcenter = vec2(self.title_img.get_size()) /2
        offset = center - imgcenter
        self.window.blit(self.title_img, offset - vec2(0, 175) )

        ## center of the image
        imgcenter = vec2(self.click_img.get_size()) /2
        offset = center - imgcenter
        self.window.blit(self.click_img, offset + vec2(0, 175) )

        ## the desired max size        
        isize = vec2(200, 200)
        # the desired frequency factor
        freq = dt*2

        # the sin of frequency gives an output between -1 and 1
        # add 1 to the result so the range changes to 2 and 0
        # divide the result by 2 to change the range to 1 and 0
        # multiply the result by 0.5 so the result is 0.5 and 0
        # add 0.5 to change the range to 1 and 0.5
        # that means our image will animate between full size to half size
        scale = (   (math.sin(freq)+1)/2   )*0.5  + 0.5

        tempImage = pygame.transform.scale(self.image, scale *isize )
        imgcenter = vec2(tempImage.get_size()) /2
        offset = center - imgcenter
        self.window.blit(tempImage, offset)



    def __del__(self):
        print("Intro is being deleted huhu")

    def update(self, world_state, delta_time: float):
        self.world_state = world_state

        pygame.display.set_caption(
            f"Snake Remastered - {int(self.clock.get_fps())} FPS"
        )
        self.window.fill(self.bg_color)

        self.draw_title()

        for player in self.world:
            player.update(self.world_state, delta_time, self.world)

        for player in self.world:
            player.draw(self.window, delta_time)
        pygame.display.flip()


    def handle_event(self, event: pygame.event.Event):

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            pygame.event.post(SwitchSceneEvent(scene_name='Snake').event)
        # for player in self.world:
        #     if hasattr(player, 'handle_event'):
        #         player.handle_event(event)

