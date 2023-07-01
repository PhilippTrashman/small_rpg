import pygame
import random

class FightScreen:

    def __init__(self, resolution: tuple, enemies: dict, players: dict):
        self.resolution = resolution
        self.enemies = enemies
        self.players = players

        
