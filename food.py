from typing import List
import pygame
from pygame import Vector2 as vec2
from snake import Snake
from world import WorldState
from enum import Enum
from random import randint
import pygame.mixer

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
        self.music  = [pygame.mixer.Sound('assets/klonk.mp3'), pygame.mixer.Sound('assets/vine-boom-sound-effect_KT89XIq.mp3') ]
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
        self.draw_box_at(surface, self.pos)