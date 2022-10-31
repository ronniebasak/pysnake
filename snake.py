from typing import List
import pygame
from pygame import Vector2 as vec2
from world import WorldState
from enum import Enum
import events as game_events
import time


class SnakeDirectionEnum(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DODWN = 4


class Snake:
    def __init__(self, dimention=100, length = 5) -> None:
        self.world_state = None
        self.BOX_DIMENTION = dimention

        self.rect_size = None
        self.box_size = None
        self.x_offset = None
        self.y_offset = None


        self.snake_color = pygame.Color(0, 255, 0)
        self.dead_color = pygame.Color(255, 0, 0)

        self.snake_length = length
        self.snake = []
        self.timer_delay = 1000/12
        self.timer = pygame.time.set_timer(game_events.SnakeTimerEvent, int(self.timer_delay))
        self.direction: SnakeDirectionEnum = SnakeDirectionEnum.RIGHT
        self.alive = True

        self.GOMusic = [
            pygame.mixer.Sound("assets/emotional-damage-meme.mp3"),
            pygame.mixer.Sound("assets/choti-bacchi-ho-kya.mp3"),
            pygame.mixer.Sound("assets/fail-sound-effect.mp3"),
            pygame.mixer.Sound("assets/the-lion-sleeps-tonight.mp3"),
            pygame.mixer.Sound("assets/tf_nemesis.mp3"),
        ]

        self.channel = pygame.mixer.Channel(0)
        self.init_snake()


    def init_snake(self):
        print("Init Snake")
        midway = int(self.BOX_DIMENTION/2)
        for k in range(0, self.snake_length):
            self.snake.append(vec2(midway-self.snake_length+k, midway))
        print(self.snake)


    def get_music(self, score):
        index = 0
        if score >= 1 and score < 3:
            index  = 1
        elif score >= 3 and score < 10:
            index = 2
        elif score >= 10 and score < 15:
            index = 3
        elif score >= 15:
            index = 4
        return self.GOMusic[index]


    def update(self, world_state: WorldState, delta_time: float, world: List):
        self.world_state = world_state

        ## update on every update
        self.rect_size = min(self.world_state.WINDOW_SIZE_WIDTH, self.world_state.WINDOW_SIZE_HEIGHT)/self.BOX_DIMENTION
        self.box_size = self.rect_size * self.BOX_DIMENTION
        self.x_offset = (self.world_state.WINDOW_SIZE_WIDTH - self.box_size)/2
        self.y_offset = (self.world_state.WINDOW_SIZE_HEIGHT - self.box_size)/2

        if self.alive:
            head = self.snake[-1]
            if head.x < 0 or head.x >= self.BOX_DIMENTION or head.y < 0 or head.y >= self.BOX_DIMENTION:
                self.alive = False
                self.snake_color = self.dead_color
                print(world_state.SCORE)
                self.channel.queue(self.get_music(world_state.SCORE))
                print(self.get_music(world_state.SCORE))
                
            elif head in self.snake[:-1]:
                self.alive = False
                self.snake_color = self.dead_color
                self.channel.queue(self.get_music(world_state.SCORE))

        elif not self.channel.get_busy():
            pygame.event.post(game_events.GameOverEvent)


    def handle_event(self, event: pygame.event.Event):
        # print("EVENT", event.type)
        if event.type == game_events.SnakeTimerEvent.type and self.alive:
            head = self.snake[-1]

            new_vec = None
            if self.direction == SnakeDirectionEnum.LEFT:
                new_vec = head + vec2(-1, 0)
            if self.direction == SnakeDirectionEnum.RIGHT:
                new_vec = head + vec2(1, 0)
            if self.direction == SnakeDirectionEnum.UP:
                new_vec = head + vec2(0, -1)
            if self.direction == SnakeDirectionEnum.DODWN:
                new_vec = head + vec2(0, 1)

            self.snake.append(new_vec)
            self.snake = self.snake[-self.snake_length:]

        elif event.type == pygame.KEYDOWN:
            if event.unicode.lower() == "w" and self.direction != SnakeDirectionEnum.DODWN:
                self.direction = SnakeDirectionEnum.UP
            elif event.unicode.lower() == "d" and self.direction != SnakeDirectionEnum.LEFT:
                self.direction = SnakeDirectionEnum.RIGHT
            elif event.unicode.lower() == "s" and self.direction != SnakeDirectionEnum.UP:
                self.direction = SnakeDirectionEnum.DODWN
            elif event.unicode.lower() == "a" and self.direction != SnakeDirectionEnum.RIGHT:
                self.direction = SnakeDirectionEnum.LEFT


    def _get_coordinate_at(self, coordinates: vec2) -> vec2:
        return vec2(self.x_offset + self.rect_size*coordinates.x, self.y_offset+self.rect_size*coordinates.y)

    
    def draw_box_at(self, surface: pygame.Surface, coordinates: vec2):
        coord = self._get_coordinate_at(coordinates)
        pygame.gfxdraw.box(surface, (coord.x, coord.y, self.rect_size, self.rect_size), self.snake_color)


    def draw(self, surface: pygame.Surface, delta_time: float):                
        # set the stage
        pygame.gfxdraw.box(surface, (self.x_offset, self.y_offset, self.box_size, self.box_size), (0,0,0))

        ## draw the snake
        for snake_tile in self.snake:
            self.draw_box_at(surface, snake_tile)