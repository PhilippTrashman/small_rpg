import pygame
import sys

class Camera:
    def __init__(self, character, resolution):
        self.character = character
        self.resolution = resolution
        self.__width = resolution[0]
        self.__height = resolution[1]

    def apply(self, entity):
        return entity.rect.move(self.character.x - self.__width // 2, self.character.y - self.__height // 2)
