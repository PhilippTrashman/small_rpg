import pygame


class FirstGame:

    def __init__(self):
        self.resolution = (800, 600)

        self.title = "Shadow Wizard Money Gang"

    def main(self):
        pygame.init()
        pygame.display.set_caption(self.title)

        screen = pygame.display.set_mode(self.resolution)

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


if __name__ == "__main__":
    game = FirstGame()
    game.main()
