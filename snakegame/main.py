import pygame
import pygame.gfxdraw
from .world import WorldState
from .events import GameOverEvent, SwitchSceneEvent
from .snake_scene import SnakeGameMeta
from .intro_scene import IntroScene

class DefaultSceneLoader:
    def __init__(self) -> None:
        pygame.init()
        self.world_state: WorldState = WorldState()
        self.SCENES: dict = {
            'Snake': SnakeGameMeta,
            'Intro': IntroScene,
        }

        self.clock = pygame.time.Clock()
        self.entrypoint: str = 'Intro'
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
            scene.scene_init(self.window, self.clock, self.world_state)
            self.scene_init = self.current_scene.init

        self.current_scene.update(self.world_state, delta_time)


    def handle_event(self, event):
        if event.type == SwitchSceneEvent.type:
            tmp = self.current_scene

            self.scene_init = False
            scene_cls = self.SCENES[event.scene_name]
            scene = scene_cls()
            self.current_scene = scene
            scene.scene_init(self.window, self.clock, self.world_state)
            self.scene_init = True
            del tmp


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