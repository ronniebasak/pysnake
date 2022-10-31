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
        pygame.display.set_caption("SnakeGame Title")

        self.clock = pygame.time.Clock()
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

    def update(self,delta_time: float):
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


def main():
    g = SnakeGameMeta()

    while g.running:
        delta_time = g.clock.tick(300) / 1000
        for event in pygame.event.get():
            # print("event", event)
            if event.type == pygame.QUIT:
                g.running = False
                pygame.quit()
                return
            elif event.type == game_events.GameOverEvent.type:
                print("Game Over: ")
                g.running = False
                pygame.quit()
                return

            else:
                # print("Event", event)
                g.handle_event(event)

        g.update(delta_time)


main()