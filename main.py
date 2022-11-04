import pygame
import pygame.gfxdraw
from random import randint
from pygame import Vector2 as vec2
from snake import Snake
from food import Food
from typing import List, overload
from world import WorldState
from overlay import Overlay
import events as game_events

class SnakeGameMeta:
    def __init__(self):
        pygame.init()
        self.world: List = []
        self.world_state: WorldState = WorldState()

        self.window = pygame.display.set_mode(
            (self.world_state.WINDOW_SIZE_WIDTH, self.world_state.WINDOW_SIZE_HEIGHT)
        )
        pygame.display.set_caption("A Python's Odyssey")

        self.clock = pygame.time.Clock()
        self.running = True
        self.bg_color = (38,38,38)

        WORLD_DIMENSION = self.world_state.WORLD_DIMENSION

        # # adding snake to our world
        snake = Snake(WORLD_DIMENSION, 5)
        # food = Food(WORLD_DIMENSION)
        # overlay = Overlay(WORLD_DIMENSION)

        self.world += [
            snake,
            # food,
            # overlay
        ]

    def update(self,delta_time: float):
        pygame.display.set_caption(
            f"A Python's Odyssey - {int(self.clock.get_fps())} FPS"
        )

        for obj in self.world:
            obj.update(self.world_state, delta_time, self.world)

        self.window.fill(self.bg_color)
        for obj in self.world:
            obj.draw(self.window, delta_time)
        pygame.display.flip()


    def handle_event(self, event: pygame.event.Event):
        for obj in self.world:
            if hasattr(obj, 'handle_event'):
                obj.handle_event(event)


def main():
    game = SnakeGameMeta()

    while game.running:
        delta_time = game.clock.tick(30) / 1000
        for event in pygame.event.get():
            # print("event", event)
            if event.type == pygame.QUIT:
                game.running = False
                pygame.quit()
                return
            elif event.type == game_events.GameOverEvent.type:
                print("Game Over: ")
                game.running = False
                pygame.quit()
                return

            else:
                # print("Event", event)
                game.handle_event(event)

        game.update(delta_time)


main()