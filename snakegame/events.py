import pygame


class GameEvents:
    SnakeTimerEvent = pygame.event.Event(pygame.USEREVENT+1)
    GameOverEvent = pygame.event.Event(pygame.USEREVENT+2)
    SnakeDeadEvent = pygame.event.Event(pygame.USEREVENT+3)