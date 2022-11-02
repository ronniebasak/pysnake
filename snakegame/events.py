import pygame
from abc import ABC, abstractclassmethod

GameEvent = pygame.event.Event

class GameEventIDs:
    SnakeTimerEvent = pygame.USEREVENT+1
    GameOverEvent = pygame.USEREVENT+2
    SnakeDeadEvent = pygame.USEREVENT+3
    SwitchSceneEvent = pygame.USEREVENT+4


class BaseEvent(ABC):
    def __init__(self, **kwargs) -> None:
        if hasattr(self, 'type'):
            self.event = pygame.event.Event(self.type, **kwargs)
        else:
            raise NotImplementedError


class SnakeTimerEvent(BaseEvent):
    type: str = GameEventIDs.SnakeTimerEvent
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)


class GameOverEvent(BaseEvent):
    type: str = GameEventIDs.GameOverEvent
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)


class SnakeDeadEvent(BaseEvent):
    type: str = GameEventIDs.SnakeDeadEvent
    def __init__(self, reason:str, **kwargs) -> None:
        super().__init__(reason=reason, **kwargs)


class SwitchSceneEvent(BaseEvent):
    type: str = GameEventIDs.SwitchSceneEvent
    def __init__(self, scene_name: str, **kwargs) -> None:
        super().__init__(scene_name=scene_name, **kwargs)