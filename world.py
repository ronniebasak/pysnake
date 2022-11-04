import pygame
from typing import List


class WorldState:
    WINDOW_SIZE_WIDTH: int = 1536
    WINDOW_SIZE_HEIGHT: int = 800
    WORLD_DIMENSION: int = 50
    SCORE:int = 0

    def __init__(self) -> None:
        ...
import events as game_events