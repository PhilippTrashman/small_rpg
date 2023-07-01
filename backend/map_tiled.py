import pygame
from pathlib import Path


class WorldScreen:
    """
    Class for creating the Screen in pygame
    remember that every pixel is either 16x16 or 32x32
    16x16 for the Over-world
    32x32 for the city
    Menus will be created differently
    """
    def __init__(self, bg: Path = None, tile_set: Path = None, resolution: tuple = (800, 600),
                 coordinate_map: tuple = ()) -> None:
        self.bg = bg
        self.tile_set = tile_set
        self.resolution = resolution
        self.loaded_bg = None

        if self.bg:
            self.load_background()
        # self.loaded_bg = pygame.image.load(self.bg)

    def load_background(self) -> None:
        self.loaded_bg = pygame.image.load(self.bg)
        bg_width, bg_height = self.loaded_bg.get_size()
        window_width, window_height = self.resolution

        scale_factor = window_width/bg_width

        scaled_bg_width = int(bg_width * scale_factor)
        scaled_bg_height = int(bg_height * scale_factor)
        scaled_bg = pygame.transform.scale(self.loaded_bg, (scaled_bg_width, scaled_bg_height))
        self.loaded_bg = scaled_bg

    def update_background(self, new_bg: Path) -> None:
        self.bg = new_bg
        self.load_background()

    def over_world_map(self):
        """
        Creates the Over-world map, The map is cut up into 20 Fields. Refer to map.png for more information
        :return:
        """
        pass


class MenuScreen:
    """
    Class for creating Menu Screens in pygame. Add elements to them and where they should be placed
    """
    def __init__(self, resolution: tuple, menu_type: str):
        available_menu_types = ['menu', 'settings', 'inventory', 'quests', "skills", "character_creator"]
        if menu_type not in available_menu_types:
            raise ValueError(f"menu_type must be one of {available_menu_types}")
        self.resolution = resolution
        self.menu_type = menu_type
        self.menu_elements = []

    def menu_screen(self):
        pass

    def settings_screen(self):
        pass

    def inventory_screen(self):
        pass

    def quests_screen(self):
        pass

    def skills_screen(self):
        pass

    def character_creator_screen(self):
        pass



