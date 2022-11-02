import pygame
import pygame.gfxdraw
from .world import WorldState
from .events import GameOverEvent
from .snake_scene import SnakeGameMeta


class DefaultSceneLoader:
    def __init__(self) -> None:
        self.world_state: WorldState = WorldState()
        self.SCENES: dict = {
            'Snake': SnakeGameMeta
        }
        self.clock = pygame.time.Clock()
        self.entrypoint: str = 'Snake'
        self.current_scene = None
        self.scene_init = False
        self.running = True
        self.window = pygame.display.set_mode(
            (self.world_state.WINDOW_SIZE_WIDTH, self.world_state.WINDOW_SIZE_HEIGHT)
        )
    
    def update(self, delta_time):
        if not self.current_scene:
            scene_cls = self.SCENES[self.entrypoint]
            scene = scene_cls()
            self.current_scene = scene
            scene.scene_init(self.window, self.clock)
            self.scene_init = self.current_scene.init
        self.current_scene.update(self.world_state, delta_time)


    def handle_event(self, event):
        if self.current_scene and self.scene_init:
            self.current_scene.handle_event(event)



def main():
    g = DefaultSceneLoader()
    while g.running:
        delta_time = g.clock.tick(300) / 1000
        for event in pygame.event.get():
            # print("event", event)
            if event.type == pygame.QUIT:
                g.running = False
                pygame.quit()
                return
            elif event.type == GameOverEvent.type:
                print("Game Over: ")
                g.running = False
                pygame.quit()
                return

            else:
                # print("Event", event)
                g.handle_event(event)

        g.update(delta_time)