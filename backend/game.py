import pygame
from backend.character_classes import CharacterClass
from backend.player import Player
from backend.npc import NPC
from backend.map_tiled import WorldScreenManaged, MapLayer
from pathlib import Path


class ScrunkleQuest:

    def __init__(self, resolution: tuple, pixel_size: int = 25, debug: bool = False):
        """
        The Constructor for Scrunkle Quest :)
        :param resolution: Sets up the Window Resolution
        """
        # Setting up basic pygame settings
        self.__resolution = resolution
        self.title = "Scrunkle Quest"
        self.__clock = pygame.time.Clock()
        self.__debug = debug
        self.__running = False

        self.player_sprites = pygame.sprite.Group()
        self.npc_sprites = pygame.sprite.Group()
        self.__screen = pygame.display.set_mode(self.__resolution)
        # Setting up Keybindings. Should be able to change them later in Settings window
        self.__key_binding = {
            "menu": pygame.K_p,
            "settings": pygame.K_o,
            "inventory": pygame.K_i,
            "quests": pygame.K_j,
            "skills": pygame.K_l,
        }

        self.bound_keys = [pygame.K_p, pygame.K_o, pygame.K_i, pygame.K_j, pygame.K_l]
        # What type of windows are available. Status screen etc
        self.windows = {
            "menu": False,
            "settings": False,
            "inventory": False,
            "quests": False,
            "skills": False
        }
        # What buttons are bound to player movement. Not currently working
        self.__player_movement = {
            "up": (pygame.K_w, pygame.K_UP),
            "down": (pygame.K_s, pygame.K_DOWN),
            "left": (pygame.K_a, pygame.K_LEFT),
            "right": (pygame.K_d, pygame.K_RIGHT),
            "sprint": (pygame.K_LSHIFT, pygame.K_RSHIFT)
        }

        # How big a single pixel will be
        self.pixel_size = pixel_size

        # placing the player in the middle of the screen
        self.player_position = (55, 50)
        self.__walking_speed = 8
        self.__last_movement_time = 0

        example_stat_sheet = {
            "strength": 1,
            "perception": 1,
            "endurance": 1,
            "charisma": 1,
            "intelligence": 1,
            "agility": 1,
            "luck": 1
        }

        # NPCs should be placed like tiles on the Interactables layer
        # Plan about how to id npcs and add their diallogues/function.
        # Maybe just use a second layer with its own tileset as the id, use the collision system that you already,
        # implemented

        # Setting up the Background
        self.__bg_x = -40 * pixel_size
        self.__bg_y = -45 * pixel_size

        # Creating Player Character
        self.player = Player(
            player_class="knight",
            stats=example_stat_sheet,
            position=self.player_position,
            pixel_size=25
        )

        self.last_move_time = 0
        # Adding Character Sprite
        self.player_sprites.add(self.player)

        self.__overworld_map_layer: [str, MapLayer] = {}
        self.__check_player_position = (0, 0)
        self.__world_screen = self.__draw_map()
        self.__world_screen_surface = self.__world_screen.get_map()
        if self.__debug:
            pygame.image.save(self.__world_screen_surface, "combined_map.png")

    def __draw_map(self) -> WorldScreenManaged:
        self.__overworld_map_layer["background"] = MapLayer(
            Path("map_tiles/new_process/overworld_upper_left_background.csv"),
            tile_size=16,
        )
        self.__overworld_map_layer["boundaries"] = MapLayer(
            Path("map_tiles/new_process/overworld_upper_left_boundaries.csv"),
            tile_size=16,
        )
        self.collisions = self.__overworld_map_layer["boundaries"].get_collision_map()
        if self.__debug:
            print(self.collisions)

        self.__overworld_map_layer["paths"] = MapLayer(
            Path("map_tiles/new_process/overworld_upper_left_paths.csv"),
            tile_size=16,
        )
        paths = self.__overworld_map_layer["paths"].get_collision_map()
        for path_row, col_row in zip(paths, self.collisions):
            for j, entry in enumerate(path_row):
                if entry is not None:
                    col_row[j] = None

        self.__overworld_map_layer["interactables"] = MapLayer(
            Path("map_tiles/new_process/overworld_upper_left_interactables.csv"),
            tile_size=16,
        )
        world_screen = WorldScreenManaged(
            Path("assets/tileset/FF5 Tileset/overworld_edited.png"),
            self.pixel_size,
            16
        )
        for layer in self.__overworld_map_layer.values():
            world_screen.add_layer(layer)
        return world_screen

    def main(self):
        print(self.__player_movement.values())
        pygame.init()
        pygame.display.set_caption(self.title)
        self.player.place_character(self.pixel_size * self.__resolution[0] / 2 // self.pixel_size,
                                    self.pixel_size * self.__resolution[1] / 2 // self.pixel_size)

        self.__running = True

        while self.__running:
            if self.__check_player_position in self.collisions:
                print("YES")
            self.__clock.tick(60)
            self.__key_event_handler()
            self.player_sprites.update()
            self.npc_sprites.update()
            # self.display_checkerboard()
            self.__draw_background()
            # self.screen.blit(self.worldmap, (self.bg_x, self.bg_y))
            self.player_sprites.draw(self.__screen)
            self.npc_sprites.draw(self.__screen)

            pygame.display.flip()
            # print("...")
        pygame.quit()

    def __key_event_handler(self) -> None:
        """
        Function for handling Key inputs for the game
        """
        current_time = pygame.time.get_ticks()
        movement_delay = 1000 / self.__walking_speed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.__running = False

        keys = pygame.key.get_pressed()

        # Check the state of keys for continuous movement

        if current_time - self.__last_movement_time >= movement_delay:
            if keys[self.__player_movement["up"][0]] or keys[self.__player_movement["up"][1]]:
                self.__move_player(0, 1)
            if keys[self.__player_movement["down"][0]] or keys[self.__player_movement["down"][1]]:
                self.__move_player(0, -1)
            if keys[self.__player_movement["left"][0]] or keys[self.__player_movement["left"][1]]:
                self.__move_player(1, 0)
            if keys[self.__player_movement["right"][0]] or keys[self.__player_movement["right"][1]]:
                self.__move_player(-1, 0)
            if keys[self.__player_movement["sprint"][0]] or keys[self.__player_movement["sprint"][0]]:
                self.__walking_speed = 14
            else:
                self.__walking_speed = 8

            self.__last_movement_time = current_time

        # Handle other bound keys
        for key in self.bound_keys:
            if keys[key]:
                self.open_window(key)

    def __move_player(self, dx: int, dy: int):
        """
        Function responsible for moving the player
        :param dx: how much to move in the x direction
        :param dy: how much to move in the y direction
        """

        # print(self.player_position[0] * self.pixel_size)
        new_bg_x = ((self.__bg_x + dx * self.pixel_size) - 400) * -1
        new_bg_y = ((self.__bg_y + dy * self.pixel_size) - 300) * -1
        self.__check_player_position = (new_bg_x, new_bg_y)
        move_flag = False

        for row in self.collisions:
            if self.__check_player_position in row:
                move_flag = False
                break
            else:
                move_flag = True
        if move_flag:
            self.__bg_x += dx * self.pixel_size
            self.__bg_y += dy * self.pixel_size

    def __draw_background(self):
        """draws worldmap and props onto the screen"""
        self.__screen.blit(self.__world_screen_surface, (self.__bg_x, self.__bg_y))

    def set_open_window_flag(self, window: str):
        for entry in self.windows:
            if entry == window:
                self.windows[entry] = True
            else:
                self.windows[entry] = False

    def open_window(self, key_type):

        if key_type == self.__key_binding["menu"] and not self.windows["menu"]:
            # print("opening menu")
            self.set_open_window_flag("menu")
            self.display_menu()

        if key_type == self.__key_binding["settings"] and not self.windows["settings"]:
            # print("opening menu")
            self.set_open_window_flag("settings")
            self.display_settings()

        if key_type == self.__key_binding["inventory"] and not self.windows["inventory"]:
            # print("opening menu")
            self.set_open_window_flag("inventory")
            self.display_inventory()

        if key_type == self.__key_binding["quests"] and not self.windows["quests"]:
            # print("opening menu")
            self.set_open_window_flag("quests")
            self.display_quests()

        if key_type == self.__key_binding["skills"] and not self.windows["skills"]:
            # print("opening menu")
            self.set_open_window_flag("skills")
            self.display_skills()

        if key_type == pygame.K_ESCAPE and self.windows["menu"]:
            # print("closing menu")
            self.close_all_windows()

    def close_all_windows(self):
        for entry in self.windows:
            self.windows[entry] = False

    def display_checkerboard(self):
        white = (50, 50, 50)
        black = (0, 0, 0)

        for y in range(0, self.__resolution[1], self.pixel_size):
            for x in range(0, self.__resolution[0], self.pixel_size):
                if (x // self.pixel_size) % 2 == (y // self.pixel_size) % 2:
                    self.__screen.fill(black, (x, y, self.pixel_size, self.pixel_size))
                else:
                    self.__screen.fill(white, (x, y, self.pixel_size, self.pixel_size))

    def display_menu(self):

        while self.windows["menu"]:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    # sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.close_all_windows()  # Exit the menu if ESC key is pressed

                    if event.type == pygame.KEYDOWN:
                        if event.key in self.bound_keys:
                            self.open_window(event.key)

            self.__screen.fill((0, 255, 0))

            pygame.display.flip()  # Update the display

    def display_settings(self):

        while self.windows["settings"]:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    # sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.close_all_windows()  # Exit the menu if ESC key is pressed

                    if event.type == pygame.KEYDOWN:
                        if event.key in self.bound_keys:
                            self.open_window(event.key)

            self.__screen.fill((0, 0, 255))

            pygame.display.flip()  # Update the display

    def display_inventory(self):

        while self.windows["inventory"]:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.close_all_windows()

                    if event.type == pygame.KEYDOWN:
                        if event.key in self.bound_keys:
                            self.open_window(event.key)

            self.__screen.fill((0, 150, 150))

            pygame.display.flip()

    def display_quests(self):
        while self.windows["quests"]:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.close_all_windows()

                    if event.type == pygame.KEYDOWN:
                        if event.key in self.bound_keys:
                            self.open_window(event.key)

            self.__screen.fill((150, 150, 0))

            pygame.display.flip()

    def display_skills(self):
        while self.windows["skills"]:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.close_all_windows()

                    if event.type == pygame.KEYDOWN:
                        if event.key in self.bound_keys:
                            self.open_window(event.key)

            self.__screen.fill((150, 150, 150))

            pygame.display.flip()

    def display_combat_encounter(self) -> None:
        """
        Function for displaying Combat menus, rolls enemies and sets background for the fight_screen constructor
        """
        running = False
        while running:

            self.__screen.fill((333, 0, 123))

            pygame.display.flip()



if __name__ == "__main__":

    game = ScrunkleQuest((800, 600))
    game.main()
