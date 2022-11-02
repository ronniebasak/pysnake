import pygame
import pygame.gfxdraw
from pygame import Vector2 as vec2
from snakegame.snake_scene.snake import Snake
from snakegame.snake_scene.food import Food
from typing import List, overload
from ..world import WorldState
from snakegame.snake_scene.overlay import Overlay




class SnakeGameMeta:
    def __init__(self):
        self.world: List = []
        self.world_state = None
        pygame.display.set_caption("SnakeGame Title")
        self.running = True
        self.bg_color = (38,38,38)

        WORLD_DIMENTION = 50

        # adding snake to our world
        snake = Snake(WORLD_DIMENTION, 5)
        food = Food(WORLD_DIMENTION)
        overlay = Overlay(WORLD_DIMENTION)

        self.world += [
            snake,
            food,
            overlay
        ]

    def __del__(self):
        print("Snake is being deleted")

    def scene_init(self, window, clock, world_state):
        self.window = window
        self.clock = clock
        self.world_state = world_state
        self.init = True


    def update(self, world_state, delta_time: float):
        self.world_state = world_state

        pygame.display.set_caption(
            f"Snake Remastered - {int(self.clock.get_fps())} FPS"
        )
        self.window.fill(self.bg_color)

        for player in self.world:
            player.update(self.world_state, delta_time, self.world)

        for player in self.world:
            player.draw(self.window, delta_time)
        pygame.display.flip()


    def handle_event(self, event: pygame.event.Event):
        for player in self.world:
            if hasattr(player, 'handle_event'):
                player.handle_event(event)

