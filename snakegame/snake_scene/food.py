from typing import List
import pygame
from pygame import Vector2 as vec2
from .snake import Snake
from ..world import WorldState
from enum import Enum
from random import randint
import pygame.mixer
from ..events import SnakeDeadEvent
import math

class Food:
    def __init__(self, dimention=100) -> None:
        self.world_state = None
        self.BOX_DIMENTION = dimention

        self.pos = vec2(self.BOX_DIMENTION/2, self.BOX_DIMENTION/2)
        self.color = pygame.Color(244,96,54)

        self.rect_size = None
        self.box_size = None
        self.x_offset = None
        self.y_offset = None
        self.init = False
        self.world = None
        self.music  = [pygame.mixer.Sound('assets/klonk.mp3'), pygame.mixer.Sound('assets/vine-boom-sound-effect_KT89XIq.mp3') ]
        self.hidden = False
        print("Music",self.music)


    def init_food_pos(self, world):
        print("Init Food")
        snake: Snake = list(filter(lambda x: isinstance(x, Snake), world)) [0]
        blacklist = snake.snake
        
        x = vec2(randint(0, self.BOX_DIMENTION-1), randint(0, self.BOX_DIMENTION-1))
        if x in blacklist:
            self.init_food_pos(world)
            return
        self.pos = x
        self.init = True


    def update(self, world_state: WorldState, delta_time: float, world: List):
        self.world = world
        self.world_state = world_state
        ## update on every update
        self.rect_size = min(self.world_state.WINDOW_SIZE_WIDTH, self.world_state.WINDOW_SIZE_HEIGHT)/self.BOX_DIMENTION
        self.box_size = self.rect_size * self.BOX_DIMENTION
        self.x_offset = (self.world_state.WINDOW_SIZE_WIDTH - self.box_size)/2
        self.y_offset = (self.world_state.WINDOW_SIZE_HEIGHT - self.box_size)/2

        if not self.init:
            self.init_food_pos(world)
        
        snake: Snake = list(filter(lambda x: isinstance(x, Snake), world)) [0]
        snake_head = snake.snake[-1]
        if snake_head == self.pos:
            snake.snake_length += 1
            world_state.SCORE += 1

            rmusic = randint(0,len(self.music)-1)
            self.music[rmusic].play()
            print("Score:", world_state.SCORE)
            self.init = False



    def _get_coordinate_at(self, coordinates: vec2) -> vec2:
        return vec2(self.x_offset + self.rect_size*coordinates.x, self.y_offset+self.rect_size*coordinates.y)

    
    def draw_box_at(self, surface: pygame.Surface, coordinates: vec2):
        coord = self._get_coordinate_at(coordinates)
        pygame.gfxdraw.box(surface, (coord.x, coord.y, self.rect_size, self.rect_size), self.color)


    def draw(self, surface: pygame.Surface, delta_time: float):     
        if not self.hidden:           
            self.draw_box_at(surface, self.pos)


    def handle_event(self, event: pygame.event.Event):
        # print("EVENT", event.type)
        if event.type == SnakeDeadEvent.type:
            self.world.append(Food2(self.BOX_DIMENTION, self.pos))
            self.hidden = True



class Food2:
    def __init__(self, dimention=100, pos = (0,0)) -> None:
        self.world_state = None
        self.BOX_DIMENTION = dimention

        # self.pos = vec2(self.BOX_DIMENTION/2, self.BOX_DIMENTION/2)
        self.pos = pos
        self.color = pygame.Color(244,96,54)
        # self.color = pygame.Color(0,96,255)

        self.rect_size = None
        self.box_size = None
        self.x_offset = None
        self.y_offset = None
        self.world = None

        self.target_pos = vec2(self.BOX_DIMENTION//2, self.BOX_DIMENTION//2)
        self.target_scale = 20
        self.dur_frames = 300

        self.glasses_img = pygame.image.load('assets/sunglass.png')
        # glasses_pos = vec2(self.BOX_DIMENTION//2, -50)
        self.glasses_pos = vec2(self.BOX_DIMENTION//2, self.BOX_DIMENTION//2)

        self.n_frames = 0

        self.font = pygame.font.SysFont("Callibri", 64)
        self.text = "GAME OVER"
        self.text_color = pygame.Color(255, 64, 32)
        self.text_img = self.font.render(self.text, True, self.text_color)


    def update(self, world_state: WorldState, delta_time: float, world: List):
        self.world = world
        self.world_state = world_state
        ## update on every update
        self.rect_size = min(self.world_state.WINDOW_SIZE_WIDTH, self.world_state.WINDOW_SIZE_HEIGHT)/self.BOX_DIMENTION
        self.box_size = self.rect_size * self.BOX_DIMENTION
        self.x_offset = (self.world_state.WINDOW_SIZE_WIDTH - self.box_size)/2
        self.y_offset = (self.world_state.WINDOW_SIZE_HEIGHT - self.box_size)/2


    def _get_coordinate_at(self, coordinates: vec2) -> vec2:
        return vec2(self.x_offset + self.rect_size*coordinates.x, self.y_offset+self.rect_size*coordinates.y)

    
    def draw_box_at(self, surface: pygame.Surface, coordinates: vec2):
        coord = self._get_coordinate_at(coordinates)

        target = self._get_coordinate_at(self.target_pos)
        f = self.n_frames/self.dur_frames if self.n_frames < self.dur_frames else 1
        interpolated_pos = coord*(1-f) + target*(f)

        interpolated_scale = self.rect_size*(1-f) + self.rect_size*self.target_scale*f
        # interpolated_scale = self.rect_size
        interpolated_pos.x -= (interpolated_scale - self.rect_size)/2
        interpolated_pos.y -= (interpolated_scale - self.rect_size)/2
        pygame.gfxdraw.box(surface, (interpolated_pos.x, interpolated_pos.y, interpolated_scale, interpolated_scale), self.color)

        ## DRAW GLASSES
        img_scale = 0.15*(1-f) + 0.4*f
        img_rotation = 360*32*(1-f) + 0*f
        # img = pygame.transform.scale(self.glasses_img, vec2(self.glasses_img.get_size())*img_scale )
        img = pygame.transform.rotozoom(self.glasses_img, img_rotation, img_scale)
        surface.blit(img, interpolated_pos)

        ## DRAW_TEXT
        tpos = interpolated_pos*(1-f) + (interpolated_pos+vec2(20, interpolated_scale+20))*f
        surface.blit(self.text_img, tpos)




    def draw(self, surface: pygame.Surface, delta_time: float):                
        self.draw_box_at(surface, self.pos)
        self.n_frames += 1


    def handle_event(self, event: pygame.event.Event):
        # print("EVENT", event.type)
        ...