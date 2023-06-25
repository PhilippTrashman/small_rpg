import pygame
from character_classes import CharacterClass
from player import Player


class FirstGame:

    def __init__(self, character_sprites: pygame.sprite.Group, resolution: tuple):
        self.resolution = resolution
        self.title = "Shadow Wizard Money Gang"
        self.clock = pygame.time.Clock()
        self.sprites = character_sprites

        self.screen = pygame.display.set_mode(self.resolution)

        self.key_binding = {
            "menu": pygame.K_p,
            "settings": pygame.K_o,
            "inventory": pygame.K_i,
            "quests": pygame.K_j,
            "skills": pygame.K_l,
        }

        self.bound_keys = [pygame.K_p, pygame.K_o, pygame.K_i, pygame.K_j, pygame.K_l]

        self.windows = {
            "menu": False,
            "settings": False,
            "inventory": False,
            "quests": False,
            "skills": False
        }

    def main(self):
        pygame.init()
        pygame.display.set_caption(self.title)

        running = True

        while running:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key in self.bound_keys:
                        self.open_window(event.key)

                    if event.key == pygame.K_ESCAPE and not self.windows["menu"]:
                        print("opening menu")
                        self.set_open_window_flag("menu")
                        self.display_menu()

            else:

                self.sprites.update()

                self.screen.fill((0, 0, 0))
                self.sprites.draw(self.screen)

            pygame.display.flip()
            # print("...")
        pygame.quit()

    def set_open_window_flag(self, window: str):
        for entry in self.windows:
            if entry == window:
                print(f"set Flag for {window}")
                self.windows[entry] = True
            else:
                self.windows[entry] = False

    def open_window(self, key_type):

        # print(self.windows)

        if key_type == self.key_binding["menu"] and not self.windows["menu"]:
            print("opening menu")
            self.set_open_window_flag("menu")
            self.display_menu()

        if key_type == self.key_binding["settings"] and not self.windows["settings"]:
            print("opening menu")
            self.set_open_window_flag("settings")
            self.display_settings()

        if key_type == self.key_binding["inventory"] and not self.windows["inventory"]:
            print("opening menu")
            self.set_open_window_flag("inventory")
            self.display_inventory()

        if key_type == self.key_binding["quests"] and not self.windows["quests"]:
            print("opening menu")
            self.set_open_window_flag("quests")
            self.display_quests()

        if key_type == self.key_binding["skills"] and not self.windows["skills"]:
            print("opening menu")
            self.set_open_window_flag("skills")
            self.display_skills()

        if key_type == pygame.K_ESCAPE and self.windows["menu"]:
            print("closing menu")
            self.close_all_windows()

    def close_all_windows(self):
        for entry in self.windows:
            self.windows[entry] = False

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


example_stat_sheet = {
    "strength": 1,
    "perception": 1,
    "endurance": 1,
    "charisma": 1,
    "intelligence": 1,
    "agility": 1,
    "luck": 1
}

if __name__ == "__main__":

    player_position = (400, 300)

    player = Player("knight", example_stat_sheet, player_position)
    sprites = pygame.sprite.Group()
    sprites.add(player)

    game = FirstGame(sprites, (800, 600))
    game.main()
