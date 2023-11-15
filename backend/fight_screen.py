import pygame
import random


class FightScreen:

    def __init__(self, resolution: tuple, enemies: dict, players: dict, screen: pygame.display):
        """
        Constructor for generating a fight screen
        :param resolution: size of the window
        :param enemies: possible enemies and their abilities, may get replaced for binary approach as a save
        :param players: player party and their abilities
        """
        self.__resolution = resolution
        # either the main game gives the fight screen possible enemies or the enemies are saved in a binary file,
        # and the main game just gives area information to determine possible enemies
        self.__enemies = enemies
        self.__screen = screen

        self.__players = players

        self.__menu_size = (self.__resolution[0], self.__resolution[1] / 4)

    def get_last_enemy_encounter(self) -> dict:
        """
        :return: dictionary containing last enemies and their exp
        """
        pass

    def get_player(self) -> dict:
        """
        :return: players after combat
        """
        pass
    