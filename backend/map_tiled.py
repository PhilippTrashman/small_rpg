import pygame
import csv
from pygame import Surface
from pathlib import Path
from typing import List, Optional
import struct


class MapLayer:
    def __init__(self, csv_file: Path, tile_size: int):
        self.__csv_file = csv_file
        self.__tile_size = tile_size
        self.__map_data = self.__load_map()
        self.__collision_map = self.__generate_collision_map()

    def __load_map(self) -> List[List[str]]:
        with open(self.__csv_file, "r") as file:
            reader = csv.reader(file)
            map_data = list(reader)
        return map_data

    def __generate_collision_map(self):
        collision_map = []
        for y, row in enumerate(self.__map_data):
            collision_row = []
            for x, tile in enumerate(row):
                if tile == "-1":
                    collision_tile = None
                else:
                    # collision_tile = (x * self.__tile_size, y * self.__tile_size)
                    # to ensure actual collision maps the pixel size needs to be correct. else the check wont work
                    collision_tile = (x * 25, y * 25)
                collision_row.append(collision_tile)
            collision_map.append(collision_row)
        return collision_map

    def get_map_data(self) -> List[List[str]]:
        return self.__map_data

    def get_collision_map(self) -> List[List[Optional[int]]]:
        return self.__collision_map


class WorldScreenManaged:
    def __init__(self, tile_set: Path, pixel_size: int, tile_size: int):
        self.__tile_set = pygame.image.load(tile_set).convert_alpha()
        self.__scaled_tile_cache = {}
        self.__pixel_size = pixel_size
        self.__tile_size = tile_size
        self.__layers: List[MapLayer] = []

    def add_layer(self, layer: MapLayer):
        self.__layers.append(layer)

    def get_map(self):
        map_surface = pygame.Surface(self.get_map_size())
        for layer in self.__layers:
            self.___draw_layer(map_surface, layer)
        return map_surface.convert_alpha()

    def ___draw_layer(self, map_surface, layer: MapLayer):
        for y, row in enumerate(layer.get_map_data()):
            for x, tile in enumerate(row):
                if tile != "-1":
                    scaled_tile = self.__get_scaled_tile(int(tile))
                    map_surface.blit(scaled_tile, (x * self.__pixel_size, y * self.__pixel_size))

    def get_map_size(self):
        max_width = max(len(layer.get_map_data()[0]) for layer in self.__layers)
        max_height = max(len(layer.get_map_data()) for layer in self.__layers)
        return max_width * self.__pixel_size, max_height * self.__pixel_size

    def get_collision_map(self, layer_index):
        return self.__layers[layer_index].get_collision_map()

    def __get_scaled_tile(self, tile_id: int) -> Surface:
        # Check if the scaled tile is already in the cache
        if tile_id in self.__scaled_tile_cache:
            return self.__scaled_tile_cache[tile_id]
        # Calculate the position of the tile in the tileset
        tile_x = tile_id % (self.__tile_set.get_width() // self.__tile_size) * self.__tile_size
        tile_y = tile_id // (self.__tile_set.get_width() // self.__tile_size) * self.__tile_size
        # Get the tile from the tileset image
        tile_image = self.__tile_set.subsurface(pygame.Rect(tile_x, tile_y, self.__tile_size, self.__tile_size))
        # Scale the tile
        scaled_tile = pygame.transform.scale(tile_image, (self.__pixel_size, self.__pixel_size))
        # Set the color key for transparency
        scaled_tile.set_colorkey((0, 0, 0))
        # Store the scaled tile in the cache
        self.__scaled_tile_cache[tile_id] = scaled_tile

        return scaled_tile


def save_maps_to_binary(file_path, map_surfaces, collision_maps):
    with open(file_path, 'wb') as file:
        for map_name, map_surface in map_surfaces.items():
            # Write a marker or header to signify a map entry
            file.write(b'MAP')
            # Write map-specific information (e.g., width, height)
            width, height = map_surface.get_size()
            file.write(struct.pack('<II', width, height))
            # Convert the map surface to bytes
            map_bytes = pygame.image.tostring(map_surface, 'RGBA')
            file.write(map_bytes)

        for map_name, collision_map in collision_maps.items():
            # Write a marker or header to signify a collision map entry
            file.write(b'COL')
            # Write collision map-specific information (e.g., width, height)
            width, height = len(collision_map[0]), len(collision_map)
            file.write(struct.pack('<II', width, height))
            # Convert the collision map to bytes
            collision_bytes = struct.pack('<{}I'.format(width * height), *collision_map)
            file.write(collision_bytes)


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


# tile_screen = WorldScreen()
# map_surface = tile_screen.render_map()

