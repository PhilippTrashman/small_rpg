import pygame
from character_classes import CharacterClass
from player import Player
from map_tiled import Screen
from pathlib import Path


class FirstGame:

    def __init__(self, resolution: tuple):
        """
        The Constructor for The Small RPG with an Unknown Name :)
        :param resolution: Sets up the Window Resolution
        """
        # Setting up basic pygame settings
        self.resolution = resolution
        self.title = "Shadow Wizard Money Gang"
        self.clock = pygame.time.Clock()

        self.sprites = pygame.sprite.Group()
        self.screen = pygame.display.set_mode(self.resolution)
        # Setting up Keybindings. Should be able to change them later in Settings window
        self.key_binding = {
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
        self.player_movement = {
            "up": (pygame.K_w, pygame.K_UP),
            "down": (pygame.K_s, pygame.K_DOWN),
            "left": (pygame.K_a, pygame.K_LEFT),
            "right": (pygame.K_d, pygame.K_RIGHT)
        }

        # How big a single pixel will be
        self.pixel_size = 25

        # placing the player in the middle of the screen
        player_position = (400, 300)
        self.walking_speed = 4

        example_stat_sheet = {
            "strength": 1,
            "perception": 1,
            "endurance": 1,
            "charisma": 1,
            "intelligence": 1,
            "agility": 1,
            "luck": 1
        }

        # Creating Player Character
        self.player = Player(player_class="knight", stats=example_stat_sheet, position=player_position, pixel_size=25,
                        walking_speed=self.walking_speed)

        self.player_position = self.player.get_player_placement()
        self.last_move_time = 0

        # Adding Character Sprite
        self.sprites.add(self.player)

        print(f"{self.pixel_size*6} or {self.resolution[1]-self.pixel_size*6}")

        # Setting up the Background
        self.background = Screen()
        self.background.update_background(Path("../assets/debug_background.png"))
        self.bg_x = 0
        self.bg_y = 0

    def main(self):
        pygame.init()
        pygame.display.set_caption(self.title)
        self.player.place_character(self.pixel_size * self.resolution[0]/2 // self.pixel_size,
                                    self.pixel_size * self.resolution[1]/2 // self.pixel_size)

        running = True

        while running:
            self.clock.tick(60)
            self.player_position = self.player.get_player_placement()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key in self.bound_keys:
                        self.open_window(event.key)

                    if event.key == pygame.K_ESCAPE and not self.windows["menu"]:
                        # print("opening menu")
                        self.set_open_window_flag("menu")
                        self.display_menu()

                    if event.key == pygame.K_LSHIFT:
                        if self.walking_speed == 4:
                            # print("changed speed to 8")
                            self.walking_speed = 8
                        elif self.walking_speed == 8:
                            # print("changed speed to 4")
                            self.walking_speed = 4
                        else:
                            self.walking_speed = 4

                        self.player.move_delay = 1/self.walking_speed*1000

            self.sprites.update()
            self.move_camera()
            # self.display_checkerboard()
            self.screen.blit(self.background.loaded_bg, (self.bg_x, self.bg_y))

            self.sprites.draw(self.screen)

            pygame.display.flip()
            # print("...")
        pygame.quit()

    def set_open_window_flag(self, window: str):
        for entry in self.windows:
            if entry == window:
                # print(f"set Flag for {window}")
                self.windows[entry] = True
            else:
                self.windows[entry] = False

    def open_window(self, key_type):

        # print(self.windows)

        if key_type == self.key_binding["menu"] and not self.windows["menu"]:
            # print("opening menu")
            self.set_open_window_flag("menu")
            self.display_menu()

        if key_type == self.key_binding["settings"] and not self.windows["settings"]:
            # print("opening menu")
            self.set_open_window_flag("settings")
            self.display_settings()

        if key_type == self.key_binding["inventory"] and not self.windows["inventory"]:
            # print("opening menu")
            self.set_open_window_flag("inventory")
            self.display_inventory()

        if key_type == self.key_binding["quests"] and not self.windows["quests"]:
            # print("opening menu")
            self.set_open_window_flag("quests")
            self.display_quests()

        if key_type == self.key_binding["skills"] and not self.windows["skills"]:
            # print("opening menu")
            self.set_open_window_flag("skills")
            self.display_skills()

        if key_type == pygame.K_ESCAPE and self.windows["menu"]:
            # print("closing menu")
            self.close_all_windows()

    def close_all_windows(self):
        for entry in self.windows:
            self.windows[entry] = False

    def move_camera(self):
        """
        Function Responsible for moving the Background, and limiting the players movement
        """
        position = self.player.get_player_placement()
        if position[0] >= self.resolution[0]-self.pixel_size*9:
            self.player.move_right_flag = False
        else:
            self.player.move_right_flag = True

        if position[0] < self.pixel_size*9:
            self.player.move_left_flag = False
        else:
            self.player.move_left_flag = True

        if position[1] >= self.resolution[1]-self.pixel_size*6:
            self.player.move_down_flag = False
        else:
            self.player.move_down_flag = True
        if position[1] < self.pixel_size*6:
            self.player.move_up_flag = False
        else:
            self.player.move_up_flag = True

        if self.player.move_flag:
            if self.player.left_movement and not self.player.move_left_flag:
                self.bg_x -= self.pixel_size
            if self.player.right_movement and not self.player.move_right_flag:
                self.bg_x += self.pixel_size
            if self.player.down_movement and not self.player.move_down_flag:
                self.bg_y -= self.pixel_size
            if self.player.up_movement and not self.player.move_up_flag:
                self.bg_y += self.pixel_size



    def display_checkerboard(self):
        white = (50, 50, 50)
        black = (0, 0, 0)

        for y in range(0, self.resolution[1], self.pixel_size):
            for x in range(0, self.resolution[0], self.pixel_size):
                if (x // self.pixel_size) % 2 == (y // self.pixel_size) % 2:
                    self.screen.fill(black, (x, y, self.pixel_size, self.pixel_size))
                else:
                    self.screen.fill(white, (x, y, self.pixel_size, self.pixel_size))

        self.move_camera()

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

            self.screen.fill((0, 255, 0))

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

            self.screen.fill((0, 0, 255))

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

            self.screen.fill((0, 150, 150))

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

            self.screen.fill((150, 150, 0))

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

            self.screen.fill((150, 150, 150))

            pygame.display.flip()

if __name__ == "__main__":

    game = FirstGame((800, 600))
    game.main()
