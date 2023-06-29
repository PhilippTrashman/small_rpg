import pygame
from pathlib import Path


class Screen:
    def __init__(self, bg: Path = None, tile_set: Path = None, resolution: tuple = (800, 600)) -> None:
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



