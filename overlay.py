import pygame
from snake import Snake
import events as game_events
from world import WorldState
from typing import List
import time

class Overlay:
    def __init__(self, dimension = 100) -> None:
        self.world_state = None
        self.BOX_DIMENSION = dimension
        self.rect_size = None
        self.box_size = None
        self.x_offset = None
        self.y_offset = None
        self.old_score = None
        self.img = None

        self.text_color = pygame.Color(251,245,243)
        
        print("Initializing Fonts")
        self.font = pygame.font.SysFont(None, 48)
        print("Fonts initialized")

        self.GOMusic = [
            pygame.mixer.Sound("assets/emotional-damage-meme.mp3"),
            pygame.mixer.Sound("assets/choti-bacchi-ho-kya.mp3"),
            pygame.mixer.Sound("assets/fail-sound-effect.mp3"),
            pygame.mixer.Sound("assets/the-lion-sleeps-tonight.mp3"),
            pygame.mixer.Sound("assets/tf_nemesis.mp3"),
        ]
        self.channel = pygame.mixer.Channel(0)
        self.is_snake_dead = False  


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
        self.rect_size = min(self.world_state.WINDOW_SIZE_WIDTH, self.world_state.WINDOW_SIZE_HEIGHT)/self.BOX_DIMENSION
        self.box_size = self.rect_size * self.BOX_DIMENSION
        self.x_offset = (self.world_state.WINDOW_SIZE_WIDTH - self.box_size)/2
        self.y_offset = (self.world_state.WINDOW_SIZE_HEIGHT - self.box_size)/2
        
        if self.old_score != world_state.SCORE:
            self.old_score = world_state.SCORE
            self.img = self.font.render(f"Score: {world_state.SCORE}", True, self.text_color)
        
        snake: Snake = list(filter(lambda x: isinstance(x, Snake), world)) [0]
        if self.is_snake_dead and not self.channel.get_busy():
            pygame.event.post(game_events.GameOverEvent)
            # print("Finished playback")


    def handle_event(self, event: pygame.event.Event):
        # print("EVENT", event.type)
        if event.type == game_events.SnakeDeadEvent.type:
            self.channel.queue(self.get_music(self.world_state.SCORE))
            self.is_snake_dead = True
            # time.sleep(0.01)

    def draw(self, surface: pygame.Surface, delta_time: float):                
        # set the stage
        # pygame.gfxdraw.box(surface, (self.x_offset, self.y_offset, self.box_size, self.box_size), (0,0,0))
        surface.blit(self.img, (self.x_offset - 200, self.y_offset+50))